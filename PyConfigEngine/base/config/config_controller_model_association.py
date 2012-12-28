# -*- coding: utf-8 -*-

class ConfigControllerModelAssociation():
    """
    Relation between two Class instancies
    """
    
    def __init__(self, instance_id=(0,0), instance_ids=None):
        """
        Constructor
        """
        self.cid = instance_id[0]
        self.id = instance_id[1]
        self.instance_ids = instance_ids
        self.is_loaded = False
    
    def __getitem__(self, key):
        return self.instance_ids[key]

    def __setitem__(self, key, value):
        self.instance_ids[key] = value

    def GetControllerId(self):
        """
        Get Controller id
        """
        return self.cid
    
    def GetId(self):
        """
        Gets Id of the Association
        """
        return self.id
        
    def SetId(self, new_id):
        """
        Sets Id of the Association
        """
        self.id = new_id

    def GetInstanceId(self):
        """
        Get Instance id as tuple (controller_id, id)
        """
        return (self.cid, self.id)

    def SetLoaded(self, is_loaded):
        """
        Set the flag that association has been properly loaded
        """
        self.is_loaded = is_loaded
        return True
        
    def IsLoaded(self):
        """
        Check if association has been properly loaded from the storage
        """
        return self.is_loaded
        
    def ToString(self):
        if (not self.is_loaded): return str(self.GetInstanceId())
        return str(self.GetInstanceId()) + ": " + str(self.instance_ids)
