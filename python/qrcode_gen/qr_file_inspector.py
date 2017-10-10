import wxversion

wxversion.select("3.0")
import wx
import wx.aui

import os, time
import wx.grid as gridlib
import threading
import pyqrcode

''' Seems no choice except using inherit the threading.thread class to creat our own thread'''


class theQrGenThread(threading.Thread):
    def __init__(self, currentPath=None, gridtable=None):
        threading.Thread.__init__(self)
        self.running = 1
        # store the file prefix name and status mapping, ex "20161023_112233_EDxxx_Case 3" : ""
        self.fileinfos = {}
        if currentPath is None:
            self.currentPath = os.getcwd()
        else:
            self.currentPath = currentPath

        self.gridtable = gridtable

    def reNewFileInfo(self):
        InfoUpdated = False
        newFileInfo = {}
        filelist = os.listdir(self.currentPath)
        for filename in filelist:
            if filename.rfind("csv") != -1:
                newFileInfo[filename[:-4]]= "OK"
                pngname = filename[:-4] + ".png"
                if not os.access(pngname, os.F_OK):
                   newFileInfo[filename[:-4]]= "Wait"
        for keyx in newFileInfo.keys():
            if not keyx in self.fileinfos.keys():
                InfoUpdated = True
                break
            if self.fileinfos[keyx] != newFileInfo[keyx]:
                InfoUpdated = True
        if len(self.fileinfos) != len(newFileInfo):
            InfoUpdated = True
        self.fileinfos = newFileInfo
        if InfoUpdated is True:
            print "Update File info"
        return InfoUpdated

    def run(self):
        # print("123");
        while (self.running):
            time.sleep(0.5)
            self.QrInpsectionCheck()
            if self.reNewFileInfo() is False:
                continue
            if self.gridtable != None:
                try:
                    self.gridtable.UpdateFileInfo(self.fileinfos)
                except:
                    #print "Failed"
                    self.gridtable=None
        print "Thread Stopped"

    def QrMacCheckToPng(self, filename):
        with open(filename, "r") as f:
            _data_from_file = f.readlines()
            f.close()
        ostr = ""
        macCnt = 0
        otype = ""
        for iline in _data_from_file:
            # print "line="+iline
            spass = iline.strip().replace(" ", "").split(",")[3]
            if spass == "PASS":
                if macCnt == 0:
                    otype = iline.split(",")[1].replace(" ", "")[:6]
                macCnt += 1
                ostr += iline.strip().replace(" ", "").split(",")[1][-6:]
        ##print "Outout=" + ostr
        finalstr = "qrc:{},type:{},list:{}".format(macCnt, otype, ostr)
        # print len(finalstr)
        # print finalstr
        big_code = pyqrcode.create(finalstr.strip(), error='L', version=18, mode='binary')
        pngN = filename.replace(".csv", ".png")
        big_code.png(pngN, scale=4, module_color=[0, 0, 0, 128])
        print("Done.")

    # only process on file once (keep it not busy)
    def QrInpsectionCheck(self):
        filelist = os.listdir(self.currentPath)

        for filename in filelist:
            if filename.rfind("csv") != -1:
                # print filename
                pngname = filename[:-4] + ".png"
                if not os.access(pngname, os.F_OK):
                    print "Generate QRCode for " + filename
                    self.QrMacCheckToPng(filename)


class macCheckQrCodePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.numColumn = 5
        self.numRows = 5
        self.gridcsv = gridlib.Grid(self, -1)
        self.gridcsv.CreateGrid(self.numRows, self.numColumn)  # , gridlib.Grid.SelectRows)
		##self.gridcsv.Set

		##self.gridcsv.Setc
        space = 2
        self.column1 = wx.BoxSizer(wx.VERTICAL)
        self.column1.Add(self.gridcsv, 0, wx.ALL, space)
        self.SetSizer(self.column1)
        self.SetAutoLayout(True)

class qrInspectionSelfTestApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        self.ithr = theQrGenThread()
        self.ithr.start()

        self.pf = wx.Frame(None, -1, "Custom Table, data driven Grid  Demo", size=(640, 480))
        self.mcpanel = macCheckQrCodePanel(self.pf)
        self.pf.Show()
        return True

    def OnExit(self):
        self.ithr.running = 0
        self.ithr.join(3.0)


'''self test is a basic, testing with no gui version'''
'''
if __name__ == "__main__":
	print "Startting QRCode Generator"
	ithr = theQrGenThread()
	ithr.start()	

	try:
		testinput = raw_input()
	except ValueError:
		print "exit by interrupt"
	finally:
		print "Stops"
		ithr.running = 0
		ithr.join(3.0)	
	
	# print "End"
'''

if __name__ == "__main__":
	print "Startting QRCode Generator"
	#ithr = theQrGenThread()
	#ithr.start()
	app = qrInspectionSelfTestApp()
	app.MainLoop()
