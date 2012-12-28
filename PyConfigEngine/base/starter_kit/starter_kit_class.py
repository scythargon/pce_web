# -*- coding: utf-8 -*-
from ..config import *

class StarterKitClass(ConfigControllerClass):
    """
    Base class for other in the configuration
    """
    
    def __init__(self, enum_config_objects, class_name):
        """
        Constructor
        """
        ConfigControllerClass.__init__(self)
        self.class_name = class_name
        self.controller_id = enum_config_objects["C_" + class_name.upper().replace(" ", "_")]
        self.storage_key = "cls_" + class_name.lower().replace(" ", "_")
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by class storage
        """
        return self.storage_key
    
    def OnInstanceBeDeleted(self, instance_to_be_deleted):
        """
        Trigger for deletion
        """
        cids = self.config_header.GetRegisteredControllersIds()
        for cid in cids:
            controller = self.config_header.GetConfigController(cid)
            if (isinstance(controller, ConfigControllerModel)):
                roles = controller.roles
                storage = controller.GetStorage()
                for role in roles:
                    links = storage.GetAll(storage.GetStorageModule().StorageExpressionAssociationContains(controller, instance_to_be_deleted.GetInstanceId(), role))
                    for link in links:
                        storage.Delete(link)
        return True

    def ToString(self):
        return self.class_name

