# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase
from ..helper import Helper

class ClassAlgorithmParamaters(ClassBase):
    """
    Class AlgorithmParamaters
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Algorithm Parameters")
        self.attributes["data_backdir_x"] = base.ConfigAttribute("BOOLEAN", "data_backdir_x", "data_backdir_x", 80, False)
        self.attributes["data_backdir_z"] = base.ConfigAttribute("BOOLEAN", "data_backdir_z", "data_backdir_z", 80, False)
        self.attributes["scale_x"] = base.ConfigAttribute("DOUBLE", "scale_x", "scale_x", 80, 0.0)
        self.attributes["scale_z"] = base.ConfigAttribute("DOUBLE", "scale_z", "scale_z", 80, 0.0)


