# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassDeviceType(ClassBase):
    """
    Class DeviceType
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Type")
        self.attributes["name"] = base.ConfigAttribute("STR63", "Name", "Short string for fast identification the object by user", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

        self.attributes["bigc_info"] = base.ConfigAttribute("TEXT", "Big Channel Info", "Big channel information [should be temporal]", 50, "")

