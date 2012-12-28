# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassDeviceChannel(ClassBase):
    """
    Class DeviceChannel
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Channel")

        self.attributes["default_value"] = base.ConfigAttribute("DOUBLE", "Default value", "Default value of the channel", 90, "")
