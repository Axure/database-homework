#-*- encoding: utf-8 -*-

import wx, sys, noname
from database import *

class login_frame(noname.login_frame):
    #check user
    def check(self, event):
        name = self.user_text.GetValue()
        passwd = self.passwd_text.GetValue()
        if check_user(name, passwd):
            wx.MessageBox("登陆成功",style=wx.OK)
            print name, passwd, "OK"
        else:
            wx.MessageBox("输入错误系统退出",style=wx.OK|wx.ICON_EXCLAMATION)
            sys.exit()

    #clear text
    def cancel(self, event):
        self.LoginFrame.user_text.SetValue("")
        self.LoginFrame.passwd_text.SetValue("")

