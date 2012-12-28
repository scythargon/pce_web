from enum_config_objects import EnumConfigObjects
from util_get_group_item_name import getGroupItemName


def createGroupItem(helper, parent_device, parent_group, index, quantity):
    group_to_inst_cid = {
        EnumConfigObjects["C_DEVICE_CHANNEL_GROUP"] : EnumConfigObjects["C_DEVICE_CHANNEL"],
        EnumConfigObjects["C_DEVICE_LINK_GROUP"] : EnumConfigObjects["C_DEVICE_LINK"],
    }

    new_item = helper.CreateEntity(group_to_inst_cid[parent_group.GetControllerId()])
    new_item["name"] = getGroupItemName(parent_group["name"], index, quantity)
    if (parent_group.GetControllerId() == EnumConfigObjects["C_DEVICE_CHANNEL_GROUP"]):
        new_item["default_value"] = parent_group["default_value"]
    helper.SaveEntity(new_item)

    new_link_components = helper.CreateEntity("M_COMPONENTS")
    new_link_components["Unit"] = parent_device.GetInstanceId()
    new_link_components["Part"] = new_item.GetInstanceId()
    helper.SaveEntity(new_link_components)

    new_link_types = helper.CreateEntity("M_TYPES")
    new_link_types["Type"] = parent_group.GetInstanceId()
    new_link_types["Subject"] = new_item.GetInstanceId()
    helper.SaveEntity(new_link_types)
    return True