import wx
import wx.xrc
import glob, os

class AddCoverDialog ( wx.Frame ):

    def selectPicture(self, event):
        selectPictureDialog = wx.FileDialog(self, "select", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        selectPictureDialog.ShowModal()
        self.picturePath.SetValue(selectPictureDialog.GetPath())
        selectPictureDialog.Destroy()

    def add(self, event):
        self.status.SetLabel("Adding... Please Wait")
        for path in glob.iglob(os.path.join(self.directoryPath.GetValue(), '*.mp3')):
            print path
            os.system("lame -b 320 --ti " + self.picturePath.GetValue() + " " + path.replace(" ", "\ ").replace("$", "\$").replace("'", "\\'").replace('"', '\\"').replace("#", "\\#").replace("[","\[").replace("]","\]").replace("!","\!").replace(">","\>").replace("<","\<").replace("|","\|").replace(";","\;").replace("{","\{").replace("}","\}").replace("(","\(").replace(")","\)").replace("~","\~"))

        for path in glob.iglob(os.path.join(self.directoryPath.GetValue(), '*.mp3.mp3')):
            os.rename(path, path[:-4])
        self.status.SetLabel("Adding Successed!!!")


    def selectDirectory(self, event):
        selectDirectoryDialog = wx.DirDialog(self, "select")
        selectDirectoryDialog.ShowModal()
        self.directoryPath.SetValue(selectDirectoryDialog.GetPath())
        selectDirectoryDialog.Destroy()
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 694,145 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.picturePath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        fgSizer1.Add( self.picturePath, 0, wx.ALL, 5 )
        
        self.pictureButton = wx.Button( self, wx.ID_ANY, u"select picture", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.pictureButton, 0, wx.ALL, 5 )
        
        self.directoryPath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        fgSizer1.Add( self.directoryPath, 0, wx.ALL, 5 )
        
        self.directoryButton = wx.Button( self, wx.ID_ANY, u"select directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.directoryButton, 0, wx.ALL, 5 )
        
        self.status = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.status.Wrap( -1 )
        fgSizer1.Add( self.status, 0, wx.ALL, 5 )
        
        self.addButton = wx.Button( self, wx.ID_ANY, u"add cover", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.addButton, 0, wx.ALL, 5 )
        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.pictureButton.Bind(wx.EVT_BUTTON, self.selectPicture)
        self.directoryButton.Bind(wx.EVT_BUTTON, self.selectDirectory)
        self.addButton.Bind(wx.EVT_BUTTON, self.add)

if __name__ == "__main__":
    app = wx.App(False)
    frame = AddCoverDialog(None)
    frame.Show()
    app.MainLoop()