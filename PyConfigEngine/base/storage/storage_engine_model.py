# -*- coding: utf-8 -*-
from storage_engine import StorageEngine

class StorageEngineModel(StorageEngine):
    """
    Model Storage Engine Interface
    """
    
    def Save(self, model_association):
        """
        Add or update association between instances
        """
        raise Exception(str(self) + ": Method not implemented")

    def Load(self, model_association):
        """
        Load association by its id
        """
        raise Exception(str(self) + ": Method not implemented")

    def Delete(self, model_association):
        """
        Delete association by its id
        """
        raise Exception(str(self) + ": Method not implemented")

    def GetAll(self, filter_expression = None):
        """
        Get specific associations of the model
        """
        raise Exception(str(self) + ": Method not implemented")

    def ToString(self):
        return "ModelStorage"
