# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase
from util_update_group_trigger import updateGroupTrigger
from ..helper import Helper

class ClassDeviceLinkGroup(ClassBase):
    """
    Class DeviceLinkGroup
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Device Link Group")
        self.attributes["quantity"] = base.ConfigAttribute("INTEGER", "Quantity", "The number of links in the group", 80, "")

    def OnInstanceUpdate(self, old_instance, new_instance):
        helper = Helper(config_header=self.config_header)
        return updateGroupTrigger(helper, old_instance, new_instance)