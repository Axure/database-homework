#-*- encoding: utf-8 -*-

import wx, sys, noname
from database import *
reload(sys) 
sys.setdefaultencoding('utf8')

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
    # 管理部门视图
    def open_add_depa(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Show()
        self.modify_depa_panel.Hide()

        
    def open_del_depa(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Hide()
        
        pass

    def open_modify_depa(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Show()
        
        depa = get_all_depa()
        self.list_depa.Clear()
        for kk in depa:
            self.list_depa.Append(depa[kk]+u'   '+str(kk))
            print depa[kk]+"    "+str(kk)
        self.list_depa.Refresh()
        

    # 管理部门事件
    def confirm_add_depa(self, event):
        Dname = self.name_depa_entry.GetValue()
        add_depa(Dname)
        wx.MessageBox("插入成功",style=wx.OK)

    def select_depa(self,event):
        global MDid
        data = self.list_depa.GetStringSelection()
        data = data.split(u'   ')
        MDid=data[1]
        MDname=data[0]
        self.depa_name_entry.SetValue(MDname)
        print self.list_depa.GetStringSelection()

    def confirm_modify_depa(self, event):
        MDname = self.depa_name_entry.GetValue()
        if MDid == None:
            wx.MessageBox("不能修改",style=wx.OK)
        else:
            update_depa(MDid, MDname)
            depa = get_all_depa()
            self.list_depa.Clear()
            for kk in depa:
                self.list_depa.Append(depa[kk]+u'   '+str(kk))
                print depa[kk]+"    "+str(kk)
            self.list_depa.Refresh()

    def confirm_del_depa(self, event):
        if MDid == None:
            wx.MessageBox("不能删除",style=wx.OK)
        else:
            del_depa(MDid)
            depa = get_all_depa()
            self.list_depa.Clear()
            for kk in depa:
                self.list_depa.Append(depa[kk]+u'   '+str(kk))
                print depa[kk]+"    "+str(kk)
            self.list_depa.Refresh()

        
    def canel_modify_dpea(self, event):
        MDid = None
        self.depa_name_entry.SetValue("")

    #管理人员视图
    def open_add_person(self, event):
        pass

    def open_modify_person(self, event):
        pass
    
    #管理人员事件



    
    # 系统设置
    def onExit(self, event):
        self.Close()
