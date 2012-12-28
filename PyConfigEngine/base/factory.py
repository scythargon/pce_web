# -*- coding: utf-8 -*-
from object import Object

class Factory(Object):
    """
    Abstract factory for constructing Classes, Models and their Storage Engines
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.__registered = dict()
        self.__keys = list()
    
    def GetRegisteredObjectIds(self):
        """
        Get a list of registered objects' ids
        """
        return self.__keys
    
    def RegisterObject(self, object_id, to_register):
        """
        Register object to be used for constructing instances
        """
        self.__keys.append(object_id)
        self.__registered[object_id] = to_register
    
    def MakeInstance(self, object_id, **params):
        """
        Make instance of the class of specified id
        """
        if (object_id not in self.__keys):
            self.SetErrMsg("Couldn't make instance of unknown class: " + str(object_id) + " Known classes:" + str(self.__registered), 5)
            return None
        return self.__registered[object_id](**params)
    
    def ToString(self):
        return "Factory: " + str(self.__registered)
