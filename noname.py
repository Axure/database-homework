# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.grid

###########################################################################
## Class login_dialog
###########################################################################

class login_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"登陆", pos = wx.Point( 800,300 ), size = wx.Size( 280,200 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 3, 2, 10, 0 )
		fgSizer3.AddGrowableCol( 3 )
		fgSizer3.AddGrowableRow( 3 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3.SetMinSize( wx.Size( 300,200 ) ) 
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"user", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.user_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.user_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.passwd_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		fgSizer3.Add( self.passwd_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.confirm_button = wx.Button( self, wx.ID_OK, u"confirm", wx.Point( -1,-1 ), wx.Size( -1,40 ), 0 )
		fgSizer3.Add( self.confirm_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_CANCEL, u"cancel", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		fgSizer3.Add( self.cancel_button, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PersonnelManagement_frame
###########################################################################

class PersonnelManagement_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PersonnelManagement", pos = wx.DefaultPosition, size = wx.Size( 700,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menu = wx.MenuBar( 0 )
		self.mana_depa_menu = wx.Menu()
		self.add_depa_item = wx.MenuItem( self.mana_depa_menu, wx.ID_ANY, u"添加部门", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_depa_menu.AppendItem( self.add_depa_item )
		
		self.modify_depa_item = wx.MenuItem( self.mana_depa_menu, wx.ID_ANY, u"修改部门", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_depa_menu.AppendItem( self.modify_depa_item )
		
		self.menu.Append( self.mana_depa_menu, u"管理部门" ) 
		
		self.mana_personnel_menu = wx.Menu()
		self.add_person_item = wx.MenuItem( self.mana_personnel_menu, wx.ID_ANY, u"添加人员", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_personnel_menu.AppendItem( self.add_person_item )
		
		self.modify_person_item = wx.MenuItem( self.mana_personnel_menu, wx.ID_ANY, u"修改人员", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_personnel_menu.AppendItem( self.modify_person_item )
		
		self.menu.Append( self.mana_personnel_menu, u"人事管理" ) 
		
		self.mana_salary_menu = wx.Menu()
		self.mana_tax_item = wx.MenuItem( self.mana_salary_menu, wx.ID_ANY, u"设置税项", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_salary_menu.AppendItem( self.mana_tax_item )
		
		self.account_salary_item = wx.MenuItem( self.mana_salary_menu, wx.ID_ANY, u"结算工资", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_salary_menu.AppendItem( self.account_salary_item )
		
		self.menu.Append( self.mana_salary_menu, u"工资管理" ) 
		
		self.mana_system_menu = wx.Menu()
		self.modify_passwd_item = wx.MenuItem( self.mana_system_menu, wx.ID_ANY, u"修改密码", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_system_menu.AppendItem( self.modify_passwd_item )
		
		self.exit_item = wx.MenuItem( self.mana_system_menu, wx.ID_ANY, u"退出系统", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_system_menu.AppendItem( self.exit_item )
		
		self.menu.Append( self.mana_system_menu, u"系统设置" ) 
		
		self.SetMenuBar( self.menu )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.welcome_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.welcome_panel.Hide()
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self.welcome_panel, wx.ID_ANY, u"welcome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer7.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.welcome_panel.SetSizer( bSizer7 )
		self.welcome_panel.Layout()
		bSizer7.Fit( self.welcome_panel )
		bSizer6.Add( self.welcome_panel, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.add_depa_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.add_depa_panel.Hide()
		
		gSizer1 = wx.GridSizer( 2, 2, 20, 0 )
		
		self.m_staticText16 = wx.StaticText( self.add_depa_panel, wx.ID_ANY, u"部门名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer1.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.name_depa_entry = wx.TextCtrl( self.add_depa_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizer1.Add( self.name_depa_entry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.submit_button = wx.Button( self.add_depa_panel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.submit_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self.add_depa_panel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.add_depa_panel.SetSizer( gSizer1 )
		self.add_depa_panel.Layout()
		gSizer1.Fit( self.add_depa_panel )
		bSizer6.Add( self.add_depa_panel, 1, wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.modify_depa_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.modify_depa_panel.Hide()
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		list_depaChoices = []
		self.list_depa = wx.ListBox( self.modify_depa_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_depaChoices, wx.LB_SINGLE )
		gSizer4.Add( self.list_depa, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.name = wx.StaticText( self.modify_depa_panel, wx.ID_ANY, u"部门名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )
		gSizer5.Add( self.name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.depa_name_entry = wx.TextCtrl( self.modify_depa_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.depa_name_entry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.confirm_modify_depa_button = wx.Button( self.modify_depa_panel, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.confirm_modify_depa_button, 0, wx.ALL, 5 )
		
		self.cancel_modify_depa_button = wx.Button( self.modify_depa_panel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.cancel_modify_depa_button, 0, wx.ALL, 5 )
		
		self.del_depa_button = wx.Button( self.modify_depa_panel, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.del_depa_button, 0, wx.ALL, 5 )
		
		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		self.modify_depa_panel.SetSizer( gSizer4 )
		self.modify_depa_panel.Layout()
		gSizer4.Fit( self.modify_depa_panel )
		bSizer6.Add( self.modify_depa_panel, 1, wx.EXPAND, 5 )
		
		self.add_person_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.add_person_panel.Hide()
		
		gSizer51 = wx.GridSizer( 0, 2, 0, 0 )
		
		select_depa_add_personChoices = []
		self.select_depa_add_person = wx.ListBox( self.add_person_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, select_depa_add_personChoices, wx.LB_SINGLE )
		gSizer51.Add( self.select_depa_add_person, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.person_name_entry = wx.TextCtrl( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.person_name_entry, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		person_sex_choiceChoices = [ u"男", u"女" ]
		self.person_sex_choice = wx.ComboBox( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, person_sex_choiceChoices, wx.CB_READONLY )
		fgSizer2.Add( self.person_sex_choice, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"所属部门", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.person_depa_entry = wx.TextCtrl( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.person_depa_entry, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"基本工资", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.person_salary_entry = wx.TextCtrl( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.person_salary_entry, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"工种", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.person_work_entry = wx.TextCtrl( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.person_work_entry, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.add_person_panel, wx.ID_ANY, u"是否离职", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer2.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		isDismiss_choiceChoices = [ u"是", u"否" ]
		self.isDismiss_choice = wx.ComboBox( self.add_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, isDismiss_choiceChoices, wx.CB_READONLY )
		fgSizer2.Add( self.isDismiss_choice, 0, wx.ALL, 5 )
		
		self.confirm_add_person_button = wx.Button( self.add_person_panel, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.confirm_add_person_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.cancel_add_person_button = wx.Button( self.add_person_panel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.cancel_add_person_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer51.Add( fgSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.add_person_panel.SetSizer( gSizer51 )
		self.add_person_panel.Layout()
		gSizer51.Fit( self.add_person_panel )
		bSizer6.Add( self.add_person_panel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.modify_person_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.modify_person_panel.Hide()
		
		gSizer7 = wx.GridSizer( 2, 2, 0, 0 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.modify_person_grid = wx.grid.Grid( self.modify_person_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.modify_person_grid.CreateGrid( 1, 4 )
		self.modify_person_grid.EnableEditing( False )
		self.modify_person_grid.EnableGridLines( True )
		self.modify_person_grid.EnableDragGridSize( False )
		self.modify_person_grid.SetMargins( 0, 0 )
		
		# Columns
		self.modify_person_grid.SetColSize( 0, 80 )
		self.modify_person_grid.SetColSize( 1, 80 )
		self.modify_person_grid.SetColSize( 2, 80 )
		self.modify_person_grid.SetColSize( 3, 69 )
		self.modify_person_grid.EnableDragColMove( False )
		self.modify_person_grid.EnableDragColSize( True )
		self.modify_person_grid.SetColLabelSize( 30 )
		self.modify_person_grid.SetColLabelValue( 0, u"编号" )
		self.modify_person_grid.SetColLabelValue( 1, u"姓名" )
		self.modify_person_grid.SetColLabelValue( 2, u"性别" )
		self.modify_person_grid.SetColLabelValue( 3, u"所属部门" )
		self.modify_person_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.modify_person_grid.EnableDragRowSize( False )
		self.modify_person_grid.SetRowLabelSize( 20 )
		self.modify_person_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.modify_person_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer61.Add( self.modify_person_grid, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer7.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		gSizer511 = wx.GridSizer( 0, 1, 0, 0 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText61 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer21.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.modify_person_name_entry = wx.TextCtrl( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.modify_person_name_entry, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer21.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		modify_person_sex_choiceChoices = []
		self.modify_person_sex_choice = wx.ComboBox( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, modify_person_sex_choiceChoices, wx.CB_READONLY )
		fgSizer21.Add( self.modify_person_sex_choice, 0, wx.ALL, 5 )
		
		self.m_staticText121 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"所属部门", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		fgSizer21.Add( self.m_staticText121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		modify_person_depa_choiceChoices = []
		self.modify_person_depa_choice = wx.ComboBox( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, modify_person_depa_choiceChoices, wx.CB_READONLY )
		fgSizer21.Add( self.modify_person_depa_choice, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"工资", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		fgSizer21.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.modify_person_salay_entry = wx.TextCtrl( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.modify_person_salay_entry, 0, wx.ALL, 5 )
		
		self.m_staticText141 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"工种", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		fgSizer21.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.modify_person_work_entry = wx.TextCtrl( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.modify_person_work_entry, 0, wx.ALL, 5 )
		
		self.m_staticText151 = wx.StaticText( self.modify_person_panel, wx.ID_ANY, u"是否离职", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer21.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		modify_person_isdissmiss_choiceChoices = []
		self.modify_person_isdissmiss_choice = wx.ComboBox( self.modify_person_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, modify_person_isdissmiss_choiceChoices, wx.CB_READONLY )
		fgSizer21.Add( self.modify_person_isdissmiss_choice, 0, wx.ALL, 5 )
		
		self.confirm_modify_person_button = wx.Button( self.modify_person_panel, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.confirm_modify_person_button, 0, wx.ALL, 5 )
		
		self.confirm_del_person_button = wx.Button( self.modify_person_panel, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.confirm_del_person_button, 0, wx.ALL, 5 )
		
		gSizer511.Add( fgSizer21, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer7.Add( gSizer511, 1, wx.EXPAND, 5 )
		
		self.modify_person_panel.SetSizer( gSizer7 )
		self.modify_person_panel.Layout()
		gSizer7.Fit( self.modify_person_panel )
		bSizer6.Add( self.modify_person_panel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.mana_tax_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.mana_tax_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_add_depa, id = self.add_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_modify_depa, id = self.modify_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_add_person, id = self.add_person_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_modify_person, id = self.modify_person_item.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.exit_item.GetId() )
		self.submit_button.Bind( wx.EVT_BUTTON, self.confirm_add_depa )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.cancel_add_depa )
		self.list_depa.Bind( wx.EVT_LISTBOX_DCLICK, self.select_depa )
		self.confirm_modify_depa_button.Bind( wx.EVT_BUTTON, self.confirm_modify_depa )
		self.cancel_modify_depa_button.Bind( wx.EVT_BUTTON, self.cancel_modify_depa )
		self.del_depa_button.Bind( wx.EVT_BUTTON, self.confirm_del_depa )
		self.select_depa_add_person.Bind( wx.EVT_LISTBOX_DCLICK, self.select_person_depa )
		self.confirm_add_person_button.Bind( wx.EVT_BUTTON, self.confirm_add_person )
		self.cancel_add_person_button.Bind( wx.EVT_BUTTON, self.cancel_add_person )
		self.modify_person_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.get_select_person )
		self.confirm_modify_person_button.Bind( wx.EVT_BUTTON, self.confirm_modify_person )
		self.confirm_del_person_button.Bind( wx.EVT_BUTTON, self.confirm_del_person )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def open_add_depa( self, event ):
		event.Skip()
	
	def open_modify_depa( self, event ):
		event.Skip()
	
	def open_add_person( self, event ):
		event.Skip()
	
	def open_modify_person( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	
	def confirm_add_depa( self, event ):
		event.Skip()
	
	def cancel_add_depa( self, event ):
		event.Skip()
	
	def select_depa( self, event ):
		event.Skip()
	
	def confirm_modify_depa( self, event ):
		event.Skip()
	
	def cancel_modify_depa( self, event ):
		event.Skip()
	
	def confirm_del_depa( self, event ):
		event.Skip()
	
	def select_person_depa( self, event ):
		event.Skip()
	
	def confirm_add_person( self, event ):
		event.Skip()
	
	def cancel_add_person( self, event ):
		event.Skip()
	
	def get_select_person( self, event ):
		event.Skip()
	
	def confirm_modify_person( self, event ):
		event.Skip()
	
	def confirm_del_person( self, event ):
		event.Skip()
	

###########################################################################
## Class account_salary_panel
###########################################################################

class account_salary_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class user_passwd_panel
###########################################################################

class user_passwd_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

