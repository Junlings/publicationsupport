class dump():
    
    def __init__(self):
        pass


class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, ErrNum):
        self.ErrNum = ErrNum

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self,errnum, obj, expr, msg):
        Error.__init__(self,errnum)
        self.expr = expr
        self.msg = msg
        self.ins = obj.__class__
        
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return "Input Error, %s,%s,%s" % (self.ins,self.msg,self.expr)
    
if __name__ == '__main__':
    
    r1 = dump()
    try:
        raise InputError(22,r1,'aaa','sss')
    except InputError as e:
        print e
    
    print 1