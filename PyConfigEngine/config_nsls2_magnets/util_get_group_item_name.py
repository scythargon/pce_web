def getGroupItemName(group_name, item_id, items_count):
    if (items_count == 1): return str(group_name)

    return str(group_name) + str(item_id)
