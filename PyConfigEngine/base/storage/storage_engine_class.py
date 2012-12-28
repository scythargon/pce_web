# -*- coding: utf-8 -*-
from storage_engine import StorageEngine

class StorageEngineClass(StorageEngine):
    """
    Class Storage Engine Interface
    """
     
    def Save(self, instance):
        """
        Save Class instance using current storage
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def Load(self, instance):
        """
        Load Class instance from current storage by instance.GetId()
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def Delete(self, instance):
        """
        Delete Class instance from current storage by id
        """
        raise Exception(str(self) + ": Method not implemented")

    def GetAll(self, filter_expression=None):
        """
        Load instance_ids of instances from current storage. Filter could be used
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def ToString(self):
        return "ClassStorage"
