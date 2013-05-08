#!/usr/bin/env python

from latex_meta_lib import metacls_objlib

class SingleSentence():
    ''' single figure class'''
    def __init__(self,tag=None):
        self.tag = tag     # variable name
        self.text = ''
        self.filepath = None       # value 
        self.format = None     # description

class Paragraph():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self,tag):
        self.tag = tag
        self.itemlib = {}
        self.count = 0
        self.libtype = SingleSentence
        self.wholetext = ''
        self.tablelist = []
        self.figurelist = []
        self.equationlist = []
        self.referencelist= []
        
    
    def Add(self,objtype,obj):
        if objtype == 'table':
            self.tablelist.append(obj)
        elif objtype == 'figure':
            self.figurelist.append(obj)
        elif objtype == 'equation':
            self.equationlist.append(obj)
        elif objtype == 'reference':
            self.referencelist.append(obj)
        else:
            raise KeyError
    
    
    def AddByDict(self,itemdict):
        self.itemdict = itemdict
    
    def ExtractTex(self):
        pass
        
        
        

class ParagraphLib():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self):
        self.tag = ''
        self.itemlib = {}
        self.count = 0
        self.libtype = Paragraph
        
        
    def AddByTex(self,tag,lines):
        p1 = Paragraph(tag)
        p1.wholetext = lines

        self.Add(p1)
        
        return p1

