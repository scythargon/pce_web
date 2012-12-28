# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase
from ..helper import Helper

class ClassBPMType(ClassBase):
    """
    Class BPMType
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "BPM Type")
        #self.attributes["I_koef"] = base.ConfigAttribute("DOUBLE", "I_koef", "I_koef", 80, 0.0)
        #self.attributes["step_x"] = base.ConfigAttribute("DOUBLE", "step_x", "step_x", 80, 0.0)
        #self.attributes["step_z"] = base.ConfigAttribute("DOUBLE", "step_z", "step_z", 80, 0.0)
        #self.attributes["shear_x"] = base.ConfigAttribute("DOUBLE", "shear_x", "shear_x", 80, 0.0)
        #self.attributes["shear_z"] = base.ConfigAttribute("DOUBLE", "shear_z", "shear_z", 80, 0.0)
        #self.attributes["angle"] = base.ConfigAttribute("DOUBLE", "angle", "angle", 80, 0.0)

        self.attributes["sensor_type"] = base.ConfigAttribute("STR63", "Sensor_type", "PIC or IPP", 80, "")
        self.attributes["params"] = base.ConfigAttribute("DICTIONARY", "params", "List of parameters depending on BPM type.", 80, {"I_koef":"", "step_x":"", "step_z":"", "shear_x":"", "shear_z":"", "angle":""})
