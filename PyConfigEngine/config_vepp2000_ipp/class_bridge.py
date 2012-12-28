# -*- coding: utf-8 -*-
from .. import base
from ..helper import Helper

from class_base import ClassBase

class ClassBridge(ClassBase):
    """
    Class Bridge
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Bridge")
        self.attributes["can_address"] = base.ConfigAttribute("STR63", "CAN address", "CAN address on the bus", 80, "")
        self.attributes["type"] = base.ConfigAttribute("STR63", "Bridge type", "Type of the bridge", 70, "")
        self.attributes["can_address"] = base.ConfigAttribute("STR63", "CAN address", "CAN address on the bus", 60, "")
        self.attributes["active_line"] = base.ConfigAttribute("INTEGER", "Active line", "ID of active line", 50, "")