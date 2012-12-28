# -*- coding: utf-8 -*-
from .. import base

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
        
        self.AddAllowedAssociation(From = {"cid" : "C_MIDDLEWARE", "id" : "EACH"}, To = {"cid" : "C_SERVER", "id" : "ANY"}, multiplicity=1)
        self.AddAllowedAssociation(From = {"cid" : "C_SERVER", "id" : "EACH"}, To = {"cid" : "C_BRIDGE", "id" : "ANY"}, multiplicity=1)
        self.AddAllowedAssociation(From = {"cid" : "C_BRIDGE", "id" : "EACH"}, To = {"cid" : "C_BPM", "id" : "ANY"}, multiplicity=1)
        self.AddAllowedAssociation(From = {"cid" : "C_BRIDGE_GROUP", "id" : "ANY"}, To = {"cid" : "C_BRIDGE", "id" : "ANY"})
        self.AddAllowedAssociation(From = {"cid" : "C_BPM", "id" : "ANY"}, To = {"cid" : "C_ALGORITHM_PARAMETERS", "id" : "ANY"})
        self.AddAllowedAssociation(From = {"cid" : "C_MODE", "id" : "EACH"}, To = {"cid" : "C_ALGORITHM_PARAMETERS", "id" : "ANY"})
        self.AddAllowedAssociation(From = {"cid" : "C_ALGORITHM", "id" : "EACH"}, To = {"cid" : "C_ALGORITHM_PARAMETERS", "id" : "ANY"})

        self.GenerateValidator()

