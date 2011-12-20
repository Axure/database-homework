#-*- encoding: utf-8 -*-

import wx, sys
from database import *
from noname import *
from PM_APP import *
class PM_App(wx.App):
     def OnInit(self):
         self.LoginFrame = login_frame(None)
         self.LoginFrame.Show()
         self.SetTopWindow(self.LoginFrame)
         self.LoginFrame.confirm.Bind(wx.EVT_BUTTON, check);
         return True
