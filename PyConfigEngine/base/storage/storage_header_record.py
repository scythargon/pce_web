# -*- coding: utf-8 -*-
from ..object import Object

class StorageHeaderRecord(Object):
    """
    Information about stored Classes and Models
    """
    
    def __init__(self, controller_id, engine_id, title, description, storage_key):
        """
        Constructor
        """
        self.controller_id = controller_id
        self.engine_id = engine_id
        self.title = title
        self.description = description
        self.storage_key = storage_key
