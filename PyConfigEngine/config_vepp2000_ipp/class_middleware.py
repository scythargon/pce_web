# -*- coding: utf-8 -*-
from .. import base

from class_base import ClassBase

class ClassMiddleware(ClassBase):
    """
    Class Middleware
    """
    
    def __init__(self):
        """
        Constructor
        """
        ClassBase.__init__(self, "Middleware")
        self.attributes["Address"] = base.ConfigAttribute("STR63", "Address", "IP address or domain name", 80, "0.0.0.0")
#        self.attributes["readable_name"] = base.ConfigAttribute("STR63", "Readable Name", "Short string for fast identification the object by user", 150, "No name")
#        self.attributes["name"] = base.ConfigAttribute("STR63", "API Name", "Short string for fast identification the object by programs", 100, "No name")
#        self.attributes["description"] = base.ConfigAttribute("TEXT", "Description", "Additional information and comments", 10, "No description")

#        self.attributes["place"] = base.ConfigAttribute("STR255", "Place", "Description of where the Server could be found", 70, "")

