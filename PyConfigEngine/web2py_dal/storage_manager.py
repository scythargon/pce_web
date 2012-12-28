# -*- coding: utf-8 -*-
from gluon.sql import *

from .. import base

from storage_header import StorageHeader

class StorageManager(base.StorageManager):
    """
    Provides high-level methods for using the storage
    """
    
    def Connect(self, params):
        """
        Try to connect to the Storage
        """
        #params = dict(uri='sqlite://test_storage.db', pool_size=10)
        try:
            self.connection = DAL(**params)
        except SyntaxError as inst:
            return self.SetErrMsg("Couldn't connect: " + str(inst), 10)
        self.storage_header = StorageHeader(self.connection)
        return True
    
    def StartTransaction(self):
        """
        Start the transaction that could be rolled back or commited
        """
        self.connection.rollback()   #clear all old operations
     
    def FinishTransaction(self, commit):
        """
        Commit or rollback the transaction
        """
        if (commit):
            self.connection.commit()
        else:
            self.connection.rollback()
     
    def ToString(self):
        return "Web2py DAL Storage Manager"
