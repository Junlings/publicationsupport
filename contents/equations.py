#!/usr/bin/env python
from latex_meta_lib import metacls_objlib
import os.path

class var():
    """ single variable class"""
    def __init__(self,tag=None,val=None,expr=None,spec=None,loc=None):
        self.tag = tag    # variable name
        self.val = val       # value 
        self.expr = expr     # description
        self.spec = spec     # exising specification the equation come from
        self.loc = loc  # detail equation location
        self.latex = None    # latex expression
        
        
    def SetValue(self,val):
        self.val = val
    
    def GetValue(self):
        return self.val
        
    def SetCondTable(self,CondTable):
        self.CondTable = CondTable
    
    def GetValueCondTable(self,Cond):
        # look up condition table keys
        return self.CondTable[Cond]
    
    def SetValueCondTable(self,Cond):
        self.val = self.CondTable[Cond]



class varlib():
    ''' variable library'''
    __metaclass__ = metacls_objlib
    def __init__(self):
        self.itemlib = {}
        self.count = 0
        self.libtype = var
           
        
    



class singleeq():
    ''' equation class refer the var in a specific varlib '''
    def __init__(self,label,spec=None,varlib={},latex=[],path=None):
        self.label = label      # equation label
        self.spec = spec        # equation source
        self.varlib = varlib        # variable library
        self.latex = latex         # latex expression
        self.tag = self.label
        self.path = path
        
    '''
    def varlib(self,expr):
        self.vlib = expr
        for i in expr.keys():
            self.__setitem__(i,expr[i])

    def __setitem__(self,key,value):
        """ now without overwrite warning check"""
        pass
        setattr(self,key,value)
        
    def __getitem__(self,key):
        try:
            self.__getattribute__(key)
        except AttributeError:
            print 'class:"' + str(self.__class__.__name__) +'"'
            print 'do not have attr.:"' + key +'"'
            print 'input skipped'
        else:
            return self.__getattribute__(key)
    '''
    
    def lhs(self,exp):
        self.lhs = exp

    def eval_lhs(self):
        self.lhs_value = self.evaluation(self.lhs)
        return self.lhs_value
    
    def rhs(self,exp): 
        self.rhs = exp
        
    def eval_rhs(self):
        self.rhs_value = self.evaluation(self.rhs)
        return self.rhs_value
    
    def evaluation(self,expression):
        # create mapping
        print eval(expression,self.varlib)
        

class Eq():
    __metaclass__ = metacls_objlib
    
    ''' variable library'''
    def __init__(self,tag,caption=''):
        self.tag = tag
        self.caption = caption
        self.itemlib = {}
        self.count = 0
        self.libtype = singleeq

    def AddPng(self,filepath):
        tf1 = singleeq('png',path=filepath)
        
        self.Add(tf1)        
        
        
               
class EqLib():
    ''' variable library'''
    __metaclass__ = metacls_objlib
    def __init__(self):
        self.itemlib = {}
        self.count = 0
        self.libtype = Eq  

    def AddByTex(self,lines):
        ''' add equations '''

        path = None
        latex = []
        label = ''
        
        for i in lines:
            it = i.content
            if 'input' in it:
                path = it[it.index('{')+1:it.index('}')]
            elif 'label' in it:
                it = it[it.index('label'):]
                label = it[it.index('{')+1:it.index('}')]
            elif 'begin{equation}' in it  or 'end{equation}' in it:
                pass
            
            else:
                latex.append(it)
        
        eq1 = singleeq('tex',latex=latex,path=path)
        Eq1 = Eq(tag=label)
        Eq1.Add(eq1)

        self.Add(Eq1)

    def AddBySelect(self,folder,filename,caption=''):

        allowextension = ['tex','wmf''mws']
        try:
            basename,extension = filename.split('.')
            
        except:
            return -1
        sf1 = singleeq(extension,path=os.path.join(folder,filename))
        
        if extension.lower() in allowextension:
            if basename not in self.itemlib.keys():
                f1 = Eq(tag=basename,caption=caption)
                f1.Add(sf1)
                self.Add(f1)
                
            else:
                f1 = self.itemlib[basename]
                f1.Add(sf1)
                    
        
if __name__ == '__main__':
    myeqlib = varlib()   
    v1 = var(**{'tag':'eta_i',
                   'val':1,
                   'expr':'load modifier: a factor relating to ductility, redundancy, and operation importance',
                   'spec':'AASHTO',
                   'loc':[1,3]})
    myeqlib.Add(v1)
    
    myeqlib.New({'tag':'eta_i2',
                   'val':1,
                   'expr':'load modifier: a factor relating to ductility, redundancy, and operation importance',
                   'spec':'AASHTO',
                   'loc':[1,3]})

    eq1 = eq('eq1')
    '''
    #============================================================================
    eta_D = var('eta_D',
                1.0,
                'a factor relating to ductility as specified in Article 1.3.3',
                'AASHTO',[1,3,3])
    eta_D.SetCondTable({'StrengthLS|nonductile':1.05,
                        'StrengthLS|ductile':1.00,
                        'StrengthLS|ductile-enhancing':0.95,
                        'OtherLS':1.0})
    
    #============================================================================
    eta_R = var('eta_R',
                1.0,
                'a factor relating to redundancy as specified in Article 1.3.4',
                'AASHTO',[1,3,4])
    eta_R.SetCondTable({'StrengthLS|nonredundent':1.05,
                        'StrengthLS|conventional redundent':1.00,
                        'StrengthLS|exceptional redundent':0.95,
                        'OtherLS':1.0})
    
    #============================================================================
    
    eta_I = var('eta_I',
                1.0,
                'a factor relating to operational importance as specified in Article 1.3.5',
                'AASHTO',[1,3,5])
    eta_I.SetCondTable({'StrengthLS|Important':1.05,
                        'StrengthLS|typical':1.00,
                        'StrengthLS|less important':0.95,
                        'OtherLS':1.0})
    
    
    
    Q_i = var('Q_i',0.9,'force effects','AASHTO',[1])
    R_n = var('R_n',0.9,'nominal resistance','AASHTO',[1])
    R_r = var('R_r',0.9,'factored resistance','AASHTO',[1])
    
    gamm_i = var('gamm_i',0.9,'load factor: a statistically based multiplier applied to force effecs','AASHTO',[1])
    fi = var('fi',1.0,'resistance factor:a statistically based multiplier applied to nominal resistance','AASHTO',[1])        
            
    
    
    
      
    eq1 = eq([eta_i,gamm_i,Q_i,R_n,R_r],'AASHTO',[1,3,2,1,1])
    eq1.lhs = 'eta_i'
    eq1.rhs = 'eta_i+eta_D'
    '''
    print 1