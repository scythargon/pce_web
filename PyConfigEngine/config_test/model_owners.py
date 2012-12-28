# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ModelOwners(base.ConfigControllerModel):
    """
    Provides high-level interface of any model
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.controller_id = EnumConfigObjects["M_OWNERS"];
        association_template = self.MakeInstance()
        association_template.instance_ids["From"] = (EnumConfigObjects["C_HUMAN"], -1)
        association_template.instance_ids["To"] = (EnumConfigObjects["C_PET"], 0)
        validator = base.ConfigControllerModelValidatorMultiplicity(self, association_template, 1)
        self.validator = validator
    
    def DeleteTarget(self, target_instance_id):
        """
        Delete all relations with specified target_instance_id
        """
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by model storage
        """
        return "mdl_owners"
    
    def ToString(self):
        return "Model Owners"
