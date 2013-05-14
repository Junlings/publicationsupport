#!/usr/bin/env python

from latex_meta_lib import metacls_objlib
import os.path

class SingleFigure():
    ''' single figure class'''
    def __init__(self,tag=None,path=None,iformat=None):
        self.tag = tag     # variable name
        self.path = path       # value 
        self.iformat = iformat     # description
        if self.tag == None:
            self.tag = iformat

class Figure():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self,tag,caption='',label=''):
        self.tag = tag
        self.itemlib = {}
        self.count = 0
        self.libtype = SingleFigure
        self.caption = caption
        self.label = label

class FigureLib():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self):
        self.itemlib = {}
        self.count = 0
        self.libtype = Figure
    
    
    def AddByTex(self,lines):
        ''' add figure by lines '''
        path = ''
        caption = ''
        label = ''
        
        for i in lines:
            it = i.content
            if 'includegraphics' in it:
                path = it[it.index('{')+1:it.index('}')]
            if 'caption' in  it:
                caption = it[it.index('{')+1:it.index('}')]
            if 'label' in it:
                label = it[it.index('{')+1:it.index('}')]
        
        sf1 = SingleFigure(path=path,iformat=path[path.index('.')+1:])
        
        f1 = Figure(tag=label,caption=caption)
        f1.Add(sf1)
        self.Add(f1)
        
    def AddBySelect(self,folder,filename,caption=''):

        
        basename,extension = filename.split('.')
        sf1 = SingleFigure(path=os.path.join(folder,filename),iformat=extension)
        
        if basename not in self.itemlib.keys():
            f1 = Figure(tag=basename,caption=caption)
            f1.Add(sf1)
            self.Add(f1)
            
        else:
            f1 = self.itemlib[basename]
            f1.Add(sf1)
            
                        
        

if __name__ == '__main__':
    s1 = SingleFigure(tag='a')
    s2 = SingleFigure(tag='b')
    myfigl = Figure('figure1')
    myfigl.Add(s1)
    myfigl.Add(s2)

    
    figurelib1 = FigureLib()
    figurelib1.Add(myfigl)

    print 1