#!/usr/bin/env python

import wx
import wx.lib.inspection
import sys,os
#from frame import Frame
#import wx.frame


class Log:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)
    write = WriteText



# menu bar is a beginning point 
class MyMainFrame(wx.Frame):
    def __init__(self, parent, id, log):
        wx.Frame.__init__(self, parent, id, 'Main Menu', size=(800,600))
        self.log = log
        self.CenterOnScreen()
        
        self.CreateStatusBar()
        self.SetStatusText("Status bar")

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu1.Append(101, "&menu101", "What the fuck")
        menuBar.Append(menu1, "&file")
        self.SetMenuBar(menuBar)

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1,
                         style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.log = log

        b = wx.Button(self, 10, "Default Button", (20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        b.SetDefault()
        b.SetSize(b.GetBestSize())

        b = wx.Button(self, 20, "HELLO AGAIN!", (20, 80)) ##, (120, 45))
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        b.SetToolTipString("This is a Hello button...")

        b = wx.Button(self, 40, "Flat Button?", (20,150), style=wx.NO_BORDER)
        b.SetToolTipString("This button has a style flag of wx.NO_BORDER.\nOn some platforms that will give it a flattened look.")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)


    def OnClick(self, event):
        self.log.write("Click! (%d)\n" % event.GetId())




class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)   
 
    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())
 
#      self.frame = wx.Frame(None, -1, "test1", pos=(50,50), size=(200,100), style=wx.DEFAULT_FRAME_STYLE, name="test2")
#        self.frame.Show()
#       self.SetTopWindow(self.frame)
#       self.panel1 = TestPanel(self.frame, Log())
#       self.frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame) 
#       self.frame.Show(True)
        
#       self.frame.SetSize((640, 480))
        self.frame = MyMainFrame(None, 1, Log())
#        self.frame.Show(True)
       
        self.SetTopWindow(self.frame)

        self.panel1 = TestPanel(self.frame, Log())
        self.frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame) 
        self.frame.Show(True)
        




        return True

    def OnExitApp(self, evt):
        print "close app"
        self.frame.Close(True)


    def OnCloseFrame(self, evt):
#    if hasattr(self, "window") and hasattr(self.window, "ShutdownDemo"):
#            self.window.ShutdownDemo()
#        evt.Skip()
        print "close frame" 
        exit()

def main():
    print " test "
    app = App()
    app.MainLoop()
#    while (True):
#        continue

if __name__ == '__main__':
    main()


