# -*- coding: utf-8 -*-
from .. import base
from ..helper import Helper

from model_base import ModelBase
from enum_config_objects import EnumConfigObjects

class ModelTypes(ModelBase):
    """
    Model Types
    """
    
    roles = ["Type", "Subject"]
    unique_roles_set = ["Type", "Subject"]

    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Types")
        
        self.AddAllowedAssociation(Type = {"cid" : "C_BPM_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_BPM", "id" : "EACH"}, multiplicity = 1)

        self.GenerateValidator()
