# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ClassHuman(base.ConfigControllerClass):
    """
    Provides high-level interface of any class
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.controller_id = EnumConfigObjects["C_HUMAN"]
        self.id = None
        self.attributes = dict(name = base.ConfigAttribute("STR63", "Name", "Name of a person", 100, "No name"), surname = base.ConfigAttribute("STR63", "Surname", "Surname of a person", 90, "No surname"))
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by class storage
        """
        return "cls_human"
    
    def ToString(self):
        return "Class Human"
