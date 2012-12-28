# -*- coding: utf-8 -*-
from ..object import Object

class StorageEngine(Object):
    """
    Storage Engine Interface
    """
    
    engine_id = None
    
    __changes_handler = None
    
    def GetStorageModule(self):
        """
        Returns Storage Module that this Engine assigns to.
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def SetChangesHandler(self, changes_handler):
        """
        Sets the error handler of the object
        """
        self.__changes_handler = changes_handler
    
    def AddChangeEvent(self, message, importance):
        """
        private method
        Sets Error Message to object
        """
        if (None != self.__changes_handler):
            self.__changes_handler.ProcessMessage(self, message, importance)
        return True

    def LaunchEngine(self, config_controller, storage_header, storage_key):
        """
        Launch the storage engine
        """
        # Compatibility tests, new tables creation and tables altering should be made
        raise Exception(str(self) + ": Method not implemented")
    
    def GetEngineId(self):
        """
        Get Storage Engine id
        """
        return self.engine_id
    
    def ToString(self):
        return "StorageEngine"
