# -*- coding: utf-8 -*-
from ..object import Object
from enum_attributes import EnumAttributes
from enum_attributes import EnumAttributeDefaults

class ConfigAttribute(Object):
    """
    Attribute Interface
    """

    def __init__(self, type_name, title, description = "", priority = 0, default_value = None):
        """
        Constructor
        High priority for more important attributes
        """
        self.default_value = default_value
        self.type = EnumAttributes[type_name]
        self.type_name = type_name
        self.priority = priority
        self.title = title
        self.description = description
        if (None == self.default_value): self.default_value = EnumAttributeDefaults[type_name]

    def GetPriority(self):
        """
        Get Priority of the attribute
        """
        return self.priority
        
    def GetType(self):
        """
        Get Type of the attribute
        """
        return self.type
    
    def GetTypeName(self):
        """
        Get Type of the attribute
        """
        return self.type_name
    
    def GetDefaultValue(self):
        """
        Get default value of the attribute
        """
        return self.default_value
        
    def GetTitle(self):
        return self.title
        
    def ToString(self):
        return self.title + ":" + self.type_name + "[=" + str(self.GetDefaultValue()) + "]"
        
    def GetDescription(self):
        return self.description
