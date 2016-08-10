# -*- coding:utf-8 -*-

import wx

from math import *

class CalcFrame(wx.Frame):
    def __init__(self, title):
        super(CalcFrame, self).__init__(None, title=title, size=(300, 250))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.textprint, flag=ex.EXPAND|wx.TOP|wx.BOTTOM, border=4)

        gridBox = wx.GridSizer(5, 4, 5, 5)
        labels==['AC', 'DEL', 'pi', 'CLOSE', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        for label in labels:
            gridBox.Add(wx.Button(self, label=label), 1, wx.EXPAND)

        vbox.Add(gridBox, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
if __name__ == '__main__':

    app = wx.App()
    CalcFrame(title='Calculator')
    app.MainLoop()