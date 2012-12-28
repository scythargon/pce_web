# -*- coding: utf-8 -*-
from .. import base

from model_base import ModelBase

class ModelPhysicalConnections(ModelBase):
    """
    Model PhysicalConnections
    """
    
    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Physical Connections")
        
        self.AddAllowedAssociation(From = {"cid" : "C_SERVER", "id" : "EACH"}, To = {"cid" : "C_BUS_CONTROLLER", "id" : "ANY"})
        self.AddAllowedAssociation(From = {"cid" : "C_BUS_CONTROLLER", "id" : "EACH"}, To = {"cid" : "C_BUS", "id" : "ANY"})
        self.AddAllowedAssociation(From = {"cid" : "C_BUS", "id" : "EACH"}, To = {"cid" : "C_DEVICE", "id" : "ANY"})

        self.GenerateValidator()

