# -*- coding: utf-8 -*- 
import time

Helper = PyConfigEngine.helper.Helper

SupportedConfigurations = [PyConfigEngine.config_test, PyConfigEngine.config_cxv2, PyConfigEngine.config_nsls2_magnets, PyConfigEngine.config_vepp2000_ipp]
SupportedStorages = [PyConfigEngine.web2py_dal]

def LoadConnection():
    if (None == session.generating_time):
        session.generating_time = time.clock()
    connection = Connection()
    # TODO: make connection id included to the service address
    if (None == session.cfg_connection_id and "connection_id" in request.vars):
        session.cfg_connection_id = request.vars["connection_id"]
    if (not connection.Load()):
        session.flash = "Connection failed: " + connection.error
        session.cfg_connection_id = None
        redirect(URL("connector", "index"))
    return connection

class Connection:
    """
    Serializable(for python pickle) helper to access the connection as persistent one
    """

    title = ""
    description = ""
    configuration = None
    storage = None
    config_manager = None
    config_header = None
    storage_manager = None
    storage_header = None
    error = "unknown reason"

    def Connect(self, connection_id):
        """
        Make connection
        """
        self.id = connection_id
        
        # Check Permissions
# TODO: Make connection possible for services
#        if (not QuickPermissionCheck("connection_" + str(self.id), "connect")):
#            self.error = "You don't have permission to use this connection."    
#            return False
            
        connection_info = db.connections[connection_id]
        if (None == connection_info):
            self.error = "Couldn't load connection info"    
            return False
        self.title = connection_info.title
        self.description = connection_info.description
        
        try:
            self.configuration = SupportedConfigurations[connection_info.configuration] #3
            self.storage = SupportedStorages[connection_info.storage] #0
            self.config_manager = self.configuration.ConfigManager()
            self.storage_manager = self.storage.StorageManager()
        except Exception, exc:
            self.error = "Unsupported Config or Storage, see server logs"
            print exc
            return False
        if (not self.storage_manager.Connect({"uri" : connection_info.uri})): #sqlite://vepp2000_ipp.db
            # TODO find out why Connect() returns false
            i=2
            self.error = "Couldn't connect to storage"
            return False
        self.config_manager.InitStorage(self.storage_manager)
        
        self.config_header = self.config_manager.GetConfigHeader()
        self.storage_header = self.storage_manager.GetStorageHeader()
        

        if (None == self.config_header):
            self.error = "Couldn't obtain ConfigHeader"    
            return False
        if (None == self.storage_header):
            self.error = "Couldn't obtain StorageHeader"    
            return False
        
        
        return True
        
    def GetId(self):
        """
        Get id of the connection
        """
        return self.id
        
    def Save(self):
        """
        Save connection to session
        """
        session.cfg_connection_id = self.id

    def Load(self):
        """
        Load connection from session
        """
        if (None == session.cfg_connection_id):
            self.error = "No connection in current session"
            return False
        return self.Connect(session.cfg_connection_id)
