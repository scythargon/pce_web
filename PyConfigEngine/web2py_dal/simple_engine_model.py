# -*- coding: utf-8 -*-
from gluon.sql import *

from .. import base

from enum_engines import EnumEngines
from storage_expressions import *
from storage_engine import StorageEngine

def ToDictionary(association):
    """
    Gets all inner data as dictionary
    """
    values = dict()
    for role, instance_id in association.instance_ids.iteritems():
        values[role + "_cid"] = instance_id[0]
        values[role + "_id"] = instance_id[1]
    return values

def FromDictionary(association, values):
    """
    Constructs association from the dictionary
    """
    for role, instance_id in association.instance_ids.iteritems():
        if (role + "_cid" in values.keys() and role + "_id" in values.keys()):
            association.instance_ids[role] = (values[role + "_cid"], values[role + "_id"])
    return True

class SimpleEngineModel(StorageEngine, base.StorageEngineModel):
    """
    Simple Model Storage Engine
    """
    
    engine_id = EnumEngines["SIMPLE_ENGINE_MODEL"]

    def __CheckInstance(self, instance):
        """
        Checks if instance corresponds to the controller
        """
        if (self.controller_id != instance.GetControllerId()): return self.SetErrMsg("Couldn't work with instance of different controller: needs " + str(self.controller_id) + ", gotten " + str(instance.GetControllerId()), 10)
        return True
    
    def LaunchEngine(self, model_controller, storage_header, storage_key):
        """
        Launch the storage engine
        """
        self.model_controller = model_controller
        self.controller_id = self.model_controller.GetConfigControllerId()
        self.storage_header = storage_header
        self.db = storage_header.connection
        
        instance = self.model_controller.MakeInstance()
        values = ToDictionary(instance)
        
        self.table_name = "sem_" + storage_key
        self.table_declaration = [self.table_name]
        for key, value in values.iteritems():
            self.table_declaration.append(Field(key, "integer"))
        self.db.define_table(*self.table_declaration)
        
        return True

    def Save(self, model_association):
        """
        Add or update association between instances
        """
        if (not self.__CheckInstance(model_association)): return None
        values = ToDictionary(model_association)

        filter_expression = None
        for role, instance_id in model_association.instance_ids.iteritems():
            if role not in self.model_controller.unique_roles_set: continue
            if (None == filter_expression):
                filter_expression = StorageExpressionAssociationContains(self.model_controller, instance_id, role)
            else:
                filter_expression = StorageExpressionAll(filter_expression, StorageExpressionAssociationContains(self.model_controller, instance_id, role))
        
        # TODO: bug if updated association duplicates existing one. 
        ids = self.GetAll(filter_expression)
        if (len(ids) > 0): model_association.SetId(ids[0].GetId())
                
        if (0 != model_association.GetId()):
            old_association = self.model_controller.MakeInstance(model_association.GetId())
            if (not self.Load(old_association)): return None
            self.db[self.table_name][model_association.GetId()] = values

            insts = list()
            for (role, new_instance) in model_association.instance_ids.iteritems():
                old_instance = old_association.instance_ids[role]
                if (new_instance != old_instance):
                    insts += ["%s: i%s -> i%s" % (role, old_instance, new_instance)]
            self.AddChangeEvent("Association has been updated: a(%s,%s) Changed: " % model_association.GetInstanceId() + ", ".join(insts) , 3)
        else:
            new_id = self.db[self.table_name].insert(**values)
            if (0 == new_id or None == new_id):
                return self.SetErrMsg("Unable to save association: " + str(ToDictionary(model_association)), 7)
            model_association.SetId(new_id)

            insts = list()
            for (role, new_instance) in model_association.instance_ids.iteritems():
                insts += ["%s: i%s" % (role, new_instance)]
            self.AddChangeEvent("Association has been added: a(%s,%s) Instances: " % model_association.GetInstanceId() + ", ".join(insts) , 3)
            self.model_controller.OnInstanceCreated(model_association)
        model_association.SetLoaded(True)
        return True
        
    def Load(self, model_association):
        """
        Get association by its id
        """
        if (not self.__CheckInstance(model_association)): return None
        row = self.db[self.table_name][model_association.GetId()]
        if (None == row): return self.SetErrMsg("Association not found by id: " + str(model_association.GetInstanceId()), 7)
        if (not FromDictionary(model_association, row)): return self.SetErrMsg("Association could not be obtained from row: " + str(row), 10)
        model_association.SetLoaded(True)
        return True

    def Delete(self, model_association):
        """
        Delete association between instances
        """
        if (not self.__CheckInstance(model_association)): return None
        if (0 == model_association.GetId()):
            return self.SetErrMsg("Unable to delete unsaved association", 7)

        if (not self.Load(model_association)): return None
        insts = list()
        for (role, new_instance) in model_association.instance_ids.iteritems():
            insts += ["%s: i%s" % (role, new_instance)]
        self.AddChangeEvent("Association has been deleted: a(%s,%s) Instances: " % model_association.GetInstanceId() + ", ".join(insts) , 3)

        del self.db[self.table_name][model_association.GetId()]
        model_association.SetId(0)
        model_association.SetLoaded(False)
        return True

    def GetAll(self, filter_expression = None):
        """
        Get ids of specific associations in the model
        """
        to_return = []
        query = None
        if (None != filter_expression): query = filter_expression.GetQuery(self.storage_header)
        rows = self.db(query).select(self.db[self.table_name].id)
        for row in rows:
            to_return.append(self.model_controller.MakeInstance(row["id"]))
        return to_return

    def ToString(self):
        return "Web2py Simple Model Storage"
