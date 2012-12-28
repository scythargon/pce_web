# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassDeviceChannel(ClassBase):
    """
    Class DeviceChannel
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Channel")
        self.attributes["name"] = base.ConfigAttribute("STR63", "Name", "Short string for fast identification the object by user", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

        self.attributes["group_num"] = base.ConfigAttribute("INTEGER", "Group Number", "Address of Channel group at Device channel groups (by its Device Type)", 90, "")
        self.attributes["needs_init"] = base.ConfigAttribute("BOOLEAN", "Needs Initialization", "Is the initialization required by the channel or not", 80, "")
        self.attributes["init_value"] = base.ConfigAttribute("TEXT", "Initialization Value", "The Value to be used if initialization is needed", 70, "")

