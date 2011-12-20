#-*- encoding: utf-8 -*-

import wx, sys
from database import *
from noname import *
from main import *

#PM_App
class PM_App(wx.App):
     def OnInit(self):
         self.LoginFrame = login_frame(None)
         self.LoginFrame.Show()
         self.SetTopWindow(self.LoginFrame)
         self.PMFrame = PersonnelManagement_frame(None)
         return True

#check user
def check(event):
    name = app.LoginFrame.user_text.GetValue()
    passwd = app.LoginFrame.passwd_text.GetValue()
    if check_user(name, passwd):
        wx.MessageBox("登陆成功",style=wx.OK)
        app.LoginFrame.Destroy()
        app.PMFrame.Show()
        print name, passwd, "OK"
    else:
        wx.MessageBox("输入错误系统退出",style=wx.OK|wx.ICON_EXCLAMATION)
        sys.exit()

#clear text
def cancel(event):
    app.LoginFrame.user_text.SetValue("")
    app.LoginFrame.passwd_text.SetValue("")

#bind button event
def BindButtonEvent():
    app.LoginFrame.confirm_button.Bind(wx.EVT_BUTTON, check)
    app.LoginFrame.cancel_button.Bind(wx.EVT_BUTTON, cancel)

if __name__ == '__main__':
    app = PM_App()
    BindButtonEvent()
    app.MainLoop()

