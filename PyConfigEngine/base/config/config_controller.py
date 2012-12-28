# -*- coding: utf-8 -*-
from ..object import Object

class ConfigController(Object):
    """
    Provides high-level interface of any class
    """
    
    controller_id = None
    config_header = None
    controller_storage = None
    errors = {}
    
    def Init(self, config_header):
        """
        Init ConfigController with proper config header
        """
        self.config_header = config_header
        self.controller_storage = self.config_header.GetStorage().GetStorage(self)
        if (None == self.controller_storage): return False
        return True
        
    def GetStorage(self):
        """
        Get Storage Engine
        """
        return self.controller_storage
        
    def GetConfigControllerId(self):
        """
        Get Configuration object id
        """
        return self.controller_id
        
    def CheckConsistency(self, fast = False, to_check=[]):
        """
        Check all stored in storage controller's information for consistency
        """
        raise Exception(str(self) + ": Method not implemented")
        
    def GetConsistencyErrors(self):
        """
        Get all consistency errors that are known at the moment
        """
        raise Exception(str(self) + ": Method not implemented")
        
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as unique key (typically, for tables' names) by storage engine
        """
        return "controller_" + str(self.controller_id)
        
    def GetConfigHeader(self):
        """
        Get configuration header
        """
        return self.config_header

    def OnInstanceBeDeleted(self, instance_to_be_deleted):
        """
        Trigger for deletion
        """
        return True

    def OnInstanceCreated(self, created_instance):
        """
        Trigger for creations
        """
        return True

    def OnInstanceUpdate(self, old_instance, new_instance):
        """
        Trigger for updates
        """
        return True

    def ToString(self):
        return "Controller " + str(self.controller_id)
