# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ModelBase(base.StarterKitModel):
    """
    Base model for other in the configuration
    """
    
    def __init__(self, model_name):
        """
        Constructor
        """
        base.StarterKitModel.__init__(self, EnumConfigObjects, model_name)

