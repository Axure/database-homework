#-*- encoding: utf-8 -*-

import wx, sys, noname
from database import *
# from person_model import *              
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
    def OnInit(self):
        self.MDid = None
        self.PDid = None
        self.persons = None
        self.tax = None
        
    # 管理部门视图
    def open_add_depa(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Show()
        self.modify_depa_panel.Hide()
        self.add_person_panel.Hide()
        self.modify_person_panel.Hide()
        self.mana_tax_panel.Hide()
        
    def open_modify_depa(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Show()
        self.add_person_panel.Hide()
        self.modify_person_panel.Hide()
        self.mana_tax_panel.Hide()
        
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
        data = self.list_depa.GetStringSelection()
        data = data.split(u'   ')
        self.MDid=data[1]
        MDname=data[0]
        self.depa_name_entry.SetValue(MDname)
        print self.list_depa.GetStringSelection()

    def confirm_modify_depa(self, event):
        MDname = self.depa_name_entry.GetValue()
        if self.MDid == None:
            wx.MessageBox("不能修改",style=wx.OK)
        else:
            update_depa(self.MDid, MDname)
            depa = get_all_depa()
            self.list_depa.Clear()
            for kk in depa:
                self.list_depa.Append(depa[kk]+u'   '+str(kk))
                print depa[kk]+"    "+str(kk)
            self.list_depa.Refresh()
            self.Mself.Did = None
            self.depa_name_entry.SetValue("")


    def confirm_del_depa(self, event):
        if self.Mself.Did == None:
            wx.MessageBox("不能删除",style=wx.OK)
        else:
            del_depa(self.Mself.Did)
            depa = get_all_depa()
            self.list_depa.Clear()
            for kk in depa:
                self.list_depa.Append(depa[kk]+u'   '+str(kk))
                print depa[kk]+"    "+str(kk)
            self.list_depa.Refresh()

        
    def canel_modify_dpea(self, event):
        self.Mself.Did = None
        self.depa_name_entry.SetValue("")

    #管理人员视图
    def open_add_person(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Hide()
        self.add_person_panel.Show()
        self.modify_person_panel.Hide()
        self.mana_tax_panel.Hide()

        depa = get_all_depa()
        self.select_depa_add_person.Clear()
        for kk in depa:
            self.select_depa_add_person.Append(depa[kk]+u'   '+str(kk))
            print depa[kk]+"    "+str(kk)
        self.select_depa_add_person.Refresh()
    
    def open_modify_person(self, event):
        self.welcome_panel.Hide()
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Hide()
        self.add_person_panel.Hide()
        self.modify_person_panel.Show()
        self.mana_tax_panel.Hide()
        self.refresh_grid()
        
    def refresh_grid(self):
        self.persons = get_all_person()
        num_rows = self.modify_person_grid.GetNumberRows()
        # 防止添加新行
        if num_rows < len(self.persons):
            self.modify_person_grid.AppendRows(len(self.persons)-num_rows)
            rows = self.modify_person_grid.GetNumberRows()
            for kk in range(0, rows):
                self.modify_person_grid.SetCellValue(kk,0, str( self.persons[kk]['Pid'] ))
                self.modify_person_grid.SetCellValue(kk,1, self.persons[kk]['Pname'])
                self.modify_person_grid.SetCellValue(kk,2, self.persons[kk]['Psex'])
                self.modify_person_grid.SetCellValue(kk,3, self.persons[kk]['Dname'])    
        else:
            sel_row = self.modify_person_grid.GetGridCursorRow()
            self.modify_person_grid.DeleteRows(sel_row)

    # 管理人员事件
    # 添加人员
    def select_person_depa(self, event):
        data = self.select_depa_add_person.GetStringSelection()
        data = data.split("   ")
        self.person_depa_entry.SetValue(data[0])
        self.Did = int(data[1])
        print self.Did

    def confirm_add_person(self, event):
        person = {}
        flag = True
        person['name'] = self.person_name_entry.GetValue()
        person['sex'] = self.person_sex_choice.GetValue()
        person['depa'] = self.person_depa_entry.GetValue()
        person['salary'] = self.person_salary_entry.GetValue()
        person['work'] = self.person_work_entry.GetValue()
        person['dismiss'] = self.isDismiss_choice.GetValue()
        person['depa'] = self.Did
        for ss in person:
            if ss == 'salary':
                try:                    # 是否可以转换为float型，异常
                    person[ss] = round(float(person[ss]), 2)
                except ValueError, e:
                    wx.MessageBox("%s数值错误"% ss,style=wx.OK)
                    flag = False

            if person[ss] == "" :
                wx.MessageBox("%s不能为空"% ss,style=wx.OK)
                flag = False
                break
        if flag == True:
            add_person(person)
            wx.MessageBox("添加成功  %s"% person['name'],style=wx.OK)
            self.person_name_entry.SetValue("")
            self.person_sex_choice.SetValue("")
            self.person_depa_entry.SetValue("")
            self.person_salary_entry.SetValue("")
            self.person_work_entry.SetValue("")
            self.isDismiss_choice.SetValue("")
            self.Did = ""

    def cancel_add_person(self, event):
        self.person_name_entry.SetValue("")
        self.person_sex_choice.SetValue("")
        self.person_depa_entry.SetValue("")
        self.person_salary_entry.SetValue("")
        self.person_work_entry.SetValue("")
        self.isDismiss_choice.SetValue("")


    # 修改人员
    def get_select_person(self, event):
        row = self.modify_person_grid.GetGridCursorRow()
        Pid = int(self.modify_person_grid.GetCellValue(row, 0)) - 1
        person = self.persons[row]
        self.modify_person_name_entry.SetValue(person['Pname'])
        self.modify_person_sex_choice.Clear()
        self.modify_person_sex_choice.AppendItems(["男","女"])
        self.modify_person_sex_choice.Select(person['Psex']!='男')
        depa = get_all_depa()
        depa_list = []
        for ss in depa:
            depa_list.append(str(depa[ss])+'   '+str(ss))
        print depa_list
        # 取出部门并显示
        self.modify_person_depa_choice.Clear()
        self.modify_person_depa_choice.AppendItems(depa_list)
        choice_depa = "%s   %d"%(person['Dname'], person['Ddepa'])
        self.modify_person_depa_choice.Select(depa_list.index(choice_depa))
        # 工资
        self.modify_person_salay_entry.SetValue(str(person['Psalary']))
        # 工种
        self.modify_person_work_entry.SetValue(person['Pwork'])
        # 离职
        self.modify_person_isdissmiss_choice.Clear()
        self.modify_person_isdissmiss_choice.AppendItems(['是','否'])
        self.modify_person_isdissmiss_choice.Select(person['Pdismiss'] != '是')
        
    def confirm_modify_person(self, event):
        flag = True
        person = {}
        row = self.modify_person_grid.GetGridCursorRow()
        Pid = self.modify_person_grid.GetCellValue(row, 0)
        person['Pid'] = Pid
        person['Pname'] = self.modify_person_name_entry.GetValue()
        person['Psex'] = self.modify_person_sex_choice.GetValue()
        depa = self.modify_person_depa_choice.GetValue()
        depa = depa.split("   ")
        person['Pdepa'] = depa[1]
        person['Psalary'] = self.modify_person_salay_entry.GetValue()
        person['Pwork'] = self.modify_person_work_entry.GetValue()
        person['Pdismiss'] = self.modify_person_isdissmiss_choice.GetValue()
        for kk in person:
            if person[kk] == "":
                flag = False
                break
            if kk == 'Psalary':
                try:                    # 是否可以转换为float型，异常
                    person[kk] = round(float(person[kk]), 2)
                except ValueError, e:
                    wx.MessageBox("工资数值错误",style=wx.OK)
                    flag = False
                break
        if flag == True:
            update_person(person)
            wx.MessageBox("修改成功  %s"% person['Pname'],style=wx.OK)
            self.refresh_grid()
        pass

    # 删除人员
    def confirm_del_person(self, event):
        print "confirm_del"
        row = self.modify_person_grid.GetGridCursorRow()
        Pid = int(self.modify_person_grid.GetCellValue(row, 0))
        del_person(Pid)
        self.refresh_grid()
        pass
    
    # 工资管理视图                        
    def open_mana_tax(self, event):
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Hide()
        self.add_person_panel.Hide()
        self.modify_person_panel.Hide()
        self.mana_tax_panel.Show()
        self.account_salary_panel.Hide()
        
    def oepn_account_salary(self, event):
        self.add_depa_panel.Hide()
        self.modify_depa_panel.Hide()
        self.add_person_panel.Hide()
        self.modify_person_panel.Hide()
        self.mana_tax_panel.Hide()
        self.account_salary_panel.Show()

    # 工资管理事件
    def confirm_add_tax(self, event):
        
        pass
    def confirm_modify_tax(self, event):
        pass
    def confirm_del_tax(self, event):
        pass
    def select_tax_item(self, event):
        pass

    # 系统
    def onExit(self, event):
        self.Close()
