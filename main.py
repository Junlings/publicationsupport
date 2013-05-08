# Get the GUI stuff
import wx
import wx.aui
# We're going to be handling files and directories
import os

# Set up some button numbers for the menu
from document import document

from generic.dict_tree import MyDictTree
from generic.generic_frame_simple import GenericFrameSimple

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

        '''
        # Add a text editor and a status bar
        # Each of these is within the current instance
        # so that we can refer to them later.
        self.control = wx.TextCtrl(self.mainpanel, 1, style=wx.TE_MULTILINE,size=(800,600))
        self.doctree = MyDictTree(self.mainpanel,'model')
        self.ModelNoteBook = wx.aui.AuiNotebook(self.mainpanel,1,size=(500,500),style=wx.aui.AUI_NB_DEFAULT_STYLE)
        #self.ModelNoteBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageChanged)


        # Set up a series of buttons arranged horizontally
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons=[]
        # Note - give the buttons numbers 1 to 6, generating events 301 to 306
        # because IB_BUTTON1 is 300
        
        functiontext = ['Parse Tex','Export to Word','Button','Button','Button','Button','Button']
        for i in range(6):
            # describe a button
            bid = i+1
            self.buttons.append(wx.Button(self, ID_BUTTON1+i, functiontext[i]))
            # add that button to the sizer2 geometry
            self.sizer2.Add(self.buttons[i],1,wx.EXPAND)

        # Set up the overall frame verically - text edit window above buttons
        # We want to arrange the buttons vertically below the text edit window
        self.sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.doctree,0,wx.EXPAND)
        self.sizer.Add(self.ModelNoteBook,1,wx.EXPAND)
        
        

        # Tell it which sizer is to be used for main frame
        # It may lay out automatically and be altered to fit window
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        # Show it !!!
        self.Show(1)

        # Define widgets early even if they're not going to be seen
        # so that they can come up FAST when someone clicks for them!
        self.aboutme = wx.MessageDialog( self, " A sample editor \n"
                            " in wxPython","About Sample Editor", wx.OK)
        self.doiexit = wx.MessageDialog( self, " Exit - R U Sure? \n",
                        "GOING away ...", wx.YES_NO)

        # dirname is an APPLICATION variable that we're choosing to store
        # in with the frame - it's the parent directory for any file we
        # choose to edit in this frame
        self.dirname = ''
        '''

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
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            
            self.doc.docx_new()
            self.doc.docx_add_by_tree()
            self.doc.docx_save(os.path.join(self.dirname, self.filename))
            #filehandle=open(os.path.join(self.dirname, self.filename),'w')
            ##filehandle.write(itcontains)
            #filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()
        

    
    
if __name__ == '__main__':        
    settings = {'title':'my Title','size':(500,500)}
    settings['menuData']=(("&File",
                            ("&Open", "Open a file to edit", 'OnOpen'),
                            ("&Edit", "Clear database", 'OnCloseWindow')),
                       ("&Tex",
                            ("&OpenTex", "Open and Parse the tex file", 'OnTexOpen'),
                            ("&Parse", "Parse the tex file", 'OnTexOpen')
                            ),
                       ("&Docx",
                            ("&Export", "Export to docx file", 'OnDocxExport')
                            )
                )
    
    settings['statusbar']=[-1,-1,-1]   
    settings['toolbarData'] = {'Mode':'HORIZONTAL',
                               'Data':[
                                  ('aa','OnCloseWindow','resource/xy.png'),
                                  ('bb','OnCloseWindow','resource/xyy.png')
                                ]}
    # Set up a window based app, and create a main window in it
    app = wx.App()
    MainWindow(None,settings).Show()
    app.MainLoop()