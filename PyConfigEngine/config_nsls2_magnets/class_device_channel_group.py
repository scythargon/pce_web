# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase
from util_update_group_trigger import updateGroupTrigger
from ..helper import Helper

class ClassDeviceChannelGroup(ClassBase):
    """
    Class DeviceChannelGroup
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Channel Group")

        self.attributes["is_writable"] = base.ConfigAttribute("BOOLEAN", "Writable", "If channels of the group is writable", 90, "")
        self.attributes["quantity"] = base.ConfigAttribute("INTEGER", "Quantity", "The number of channels in the group", 80, "1")
        self.attributes["min_value"] = base.ConfigAttribute("DOUBLE", "Minimum value", "Default minimum value of each channel in the group", 72, "")
        self.attributes["max_value"] = base.ConfigAttribute("DOUBLE", "Maximum value", "Default maximum value of each channel in the group", 71, "")
        self.attributes["default_value"] = base.ConfigAttribute("DOUBLE", "Default value", "Default value of each channel in the group", 70, "")
	self.attributes["params"] = base.ConfigAttribute("DICTIONARY", "Parameters", "A set of channel parameters", 60)

    def OnInstanceUpdate(self, old_instance, new_instance):
        helper = Helper(config_header=self.config_header)
        return updateGroupTrigger(helper, old_instance, new_instance)