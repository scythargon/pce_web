# -*- coding: utf-8 -*-

class ErrorHandler:
    """
    Interface class for catching and processing error messages
    """
    
    def ProcessMessage(self, sender, message, warning_level):
        """
        Process error message
        """
        print (self.GetWarningLevel(warning_level), message)
        
    def GetWarningLevel(self, warning_level):
        if (warning_level<1): return "Note"
        if (warning_level<3): return "Warning"
        if (warning_level<5): return "Error"
        if (warning_level<8): return "Critical Error"
        return "Fatal Error"
         
