# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase

class ModelTagging(ModelBase):
    """
    Model Tagging
    """
    
    roles = ["Tag", "Subject"]
    unique_roles_set = ["Tag", "Subject"]

    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Tagging")
        
        self.AddAllowedAssociation(Tag = {"cid" : "C_TAG", "id" : "ANY"}, Subject = {"cid" : "C_TAG", "id" : "EACH"}, multiplicity=1)
        self.AddAllowedAssociation(Tag = {"cid" : "C_TAG", "id" : "ANY"}, Subject = {"cid" : "ANY", "id" : "ANY"})


        self.GenerateValidator()

