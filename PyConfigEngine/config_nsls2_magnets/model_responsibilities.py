# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase

class ModelResponsibilities(ModelBase):
    """
    Model Responsibilities
    """
    
    roles = ["Responsible", "Subject"]
    unique_roles_set = ["Responsible", "Subject"]

    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Responsibilities")
        
        self.AddAllowedAssociation(Responsible = {"cid" : "C_SERVER", "id" : "ANY"}, Subject = {"cid" : "C_IOC", "id" : "EACH"}, multiplicity=1)
        self.AddAllowedAssociation(Responsible = {"cid" : "C_IOC", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE", "id" : "EACH"}, multiplicity=1)


        self.GenerateValidator()

