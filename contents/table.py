#!/usr/bin/env python

from latex_meta_lib import metacls_objlib
import os.path

class SingleTable():
    ''' single figure class'''
    def __init__(self,tag,latex='',path=None):
        self.tag = tag     # variable name
        self.filepath = None       # value 
        self.format = None     # description
        self.latex = latex
        self.path = path

class Table():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self,tag,caption='',path=None):
        self.tag = tag
        self.caption = caption
        self.itemlib = {}
        self.count = 0
        self.libtype = SingleTable
        self.path = path

    def AddPng(self,filepath):
        tf1 = SingleTable(tag='png',path=filepath)
        
        self.Add(tf1)        
        
class TableLib():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self):
        self.itemlib = {}
        self.count = 0
        self.libtype = Table
        

    def AddByTex(self,lines):
        ''' add figure by lines '''
        path = ''
        caption = ''
        label = ''
        temp = ''
        for i in lines:
            
            it = i.content
            temp += it + '\n'
            if 'includegraphics' in it:
                path = it[it.index('{')+1:it.index('}')]
            if 'caption' in  it:
                caption = it[it.index('{')+1:it.index('}')]
            if 'label' in it:
                label = it[it.index('{')+1:it.index('}')]
        
        ind1 = temp.index('begin{tabular}') 
        ind2 = temp.index('end{tabular}') + 12
        latex = temp[ind1-1:ind2]
        
        tf1 = SingleTable(tag='tex',latex=latex)
        
        t1 = Table(tag=label,caption=caption)
        t1.Add(tf1)
        self.Add(t1)
        
        return t1
    
    def AddBySelect(self,folder,filename,caption=''):

        allowextension = ['tex','xls''xlsx']
        try:
            basename,extension = filename.split('.')
            
        except:
            return -1
        sf1 = SingleTable(path=os.path.join(folder,filename),tag=extension)
        
        if extension.lower() in allowextension:
            if basename not in self.itemlib.keys():
                f1 = Table(tag=basename,caption=caption)
                f1.Add(sf1)
                self.Add(f1)
                
            else:
                f1 = self.itemlib[basename]
                f1.Add(sf1)
            
        