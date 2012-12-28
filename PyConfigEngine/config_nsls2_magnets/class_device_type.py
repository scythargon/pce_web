# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase
from ..helper import Helper

class ClassDeviceType(ClassBase):
    """
    Class DeviceType
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Type")

        self.attributes["params"] = base.ConfigAttribute("DICTIONARY", "Parameters", "A set of device parameters", 90, {"PSy" : "BR"})
        self.attributes["template"] = base.ConfigAttribute("STR63", "Template", "Template file for generating IOC's shell commands", 80)

    def OnInstanceBeDeleted(self, instance_to_be_deleted):
        helper = Helper(config_header=self.config_header)

        parts = helper.NavigateMultiple("M_COMPONENTS", {"Unit" : instance_to_be_deleted}, "Part")
        for part in parts:
            self.config_header.GetConfigController(part.GetControllerId()).GetStorage().Delete(part)



