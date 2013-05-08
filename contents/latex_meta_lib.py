#!/usr/bin/env python
"""
Class defination of the latex file handing program
"""
#!/usr/bin/env python

import pickle
from cexpection import InputError

def Meta_New(obj,kargs):
    x = obj.libtype

    newvar = x(**kargs)
    obj.AddSingle(newvar)

def Meta_Add(obj,item):
    """
    Meta function for adding the item to the specified list
    """
    a = item.__class__.__name__
    if a == obj.libtype.__name__:
        obj.AddSingle(item)
    
def Meta_CheckKey(obj,key):
    ''' check if key exist in itemlib'''
    if key in obj.itemlib.keys():
        return 1
    else:
        return 0

def Meta_AddSingle(obj,var):
    ''' add single var instance'''
    if not obj.CheckKey(var.tag):
        obj.itemlib[var.tag] = var
        obj.count += 1
    else:
        try:
            raise InputError('00001',obj,var,'Duplicate Key:%s' % var.tag)
        except InputError as e:
            print e
            
def Meta_AddList(obj,*varlist):
    ''' add var instance list'''
    for var in varlist:
        obj.AddSingle(var)
    

class metacls_objlib(type):
    """
    Defination of metaclass of class instant object lib
    """
    def __new__(meta, classname, supers, classdict):
        #print ('In MetaOne.new:', classname, supers, classdict)
        
        # specify the initialize function
        #classdict['copy'] = Meta_Copy
        #classdict['save'] = Meta_Save
        #classdict['load'] = Meta_Load
        #classdict['tag'] = Meta_settag
        classdict['CheckKey'] = Meta_CheckKey
        classdict['AddSingle'] = Meta_AddSingle
        classdict['AddList'] = Meta_AddList
        classdict['Add'] = Meta_Add
        classdict['New'] = Meta_New
        #classdict['assemble'] = Meta_Assemble
        #classdict['delt'] = Meta_Del
        #classdict['__getitem__'] = Meta_get
        classdict['seq'] = -1
        classdict['tag'] = 'Default'
        classdict['count'] = 0
        classdict['itemlib'] = {}
        classdict['libtype'] = None
        
        return type.__new__(meta, classname, supers, classdict)
    

        