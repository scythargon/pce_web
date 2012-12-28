# -*- coding: utf-8 -*-
from .. import base

class StorageEngine(base.StorageEngine):
    """
    Storage Engine Interface
    """
    
    def GetStorageModule(self):
        """
        Returns Storage Module that this Engine assigns to.
        """
        from .. import web2py_dal as StorageModule
        return StorageModule

