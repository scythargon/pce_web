from .. import base
from enum_config_objects import *

class ValidatorDeviceName(base.ConfigControllerModelValidator):
    config_header = None
    label = "Device names check"

    def __init__(self, model):
        self.model = model
        
    def LoadInstance(self, instance_id):
        controller = self.config_header.GetConfigController(instance_id[0])
        ret = controller.MakeInstance(instance_id[1])
        controller.GetStorage().Load(ret)
        return ret

    def IsValid(self, association):
        """
        Checks if association suits the model
        """
        self.errors = []
        self.config_header = self.model.GetConfigHeader()

        this_device_instance_id = association.instance_ids["Subject"]
        this_server_instance_id = association.instance_ids["Responsible"]
        if (this_device_instance_id[0] != EnumConfigObjects["C_DEVICE"]): return True
        if (this_server_instance_id[0] != EnumConfigObjects["C_SERVER"]): return True
        this_device = self.LoadInstance(this_device_instance_id)
        this_server = self.LoadInstance(this_server_instance_id)

        storage_module = self.model.GetStorage().GetStorageModule()
        filter = storage_module.StorageExpressionAssociationContains(self.model, this_server.GetInstanceId(), "Responsible")
        links = self.model.GetStorage().GetAll(filter)

        is_valid = True
        for link in links:
            self.model.GetStorage().Load(link)
            other_device = self.LoadInstance(link.instance_ids["Subject"])
            if (other_device.GetInstanceId() == this_device.GetInstanceId()): continue
            if (other_device.attributes["name"] == this_device.attributes["name"]):
                msg = ""
                msg += "Same names of devices:"
                msg += "i(%s, %s), " % this_device.GetInstanceId()
                msg += "i(%s, %s)" % other_device.GetInstanceId()
                self.errors.append(base.ConfigControllerError("Device names of a single server must be unique.", 10, msg))
                is_valid = False

        return is_valid
