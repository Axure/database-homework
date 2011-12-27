# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PersonnelManagement", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		self.mana_bonus_item = wx.MenuItem( self.mana_salary_menu, wx.ID_ANY, u"设置应发", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_salary_menu.AppendItem( self.mana_bonus_item )
		
		self.mana_fine_item = wx.MenuItem( self.mana_salary_menu, wx.ID_ANY, u"设置应扣", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_salary_menu.AppendItem( self.mana_fine_item )
		
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
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		list_depaChoices = []
		self.list_depa = wx.ListBox( self.modify_depa_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_depaChoices, wx.LB_SINGLE )
		gSizer4.Add( self.list_depa, 0, wx.ALL|wx.EXPAND, 5 )
		
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
		bSizer6.Add( self.modify_depa_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_add_depa, id = self.add_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_modify_depa, id = self.modify_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.exit_item.GetId() )
		self.submit_button.Bind( wx.EVT_BUTTON, self.confirm_add_depa )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.cancel_add_depa )
		self.list_depa.Bind( wx.EVT_LISTBOX_DCLICK, self.select_depa )
		self.confirm_modify_depa_button.Bind( wx.EVT_BUTTON, self.confirm_modify_depa )
		self.cancel_modify_depa_button.Bind( wx.EVT_BUTTON, self.cancel_modify_depa )
		self.del_depa_button.Bind( wx.EVT_BUTTON, self.confirm_del_depa )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def open_add_depa( self, event ):
		event.Skip()
	
	def open_modify_depa( self, event ):
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
	

###########################################################################
## Class search_person_panel
###########################################################################

class search_person_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class modify_person_panel
###########################################################################

class modify_person_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class mana_tax_panel
###########################################################################

class mana_tax_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

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
	

