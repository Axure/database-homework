#-*- encoding: utf-8 -*-

import wx, sys
from Frame import *

#PM_App wx.App
class PM_App(wx.App):
    def OnInit(self):
         self.PM_Frame = PM_frame(None)
         self.SetTopWindow(self.PM_Frame)
         return True

if __name__ == '__main__':
    global x;
    app = PM_App()
    while True:
        login = login_dialog(None)
        answer = login.ShowModal()
        print answer
        if answer == wx.ID_OK:
            x = login.check()
            break
        else:
            login.Destroy()
            app.Destroy()
            sys.exit()

    if x == True:
        app.PM_Frame.Show()
    else:
        sys.exit()
    app.MainLoop()
