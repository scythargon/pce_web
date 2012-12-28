# -*- coding: utf-8 -*-
from .. import base

from class_server import ClassServer
from class_ioc import ClassIOC
from class_device import ClassDevice
from class_device_type import ClassDeviceType
from class_device_channel import ClassDeviceChannel
from class_device_channel_group import ClassDeviceChannelGroup
from class_device_link import ClassDeviceLink
from class_device_link_group import ClassDeviceLinkGroup
from class_device_connector_type import ClassDeviceConnectorType
from class_tag import ClassTag

from model_components import ModelComponents
from model_types import ModelTypes
from model_logical_connections import ModelLogicalConnections
from model_responsibilities import ModelResponsibilities
from model_tagging import ModelTagging

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
        self.object_factory.RegisterObject(ClassServer().GetConfigControllerId(), ClassServer)
        self.object_factory.RegisterObject(ClassIOC().GetConfigControllerId(), ClassIOC)
        self.object_factory.RegisterObject(ClassDevice().GetConfigControllerId(), ClassDevice)
        self.object_factory.RegisterObject(ClassDeviceType().GetConfigControllerId(), ClassDeviceType)
        self.object_factory.RegisterObject(ClassDeviceChannel().GetConfigControllerId(), ClassDeviceChannel)
        self.object_factory.RegisterObject(ClassDeviceChannelGroup().GetConfigControllerId(), ClassDeviceChannelGroup)
        self.object_factory.RegisterObject(ClassDeviceLink().GetConfigControllerId(), ClassDeviceLink)
        self.object_factory.RegisterObject(ClassDeviceLinkGroup().GetConfigControllerId(), ClassDeviceLinkGroup)
        self.object_factory.RegisterObject(ClassDeviceConnectorType().GetConfigControllerId(), ClassDeviceConnectorType)
        self.object_factory.RegisterObject(ClassTag().GetConfigControllerId(), ClassTag)

        self.object_factory.RegisterObject(ModelComponents().GetConfigControllerId(), ModelComponents)
        self.object_factory.RegisterObject(ModelTypes().GetConfigControllerId(), ModelTypes)
        self.object_factory.RegisterObject(ModelResponsibilities().GetConfigControllerId(), ModelResponsibilities)
        self.object_factory.RegisterObject(ModelLogicalConnections().GetConfigControllerId(), ModelLogicalConnections)
        self.object_factory.RegisterObject(ModelTagging().GetConfigControllerId(), ModelTagging)

        base.ConfigHeader.__init__(self, EnumConfigObjects)

    def ToString(self):
        return "NSLS II Magnets Configuration Header"
