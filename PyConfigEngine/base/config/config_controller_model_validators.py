# -*- coding: utf-8 -*-
from ..object import Object
from config_controller_error import ConfigControllerError

class ConfigControllerModelValidator(Object):
    """
    Base interface for creating Consistency rules for models
    """
    
    last_checked = None
    label = "Unnamed Error"
    warning_level = 1
    description = ""
    errors = []
    
    def GetValidationError(self):
        """
        Get errors caused by validation as XML
        """
        return ConfigControllerError(self.label, self.warning_level, self.description, self.errors)
    
    def IsValid(self, association):
        """
        Checks if association suits the model
        """
        raise Exception(str(self) + ": Method not implemented")
        
class ConfigControllerModelValidatorAll(ConfigControllerModelValidator):
    """
    Base interface for creating Consistency rules for models
    """
    
    label = "Fix all next errors to make it valid"
    
    def __init__(self, *validators):
        """
        Constructor
        """
        self.validators = validators
    
    def IsValid(self, association):
        """
        Checks if association suits the model
        """
        self.errors = []
        no_error = True
        for validator in self.validators:
            if (not validator.IsValid(association)):
                self.errors.append(validator.GetValidationError())
                no_error = False
        return no_error
        
class ConfigControllerModelValidatorAny(ConfigControllerModelValidator):
    """
    Base interface for creating Consistency rules for models
    """
    
    label = "Fix any of next errors to make it valid"
    
    def __init__(self, *validators):
        """
        Constructor
        """
        self.validators = validators
    
    def IsValid(self, association):
        """
        Checks if association suits the model
        """
        self.errors = []
        no_error = False
        for validator in self.validators:
            if (not validator.IsValid(association)):
                self.errors.append(validator.GetValidationError())
            else:
                no_error = True
        return no_error

        
class ConfigControllerModelValidatorMultiplicity(ConfigControllerModelValidator):
    """
    Base interface for creating Consistency rules for models
    """
    
    label = "Multiplicity check"
    
    model = None
    
    def __init__(self, model, association_template, multiplicity):
        """
        Constructor
        association_template: 
        use standard model_association to specify a template
        fill class_id and id by 0 - for any value, -1 - for current_association value, >0 for constant value
        multiplicity: -1 - any number, >1 - max allowed number
        """
        self.model = model
        self.association_template = association_template
        self.multiplicity = multiplicity
    
    def GetTemplateDescription(self):
        """
        Beautify template description
        """
        error_msg = "Allowed "
        if (self.multiplicity > 0):
            error_msg += "maximum of " + str(self.multiplicity) + " association(s): "
        else:
            error_msg += " association(s): "
        for role in self.model.roles:
            if (role != self.model.roles[0]): error_msg += ", "
            template_instance_id = self.association_template.instance_ids[role]
            error_msg += role + ": "
            if ((0, 0) == template_instance_id):
                error_msg += "any instance of any class"
                continue
            if (0 == template_instance_id[1] and template_instance_id[0] > 0):
                error_msg += "any instance of c(" + str(template_instance_id[0]) + ") "
                continue
            if (-1 == template_instance_id[1] and template_instance_id[0] > 0):
                error_msg += "each instance of c(" + str(template_instance_id[0]) + ") "
                continue
            error_msg += str(template_instance_id)
        return error_msg

    def IsValid(self, association):
        """
        Checks if association suits the model
        """
        self.errors = []
        if (None == self.model):
            raise Exception("None model passed to the validator")
        l1 = len(self.association_template.instance_ids)
        l2 = len(association.instance_ids)
        if (l1 != l2):
            self.SetErrMsg("Wrong roles number in a model '" + self.model.ToString() + "': awaiting " + str(l1) + ", gotten " + str(l2), 10)
            return False
        
        model_storage = self.model.GetStorage()
        if (None == model_storage):
            self.SetErrMsg("Couldn't get storage of a model: " + self.model.ToString(), 10)
            return False
        
        storage_module = model_storage.GetStorageModule()
        
        cur_filter_expression = None
        for role, template_instance_id in self.association_template.instance_ids.iteritems():
            filter_instance_id = [0,0]
            for i in (0,1):
                if (template_instance_id[i] == -1):
                    filter_instance_id[i] = association.instance_ids[role][i]
                if (template_instance_id[i] > 0):
                    filter_instance_id[i] = association.instance_ids[role][i]
                    if (template_instance_id[i] != association.instance_ids[role][i]):
                        self.errors.append(ConfigControllerError("Rule isn't applicable", 0, self.GetTemplateDescription()))
                        return False
            new_expression = storage_module.StorageExpressionAssociationContains(self.model, filter_instance_id, role)
            if (None == cur_filter_expression):
                cur_filter_expression = new_expression
            else:
                cur_filter_expression = storage_module.StorageExpressionAll(cur_filter_expression, new_expression)
        
        if (None == cur_filter_expression):
            raise Exception("Bad template association has been passed to the multiplicity validator of the model: " + self.model.ToString())
        found_associations = model_storage.GetAll(cur_filter_expression)
        stored_association_number = len(found_associations)
        if (not association.IsLoaded()):
            stored_association_number += 1
        
        if (-1 == self.multiplicity): return True
        #if (0 == self.multiplicity): raise Exception("Bad multiplicity specified")
        if (0 <= self.multiplicity and stored_association_number > self.multiplicity):
            error_msg = "Found " + str(stored_association_number) + " association(s) : "
            for association in found_associations:
                if (association != found_associations[0]): error_msg += ", "
                error_msg += "a" + str(association.GetInstanceId())
            error_msg += ". "
            error_msg += self.GetTemplateDescription()
            self.errors.append(ConfigControllerError("Too many associations", 7, error_msg))
            return False
        return True
