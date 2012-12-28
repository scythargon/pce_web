# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassBusControllerType(ClassBase):
    """
    Class BusControllerType
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Bus Controller Type")
        self.attributes["name"] = base.ConfigAttribute("STR63", "Name", "Short string for fast identification the object by user", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

        self.attributes["config_format"] = base.ConfigAttribute("TEXT", "Configuration String Format", "Format of the configuration string to be used by driver", 90, "")

