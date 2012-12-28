# -*- coding: utf-8 -*-
from ..object import Object
from config_controller import ConfigController
from config_controller_class_instance import ConfigControllerClassInstance

class ConfigControllerClass(ConfigController):
    """
    Provides high-level interface of any class
    """
    
    controller_id = None
    
    def __init__(self):
        """
        Constructor
        """
        self.attributes = dict()
        self.errors = {}
    
    def MakeInstance(self, new_id=0):
        """
        Make instance of the Class
        """
        instance_id = (self.controller_id, new_id)
        fields = dict()
        for attribute_name, attribute in self.attributes.iteritems():
            fields[attribute_name] = attribute.GetDefaultValue()
        return ConfigControllerClassInstance(instance_id, fields)
        
    def GetAttributes(self):
        """
        Get a dictionary of attributes
        """
        return self.attributes
        
    def GetSortedAttributeNames(self):
        """
        Get Sorted by priority attribute names
        """
        pairs = list()
        for attribute_name, attribute in self.attributes.iteritems():
            pairs.append((attribute.GetPriority(), attribute_name))
        pairs.sort()
        pairs.reverse()
        to_return = list()
        for (priority, attribute_name) in pairs:
            to_return.append(attribute_name)
        return to_return
    
    def GetPreferredStorageName(self):
        """
        Get preferred name for using as a key by class storage
        """
        return "cls_" + str(self.controller_id)
    
    def CheckConsistency(self, fast = False, to_check=[]):
        """
        Check all stored in storage controller's information for consistency
        """
        return True
    
    def GetConsistencyErrors(self):
        """
        Get all consistency errors that are known at the moment
        """
        return ConfigControllerError("Class '" + self.ToString() + "'", 0, "", self.errors.values)
    

    def ToString(self):
        return "Class<" + str(self.controller_id) + ", " + str(self.id) + ">"
