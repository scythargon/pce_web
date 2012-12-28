# -*- coding: utf-8 -*-

EnumAttributes = dict()    
"""
Enumerator of supported attribute types
"""
EnumAttributes["TEXT"] = 1
EnumAttributes["STR255"] = 2
EnumAttributes["STR63"] = 3
EnumAttributes["DOUBLE"] = 4
EnumAttributes["FLOAT"] = 5
EnumAttributes["INTEGER"] = 6
EnumAttributes["BOOLEAN"] = 7
EnumAttributes["DICTIONARY"] = 8

EnumAttributeDefaults = dict()
"""
Enumerator of default attribute values
"""
EnumAttributeDefaults["TEXT"] = ""
EnumAttributeDefaults["STR255"] = ""
EnumAttributeDefaults["STR63"] = ""
EnumAttributeDefaults["DOUBLE"] = 0.0
EnumAttributeDefaults["FLOAT"] = 0.0
EnumAttributeDefaults["INTEGER"] = 0
EnumAttributeDefaults["BOOLEAN"] = False
EnumAttributeDefaults["DICTIONARY"] = {}

