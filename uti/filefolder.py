import os
import shutil

def ensure_dir(f):
    #d = os.path.dirname(f)
    if not os.path.exists(f):
        os.makedirs(f)
        
        
def copyfile(srcfile,dstname,dstroot):
    assert not os.path.isabs(srcfile)
    filename = os.path.basename(srcfile)
    dstdir =  os.path.join(dstroot, dstname)
    
    #os.makedirs(dstdir) # create all directories, raise an error if it already exists
    shutil.copy(srcfile, dstdir)