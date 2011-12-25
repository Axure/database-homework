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
		
		self.del_depa_item = wx.MenuItem( self.mana_depa_menu, wx.ID_ANY, u"删除部门", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_depa_menu.AppendItem( self.del_depa_item )
		
		self.menu.Append( self.mana_depa_menu, u"管理部门" ) 
		
		self.mana_personnel_menu = wx.Menu()
		self.add_person_item = wx.MenuItem( self.mana_personnel_menu, wx.ID_ANY, u"添加人员", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_personnel_menu.AppendItem( self.add_person_item )
		
		self.search_person_item = wx.MenuItem( self.mana_personnel_menu, wx.ID_ANY, u"查看人员", wx.EmptyString, wx.ITEM_NORMAL )
		self.mana_personnel_menu.AppendItem( self.search_person_item )
		
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
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
		self.m_toolBar1.AddSeparator()
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"account_salary", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
		self.m_toolBar1.AddSeparator()
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"exit", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
		self.m_toolBar1.Realize() 
		
		bSizer1.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
		
		self.welcome = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.welcome, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_add_depa, id = self.add_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_modify_depa, id = self.modify_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.open_del_depa, id = self.del_depa_item.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.exit_item.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def open_add_depa( self, event ):
		event.Skip()
	
	def open_modify_depa( self, event ):
		event.Skip()
	
	def open_del_depa( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	

###########################################################################
## Class add_depa_panel
###########################################################################

class add_depa_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		gSizer1 = wx.GridSizer( 2, 2, 20, 0 )
		
		gSizer1.SetMinSize( wx.Size( 20,20 ) ) 
		self.depa_name = wx.StaticText( self, wx.ID_ANY, u"部门名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.depa_name.Wrap( -1 )
		gSizer1.Add( self.depa_name, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.name_depa_entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gSizer1.Add( self.name_depa_entry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.submit_button = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.submit_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.SetSizer( gSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class del_depa_panel
###########################################################################

class del_depa_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )
		
		self.list_depa = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
		gSizer4.Add( self.list_depa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.del_button = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.del_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( gSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class modify_depa_panel
###########################################################################

class modify_depa_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.list_depa = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), wx.LC_ICON )
		gSizer4.Add( self.list_depa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.name = wx.StaticText( self, wx.ID_ANY, u"部门名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )
		gSizer5.Add( self.name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.depa_name_entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.depa_name_entry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.submit_button = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.submit_button, 0, wx.ALL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		self.SetSizer( gSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class add_person_panel
###########################################################################

class add_person_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

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
	

###########################################################################
## Class MyPanel11
###########################################################################

class MyPanel11 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

