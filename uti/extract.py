import re


def extract_char(strexp,char):
    
    if len(strexp) > 0:
        try:
            ind = strexp.index(char) + 1
            return [ind,strexp[ind:]]
        except:
            return [-1,strexp]
                
                
def extract_quote(strexp):
    ind = []
    n = 0
    while 1:
        [ind_left,strexp] = extract_char(strexp,'{')
        [ind_right,strexp] = extract_char(strexp,'}')
        
        if ind_left != -1 and ind_right!= -1:
            ind.append([ind_left + n,ind_right + n + ind_left-1])
            n = ind_right + n + ind_left
        else:
            break
    return ind


def typejudge(strexp,inditem):
    ind0 = inditem[0]
    ind1 =  inditem[1]
    
    ind_slash = strexp[:ind0][::-1].index(' ')
    label = strexp[ind0-ind_slash:ind0]
    if 'Fig' in label or 'fig' in label or 'Figure' in label or 'figure' in label:
        otype = 'Figure'
    elif 'Table' in label or 'tabel' in label:
        otype = 'Table'
    elif 'Eq' in label or 'eq' in label or 'eq.' in label or 'Eq.' in label:
        otype = 'Equation'
    elif 'cite' in label:
        otype = 'Reference'
    else:
        otype = 'error'
    return [otype,strexp[ind0:ind1]]


    
def extract_labels(strexp):
    res = {'Table':[],'Equation':[],'Reference':[],'Figure':[],'error':[]}
    itemres = None
    if strexp != None:
        try:
            bb = extract_quote(strexp)
        except:
            bb = []
        for i in range(0,len(bb)):
            itemres = typejudge(strexp,bb[i])
            res[itemres[0]].append(itemres[1])

    return res

if __name__ == '__main__':

    aa = """The Fig.~\ref{Fig_compout_setup2} shear force in \cite{09448,12449}.  beams is mainly Table~\ref{Fig_compout_aa}  transferred by \cite{09448}.  two mechanisms Eq~\ref{Eq_22} strength concrete (NSC). One is the shear contribution from concrete portion in compression zone and the other is from the effects of aggregate interlocking. Due to the existence of the shear reinforcement, the NSC beam under 3-points bending test usually exhibits flexural failure with widened crack at the middle span. However, for beams made of UHPC, the situation is different. Due to the absence of the coarse aggregates and existence of the fibers, the shear can be transferred by three main mechanisms as shown in Fig.~\ref{Fig_compout_setup}. The failure model for the conventional 3-points bending test was basically the shear failure when there is no shear reinforcement. Because UHPC has considerable tensile strength, very high post-crack strength, and good bond strength with the longitudinal reinforcement, the flexural cracks width can be fully controlled while the shear cracks are free to develop due to the lack of reinforcement crossing the cracking plane. Hence, the dowel action contribution is worthy an investigation, because the dowel force can be fully activated due to the localized deformation at shear cracks. Generally, the total shear resistance can be expressed as follows in Eq.(1), in which dowel action contribution towards the total loading capacity is considered explicitly. The estimation of peak dowel force and its critical influential factors are worth investigation to obtain a better estimation of the shear strength of the un-shear-reinforced UHPC beams."""
    
    
    bb = extract_labels(aa)

    print 1