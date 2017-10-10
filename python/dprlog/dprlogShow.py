#!/usr/bin/env python

import wxversion
wxversion.select("3.0")
import wx
import wx.calendar
import wx.lib.inspection
import wx.aui

from logAnalyzer import logAnalyzerPanel
# import dprlog_disp

from dprlog_disp import dispPlane,fileDisplayPanel,dispInfoPlane


class ParentFrame(wx.aui.AuiMDIParentFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIParentFrame.__init__(self, parent, -1,
                                          title="AuiMDIParentFrame",
                                          size=(1024,768),
                                          style=wx.DEFAULT_FRAME_STYLE)
        self.count = 0
        self.workdir="C:\M2C\EslWebSystem\workdir"
        mb = self.MakeMenuBar()
        self.SetMenuBar(mb)
        self.CreateStatusBar()
        self.Bind(wx.EVT_CLOSE, self.OnDoClose)
        
    def MakeMenuBar(self):
        mb = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "Change workdir")
        self.Bind(wx.EVT_MENU, self.OnChangeDir, item)
        item = menu.Append(-1, "Load Log")
        self.Bind(wx.EVT_MENU, self.OnLoadLog, item)
        item = menu.Append(-1, "Load Info")
        self.Bind(wx.EVT_MENU, self.OnLoadInfo, item)
        item = menu.Append(-1, "Load DVH")
        self.Bind(wx.EVT_MENU, self.OnLoadDVH, item)

        item = menu.Append(-1, "Close parent")
        self.Bind(wx.EVT_MENU, self.OnDoClose, item)
        mb.Append(menu, "&File")
        return mb
        
    def OnNewChild(self, evt):
        self.count += 1
        child = ChildFrame(self, self.count)
        child.Activate()

    def OnLoadLog(self, evt):
        self.count += 1
        child = LogChildFrame(self, self.count, self.workdir)
        child.Activate()

    def OnLoadInfo(self, evt):
        self.count += 1
        child = InfoDisplayChildFrame(self, self.count, self.workdir)
        child.Activate()

    def OnLoadDVH(self, evt):
        self.count += 1
        child = LogAnalysisChildFrame(self, self.count, self.workdir)
        child.Activate()



    def OnChangeDir(self, evt):
        # In this case we include a "New directory" button.
        dlg = wx.DirDialog(self, "Choose a directory:",
                           defaultPath=self.workdir,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it.
        if dlg.ShowModal() == wx.ID_OK:
            self.workdir=dlg.GetPath()

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()


    def OnDoClose(self, evt):
        # Close all ChildFrames first else Python crashes
        for m in self.GetChildren():
            if isinstance(m, wx.aui.AuiMDIClientWindow):
                for k in m.GetChildren():
                    if isinstance(k, ChildFrame):
                        k.Close()  
        evt.Skip()
        

# ----------------------------------------------------------------------


class ChildFrame(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent, count):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Child: %d" % count)
        mb = parent.MakeMenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "This is child %d's menu" % count)
        mb.Append(menu, "&Child")
        self.SetMenuBar(mb)
        
        p = wx.Panel(self)
        wx.StaticText(p, -1, "This is child %d" % count, (10,10))
        p.SetBackgroundColour('light blue')

        sizer = wx.BoxSizer()
        sizer.Add(p, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        wx.CallAfter(self.Layout)

# ----------------------------------------------------------------------


class LogChildFrame(ChildFrame):
    def __init__(self, parent, count, workdir):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Log")

        self.workdir = workdir
        testplane1 = dispPlane(self, self.workdir)
        sizer = wx.BoxSizer()
        sizer.Add(testplane1, 1, wx.EXPAND)
        self.SetSizer(sizer)	       
        self.SetAutoLayout(True)
        wx.CallAfter(self.Layout)


class InfoDisplayChildFrame(ChildFrame):
    def __init__(self, parent, count, workdir):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Info")

        self.workdir = workdir
        testplane1 = dispInfoPlane(self, self.workdir)
        sizer = wx.BoxSizer()
        sizer.Add(testplane1, 1, wx.EXPAND)
        self.SetSizer(sizer)	       
        self.SetAutoLayout(True)
        wx.CallAfter(self.Layout)


class LogAnalysisChildFrame(ChildFrame):
    def __init__(self, parent, count, workdir):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="DVH")

        self.workdir = workdir
        testplane1 = logAnalyzerPanel(self, self.workdir)
        sizer = wx.BoxSizer()
        sizer.Add(testplane1, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        wx.CallAfter(self.Layout)

'''
class TestChildFrame(ChildFrame):
    def __init__(self, parent, count):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="TestCHILD")
        mb = parent.MakeMenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "This is child %d's menu" % count)
        mb.Append(menu, "&Child")
        self.SetMenuBar(mb)
        
        p = wx.Panel(self)
        wx.StaticText(p, -1, "This is child %d" % count, (10,10))
        p.SetBackgroundColour('light blue')

        sizer = wx.BoxSizer()
        sizer.Add(p, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        wx.CallAfter(self.Layout)
'''


class TestPanel(wx.Panel):
    def __init__(self, parent):       
        wx.Panel.__init__(self, parent, -1)
        # b = wx.Button(self, -1, "Show a AuiMDIParentFrame", (50,50))
        # self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        pf = ParentFrame(self)
        pf.Show()

    def OnButton(self, evt):
        pf = ParentFrame(self)
        pf.Show()

'''        
class TestPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        

        l1 = wx.StaticText(self, -1, "DPR Log")
        t1 = wx.TextCtrl(self, -1,                        
                        "Here is for DPR LOG",
                       size=(800, 400), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        l2 = wx.StaticText(self, -1, "AP Info")
        t2 = wx.TextCtrl(self, -1,
                        "Here is a looooooooooooooong line of text set in the control.\n\n"
                        "The quick brown fox jumped over the lazy dog...",
                       size=(400, 200), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)

        l3 = wx.StaticText(self, -1, "RT Info")
        t3 = wx.TextCtrl(self, -1,
                        "Here is a looooooooooooooong line of text set in the control.\n\n"
                        "The quick brown fox jumped over the lazy dog...",
                       size=(400, 200), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)

        t3.SetInsertionPoint(0)
        self.Bind(wx.EVT_TEXT, self.EvtText, t3)
        self.Bind(wx.EVT_TEXT_ENTER, self.EvtTextEnter, t3)
        
        b = wx.Button(self, -1, "Test Replace")
        self.Bind(wx.EVT_BUTTON, self.OnTestReplace, b)
        b2 = wx.Button(self, -1, "Test GetSelection")
        self.Bind(wx.EVT_BUTTON, self.OnTestGetSelection, b2)
        b3 = wx.Button(self, -1, "Test WriteText")
        self.Bind(wx.EVT_BUTTON, self.OnTestWriteText, b3)
        self.tc = t3


        l4 = wx.StaticText(self, -1, "Rich Text")
        t4 = wx.TextCtrl(self, -1, "If supported by the native control, this is red, and this is a different font.",
                        size=(200, 100), style=wx.TE_MULTILINE|wx.TE_RICH2)
        t4.SetInsertionPoint(0)
        t4.SetStyle(44, 47, wx.TextAttr("RED", "YELLOW"))
        points = t4.GetFont().GetPointSize()  # get the current size
        f = wx.Font(points+3, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        t4.SetStyle(63, 77, wx.TextAttr("BLUE", wx.NullColour, f))

        l5 = wx.StaticText(self, -1, "Test Positions")
        t5 = wx.TextCtrl(self, -1, "0123456789\n" * 5, size=(200, 100),
                         style = wx.TE_MULTILINE
                         #| wx.TE_RICH
                         | wx.TE_RICH2
                         )
        t5.Bind(wx.EVT_LEFT_DOWN, self.OnT5LeftDown)
        self.t5 = t5

        space = 6
        bsizer = wx.BoxSizer(wx.VERTICAL)
        bsizer.Add(b, 0, wx.GROW|wx.ALL, space)
        bsizer.Add(b2, 0, wx.GROW|wx.ALL, space)
        bsizer.Add(b3, 0, wx.GROW|wx.ALL, space)

        sizer = wx.FlexGridSizer(cols=3, hgap=space, vgap=space)
        sizer.AddMany([ l1, t1, (0,0),
                        l2, t2, (0,0),
                        l3, t3, bsizer,
                        l4, t4, (0,0),
                        l5, t5, (0,0),
                        ])
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(sizer, 0, wx.ALL, 25)
        self.SetSizer(border)
        self.SetAutoLayout(True)


    def EvtText(self, event):
        print('EvtText: %s\n' % event.GetString())

    def EvtTextEnter(self, event):
        print('EvtTextEnter\n')
        event.Skip()

    def EvtChar(self, event):
        print('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()


    def OnTestReplace(self, evt):
        self.tc.Replace(5, 9, "IS A")
        #self.tc.Remove(5, 9)

    def OnTestWriteText(self, evt):
        self.tc.WriteText("TEXT")

    def OnTestGetSelection(self, evt):
        start, end = self.tc.GetSelection()
        text = self.tc.GetValue()
        if wx.Platform == "__WXMSW__":  # This is why GetStringSelection was added
            text = text.replace('\n', '\r\n')

        self.log.write("multi-line GetSelection(): (%d, %d)\n"
                       "\tGetStringSelection(): %s\n"
                       "\tSelectedText: %s\n" %
                       (start, end,
                        self.tc.GetStringSelection(),
                        repr(text[start:end])))

        start, end = self.tc1.GetSelection()
        text = self.tc1.GetValue()

        if wx.Platform == "__WXMSW__":  # This is why GetStringSelection was added
            text = text.replace('\n', '\r\n')

        self.log.write("single-line GetSelection(): (%d, %d)\n"
                       "\tGetStringSelection(): %s\n"
                       "\tSelectedText: %s\n" %
                       (start, end,
                        self.tc1.GetStringSelection(),
                        repr(text[start:end])))


    def OnT5LeftDown(self, evt):
        evt.Skip()
        wx.CallAfter(self.LogT5Position, evt)

    def LogT5Position(self, evt):
        text = self.t5.GetValue()
        ip = self.t5.GetInsertionPoint()
        lp = self.t5.GetLastPosition()
        self.log.write("LogT5Position:\n"
                       "\tGetInsertionPoint:\t%d\n"
                       "\ttext[insertionpoint]:\t%s\n"
                       "\tGetLastPosition:\t%d\n"
                       "\tlen(text):\t\t%d\n"
                       % (ip, text[ip], lp, len(text)))


'''


class dprMainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DPR LOG Inspection', size=(800,600))
        self.testplane1 = TestPanel(self)
        pass


class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)
    
    def OnInit(self):
        #self.frame = dprMainFrame(None, 1)
        #self.frame.Show(True)
        
        self.pf = ParentFrame(None)
        self.pf.Show()

        # self.inspector = wx.lib.inspection.InspectionTool()
        # self.inspector.Show()
        return 1  

def testApp():
    print "Self testing function is written here"
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    testApp()		
		

