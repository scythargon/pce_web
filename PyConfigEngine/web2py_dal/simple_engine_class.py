# -*- coding: utf-8 -*-
from gluon.sql import *

from .. import base

from enum_engines import EnumEngines
from storage_engine import StorageEngine
import simplejson as json

class SimpleEngineClass(StorageEngine, base.StorageEngineClass):
    """
    Simple Class Storage Engine
    """
    
    engine_id = EnumEngines["SIMPLE_ENGINE_CLASS"]
    
    def __CheckInstance(self, instance):
        """
        Checks if instance corresponds to the controller
        """
        if (self.controller_id != instance.GetControllerId()): return self.SetErrMsg("Couldn't work with instance of different controller: needs " + str(self.controller_id) + ", gotten " + str(instance.GetControllerId()), 10)
        return True
    
    def LaunchEngine(self, class_controller, storage_header, storage_key):
        """
        Launch the storage engine
        """
        self.class_controller = class_controller
        self.controller_id = self.class_controller.GetConfigControllerId()
        self.storage_header = storage_header
        self.db = storage_header.connection
        
        self.table_name = "sec_" + storage_key

        instance = self.class_controller.MakeInstance()
        self.table_declaration = [self.table_name]
        self.instance_fields = list()
        for name,attribute in self.class_controller.attributes.iteritems():
            #TODO: Add more attributes support
            attr_type = attribute.GetType()
            if (attr_type == base.EnumAttributes["TEXT"]):
                field = Field(name, "text", default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["STR255"]):
                field = Field(name, "string", length=255, default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["STR63"]):
                field = Field(name, "string", length=63, default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["DOUBLE"]):
                field = Field(name, "double", default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["FLOAT"]):
                field = Field(name, "double", default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["INTEGER"]):
                field = Field(name, "integer", default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["BOOLEAN"]):
                field = Field(name, "boolean", default=attribute.GetDefaultValue())
            elif (attr_type == base.EnumAttributes["DICTIONARY"]):
                field = Field(name, "text", default=json.dumps(attribute.GetDefaultValue()))
            else:
                return self.SetErrMsg("Engine doesn't support attribute of type #" + str(attribute.GetType()), 10)
            self.table_declaration.append(field)
            self.instance_fields.append(name)
        self.db.define_table(*self.table_declaration)
        return True
        
    def Save(self, instance):
        """
        Save Class instance using current storage
        """
        if (not self.__CheckInstance(instance)): return None
        values = {}
        fld_cnt_needed = len(self.instance_fields)
        fld_cnt_gotten = len(instance.attributes)
        if (fld_cnt_needed != fld_cnt_gotten): return self.SetErrMsg("Couldn't save instance with different sized fields' sets: needs " + str(fld_cnt_needed) + ", gotten " + str(fld_cnt_gotten), 10)
        for name, value in instance.attributes.iteritems():
            if (name not in self.instance_fields): return self.SetErrMsg("Couldn't save instance with different fields' sets: no such stored field as " + name, 10)
            if (self.class_controller.attributes[name].GetType() == base.EnumAttributes["DICTIONARY"]):
                if (type(value) != dict): raise Exception("Dictionary field " + name + " must contain dict() value, but contains: " + str(type(value)))
                value = json.dumps(value)
            values[name] = value
        t_id = instance.GetId()
        if (0 == t_id):
            t_id = self.db[self.table_name].insert(**values)
            if (None == t_id or 0 == t_id): self.SetErrMsg("Couldn't insert record:" + str(values), 7)
            instance.SetId(t_id)
            attrs = list()
            for (key, value) in values.iteritems():
                t_attr = {"key" : key, "value" : value}
                attrs += ["%(key)s: %(value)s" % t_attr]
            self.AddChangeEvent("Instance has been added: i(%s,%s), Attributes: " % instance.GetInstanceId() + ", ".join(attrs) , 3)
            self.class_controller.OnInstanceCreated(instance)
        else:
            old_inst = self.class_controller.MakeInstance(instance.GetId())
            self.Load(old_inst)
            old_values = self.db[self.table_name][t_id].as_dict()
            self.db[self.table_name][t_id] = values
            delta = list()
            attrs_changes = list()
            for (key,new_value) in values.iteritems():
                old_value = old_values[key]
                if (old_value != new_value): 
                    t_delta = {"key" : key, "old_value" : old_value, "new_value" : new_value}
                    delta += [t_delta]
                    attrs_changes += ["%(key)s: %(old_value)s -> %(new_value)s" % t_delta]
            self.AddChangeEvent("Instance has been updated: i(%s,%s) Changed: " % instance.GetInstanceId() + ", ".join(attrs_changes) , 3)
            self.class_controller.OnInstanceUpdate(old_inst, instance)
        instance.SetLoaded(True)
        return True
    
    def Load(self, instance):
        """
        Load Class instance from current storage by instance.GetId()
        """
        if (not self.__CheckInstance(instance)): return None
        record = self.db[self.table_name][instance.GetId()]
        if (None == record): return self.SetErrMsg("Couldn't load record " + str(instance.GetId()) + " from table " + self.table_name, 3)
        for name in instance.attributes.keys():
            if (name in record.keys()):
                value = record[name]
                if (self.class_controller.attributes[name].GetType() == base.EnumAttributes["DICTIONARY"]):
                    if (value):
                        value = json.loads(value)
                    else:
                        value = {}
                instance.attributes[name] = value
            else:
                return self.SetErrMsg("Couldn't load instance with different fields' sets: no such loaded field as " + name, 7)
        instance.SetLoaded(True)
        return True
    
    def Delete(self, instance):
        """
        Delete Class instance from current storage by id
        """
        values = self.db[self.table_name][instance.GetId()].as_dict()
        attrs = list()
        for (key, value) in values.iteritems():
            t_attr = {"key" : key, "value" : value}
            attrs += ["%(key)s: %(value)s" % t_attr]
        self.AddChangeEvent("Instance has been deleted: i(%s,%s) Attributes: " % instance.GetInstanceId() + ", ".join(attrs) , 3)
        if (not self.__CheckInstance(instance)): return None
        self.class_controller.OnInstanceBeDeleted(instance)
        del self.db[self.table_name][instance.GetId()]
        instance.SetId(0)
        instance.SetLoaded(False)
        return True

    def GetAll(self, filter_expression=None):
        """
        Load All instances from current storage. Filter could be used
        """
        to_return = []
        query = None
        if (None != filter_expression): query = filter_expression.GetQuery(self.storage_header)
        raws = self.db(query).select(self.db[self.table_name].id)
        for raw in raws:
            to_return.append(self.class_controller.MakeInstance(raw.id))
        return to_return
    
    def ToString(self):
        return "Web2py Simple Class Storage"
