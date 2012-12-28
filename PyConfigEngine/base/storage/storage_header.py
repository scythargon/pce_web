# -*- coding: utf-8 -*-
from ..object import Object

class StorageHeader(Object):
    """
    Information about stored Classes and Models
    """
     
    __changes_handler = None
    storage_engine_factory = None
    storage_engines = None
    connection = None
    
    def __init__(self, connection):
        """
        Constructor
        """
        self.connection = connection
        self.storage_engines = dict()

    def GetStorageModule(self):
        """
        Returns Storage Module that this Engine assigns to.
        """
        raise Exception(str(self) + ": Method not implemented")

    def GetRegisteredStoragesIds(self):
        """
        Get All registered storage ids
        """
        return self.storage_engine_factory.GetRegisteredObjectIds()
    
    def SetChangesHandler(self, changes_handler):
        """
        Sets the error handler of the object
        """
        self.__changes_handler = changes_handler
        for (key,engine) in self.storage_engines.iteritems():
            engine.SetChangesHandler(self.__changes_handler)
    
    def SaveRecord(self, header_record):
        """
        Add or update registration information of an object
        """
        raise Exception(str(self) + ": Method not implemented")
        
    def GetRecord(self, object_id):
        """
        Get Model Storage accoriding to registered information
        """
        raise Exception(str(self) + ": Method not implemented")

    def GetStorage(self, config_controller):
        """
        Get Class Storage accoriding to registered information
        """
        if (None == config_controller): raise Exception("Config Controller hasn't been obtained")
        controller_id = config_controller.GetConfigControllerId()
        
        if (controller_id not in self.storage_engines):
            # Loading Engine information record.
            record = self.GetRecord(controller_id)
            if (None == record):
                return self.SetErrMsg("Couldn't load header information record for controller_id = " + str(controller_id), 7)
            
            # Constructing Engine.
            new_storage = self.storage_engine_factory.MakeInstance(record.engine_id)
            if (None == new_storage):
                return self.SetErrMsg("Couldn't construct Storage Engine by engine_id = " + str(record.engine_id), 7)
            
            # Launching the Engine.
            if (None == new_storage.LaunchEngine(config_controller, self, record.storage_key)):
                return self.SetErrMsg("Couldn't launch the engine " + new_storage.ToString() + " with a key " + str(record.storage_key))
            new_storage.SetChangesHandler(self.__changes_handler)
            self.storage_engines[controller_id] = new_storage
            
        return self.storage_engines[controller_id]
    
    def ToString(self):
        return "Storage Header"
