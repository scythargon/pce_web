from .. import base
from enum_config_objects import *
from ..helper import Helper

class ValidatorConnectorsMatch(base.ConfigControllerModelValidator):
    config_header = None
    label = "Device Connections check"

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
        hlp = Helper(config_header=self.config_header)

        link = hlp.GetEntityByInstanceId(association["From"])
        channel = hlp.GetEntityByInstanceId(association["To"])

        link_type = hlp.Navigate("M_TYPES", {"Subject" : link}, "Type")
        channel_type = hlp.Navigate("M_TYPES", {"Subject" : channel}, "Type")



        if (link_type.GetId() != channel_type.GetId()):
            link_device = hlp.Navigate("M_COMPONENTS", {"Part" : link}, "Unit")
            channel_device = hlp.Navigate("M_COMPONENTS", {"Part" : channel}, "Unit")
            msg = "Different connector types. "
            msg += "Link: "
            msg += "i(%s, %s)>" % link_device.GetInstanceId()
            msg += "i(%s, %s)[" % link.GetInstanceId()
            msg += "i(%s, %s)], " % link_type.GetInstanceId()
            msg += "Channel: "
            msg += "i(%s, %s)>" % channel_device.GetInstanceId()
            msg += "i(%s, %s)[" % channel.GetInstanceId()
            msg += "i(%s, %s)]" % channel_type.GetInstanceId()
            self.errors.append(base.ConfigControllerError("Wrong Connection", 10, msg))
            return False
        return True
