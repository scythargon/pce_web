# -*- coding: utf-8 -*-

class ChangesHandler:
    """
    Interface class for catching and processing error messages
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.ClearLog()
    
    def GetLog(self):
        """
        Get Logged information
        """
        return self.log
    
    def ClearLog(self):
        """
        Clear Logged information
        """
        self.log = list()
    
    def ProcessMessage(self, sender, message, importance):
        """
        Process message
        """
        self.log += [{"sender" : sender, "importance" : importance, "message" : message}]

