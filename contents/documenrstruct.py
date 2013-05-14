from contents.paragraph import Paragraph, SingleSentence
from lxml import etree

class DocumentStruct():
    ''' this is the document class for connect with tex and ms.word'''
    
    def __init__(self,**kargs):
        self.root = etree.Element('document',attrib=kargs)
    
    def AddSection(self,parent,tag,text,**kargs):
        newsection = etree.SubElement(parent, tag)
        newsection.attrib.update(kargs)
        newsection.text = text
        
        return newsection
    
    def AddParagraph(self,parent,paragraph):
        para = etree.SubElement(parent, 'paragraph')
        try:
            para.text = paragraph.tag
        except:
            para.text = 'error'
        return para
        
    def AddObj(self,parent,objtype,objtag):
        new_element = etree.SubElement(parent, objtype)
        para.text = objtag
          
        
    
    def pretty(self):
        return etree.tostring(self.root, pretty_print=True)
    
    def exportfile(self,filename):

        #filename='/tmp/test.xml'
        with open(filename,'w') as f:
            f.write(etree.tostring(self.root))
    
    def importfile(self,filename):
        with open(filename,'r') as f:
            content = f.read()
        myobject=self.root.fromstring(content)
    
if __name__ == '__main__':
    
    p1 = Paragraph('p1')
    
    for i in range(0,10):
        tag = i
        ss1  = SingleSentence(tag)
        ss1.text = 'this is first paragraph' + str(i)*7
        
        p1.Add(ss1)

    
    d1 = DocumentStruct(longname='Shear analysis')
    s1 = d1.AddSection(d1.root,longname='Section 1')
    s11 = d1.AddSection(s1,longname='Section 11')
    
    d1.AddParagraph(s11,p1)
    
    aa = etree.tostring(d1.root, pretty_print=True)
    

    
    print 1