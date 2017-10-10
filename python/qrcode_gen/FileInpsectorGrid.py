#!/usr/bin/env python

import os
import qr_file_inspector
import wx
import wx.grid as gridlib
#import threading
import random

FI_DATE_COL = 0
FI_TIME_COL = 1
FI_TYPE_COL = 2
FI_CASE_COL = 3
FI_STATE_COL = 4
FI_BUTTON_COL = 5
FI_TOTAL_COL = 6



class FileInspectorTable(gridlib.PyGridTableBase):
    def __init__(self, path=None):
        gridlib.PyGridTableBase.__init__(self)
        if path is None:
            self.path = os.getcwd()
        self.path = path
        ## TBD: Create thread here to update data to table!?
        self.labels =['Date','Time','ED Type','Case #',"State", "Button"]
        self.labelTypes = [gridlib.GRID_VALUE_STRING,
                           gridlib.GRID_VALUE_STRING,
                           gridlib.GRID_VALUE_STRING,
                           gridlib.GRID_VALUE_STRING,
                           gridlib.GRID_VALUE_STRING,
                           gridlib.GRID_VALUE_STRING]
        self.filelist={}


    def GetNumberRows(self):
        # TBD: Number of rows get by the thread
        return len(self.filelist)

    def GetNumberCols(self):
        return FI_TOTAL_COL

    def IsEmptyCell(self, row, col):
        if col == FI_BUTTON_COL:
            return True
        if row > len(self.filelist):
            return True
        return False

    def GetValue(self, row, col):
        try:
            keylist = self.filelist.keys()
            keylist.sort()
            if col is FI_DATE_COL:
                return keylist[row].split("_")[0]
            elif col is FI_TIME_COL:
                return keylist[row].split("_")[1]
            elif col is FI_TYPE_COL:
                return  keylist[row].split("_")[2] +" "+ keylist[row].split("_")[3] +" " + keylist[row].split("_")[4]
            elif col is FI_CASE_COL:
                return keylist[row].split("_")[5]
            elif col is FI_STATE_COL:
                return self.filelist[keylist[row]]
            else:
                return "NULL"
        except IndexError,KeyError:
            if (col == 0):
                return "Add"
            else:
                return "Invalid"

    def TriggerViewUpdate(self):
        self.msg = gridlib.GridTableMessage(self,            # The table
                gridlib.GRIDTABLE_REQUEST_VIEW_GET_VALUES, # what we did to it
                0,0
                )
        self.GetView().ProcessTableMessage(self.msg)
        self.GetView().Scroll(2, self.GetView().GetNumberRows())

        #self.GetView().Scroll(2,5)


    def UpdateFile(self, filename, status):
        if filename in filelist.keys():
            if filelist[filename] != status:
                filelist[filename] = status
                self.TriggerViewUpdate()
        else:
            filelist[filename] = status
            self.TriggerViewUpdate()

    def UpdateFileInfo(self, fileInfo):
        if len(fileInfo) > len(self.filelist):
            print "Add Row!"
            self.msg = gridlib.GridTableMessage(self,            # The table
                    gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
                    len(fileInfo) - len(self.filelist))
            self.GetView().ProcessTableMessage(self.msg)

        if len(fileInfo) < len(self.filelist):
            print "Delete Line!"
            self.msg = gridlib.GridTableMessage(self,            # The table
                    gridlib.GRIDTABLE_NOTIFY_ROWS_DELETED, # what we did to it
                     0,len(self.filelist)-len(fileInfo))
            self.GetView().ProcessTableMessage(self.msg)
            print "Delete Done!"
        self.filelist = fileInfo
        self.TriggerViewUpdate()
    def AddRow(self):
        self.msg = gridlib.GridTableMessage(self,            # The table
                gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
                1                                       # how many
                )

        self.GetView().ProcessTableMessage(self.msg)

    def SetValue(self, row, col, value):
        return True

    #--------------------------------------------------
    # Some optional methods
    # Called when the grid needs to display labels
    def GetColLabelValue(self, col):
        return self.labels[col]

    # Called to determine the kind of editor/renderer to use by
    # default, doesn't necessarily have to be the same type used
    # natively by the editor/renderer if they know how to convert.
    def GetTypeName(self, row, col):
        return  gridlib.GRID_VALUE_STRING


    # Called to determine how the data can be fetched and stored by the
    # editor and renderer.  This allows you to enforce some type-safety
    # in the grid.
    def CanGetValueAs(self, row, col, typeName):
        return  gridlib.GRID_VALUE_STRING


    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)

class FileInspectorGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)

        self.table = FileInspectorTable()

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(self.table, True)

        #self.SetRowLabelSize(50)
        self.SetMargins(2,2)
        #self.SetAutoLayoutAutoSize(True)
        self.SetColSize(2,200)
        #gridlib.EVT_GRID_CELL_LEFT_DCLICK(self, self.OnFiGridLeftDClick)


    # I do this because I don't like the default behaviour of not starting the
    # cell editor on double clicks, but only a second click.
    def OnFiGridLeftDClick(self, evt):
        if self.CanEnableCellControl():
            self.EnableCellEditControl()
        self.table.AddRow()


class FileInspectorFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'File Inspector', size = (720,600), style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        self.CenterOnScreen()
        self.CreateStatusBar()
        self.SetStatusText("OK")
        self.EditorPanel = wx.Panel(self, -1, style = 0)
        self.fileInsGrid = FileInspectorGrid(self.EditorPanel)

        self.bs = wx.BoxSizer(wx.VERTICAL)

        self.bs.Add(self.fileInsGrid, 1 , wx.GROW|wx.ALL, 5)
        #self.bs.Add(b)
        self.EditorPanel.SetSizer(self.bs)
#self.bs.Fit(self.stockInfoGrid)


    def OnCloseWindow(self,event):
        print("Close Windows")
        self.fileInsGrid.done()
    def OnButton(self, evt):
         print "Save All into file"
#        self.SetFocus()


class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        self.frame = FileInspectorFrame(None, 1)
        self.frame.Show(True)
        self.ithr = qr_file_inspector.theQrGenThread(gridtable = self.frame.fileInsGrid.table)
        self.ithr.start()
        return True

    def OnExit(self):
        self.ithr.running = 0
        self.ithr.join(3.0)

if __name__ == "__main__":
    #print "Starting test"
    app = App()
    app.MainLoop()