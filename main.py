import wx
from noname import *

app = wx.App()
win = loginFrame(None)

if __name__ == '__main__':
    win.Show()
    app.MainLoop()
