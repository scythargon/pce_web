# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase

class ModelComponents(ModelBase):
    """
    Model Components
    """
    
    roles = ["Unit", "Part"]
    unique_roles_set = ["Unit", "Part"]

    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Components")
        
        self.AddAllowedAssociation(Unit = {"cid" : "C_DEVICE_TYPE", "id" : "EACH"}, Part = {"cid" : "C_DEVICE_CHANNEL_GROUP", "id" : "ANY"})
        self.AddAllowedAssociation(Unit = {"cid" : "C_DEVICE_TYPE", "id" : "EACH"}, Part = {"cid" : "C_DEVICE_LINK_GROUP", "id" : "ANY"})
        self.AddAllowedAssociation(Unit = {"cid" : "C_DEVICE", "id" : "EACH"}, Part = {"cid" : "C_DEVICE_CHANNEL", "id" : "ANY"})
        self.AddAllowedAssociation(Unit = {"cid" : "C_DEVICE", "id" : "EACH"}, Part = {"cid" : "C_DEVICE_LINK", "id" : "ANY"})

        self.GenerateValidator()
