# Get the GUI stuff
import wx
import wx.aui
# We're going to be handling files and directories
import os
from lxml import etree
# Set up some button numbers for the menu
from document import document

from generic.dict_tree import MyDictTree
from generic.generic_frame_simple import GenericFrameSimple
import cPickle as pickle

ID_ABOUT=101
ID_OPEN=102
ID_SAVE=103
ID_BUTTON1=300
ID_EXIT=200

class MainWindow(GenericFrameSimple):
    def __init__(self,parent,settings):
        # based on a frame, so set up the frame
        GenericFrameSimple.__init__(self,parent,wx.ID_ANY, settings)
        
        
        self.mainpanel = wx.Panel(self, -1,style=wx.EXPAND)
        
        self.doctree = MyDictTree(self.mainpanel,'Document')

        
        self.ModelNoteBook = wx.aui.AuiNotebook(self.mainpanel,1,size=(500,500),style=wx.aui.AUI_NB_DEFAULT_STYLE)

        self.sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.doctree,0,wx.EXPAND)
        self.sizer.Add(self.ModelNoteBook,1,wx.EXPAND)
        self.mainpanel.SetSizer(self.sizer)
        
        self.doc = document()
        
        self.dirname = ''

    
    def OnProjNew(self,event):
        pass

    def OnAbout(self,e):
        # A modal show will lock out the other windows until it has
        # been dealt with. Very useful in some programming tasks to
        # ensure that things happen in an order that the programmer
        # expects, but can be very frustrating to the user if it is
        # used to excess!
        self.aboutme.ShowModal() # Shows it
        # widget / frame defined earlier so it can come up fast when needed

    def OnExit(self,e):
        # A modal with an "are you sure" check - we don't want to exit
        # unless the user confirms the selection in this case ;-)
        igot = self.doiexit.ShowModal() # Shows it
        if igot == wx.ID_YES:
            self.Close(True) # Closes out this simple application

    def OnOpen(self,e):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'r')
            #self.control.SetValue(filehandle.read())
            self.NbAddPage(self.filename,filehandle.read())
            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
        dlg.Destroy()
        
    def NbAddPage(self,filename,content):

        page = wx.TextCtrl(self.ModelNoteBook, -1, filename, style=wx.TE_MULTILINE)
        page.SetValue(content)
        self.ModelNoteBook.AddPage(page, filename)

    def OnSave(self,e):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.control.GetValue()

            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()
    

    def OnTexOpen(self,e):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            fileloc = os.path.join(self.dirname, self.filename)
            filehandle=open(fileloc,'r')

            self.NbAddPage(self.filename,filehandle.read())
            
            self.doc.import_tex(fileloc)
            self.doc.extract()
            aa = self.doc.struct.pretty()
            self.NbAddPage(self.filename+'_struct',aa)            
            
            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
        dlg.Destroy()
        self.DocTreeRefresh()
        
    
    def DocTreeRefresh(self):
        
        self.doctree.create_nodes_dict(self.doctree.RootItem,self.doc.GetTreeDict())
        self.doctree.GetParent().Refresh()
        self.doctree.GetParent().SetFocus()
        
        
    def OnDocxExport(self,event):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.docx", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            # Open the file for write, write, close
            filename=dlg.GetFilename()
            dirname=dlg.GetDirectory()
            self.doc.docx_export(dirname,filename)
            
            #self.doc.docx_new()
            #self.doc.docx_add_by_tree()
            #self.doc.docx_save(os.path.join(self.dirname, self.filename))
            #filehandle=open(os.path.join(self.dirname, self.filename),'w')
            ##filehandle.write(itcontains)
            #filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()
    
    
    def OpenFile(self,wildcard="*.*"):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", wildcard, \
                wx.OPEN|wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            # Open the file for write, write, close
            filename=dlg.GetFilenames()
            dirname=dlg.GetDirectory()
            return dirname,filename
        else:
            return None,None
        dlg.Destroy()        
        

    def NewFolder(self):
        dialog = wx.DirDialog(None, "Please choose your project directory:",\
        style=1 ,defaultPath='export', pos = (10,10))
        if dialog.ShowModal() == wx.ID_OK:
            _selectedDir = dialog.GetPath()
            return _selectedDir
        else:
            #app.Close()
            dialog.Destroy()
            return _userCancel
                        
        
    def OnProjSave(self,event):
        folder = self.NewFolder()
        #self.doc.workdir = folder
        self.doc.exportdst = folder
        self.doc.ExportProject(folder)
        
        
        
        
    def OnFigureOpen(self,event):
        newfolder,filenames = self.OpenFile()
        for filename in filenames:
            self.doc.figurelib.AddBySelect(newfolder,filename)
        self.DocTreeRefresh()
    
    def OnFigure2PNG(self,event):
        self.doc.FigureEps2Png()
    
    def OnFigure2EPS(self,event):pass
    
    def OnTableOpen(self,event):
        newfolder,filenames = self.OpenFile()
        for filename in filenames:
            self.doc.tablelib.AddBySelect(newfolder,filename)
        self.DocTreeRefresh()
        
    def OnTable2PNG(self,event):
        self.doc.TableTex2Png()
    
    def OnTable2TEX(self,event):pass
    
    def OnEqOpen(self,event):
        newfolder,filenames = self.OpenFile()
        for filename in filenames:
            self.doc.eqlib.AddBySelect(newfolder,filename)
        self.DocTreeRefresh()
        
    def OnEq2PNG(self,event):
        self.doc.EqTex2Png()
    
    def OnEq2TEX(self,event):pass    
    
    
if __name__ == '__main__':        
    settings = {'title':'my Title','size':(500,500)}
    settings['menuData']=(("&File",
                            ("&New", "New Project", 'OnProjNew'),
                            ("&Save", "Save Project", 'OnProjSave'),
                            ("&Edit", "Clear database", 'OnCloseWindow')),
                       ("&Tex",
                            ("&OpenTex", "Open and Parse the tex file", 'OnTexOpen'),
                            ),
                       ("&Figure",
                            ("&Open", "Open and figure file", 'OnFigureOpen'),
                            ("&->PNG", "convert to PNG", 'OnFigure2PNG'),
                            ("&->EPS", "convert to EPS", 'OnFigure2EPS')
                            ),
                       ("&Table",
                            ("&Open", "Open Table files", 'OnTableOpen'),
                            ("&->PNG", "convert to PNG", 'OnTable2PNG'),
                            ("&->Tex", "convert to Tex", 'OnTable2TEX')
                            ),
                       ("&Equation",
                            ("&Open", "Open equation files", 'OnEqOpen'),
                            ("&->PNG", "convert to PNG", 'OnEq2PNG'),
                            ("&->Tex", "convert to Tex", 'OnEq2TEX')
                            ),
                       ("&Docx",
                            ("&Export", "Export to docx file", 'OnDocxExport')
                            )
                )
    
    settings['statusbar']=[-1,-1,-1]   
    settings['toolbarData'] = {'Mode':'HORIZONTAL',
                               'Data':[
                                  ('aa','OnTexOpen','resource/xy.png'),
                                  ('bb','OnDocxExport','resource/xyy.png')
                                ]}
    # Set up a window based app, and create a main window in it
    app = wx.App()
    MainWindow(None,settings).Show()
    app.MainLoop()