# -*- coding: utf-8 -*-
from .. import base

class StorageExpression(base.StorageExpression):
    """
    Base Expression object to be used in queries
    """
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        raise Exception(str(self) + ": Method not implemented")
    

class StorageExpressionAll(StorageExpression, base.StorageExpressionAll):
    """
    i.e. AND binary operator
    """
    def __init__(self, *args):
        base.StorageExpressionAll.__init__(self, *args)
        
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        to_return = None
        for expr in self.expressions:
            t_query = expr.GetQuery(storage_header)
            if (None == to_return):
                to_return = t_query
            else:
                to_return = to_return & t_query
        return to_return
    
    
class StorageExpressionAny(StorageExpression, base.StorageExpressionAny):
    """
    i.e. OR binary operator
    """
    def __init__(self, *args):
        base.StorageExpressionAny.__init__(self, *args)
        
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        to_return = None
        for expr in self.expressions:
            t_query = expr.GetQuery(storage_header)
            if (None == to_return):
                to_return = t_query
            else:
                to_return = to_return | t_query
        return to_return
    
    
class StorageExpressionNot(StorageExpression, base.StorageExpressionNot):
    """
    i.e. NOT unary operator
    """
    def __init__(self, not_expression):
        base.StorageExpressionNot.__init__(self, not_expression)
        
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        return ~self.not_expression.GetQuery(storage_header)
    
    
class StorageExpressionAttributeValue(StorageExpression, base.StorageExpressionAttributeValue):
    """
    Attribute value comparator
    """

    def __init__(self, config_object_class, attribute_name, operation, value):
        """
        Constructor
        """
        base.StorageExpressionAttributeValue.__init__(self, config_object_class, attribute_name, operation, value)
        
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        class_storage = self.config_object_class.GetStorage()
        #return class_storage.table_name + "." + str(self.attribute_name).strip(" ") + " " + str(self.operation).strip(" ") + " '" + str(self.value).strip(" ") + "'"
        operation = self.operation.strip(" ")
        value = str(self.value).strip(" ")
        if (operation == "=="):
            return storage_header.connection[class_storage.table_name][self.attribute_name] == value
        if (operation == "<"):
            return storage_header.connection[class_storage.table_name][self.attribute_name] < value
        if (operation == ">"):
            return storage_header.connection[class_storage.table_name][self.attribute_name] > value
        raise Exception("Not supported operation for ExpressionAttributeValue: " + operation)
    

class StorageExpressionAssociationContains(StorageExpression, base.StorageExpressionAssociationContains):
    """
    Association instance requiring
    for class_id and id: 0 - any value, >0 - specified value
    """

    def __init__(self, config_object_model, instance_id, association_role):
        """
        Constructor
        """
        base.StorageExpressionAssociationContains.__init__(self, config_object_model, instance_id, association_role)
        
    def GetQuery(self, storage_header):
        """
        Create a query
        """
        model_storage = self.config_object_model.GetStorage()
        
        if (0 == self.instance_id[0] and 0 == self.instance_id[1]): return self.SetErrMsg("Expression couldn't contain association with ANY instance", 10)
        query1 = (storage_header.connection[model_storage.table_name][self.association_role + "_cid"] == self.instance_id[0])
        if (0 == self.instance_id[1]): return query1
        query2 = (storage_header.connection[model_storage.table_name][self.association_role + "_id"] == self.instance_id[1])
        if (0 == self.instance_id[0]): return query2
        return query1 & query2
