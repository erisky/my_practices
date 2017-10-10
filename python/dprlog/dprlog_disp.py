
'''#!/usr/bin/env python'''


import wx
import sys,os
from datetime import date
import wx.grid as gridlib
import fileinput


def getLinesFromFile(filename):
    count = 0
    for lines in fileinput.input(filename):
        count += 1

    print(count)
    return count


class csvDisplayPanel(wx.Panel):
    # A Panel class display the file with one reload button
    def __init__(self, parent, name, filePath, rows=1):
        wx.Panel.__init__(self, parent, -1)

        self.filePath = filePath
        print('file%s' % filePath)
        self.st = wx.StaticText(self, -1, name)
        self.buttonReload = wx.Button(self, -1, "Reload")
        self.Bind(wx.EVT_BUTTON, self.OnReloadPressed, self.buttonReload)

        self.gridcsv = gridlib.Grid(self,-1)

        self.numColumn = 0
        self.numRows = rows
        rows_temp = 0
        for lines in fileinput.input(self.filePath):
            # print(lines)
            ll = lines.split(',')
            if len(ll) > self.numColumn:
                self.numColumn = len(ll)
            rows_temp += 1 ;
        if rows_temp > self.numRows:
            self.numRows = rows_temp

        fileinput.close()

        # print(self.numRows+3, self.numColumn+1)
        self.numRows += 1
        self.gridcsv.CreateGrid(self.numRows, self.numColumn)#, gridlib.Grid.SelectRows)

        '''
        ri = 0
        for lines in fileinput.input(self.filePath):
            ll = lines.split(',')
            print(ll)
            for si in range(len(ll)):
                self.gridcsv.SetCellValue(ri, si, ll[si])
                if len(ll[si])>12:
                    self.gridcsv.SetColSize(si, 100)
                else:
                    self.gridcsv.SetColSize(si, 60)
            ri += 1
        #self.gridcsv.SetCellValue(1, 1, "Another cell")
        '''
        self.OnReloadPressed(0)

        space=2
        self.column1 = wx.BoxSizer(wx.VERTICAL)
        self.column1.Add(self.st, 0, wx.ALL, space)
        self.column1.Add(self.buttonReload, 0, wx.ALL, space)
        self.Rows = wx.BoxSizer(wx.HORIZONTAL)
        self.Rows.Add(self.column1, 0, wx.ALL, space)
        self.Rows.Add(self.gridcsv, 0, wx.ALL, space)
        self.SetSizer(self.Rows)




        # self.gridcsv.LoadFile(filePath)


        # self.f = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        # cb=wx.ColourDatabase()
        # self.fcolor = cb.Find("YELLOW")
        # self.bcolor = cb.Find("BLACK")

        # self.textshow.SetBackgroundColour(self.bcolor)
        # self.textshow.SetDefaultStyle(wx.TextAttr(self.fcolor, self.bcolor))
        # self.textshow.SetStyle(0, self.textshow.GetLastPosition(), wx.TextAttr(self.fcolor, self.bcolor, self.f))
        # self.textshow.ShowPosition(self.textshow.GetLastPosition()-600);
        self.SetAutoLayout(True)

    def OnReloadPressed(self, evt):
        '''
        self.Rows.Remove(self.column1)
        self.Rows.Remove(self.gridcsv)

        self.Rows.Add(self.buttonReload)

        self.SetSizer(self.Rows)
        wx.CallAfter(self.Layout)
        '''
        for rw in range(self.numRows):
            for cl in range(self.numColumn):
                self.gridcsv.SetCellValue(rw, cl, "")
        ri = 0
        for lines in fileinput.input(self.filePath):
            ll = lines.split(',')
            # print(ll)
            for si in range(len(ll)):
                # print(ri,si)
                self.gridcsv.SetCellValue(ri, si, ll[si])
                if len(ll[si]) >= 8 :
                    self.gridcsv.SetColSize(si, 110)
                else:
                    self.gridcsv.SetColSize(si, 50)
            ri += 1

    def changeFile(self, name, filename):
        self.filePath = filename
        self.OnReloadPressed(0)
        self.st.SetLabelText(name)


class fileDisplayPanel(wx.Panel):
    # A Panel class display the file with one reload button
    def __init__(self, parent, name, filePath, width=600, height=400):
        wx.Panel.__init__(self, parent, -1)
        
        self.filePath = filePath
        self.st = wx.StaticText(self, -1, name)
        self.buttonReload = wx.Button(self, -1, "Reload")    
        self.Bind(wx.EVT_BUTTON, self.OnReloadPressed, self.buttonReload)                
        self.textshow = wx.TextCtrl(self, -1,                        
                        "No File Loaded",
                       size=(width, height), style=wx.TE_MULTILINE|wx.TE_RICH2)
        space=2
        self.column1 = wx.BoxSizer(wx.VERTICAL)
        self.column1.Add(self.st, 0, wx.ALL, space)
        self.column1.Add(self.buttonReload, 0, wx.ALL, space)
        self.Rows = wx.BoxSizer(wx.HORIZONTAL) 
        self.Rows.Add(self.column1, 0, wx.ALL, space)
        self.Rows.Add(self.textshow, 0, wx.ALL, space)
        self.SetSizer(self.Rows)
        
        self.textshow.LoadFile(filePath)

        
        self.f = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        cb=wx.ColourDatabase()
        self.fcolor = cb.Find("YELLOW")
        self.bcolor = cb.Find("BLACK")
        
        self.textshow.SetBackgroundColour(self.bcolor)        
        self.textshow.SetDefaultStyle(wx.TextAttr(self.fcolor, self.bcolor))        
        self.textshow.SetStyle(0, self.textshow.GetLastPosition(), wx.TextAttr(self.fcolor, self.bcolor, self.f))
        self.textshow.ShowPosition(self.textshow.GetLastPosition()-600);
        self.SetAutoLayout(True)
    
    def OnReloadPressed(self, evt):        
        self.textshow.LoadFile(self.filePath)
        #self.t1.SetEditable(False)
              
        self.textshow.SetStyle(0, self.textshow.GetLastPosition(), wx.TextAttr(self.fcolor, self.bcolor, self.f))
        self.textshow.ShowPosition(self.textshow.GetLastPosition()-600);

    def changeFile(self, name, filename):
        self.filePath = filename
        self.OnReloadPressed(0)
        self.st.SetLabelText(name)


class dispPlane(wx.Panel):
    def __init__(self, parent, workdir):
        wx.Panel.__init__(self, parent, -1)

        self.workdir = workdir

        dprDisplay = fileDisplayPanel(self, "Dprlog", self.workdir + "\log\dprlog.log")
        crtDisplay = fileDisplayPanel(self, "Critical",self.workdir + "\log\crit.log")
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(dprDisplay, 0, wx.ALL, 2)       
        border.Add(crtDisplay, 0, wx.ALL, 2)
        
        self.SetSizer(border)
        self.SetAutoLayout(True)


class dispInfoPlane(wx.Panel):
    def __init__(self, parent, workdir):
        wx.Panel.__init__(self, parent, -1)
        self.workdir = workdir
        self.rtnum = 0
        self.rtbuttons = []
        self.rtnames = []
        apinfoPath = self.workdir + "\\ap_info.csv"
        # apInfoDisplay = fileDisplayPanel(self, "AP", apinfoPath, 800, 200)
        apInfoDisplay = csvDisplayPanel(self, "AP", apinfoPath)

        self.daemon_ver_st = wx.StaticText(self, -1, "Daemon Ver:")

        daemon_ver_file_path = self.workdir + "\\version.txt"
        linelist = fileinput.input(daemon_ver_file_path)

        self.daemon_ver_st.SetLabelText(linelist[0])
        fileinput.close()

        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(self.daemon_ver_st, 0, wx.ALL, 2)
        border.Add(apInfoDisplay, 0, wx.ALL, 2)
        # crtDisplay = fileDisplayPanel(self, "RT","C:\M2C\EslWebSystem\workdir\log\crit.log",800,400)
        filelist = os.listdir(workdir)
        button_border = wx.BoxSizer(wx.HORIZONTAL)

        self.maxRows = 4
        for dirname in filelist:
            if dirname.rfind("lmrt") != -1 and dirname[18:] == "info.csv":
                temp = getLinesFromFile(self.workdir + "\\" + dirname)
                if temp > self.maxRows:
                    self.maxRows = temp
                rtname = dirname[5:17]
                self.rtnames.append(rtname)
                tempbuton = wx.Button(self, self.rtnum, rtname)
                self.oc = tempbuton.GetBackgroundColour()
                self.rtbuttons.append(tempbuton)
                self.Bind(wx.EVT_BUTTON, self.OnApButtonPressed, tempbuton)
                button_border.Add(self.rtbuttons[self.rtnum], 0, wx.ALL, 2)
                self.rtnum += 1
                print("dir:%s" % dirname)
                # print(dirname)

        border.Add(button_border, 0, wx.ALL, 2)
        if self.rtnum >= 1:
            tempbuton = self.rtbuttons[0]
            tempbuton.SetBackgroundColour(wx.YELLOW)
            dirname = "lmrt_" + self.rtnames[0] + "_info.csv"
            self.crtDisplay = csvDisplayPanel(self, "RTs @ AP:\r\n" + self.rtnames[0], self.workdir + "\\" + dirname, self.maxRows)
            border.Add(self.crtDisplay, 0, wx.ALL, 2)

        self.SetSizer(border)
        self.SetAutoLayout(True)

    def OnApButtonPressed(self, evt):
        for btn in self.rtbuttons:
            btn.SetBackgroundColour(self.oc)
        tempbuton = self.rtbuttons[evt.GetId()]
        tempbuton.SetBackgroundColour(wx.YELLOW)
        dirname =self.workdir + "\\" + "lmrt_" + self.rtnames[evt.GetId()] + "_info.csv"
        tempname ="RTs @ AP:\r\n" + self.rtnames[evt.GetId()]
        self.crtDisplay.changeFile(tempname,dirname)
        wx.CallAfter(self.Layout)

    
class dispPlaneOLD(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        
        # bgcolor = wx.SystemSettings.GetColour(getattr(wx, 'SYS_COLOUR_HIGHLIGHT'))
        cb=wx.ColourDatabase()
        self.tcolor = cb.Find("LIGHT BLUE")
        self.wcolor = cb.Find("BLACK")
        self.font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.SetBackgroundColour(self.tcolor)
        buttonReload = wx.Button(self, -1, "Reload")
        self.Bind(wx.EVT_BUTTON, self.OnReloadPressed, buttonReload)
        buttonOther = wx.Button(self, -1, "Other")
        buttonTest = wx.Button(self, -1, "Test")
        bsizer1row = wx.BoxSizer(wx.HORIZONTAL )
        bsizer1row.Add(buttonReload, 0, wx.GROW|wx.ALL, 2)
        bsizer1row.Add(buttonOther, 0, wx.GROW|wx.ALL, 2)
        bsizer1row.Add(buttonTest, 0, wx.GROW|wx.ALL, 2)

        
        f = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        l1 = wx.StaticText(self, -1, "DPR Log")
        # l1.setDefaultStyle(wx.TextAttr(self.tcolor, self.wcolor,self.font))
        t1 = wx.TextCtrl(self, -1,                        
                        "Here is for DPR LOG",
                       size=(800, 300), style=wx.TE_MULTILINE|wx.TE_RICH2)

        self.t1 = t1               
        self.t1.SetBackgroundColour(self.wcolor)                

        space = 3

        sizer = wx.FlexGridSizer(cols=3, hgap=space, vgap=space)
        sizer.AddMany([ (0,0), bsizer1row, (0,0),
                        l1, t1, (0,0),
                        ])
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(sizer, 0, wx.ALL, 25)
        
        testp = fileDisplayPanel(self, "test","C:\M2C\EslWebSystem\workdir\log\dprlog.log")
        border.Add(testp, 0, wx.ALL, 25)
        
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


    def OnReloadPressed(self, evt):        
        
        f = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        cb=wx.ColourDatabase()
        fcolor = cb.Find("YELLOW")
        bcolor = cb.Find("BLACK")
        self.t1.SetDefaultStyle(wx.TextAttr(fcolor, bcolor))


        self.t1.LoadFile("C:\M2C\EslWebSystem\workdir\log\dprlog.log")
        #self.t1.SetEditable(False)
        ln  = self.t1.GetNumberOfLines()
        print ('lines:%d' % self.t1.GetNumberOfLines())        
        pos  = self.t1.XYToPosition(ln,0)
        print ('pos:%d' % pos)        
        
        self.t1.SetStyle(0, self.t1.GetLastPosition(), wx.TextAttr(fcolor, bcolor, f))
        self.t1.ShowPosition(self.t1.GetLastPosition()-600);
        #self.t1.ShowPosition(0);
        #self.t1.ShowPosition(self.t1.GetLastPosition());

        #evt.Skip()
        
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

        
        
