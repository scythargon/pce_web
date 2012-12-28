# -*- coding: utf-8 -*-
from .. import base
from ..helper import Helper

from class_base import ClassBase

class ClassDevice(ClassBase):
    """
    Class Device
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device")

        self.attributes["params"] = base.ConfigAttribute("DICTIONARY", "Parameters", "A set of device parameters", 90)

    def OnInstanceBeDeleted(self, instance_to_be_deleted):
        helper = Helper(config_header=self.config_header)

        parts = helper.NavigateMultiple("M_COMPONENTS", {"Unit" : instance_to_be_deleted}, "Part")
        for part in parts:
            self.config_header.GetConfigController(part.GetControllerId()).GetStorage().Delete(part)
        
        ClassBase.OnInstanceBeDeleted(self, instance_to_be_deleted)
