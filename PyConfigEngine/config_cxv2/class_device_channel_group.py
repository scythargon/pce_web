# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassDeviceChannelGroup(ClassBase):
    """
    Class DeviceChannelGroup
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Channel Group")
        self.attributes["name"] = base.ConfigAttribute("STR63", "Name", "Short string for fast identification the object by user", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

        self.attributes["is_writable"] = base.ConfigAttribute("BOOLEAN", "Writable", "If channels of the group is writable", 90, "")
        self.attributes["quantity"] = base.ConfigAttribute("INTEGER", "Quantity", "The number of channels in the group", 80, "")
#        self.attributes["length"] = base.ConfigAttribute("INTEGER", "Length", "Length of Value vector for each channel in the group", 70, "")
        self.attributes["group_number"] = base.ConfigAttribute("INTEGER", "Group Number", "The priority for group sorting", 80, "")

