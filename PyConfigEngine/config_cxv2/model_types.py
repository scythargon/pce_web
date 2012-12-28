# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase

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
        
        self.AddAllowedAssociation(Type = {"cid" : "C_BUS_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_BUS", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_BUS_CONTROLLER_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_BUS_CONTROLLER", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE", "id" : "EACH"}, multiplicity = 1)

        self.GenerateValidator()
