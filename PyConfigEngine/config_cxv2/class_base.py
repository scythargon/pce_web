# -*- coding: utf-8 -*-
from .. import base

from enum_config_objects import EnumConfigObjects

class ClassBase(base.StarterKitClass):
    """
    Base class for other in the configuration
    """
    
    def __init__(self, class_name):
        """
        Constructor
        """
        base.StarterKitClass.__init__(self, EnumConfigObjects, class_name)
        self.attributes["dbg_import_key"] = base.ConfigAttribute("STR255", "Debug Import Key", "Unique key to identify object during import (to preserve objects locations in plugins)", 0, "---")

