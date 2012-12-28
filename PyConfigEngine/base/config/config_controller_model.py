# -*- coding: utf-8 -*-
from ..object import Object
from config_controller import ConfigController
from config_controller_error import ConfigControllerError
from config_controller_model_association import ConfigControllerModelAssociation

class ConfigControllerModel(ConfigController):
    """
    Provides high-level interface of any model
    """
    
    roles = ["From", "To"]
    unique_roles_set = ["From", "To"]
    validator = None
    allowed_templates = []
    
    def GetRoles(self):
        """
        Get Model Roles
        """
        return self.roles
    
    def MakeInstance(self, new_id=0):
        """
        Make instance of model association
        """
        instance_id = (self.controller_id, new_id)
        fields = dict()
        for role in self.roles:
            fields[role] = (0,0)
        return ConfigControllerModelAssociation(instance_id, fields)

    def CheckTarget(self, target_instance_id):
        """
        Check target class instance for correct model relations
        """
        model_storage = self.GetStorage()
        storage_module = model_storage.GetStorageModule()
        filter_expression = None
        for role in roles:
            new_filter_expression = storage_module.StorageExpressionAssociationContains(self, target_instance_id, role)
            if (None == filter_expression):
                filter_expression = new_filter_expression
            else:
                filter_expression = storage_module.StorageExpressionAny(filter_expression, new_filter_expression)
        if (None == filter_expression): raise Exception("Couldn't compose proper filter - check model association roles")
        associations = model_storage.GetAll(filter_expression)
        
        return self.__CheckAssociations(associations)
    
    def CheckConsistency(self, fast=False, to_check=[]):
        """
        Check whole model for correct model relations (consistency check)
        """
        model_storage = self.GetStorage()
        associations = []
        if (fast):
            for instance_id in to_check:
                associations.append(self.MakeInstance(instance_id[1]))
        else:
            associations = model_storage.GetAll()
        return self.__CheckAssociations(associations)
    
    def __CheckAssociations(self, associations):
        """
        Check Association List
        """
        if (None == self.validator): raise Exception("No model validator to check its consistency")
        model_storage = self.GetStorage()
        storage_module = model_storage.GetStorageModule()
        self.errors = {}
        no_errors = True
        for association in associations:
            if (not model_storage.Load(association)): continue
            if (not self.validator.IsValid(association)):
                self.errors[association.GetInstanceId()] = self.validator.GetValidationError()
                no_errors = False
        return no_errors
    
    def GetConsistencyErrors(self):
        """
        Get all consistency errors that are known at the moment
        """
        return self.errors
    
    def DeleteTarget(self, target_instance_id):
        """
        Delete all relations with specified target_instance_id
        """
        raise Exception(str(self) + ": Method not implemented")
    
    def GetPreferredStorageName(self):
        """
        Get preferred name for using as a key by model storage
        """
        return "mdl_" + str(self.controller_id)
    
    def ToString(self):
        return "Model_" + str(self.controller_id)
