# -*- coding: utf-8 -*-

class ConfigControllerClassInstance():
    """
    Class Instance - atomic configuration information
    """
    
    def __init__(self, instance_id=(0,0), attributes=None):
        """
        Constructor
        """
        self.cid = instance_id[0]
        self.id = instance_id[1]
        self.attributes = attributes
        self.is_loaded = False

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def GetControllerId(self):
        """
        Get Controller id
        """
        return self.cid
    
    def GetId(self):
        """
        Get id
        """
        return self.id
    
    def SetId(self, new_id):
        """
        Set id
        """
        self.id = new_id
        return True
    
    def GetInstanceId(self):
        """
        Get Instance id as tuple (controller_id, id)
        """
        return (self.cid, self.id)

    def SetLoaded(self, is_loaded):
        """
        Set the flag that instance has been properly loaded
        """
        self.is_loaded = is_loaded
        return True
        
    def IsLoaded(self):
        """
        Check if instance has been properly loaded from the storage
        """
        return self.is_loaded
        
    def ToString(self):
        if (not self.is_loaded): return str(self.GetInstanceId())
        return str(self.GetInstanceId()) + ": " + str(self.attributes)
