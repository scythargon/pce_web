from enum_config_objects import EnumConfigObjects
from util_get_group_item_name import getGroupItemName
from util_create_group_item import createGroupItem

def updateGroupTrigger(helper, group_inst_old, group_inst_new):
    group_to_inst_cid = {
        EnumConfigObjects["C_DEVICE_CHANNEL_GROUP"] : EnumConfigObjects["C_DEVICE_CHANNEL"],
        EnumConfigObjects["C_DEVICE_LINK_GROUP"] : EnumConfigObjects["C_DEVICE_LINK"],
    }

#    update_map = {}
#    for i in range(0, group_inst_new["quantity"]):
#        update_map[getGroupItemName(group_inst_old["name"], i, group_inst_new["quantity"])] = getGroupItemName(group_inst_new["name"], i, group_inst_new["quantity"])

    items_names_old = []
    for i in range(0, group_inst_old["quantity"]):
        items_names_old += [getGroupItemName(group_inst_old["name"], i, group_inst_old["quantity"])]
    items_names_new = []
    for i in range(0, group_inst_new["quantity"]):
        items_names_new += [getGroupItemName(group_inst_new["name"], i, group_inst_new["quantity"])]


    group_instances = helper.NavigateMultiple("M_TYPES", {"Type" : group_inst_new}, "Subject")
    for ginst in group_instances:
        if (ginst.GetControllerId() not in [EnumConfigObjects["C_DEVICE_CHANNEL"], EnumConfigObjects["C_DEVICE_LINK"]]): continue
        if (ginst["name"] not in items_names_old):
            print "Error: Couldn't assign group instance: %s" % ginst.GetInstanceId()
            continue
        old_name_index = items_names_old.index(ginst["name"])
        if (len(items_names_new) > old_name_index):
            ginst["name"] = items_names_new[old_name_index]
        else:
            helper.DeleteEntity(ginst)
        helper.SaveEntity(ginst)
    if (len(items_names_new) > len(items_names_old)):
        device_type = helper.Navigate("M_COMPONENTS", {"Part" : group_inst_new}, "Unit")
        devices = helper.NavigateMultiple("M_TYPES", {"Type" : device_type}, "Subject")
        for device in devices:
            for i in range(len(items_names_old), len(items_names_new)):
                createGroupItem(helper, device, group_inst_new, i, len(items_names_new))

