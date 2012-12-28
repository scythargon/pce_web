# -*- coding: utf-8 -*-
from ..object import Object

class ConfigHeader(Object):
    """
    Information about configuration parts: Classes and Models
    """
    
    storage_header = None
    object_factory = None
    
    def __init__(self, enum_config_objects):
        """
        Constructor
        """
        self.controllers = {}
        self.enum_config_objects = enum_config_objects

    def InitStorage(self, storage_header):
        """
        Init ConfigHeader with proper StorageHeader
        """
        self.storage_header = storage_header

    def GetStorage(self):
        """
        Get class instance by class_id
        """
        return self.storage_header
    
    def GetRegisteredControllersIds(self):
        """
        Get All registered controller ids
        """
        return self.object_factory.GetRegisteredObjectIds()
    
    def GetConfigController(self, obj_id):
        """
        Get ConfigController
        """
        if (obj_id not in self.controllers.keys()):
            new_instance = self.object_factory.MakeInstance(obj_id)
            if (None == new_instance): return self.SetErrMsg("Couldn't get config object with id: " + str(obj_id), 7)
            
            storage_for_new_instance = self.storage_header.GetStorage(new_instance)
            if (None == storage_for_new_instance or None == new_instance.Init(self)): return self.SetErrMsg("Couldn't init storage of ConfigController: " + new_instance.ToString(), 7)
            
            self.controllers[obj_id] = new_instance

        return self.controllers[obj_id]
    
    def ToString(self):
        return "Configuration Header"
