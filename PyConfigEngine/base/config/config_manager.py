# -*- coding: utf-8 -*-
from ..object import Object

class ConfigManager(Object):
    """
    Provides high-level methods for using the configuration
    """

    config_header = None
    
    def InitStorage(self, storage_manager):
        """
        Link ConfigManager with StorageManager
        """
        self.storage_manager = storage_manager
        self.storage_header = self.storage_manager.GetStorageHeader()
        return self.config_header.InitStorage(self.storage_header)
        
    def GetConfigHeader(self):
        """
        Get configuration header
        """
        return self.config_header
    
    def ToString(self):
        return "Configuration Manager"
