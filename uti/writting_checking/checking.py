#!/usr/bin/env python
#!/usr/bin/env python
# This should probably be replaced with a demo that shows all
# line and marker types in a single panel, with labels.
import os
import shutil
import datetime


def checking_file(filename):
    if '.' not in filename:
        filename=filename+'.tex'
    f_full=open(filename,'rU')
    
    f_write=open(filename+'_num.txt','w')
    
    line_content='main'
    linNum=1
    while 1:
        line=f_full.readline()
        if len(line)==0:  ## end of file
            break
        else:
            line='['+str(linNum)+'] '+line
            linNum=linNum+1
            f_write.write(line)
            
    f_write.close()
    

def extract_content(linecontent,i,n):
    if n==5 and len(linecontent)>5:
        if i==1:
            tempcontent=[linecontent[0],' ',linecontent[i],' ',linecontent[i+1],' ',linecontent[i+2],'\n']
        elif i==2:
            tempcontent=[linecontent[0],' ',linecontent[i-1],' ',linecontent[i],' ',linecontent[i+1],' ',linecontent[i+2],' ',linecontent[i+3],'\n']
        elif i==len(linecontent)-1:
            tempcontent=[linecontent[0],' ',linecontent[i-2],' ',linecontent[i-1],' ',linecontent[i],'\n']
        elif i==len(linecontent)-2:
            tempcontent=[linecontent[0],' ',linecontent[i-2],' ',linecontent[i-1],' ',linecontent[i],' ',linecontent[i+1],'\n']
        else:
            #print 'linecontent',linecontent,'i',i
            tempcontent=[linecontent[0],' ',linecontent[i-2],' ',linecontent[i-1],' ',linecontent[i],' ',linecontent[i+1],' ',linecontent[i+2],'\n']
            
            
    elif n==7:
        startID=max(1,i-3)
        tempcontent=[linecontent[0]]
        endID=min(len(linecontent),i+3)
        #print startID,endID
        for j in range(startID,endID):
            tempcontent.append(linecontent[j])
            tempcontent.append(' ')
        tempcontent.append('\n')
    
    elif n==9:
        startID=max(1,i-4)
        tempcontent=[linecontent[0]]
        endID=min(len(linecontent),i+4)
        #print startID,endID
        for j in range(startID,endID):
            tempcontent.append(linecontent[j])
            tempcontent.append(' ')
        tempcontent.append('\n')
    
    else:
        tempcontent=linecontent
    return tempcontent





def check_keyword(filename,keyword,linecontent,mode='Match'):

    filename='check/'+'['+keyword+']_'+filename+'_check.txt'
    #print filename
    export=[]
    f_write=open(filename,'a')
    for j in range(0,len(linecontent)):
        for i in range(0,len(linecontent[j])):
            #if linecontent[j][i]=='a' or linecontent[j][i]=='A' or linecontent[j][i]=='an' or linecontent[j][i]=='An':
            if mode=='Match':
                if linecontent[j][i]==keyword:
                    export.extend(extract_content(linecontent[j],i,9))
            elif mode=='within':
                if keyword in linecontent[j][i]:
                    export.extend(extract_content(linecontent[j],i,9))
                
            else:
                pass
                #print linecontent[j][i]
            
    for j in range(0,len(export)):
    
        f_write.write(export[j])
        
    f_write.close()
    
def checking_content(filename):

    f_full=open(filename,'r')
    
    
    
    linecontent=[]
    while 1:
        line=f_full.readline()
        if len(line)==0:  ## end of file
            break
        else:
            linecontent.append(line.split(' '))
    
    check_keyword(filename,'is',linecontent)
    check_keyword(filename,'were',linecontent)
    check_keyword(filename,'am',linecontent)
    check_keyword(filename,'are',linecontent)
    check_keyword(filename,'a',linecontent)
    check_keyword(filename,'An',linecontent)
    check_keyword(filename,'A',linecontent)
    check_keyword(filename,'an',linecontent)
    check_keyword(filename,'the',linecontent)
    check_keyword(filename,'respectively',linecontent)
    check_keyword(filename,'Respectively',linecontent)
    check_keyword(filename,'Respect',linecontent)
    check_keyword(filename,'respect',linecontent)
    check_keyword(filename,'lot',linecontent)
    check_keyword(filename,'above',linecontent)
    check_keyword(filename,'-',linecontent,mode='within')
    check_keyword(filename,'absolutely',linecontent)
    check_keyword(filename,'accurate',linecontent,mode='within')
    check_keyword(filename,'effect',linecontent)
    check_keyword(filename,'affect',linecontent)
    check_keyword(filename,'this',linecontent)
    check_keyword(filename,'those',linecontent)
    check_keyword(filename,'most',linecontent,mode='within')
    check_keyword(filename,'also',linecontent,mode='within')
    check_keyword(filename,'amount',linecontent,mode='within')
    check_keyword(filename,'and',linecontent,mode='within')
    check_keyword(filename,'I',linecontent)
    
    check_keyword(filename,'as',linecontent)
    check_keyword(filename,'because',linecontent)
    check_keyword(filename,'since',linecontent)
    check_keyword(filename,'As',linecontent)
    check_keyword(filename,'Because',linecontent)
    check_keyword(filename,'Since',linecontent)
    check_keyword(filename,'Beside',linecontent)
    check_keyword(filename,'principle',linecontent)
    check_keyword(filename,'Principle',linecontent)
    
checking_file('Disseration_jun_Publish@2010_10_28_assemble')
checking_content('Disseration_jun_Publish@2010_10_28_assemble.tex_num.txt')