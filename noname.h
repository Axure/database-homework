///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2009)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __noname__
#define __noname__

#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class login
///////////////////////////////////////////////////////////////////////////////
class login : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText1;
		wxTextCtrl* user;
		wxStaticText* m_staticText3;
		wxTextCtrl* passwd;
		wxButton* confirm;
		wxButton* m_button5;
	
	public:
		
		login( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("login"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		~login();
	
};

#endif //__noname__
