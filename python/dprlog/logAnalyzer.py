"""
This Module is intend for DVH log analysis
"""


import wx
import subprocess
import sys,os
import fileinput
from datetime import date


class logAnalyzerPanel(wx.Panel):
    def __init__(self, parent, workdir):
        wx.Panel.__init__(self, parent, -1)

        self.workdir = workdir
        self.st = wx.StaticText(self, -1, "workdir: " + workdir)
        self.btnregen = wx.Button(self, -1, "Re-generate DVH")
        self.Bind(wx.EVT_BUTTON, self.OnGenDVH, self.btnregen)
        delta_list=[]
        for val in range(-23,24,1):
            if val <= 0:
                delta_list.append(str(val))
            else:
                delta_list.append("+" + str(val))

        self.delta_combo = wx.ComboBox(self, -1, "Time delta", (30, 50),
                                        (50, -1), delta_list,
                                        wx.CB_DROPDOWN)
                                        # | wx.TE_PROCESS_ENTER
                                        # | wx.CB_SORT)
        self.delta_combo.SetSelection(23)
        #self.Bind(wx.EVT_COMBOBOX, self.deltaSelection, self.delta_combo)

        self.space = 2
        space = self.space
        self.column1 = wx.BoxSizer(wx.HORIZONTAL)
        self.column1.AddSpacer(20)
        self.column1.Add(self.st, 0, wx.ALL, space)
        self.column1.AddSpacer(20)
        self.column1.Add(self.btnregen, 0, wx.ALL, space)
        self.column1.AddSpacer(20)
        self.column1.Add(self.delta_combo, 0, wx.ALL, space)


        # Create List for filenames
        filelist = os.listdir(workdir + "\\dvh")
        self.listmacs = []
        for filename in filelist:
            if filename.rfind("dvhc") != -1:
                self.listmacs.append(filename)

        # 2nd Row - Combox
        self.mac_combobox = wx.ComboBox(self, -1, "select MAC", (90, 50),
                                        (200, -1), self.listmacs,
                                        wx.CB_DROPDOWN
                                        # | wx.TE_PROCESS_ENTER
                                        | wx.CB_SORT)

        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.mac_combobox)

        self.l1 = wx.StaticText(self, -1, "Filter: ")
        self.t1 = wx.TextCtrl(self, -1, "", size=(80, -1),style=wx.TE_PROCESS_ENTER)

        # clear/Append
        # self.mac_combobox.

        self.Row2 = wx.BoxSizer(wx.HORIZONTAL)
        self.Row2.AddSpacer(20)
        self.Row2.Add(self.mac_combobox, 0, wx.ALL, space)
        self.Row2.AddSpacer(20)
        self.Row2.Add(self.l1, 0, wx.ALL, space)
        self.Row2.Add(self.t1, 0, wx.ALL, space)
        self.Bind(wx.EVT_TEXT_ENTER, self.EvtTextEnter, self.t1)


        # row 3 : filter settings
        #self.
        self.dvhshow = wx.TextCtrl(self, -1,
                        "",
                       size=(500, 800), style=wx.TE_MULTILINE|wx.TE_RICH2)
        self.f = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.dvhshow.SetFont(self.f)
        self.dvhshow.SetBackgroundColour(wx.LIGHT_GREY)

        # Radio Box
        analysisList = ['LR', 'Battery']



        self.rb = wx.RadioBox(
                self, -1, "Select Analysis", wx.DefaultPosition, wx.DefaultSize,
                analysisList, 1, wx.RA_SPECIFY_COLS
                )

        self.Bind(wx.EVT_RADIOBOX, self.updateAnalysis, self.rb)

        self.top_anylysis = wx.TextCtrl(self, -1,
                        "",
                       size=(400, 300), style=wx.TE_MULTILINE|wx.TE_RICH2)

        self.bottom_anylysis = wx.TextCtrl(self, -1,
                        "",
                       size=(400, 300), style=wx.TE_MULTILINE|wx.TE_RICH2)


        self.Row3 = wx.BoxSizer(wx.HORIZONTAL)
        self.Row3.AddSpacer(20)
        self.Row3.Add(self.dvhshow, 0, wx.ALL, space)

        ana_sizer = wx.BoxSizer(wx.VERTICAL)

        ana_sizer.Add(self.top_anylysis, 0, wx.ALL, space)
        ana_sizer.AddSpacer(20)
        ana_sizer.Add(self.bottom_anylysis, 0, wx.ALL, space)

        self.Row3.Add(self.rb, 0, wx.ALL, space)
        self.Row3.Add(ana_sizer, 0, wx.ALL, space)
        # row 4 : Text display

        self.vrtSizer = wx.BoxSizer(wx.VERTICAL)
        self.vrtSizer.AddMany([(10,20),
                              self.column1,
                              (10,20),
                               self.Row2,
                               self.Row3])
        #    Add(, 0, wx.ALL, space)
        #self.vrtSizer.Add(self.Row2, 0, wx.ALL, space)

        self.SetSizer(self.vrtSizer)
        self.SetAutoLayout(True)

    def winpath_to_cygpath(self, winpath):
        cygpath = '/cygdrive/'
        lowerpath = winpath.lower()
        for ch in range(len(lowerpath)):
            if lowerpath[ch] == '\\':
                cygpath += '/'
            elif lowerpath[ch] == ':':
                pass
            else:
                cygpath += lowerpath[ch]
        print(cygpath)
        return cygpath

    def OnGenDVH(self, evt):
        dvhpath = self.winpath_to_cygpath(self.workdir + "/dvh")
        delta = self.delta_combo.GetStringSelection()
        #os.execl("dvh_conv", "dvh_conv", dvhpath)
        self.btnregen.Disable()
        self.btnregen.SetLabelText("In Progress")
        delta = self.delta_combo.GetStringSelection()
        print(delta)
        print(subprocess.check_output(["./dvh_conv", dvhpath, delta]))
        self.btnregen.Enable()
        self.btnregen.SetLabelText("Re-generate DVH")
        self.updateCb()
        pass

    def EvtComboBox(self, evt):
        print('EvtComboBox: %s' % (evt.GetString()))
        self.dvhshow.LoadFile(self.workdir + "\\dvh\\" + evt.GetString())
        self.updateAnalysis(None)
        pass

    def updateCb(self):
        filelist = os.listdir(self.workdir + "\\dvh")
        self.listmacs = []
        for filename in filelist:
            if filename.rfind("dvhc") != -1:
                self.listmacs.append(filename)
        self.mac_combobox.Clear()
        for item in self.listmacs:
            temp = self.t1.GetLineText(0)
            if item.rfind(temp) != -1:
                self.mac_combobox.Append(item)

    def lr_stats(self):
        lr_count = 0
        try:
            for dvhline in fileinput.input(self.workdir + "\\dvh\\" + self.mac_combobox.GetStringSelection()):
                # self.daemon_ver_st.SetLabelText(linelist[0])
                if (dvhline.find("LR")) != -1 :
                    self.top_anylysis.WriteText(dvhline)
            fileinput.close()
        except IOError:
                print ("No file")

    def battery_stats(self):
        try:
            for dvhline in fileinput.input(self.workdir + "\\dvh\\" + self.mac_combobox.GetStringSelection()):
                # self.daemon_ver_st.SetLabelText(linelist[0])
                if (dvhline.find("NVR")) != -1 :
                    self.top_anylysis.WriteText(dvhline)
            fileinput.close()
        except IOError:
                print ("No file")

    def summary_stats(self):
        num_total = 0
        num_suc = 0
        try:
            for dvhline in fileinput.input(self.workdir + "\\dvh\\" + self.mac_combobox.GetStringSelection()):
                # self.daemon_ver_st.SetLabelText(linelist[0])
                if (dvhline.find("DATA PUSH")) != -1:
                    num_total += 1
                if (dvhline.find("DATA PUSH Success")) != -1:
                    num_suc += 1
            fileinput.close()
        except IOError:
                print ("No file")
                return None

        self.bottom_anylysis.SetInsertionPoint(0)
        if num_total > 0:
            self.bottom_anylysis.WriteText("SUCCESS Rate = {0:.2f} %, ({1}/{2}) \r\n".format(float(num_suc*100)/float(num_total),num_suc, num_total))
        else:
            self.bottom_anylysis.WriteText("SUCCESS Rate = {0:.2f} %, ({1}/{2}) \r\n".format(0, num_suc, num_total))

    def updateAnalysis(self, event):
        # print("Event :%d" % event.GetInt())
        if self.rb.GetSelection() == 0:
            self.top_anylysis.Clear()
            self.lr_stats()
        elif self.rb.GetSelection() == 1:
            self.top_anylysis.Clear()
            self.battery_stats()

        self.summary_stats()

    def EvtTextEnter(self, event):
        # self.updateCb()
        self.mac_combobox.Clear()
        temp = self.t1.GetLineText(0)
        dlg = wx.ProgressDialog("Filtering in progress",
                               "In progress",
                               40,
                               parent=self,
                               style = 0
                                | wx.PD_APP_MODAL
                                #| wx.PD_CAN_ABORT
                                #| wx.PD_CAN_SKIP
                                | wx.PD_ELAPSED_TIME
                                #| wx.PD_ESTIMATED_TIME
                                | wx.PD_REMAINING_TIME
                                #| wx.PD_AUTO_HIDE
                                )
        ttn = len(self.listmacs)
        xunit = len(self.listmacs)/40
        xpre = 0
        ci = 0
        dlg.Update(0, "In progress")
        for item in self.listmacs:
            ci += 1
            if (ci / xunit) > xpre:
                xpre = ci / xunit
                if xpre < 40:
                    dlg.Update(xpre)

            if item.rfind(temp) != -1:
                self.mac_combobox.Append(item)

        dlg.Update(40)
        dlg.Destroy()
        event.Skip()