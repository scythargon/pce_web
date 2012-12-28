# -*- coding: utf-8 -*-
from gluon.sql import *

from .. import base

from simple_engine_class import SimpleEngineClass
from simple_engine_model import SimpleEngineModel

class StorageHeader(base.StorageHeader):
    """
    Information about stored Classes and Models
    """
     
    def __init__(self, connection):
        """
        Constructor
        """
        base.StorageHeader.__init__(self, connection)
        self.storage_engine_factory = base.Factory()
        self.storage_engine_factory.RegisterObject(SimpleEngineClass().GetEngineId(), SimpleEngineClass)
        self.storage_engine_factory.RegisterObject(SimpleEngineModel().GetEngineId(), SimpleEngineModel)
        
        #controller_id, engine_id, title, description, storage_key
        fields = []
        fields.append(Field("controller_id", "integer", unique=True))
        fields.append(Field("engine_id", "integer"))
        fields.append(Field("title", "string", length=100))
        fields.append(Field("description", "text"))
        fields.append(Field("storage_key", "text"))
        self.connection.define_table("header_records", *fields)
        self.connection.commit()

    def GetStorageModule(self):
        """
        Returns Storage Module that this Engine assigns to.
        """
        from .. import web2py_dal as StorageModule
        return StorageModule
    
    def SaveRecord(self, header_record):
        """
        Add or update registration information of an object
        """
        # Should properly process storage_key update.
        old_value = self.GetRecord(header_record.controller_id)
        if (None != old_value and header_record.storage_key != old_value.storage_key):
            self.SetErrMsg("Couldn't change storage key - use migration mechanism: " + str(header_record.storage_key), 10)
            header_record.storage_key = old_value.storage_key
        values = dict()
        values["controller_id"] = header_record.controller_id
        values["engine_id"] = header_record.engine_id
        values["title"] = header_record.title
        values["description"] = header_record.description
        values["storage_key"] = header_record.storage_key
        
        if (None != old_value):
            self.connection(self.connection["header_records"].controller_id==header_record.controller_id).update(**values)
        else:
            self.connection["header_records"].insert(**values)
        return True
        
    def GetRecord(self, controller_id):
        """
        Get Model Storage accoriding to registered information
        """
        values = self.connection(self.connection["header_records"].controller_id==controller_id).select(self.connection["header_records"].ALL).first()
        if (None == values):
            self.SetErrMsg("Couldn't load header information for controller_id: " + str(controller_id), 1)
            return None
        header_record = base.StorageHeaderRecord(values.controller_id, values.engine_id, values.title, values.description, values.storage_key)
        return header_record
        
    def ToString(self):
        return "Web2py Storage Header"
