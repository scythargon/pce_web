# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ModelFriends(base.ConfigControllerModel):
    """
    Provides high-level interface of any model
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.controller_id = EnumConfigObjects["M_FRIENDS"];
        association_template1 = self.MakeInstance()
        association_template1.instance_ids["From"] = (EnumConfigObjects["C_HUMAN"], -1)
        association_template1.instance_ids["To"] = (EnumConfigObjects["C_HUMAN"], 0)
        validator1 = base.ConfigControllerModelValidatorMultiplicity(self, association_template1, -1)
        association_template2 = self.MakeInstance()
        association_template2.instance_ids["From"] = (EnumConfigObjects["C_PET"], -1)
        association_template2.instance_ids["To"] = (EnumConfigObjects["C_PET"], 0)
        validator2 = base.ConfigControllerModelValidatorMultiplicity(self, association_template2, -1)
        self.validator = base.ConfigControllerModelValidatorAny(validator1, validator2)

    def DeleteTarget(self, target_instance_id):
        """
        Delete all relations with specified target_instance_id
        """
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by model storage
        """
        return "mdl_friends"
    
    def ToString(self):
        return "Model Friends"
