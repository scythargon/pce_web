# -*- coding: utf-8 -*-
from .. import base
from validator_connectors_match import ValidatorConnectorsMatch
from model_base import ModelBase

class ModelLogicalConnections(ModelBase):
    """
    Model LogicalConnections
    """
    
    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Logical Connections")
        
        self.AddAllowedAssociation(From = {"cid" : "C_DEVICE_LINK", "id" : "EACH"}, To = {"cid" : "C_DEVICE_CHANNEL", "id" : "ANY"}, multiplicity=1)

        self.specific_validator = ValidatorConnectorsMatch(self)

        self.GenerateValidator()

