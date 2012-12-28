# -*- coding: utf-8 -*-
class Object:
    """
    Object that checks consistancy itself
    """
    
    __error_handler = None
    
    def SetErrorHandler(self, error_handler):
        """
        Sets the error handler of the object
        """
        self.__error_handler = error_handler

    def SetErrMsg(self, message, warning_level):
        """
        private method
        Sets Error Message to object
        """
        print message
        if (None != self.__error_handler):
            self.__error_handler.ProcessMessage(self, message, warning_level)
        return None

    def ToString(self):
        """
        Gets a String Representation of the object
        """
        return "<Unnamed Object>"
        
    def GetDescription(self):
        """
        Gets a Description of the object
        """
        return "<No Description>"
