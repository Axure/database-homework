import wx
from interface import *

app = wx.App()
win = login_frame(None)

if __name__ == '__main__':
    win.Show()
    app.MainLoop()
