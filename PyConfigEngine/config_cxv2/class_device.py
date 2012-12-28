# -*- coding: utf-8 -*-
from .. import base

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
        self.attributes["readable_name"] = base.ConfigAttribute("STR63", "Readable Name", "Short string for fast identification the object by user", 150, "No name")
        self.attributes["name"] = base.ConfigAttribute("STR63", "API Name", "Short string for fast identification the object by programs", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

        self.attributes["addr"] = base.ConfigAttribute("STR63", "Address", "Address of the Device at the Bus", 90, "")
        self.attributes["init_str"] = base.ConfigAttribute("TEXT", "Initialize String", "String to initialize the Device by the driver", 80, "")
#        self.attributes["place"] = base.ConfigAttribute("STR255", "Place", "Description of where the Device could be found", 70, "")
        self.attributes["sequence_number"] = base.ConfigAttribute("INTEGER", "Sequence Number", "Sequence number for sorting devices during export", 30, "")

