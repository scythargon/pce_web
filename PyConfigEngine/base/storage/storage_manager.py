# -*- coding: utf-8 -*-
from ..object import Object

class StorageManager(Object):
    """
    Provides high-level methods for using the storage
    """

    def __init__(self):
        """
        Constructor
        """
        self.storage_header = None
    
    def Connect(self, params):
        """
        Try to connect to the Storage
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def GetStorageHeader(self):
        """
        Get storage header
        """
        return self.storage_header
    
    def StartTransaction(self):
        """
        Start the transaction that could be rolled back or commited
        """
        raise Exception(str(self) + ": Method not implemented")
     
    def FinishTransaction(self, commit):
        """
        Commit or rollback the transaction
        """
        raise Exception(str(self) + ": Method not implemented")

    def GetConnection(self):
        """
        Gets db connection
        """
        return self.storage_header.connection
    
    def ToString(self):
        return "Storage Manager"
