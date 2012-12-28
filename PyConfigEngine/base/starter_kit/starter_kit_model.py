# -*- coding: utf-8 -*-
from ..config import *

class StarterKitModel(ConfigControllerModel):
    """
    Base model for other in the configuration
    """
    
    def __init__(self, enum_config_objects, model_name):
        """
        Constructor
        """
        self.enum_config_objects = enum_config_objects
        self.model_name = model_name
        self.controller_id = self.enum_config_objects["M_" + model_name.upper().replace(" ", "_")]
        self.storage_key = "mdl_" + model_name.lower().replace(" ", "_")
        self.allowed_associations = []
        self.std_validators = []
        self.specific_validator = None
    
    def AddAllowedAssociation(self, **params):
        """
        Helper for fast association templates creation
        params = {"role" : {"cid" : 10, "id" : "EACH"}, "multiplicity" : 1}
        """
        multiplicity = -1

        instance_key_map = {"cid" : 0, "id" : 1}
        instance_value_map = {"ANY" : 0, "EACH" : -1}

        association_template = self.MakeInstance()
        
        allowed_association = dict()
        for param, param_value in params.iteritems():
            if ("multiplicity" == param):
                multiplicity = param_value
                continue
            if (param in self.roles):
                instance_info = param_value
                role = param
                allowed_association[role] = {"cid" : "ANY", "id" : "ANY"}
                instance_id = [instance_value_map["ANY"], instance_value_map["ANY"]]
                for key, value in instance_info.iteritems():
                    if (key in instance_key_map):
                        instance_value = None
                        if (value in instance_value_map):
                            instance_id[instance_key_map[key]] = instance_value_map[value]
                        elif (key=="cid" and value in self.enum_config_objects):
                            instance_id[instance_key_map[key]] = self.enum_config_objects[value]
                        else:
                            instance_id[instance_key_map[key]] = value
                        allowed_association[role][key] = value
                association_template.instance_ids[role] = instance_id
                continue
            self.SetErrMsg("Couldn't create allowed association using unknown key: " + str(key), 10)
        allowed_association["multiplicity"] = multiplicity
        self.allowed_templates.append(association_template)
        validator = ConfigControllerModelValidatorMultiplicity(self, association_template, multiplicity)
        validator.warning_level = 0
        self.std_validators.append(validator)
        self.allowed_associations.append(allowed_association)
    
    def GetAllowedAssociations(self, target_instance_id = None, target_role = None):
        """
        Get allowed associations
        """
        if (None == target_instance_id): return self.allowed_associations
        to_return = list()
        all_roles = self.roles
        if (None != target_role): all_roles = [target_role,]
        for allowed_association in self.allowed_associations:
            for role in all_roles:
                allowed_cid = allowed_association[role]["cid"]
                allowed_id = allowed_association[role]["id"]
                t_cid = target_instance_id[0]
                t_id = target_instance_id[0]
                co_enum = self.enum_config_objects
                if (allowed_cid in ("ANY", "EACH", t_cid) or (allowed_cid in co_enum and co_enum[allowed_cid] == t_cid)):
                    if (allowed_id in ("ANY", "EACH", t_id)):
                        to_return.append(allowed_association)
                        continue
        return to_return
    
    def GenerateValidator(self):
        """
        Fills validator field using allowed associations std_validator and specific_validator if specified.
        """
        std_validator = ConfigControllerModelValidatorAny(*self.std_validators)
        std_validator.label = "Multiplicities"
        std_validator.warning_level = 5
        if (None == self.specific_validator):
            self.validator = std_validator
        else:
            self.validator = ConfigControllerModelValidatorAll(std_validator, self.specific_validator)
            self.validator.label = "Complex"
        return True
    
    def DeleteTarget(self, target_instance_id):
        """
        Delete all relations with specified target_instance_id
        """
        return True
    
    def GetPreferredStorageKey(self):
        """
        Get preferred name for using as a key by model storage
        """
        return self.storage_key
    
    def ToString(self):
        return self.model_name

