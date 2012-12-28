# -*- coding: utf-8 -*-

class ConfigControllerError:
    """
    Container of tree-formed sub-errors
    """
    
    def __init__(self, label, warning_level, description="", sub_errors=[]):
        """
        Constructor
        """
        self.label = label
        self.warning_level = warning_level
        self.description = description
        self.sub_errors = sub_errors
        self.max_warning_level = self.warning_level
        for error in self.sub_errors:
            if (error.max_warning_level > self.max_warning_level): self.max_warning_level = error.max_warning_level

