# -*- coding: utf-8 -*-
from .. import base

from class_human import ClassHuman
from class_pet import ClassPet
from model_friends import ModelFriends
from model_owners import ModelOwners

from enum_config_objects import EnumConfigObjects

class ConfigHeader(base.ConfigHeader):
    """
    Information about configuration parts: Classes and Models
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.object_factory = base.Factory()
        self.object_factory.RegisterObject(ClassHuman().GetConfigControllerId(), ClassHuman)
        self.object_factory.RegisterObject(ClassPet().GetConfigControllerId(), ClassPet)
        self.object_factory.RegisterObject(ModelFriends().GetConfigControllerId(), ModelFriends)
        self.object_factory.RegisterObject(ModelOwners().GetConfigControllerId(), ModelOwners)
        base.ConfigHeader.__init__(self, EnumConfigObjects)

    def ToString(self):
        return "Configuration Header"
