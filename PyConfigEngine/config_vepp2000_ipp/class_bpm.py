# -*- coding: utf-8 -*-
from .. import base
from ..helper import Helper

from class_base import ClassBase

class ClassBPM(ClassBase):
    """
    Class BPM
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "BPM")
        self.attributes["address"] = base.ConfigAttribute("INTEGER", "Address", "Block sequence number on the line", 80, "")
        self.attributes["zero_file"] = base.ConfigAttribute("STR255", "Zero file", "Path to the file of zeros", 70, "")
        self.attributes["background_file"] = base.ConfigAttribute("STR255", "Background file", "Background_file", 70, "")