#-*- encoding: utf-8 -*-

import wx, sys, noname
from database import *

class login_dialog(noname.login_dialog):
    #check user
    def check(self):
        name = self.user_text.GetValue()
        passwd = self.passwd_text.GetValue()
        if check_user(name, passwd):
            wx.MessageBox("登陆成功",style=wx.OK)
            # print name, passwd, "OK"
            return True
        else:
            wx.MessageBox("输入错误系统退出",style=wx.OK|wx.ICON_EXCLAMATION)
            return False
    
class PM_frame(noname.PersonnelManagement_frame):
    # 管理部门
    def open_add_depa(self, event):
        pass
    def open_del_depa(self, event):
        pass
    def open_modify_depa(self, event):
        pass
    # 系统设置
    def onExit(self, event):
        self.Close()
