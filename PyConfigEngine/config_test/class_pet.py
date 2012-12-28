# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ClassPet(base.ConfigControllerClass):
    """
    Provides high-level interface of any class
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.controller_id = EnumConfigObjects["C_PET"]
        self.id = None
        self.attributes = dict(nickname = base.ConfigAttribute("STR63", "Nickname", "Nickname of the pet", 90, "No nickname"), animal_kind = base.ConfigAttribute("STR63", "Animal Kind", "Animal Kind of the pet", 100, "Unknown animal"))
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by class storage
        """
        return "cls_pet"
    
    def ToString(self):
        return "Class Pet"
