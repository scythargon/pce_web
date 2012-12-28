# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassBus(ClassBase):
    """
    Class Bus
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Bus")
        self.attributes["name"] = base.ConfigAttribute("STR63", "Name", "Short string for fast identification the object by user", 100, "No name")
        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

#        self.attributes["addr"] = base.ConfigAttribute("STR63", "Address", "Address of the Bus at the Bus Controller", 90, "")
#        self.attributes["init_str"] = base.ConfigAttribute("TEXT", "Initialize String", "String to initialize the Bus by the driver", 80, "")
#        self.attributes["place"] = base.ConfigAttribute("STR255", "Place", "Description of where the Bus could be found", 70, "")

