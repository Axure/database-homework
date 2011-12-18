///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2009)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

login::login( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxFlexGridSizer* fgSizer3;
	fgSizer3 = new wxFlexGridSizer( 2, 2, 0, 0 );
	fgSizer3->AddGrowableCol( 3 );
	fgSizer3->AddGrowableRow( 3 );
	fgSizer3->SetFlexibleDirection( wxBOTH );
	fgSizer3->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("user"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	fgSizer3->Add( m_staticText1, 0, wxALL, 5 );
	
	user = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( user, 0, wxALL, 5 );
	
	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("password"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	fgSizer3->Add( m_staticText3, 0, wxALL, 5 );
	
	passwd = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( passwd, 0, wxALL, 5 );
	
	confirm = new wxButton( this, wxID_ANY, wxT("confirm"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( confirm, 0, wxALL, 5 );
	
	m_button5 = new wxButton( this, wxID_ANY, wxT("cancel"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_button5, 0, wxALL, 5 );
	
	this->SetSizer( fgSizer3 );
	this->Layout();
}

login::~login()
{
}
