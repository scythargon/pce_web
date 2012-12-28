# -*- coding: utf-8 -*-
from .. import base
from ..helper import Helper

from model_base import ModelBase
from enum_config_objects import EnumConfigObjects
from util_create_group_item import createGroupItem

class ModelTypes(ModelBase):
    """
    Model Types
    """
    
    roles = ["Type", "Subject"]
    unique_roles_set = ["Type", "Subject"]

    def __init__(self):
        """
        Constructor
        """
        ModelBase.__init__(self, "Types")
        
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_CHANNEL_GROUP", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE_CHANNEL", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_LINK_GROUP", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE_LINK", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_CONNECTOR_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE_CHANNEL_GROUP", "id" : "EACH"}, multiplicity = 1)
        self.AddAllowedAssociation(Type = {"cid" : "C_DEVICE_CONNECTOR_TYPE", "id" : "ANY"}, Subject = {"cid" : "C_DEVICE_LINK_GROUP", "id" : "EACH"}, multiplicity = 1)

        self.GenerateValidator()

    def OnInstanceCreated(self, created_association):
        """
        Trigger for creations
        """

        device_type_instance_id = created_association.instance_ids["Type"]
        device_instance_id = created_association.instance_ids["Subject"]

        if (device_type_instance_id[0] == EnumConfigObjects["C_DEVICE_TYPE"] and device_instance_id[0] == EnumConfigObjects["C_DEVICE"]):
            helper = Helper(config_header=self.config_header)
            device_type = helper.GetEntityByInstanceId(device_type_instance_id)
            device = helper.GetEntityByInstanceId(device_instance_id)
            channel_cls = self.config_header.GetConfigController(EnumConfigObjects["C_DEVICE_CHANNEL"])
            link_cls = self.config_header.GetConfigController(EnumConfigObjects["C_DEVICE_LINK"])
            components_mdl = self.config_header.GetConfigController(EnumConfigObjects["M_COMPONENTS"])
            types_mdl = self.config_header.GetConfigController(EnumConfigObjects["M_TYPES"])
            
            device["params"] = device_type["params"]
            helper.SaveEntity(device)

            groups = helper.NavigateMultiple("M_COMPONENTS", {"Unit" : device_type}, "Part")

            for group in groups:
                group_cid = group.GetControllerId()

                item_controller = None
                if (group_cid == EnumConfigObjects["C_DEVICE_CHANNEL_GROUP"]):
                    item_controller = channel_cls
                elif (group_cid == EnumConfigObjects["C_DEVICE_LINK_GROUP"]):
                    item_controller = link_cls
                if (not item_controller): continue

                quantity = group["quantity"]
                for i in range(0, quantity):
                    createGroupItem(helper, device, group, i, quantity)

        return True
