# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase
from validator_device_name import ValidatorDeviceName

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
        
        self.AddAllowedAssociation(Responsible = {"cid" : "C_SERVER", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE", "id" : "EACH"}, multiplicity = 1)

        self.specific_validator = ValidatorDeviceName(self)

        self.GenerateValidator()

