# -*- coding: utf-8 -*-
from .. import base

from config_header import ConfigHeader

class ConfigManager(base.ConfigManager):
    """
    Provides high-level methods for using the configuration
    """
    
    def __init__(self):
        self.config_header = ConfigHeader()
    
    def ToString(self):
        return "Test Configuration Manager"
