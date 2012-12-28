# -*- coding: utf-8 -*-
from .. import base

from class_bus import ClassBus
from class_bus_type import ClassBusType
from class_bus_controller import ClassBusController
from class_bus_controller_type import ClassBusControllerType
from class_device import ClassDevice
from class_device_type import ClassDeviceType
from class_device_channel import ClassDeviceChannel
from class_device_channel_group import ClassDeviceChannelGroup
from class_server import ClassServer

from model_components import ModelComponents
from model_types import ModelTypes
from model_physical_connections import ModelPhysicalConnections
from model_responsibilities import ModelResponsibilities

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
        self.object_factory.RegisterObject(ClassBus().GetConfigControllerId(), ClassBus)
        self.object_factory.RegisterObject(ClassBusType().GetConfigControllerId(), ClassBusType)
        self.object_factory.RegisterObject(ClassBusController().GetConfigControllerId(), ClassBusController)
        self.object_factory.RegisterObject(ClassBusControllerType().GetConfigControllerId(), ClassBusControllerType)
        self.object_factory.RegisterObject(ClassDevice().GetConfigControllerId(), ClassDevice)
        self.object_factory.RegisterObject(ClassDeviceType().GetConfigControllerId(), ClassDeviceType)
        self.object_factory.RegisterObject(ClassDeviceChannel().GetConfigControllerId(), ClassDeviceChannel)
        self.object_factory.RegisterObject(ClassDeviceChannelGroup().GetConfigControllerId(), ClassDeviceChannelGroup)
        self.object_factory.RegisterObject(ClassServer().GetConfigControllerId(), ClassServer)

        self.object_factory.RegisterObject(ModelComponents().GetConfigControllerId(), ModelComponents)
        self.object_factory.RegisterObject(ModelTypes().GetConfigControllerId(), ModelTypes)
        self.object_factory.RegisterObject(ModelPhysicalConnections().GetConfigControllerId(), ModelPhysicalConnections)
        self.object_factory.RegisterObject(ModelResponsibilities().GetConfigControllerId(), ModelResponsibilities)
        base.ConfigHeader.__init__(self, EnumConfigObjects)

    def ToString(self):
        return "LIA Configuration Header"
