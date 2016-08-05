#-*- coding:utf-8 -*-

import wx

"""
#每一个wxPython的程序必须有一个wx.App对象
app = wx.App()


#实例化一个frame
# None:当前窗口的父窗口parent，如果当前窗口是最顶层的话，则parent=None, 如果不是顶层窗口，则它的值为所属frame的名字
# -1：id值， -1的话程序会自动生成一个id
# pos：位置
# size： 宽， 高

frame = wx.Frame(None, -1, title='wx_00_base.py', pos=(300, 400), size=(200, 150))

#居中处理
frame.Centre()

#显示frame
frame.show()

#进入循环，等待窗口响应
app.MainLoop(i)
"""

class Example(wx.Frame):


    def __init__(self, title):
        super(Example, self).__init__(None, title=title, size=(250, 150))


        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()



    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)



if __name__ == '__main__':
    app = wx.App()
    Example('Line')
    app.MainLoop()
