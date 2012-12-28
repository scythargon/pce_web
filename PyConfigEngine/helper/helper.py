from .. import base

class Helper():
    """
    Helper to simplify script writing
    """
    
    def __init__(self, connection=None, enum_config_objects=None, use_exceptions = False, config_header=None):
        """
        Constructor
        """
        if (config_header):
            self.config_header = config_header
        elif (connection): # Legacy support
            self.config_header = connection.config_header
        else:
            raise Exception("Connection or config_header must be specified")

        self.enum_config_objects = self.config_header.enum_config_objects

        if (enum_config_objects): # Legacy support
            self.enum_config_objects = enum_config_objects

        self.storage_header = self.config_header.storage_header
        self.storage_module = self.storage_header.GetStorageModule()

        self.use_exceptions = use_exceptions
        self.error = None
    
    def SetError(self, error_msg):
        """
        Set Error Message
        """
        if (self.use_exceptions): raise Exception(error_msg)
        self.error = error_msg
        return None
    
    def GetEntities(self, controller_name_id, filter_dict = {}):
        """
        Get Multiple Entities Helper
        """
        key = controller_name_id
        if (type(key) != int): key = self.enum_config_objects[key]
        controller = self.config_header.GetConfigController(key)
        filters = list()
        is_class = isinstance(controller, base.ConfigControllerClass)
        for key,value in filter_dict.iteritems():
            if (is_class):
                filters.append(self.storage_module.StorageExpressionAttributeValue(controller, key, "==", value))
            else:
                filters.append(self.storage_module.StorageExpressionAssociationContains(controller, value.GetInstanceId(), key))
        filter_all = self.storage_module.StorageExpressionAll(*filters)
        entities = controller.GetStorage().GetAll(filter_all)
        for entity in entities:
            self.__LoadEntity(entity)
        return entities
    
    def GetEntity(self, controller_name_id, filter_dict):
        """
        Get Entity Helper
        """
        entities = self.GetEntities(controller_name_id, filter_dict)
        entity = None
        if (len(entities) != 1):
            return self.SetError("Couldn't get specified entity " + str(controller_name_id) + " filter: " + str(filter_dict) + " found: " + str(len(entities)))
        entity = entities[0]
        self.__LoadEntity(entity)
        return entity
        
    def GetEntityByInstanceId(self, instance_id):
        """
        Get Entity by instance_id pair
        """
        controller = self.config_header.GetConfigController(instance_id[0])
        entity = controller.MakeInstance(instance_id[1])
        self.__LoadEntity(entity)
        return entity
        
    def __LoadEntity(self, entity):
        """
        Load entity completely
        """
        controller = self.config_header.GetConfigController(entity.GetControllerId())
        if (not controller.GetStorage().Load(entity)):
            return self.SetError("Couldn't load entity:" + str(entity.GetInstanceId()))
        return True
        
    def Navigate(self, controller_name, associations_filter_dict, role_to_use, instance_filter_dict={}):
        """
        Navigate using model
        """
        entities = self.NavigateMultiple(controller_name, associations_filter_dict, role_to_use, instance_filter_dict)
        if (len(entities) != 1):
            return self.SetError("Couldn't get specified entity " + str(controller_name) + ">" + str(role_to_use) + " filters: assoc=" + str(associations_filter_dict) + ", inst=" + str(instance_filter_dict) + " found: " + str(len(entities)))
        return entities[0]

    def NavigateMultiple(self, controller_name, associations_filter_dict, role_to_use, instances_filter_dict={}):
        """
        Navigate using model
        """
        associations = self.GetEntities(controller_name, associations_filter_dict)
        entities = []
        for association in associations:
            entity = self.GetEntityByInstanceId(association.instance_ids[role_to_use])
            suits = True
            for key,value in instances_filter_dict.iteritems():
                if (key == "class"):
                    if (self.enum_config_objects[value] != entity.GetControllerId()):
                        suits = False
                        break
                elif (key == "cid"):
                    if (value != entity.GetControllerId()):
                        suits = False
                        break
                elif (entity.attributes[key]!=value):
                    suits = False
                    break
            if (suits): entities += [entity]
        return entities

    def CreateEntity(self, controller_name_id):
        if (type(controller_name_id) == str): controller_name_id = self.enum_config_objects[controller_name_id]
        controller = self.config_header.GetConfigController(controller_name_id)
        ret = controller.MakeInstance()
        return ret

    def SaveEntity(self, entity):
        """
        Save Entity From DB
        """
        controller = self.config_header.GetConfigController(entity.GetControllerId())
        if (not controller.GetStorage().Save(entity)):
            return self.SetError("Couldn't save entity:" + str(entity.GetInstanceId()))
        return True

    def DeleteEntity(self, entity):
        """
        Delete Entity From DB
        """
        controller = self.config_header.GetConfigController(entity.GetControllerId())
        if (not controller.GetStorage().Delete(entity)):
            return self.SetError("Couldn't delete entity:" + str(entity.GetInstanceId()))
        return True
