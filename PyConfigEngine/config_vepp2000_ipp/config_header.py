# -*- coding: utf-8 -*-
from .. import base

from class_middleware import ClassMiddleware
from class_server import ClassServer
from class_bridge import ClassBridge
from class_bpm import ClassBPM
from class_bpm_type import ClassBPMType
from class_mode import ClassMode
from class_algorithm import ClassAlgorithm
from class_bridge_group import ClassBridgeGroup
from class_algorithm_parameters import ClassAlgorithmParamaters

from model_types import ModelTypes
from model_logical_connections import ModelLogicalConnections

from enum_config_objects import EnumConfigObjects

class ConfigHeader(base.ConfigHeader):
    """
    Information about configuration parts: Classes and Models
    """
    
    def __init__(self):
        """
        Constructor
        """

        self.object_factory = base.Factory()
        self.object_factory.RegisterObject(ClassMiddleware().GetConfigControllerId(), ClassMiddleware)
        self.object_factory.RegisterObject(ClassServer().GetConfigControllerId(), ClassServer)
        self.object_factory.RegisterObject(ClassBridge().GetConfigControllerId(), ClassBridge)
        self.object_factory.RegisterObject(ClassBPM().GetConfigControllerId(), ClassBPM)
        self.object_factory.RegisterObject(ClassBPMType().GetConfigControllerId(), ClassBPMType)
        self.object_factory.RegisterObject(ClassMode().GetConfigControllerId(), ClassMode)
        self.object_factory.RegisterObject(ClassAlgorithm().GetConfigControllerId(), ClassAlgorithm)
        self.object_factory.RegisterObject(ClassBridgeGroup().GetConfigControllerId(), ClassBridgeGroup)
        self.object_factory.RegisterObject(ClassAlgorithmParamaters().GetConfigControllerId(), ClassAlgorithmParamaters)

        self.object_factory.RegisterObject(ModelTypes().GetConfigControllerId(), ModelTypes)
        self.object_factory.RegisterObject(ModelLogicalConnections().GetConfigControllerId(), ModelLogicalConnections)

        base.ConfigHeader.__init__(self, EnumConfigObjects)

    def ToString(self):
        return "VEPP-2000 IPP Configuration Header"
