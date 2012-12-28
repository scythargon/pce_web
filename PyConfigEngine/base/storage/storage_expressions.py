# -*- coding: utf-8 -*-
from ..object import Object

class StorageExpression(Object):
    """
    Base Expression object to be used in queries
    """

class StorageExpressionAll(StorageExpression):
    """
    i.e. AND binary operator
    """
     
    def __init__(self, *args):
        """
        Constructor
        """
        self.expressions = args

class StorageExpressionAny(StorageExpression):
    """
    i.e. OR binary operator
    """
     
    def __init__(self, *args):
        """
        Constructor
        """
        self.expressions = args

class StorageExpressionNot(StorageExpression):
    """
    i.e. NOT unary operator
    """
     
    def __init__(self, not_expression):
        """
        Constructor
        """
        self.not_expression = not_expression
        
class StorageExpressionAttributeValue(StorageExpression):
    """
    Attribute value comparator
    """

    def __init__(self, config_object_class, attribute_name, operation, value):
        """
        Constructor
        """
        self.config_object_class = config_object_class
        self.attribute_name = attribute_name
        self.operation = operation
        self.value = value

class StorageExpressionAssociationContains(StorageExpression):
    """
    Association instance requiring
    for class_id and id: 0 - any value, >0 - specified value
    """

    def __init__(self, config_object_model, instance_id, association_role):
        """
        Constructor
        """
        self.config_object_model = config_object_model
        self.instance_id = instance_id
        self.association_role = association_role


