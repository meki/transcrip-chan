# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class AppBaseFrame
###########################################################################


class AppBaseFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"transcrip-chan", pos=wx.DefaultPosition, size=wx.Size(600, 400),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL, name=u"Transcrip-chan")

        self.SetSizeHints(wx.Size(600, 400), wx.Size(600, 400))
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT,
                     wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BIZ UDPゴシック"))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.titleText = wx.StaticText(self, wx.ID_ANY, u"文字起こしちゃん", wx.DefaultPosition, wx.Size(
            600, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.titleText.Wrap(-1)

        self.titleText.SetFont(wx.Font(
            28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BIZ UDPゴシック"))

        bSizer.Add(self.titleText, 0, wx.ALL, 5)

        radioBoxModelsChoices = [u"極小", u"小", u"中", u"大"]
        self.radioBoxModels = wx.RadioBox(self, wx.ID_ANY, u"モデル選択（右ほど遅くて正確）", wx.Point(
            -1, -1), wx.DefaultSize, radioBoxModelsChoices, 4, wx.RA_SPECIFY_COLS)
        self.radioBoxModels.SetSelection(0)
        self.radioBoxModels.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BIZ UDPゴシック"))
        self.radioBoxModels.SetToolTip(
            u"大きなモデルほどメモリ、ディスク容量が必要です。エラーが発生した場合は小さなモデルを選択してみてください。")

        bSizer.Add(self.radioBoxModels, 0, wx.ALIGN_CENTER, 5)

        gSizer1 = wx.GridSizer(0, 1, 0, 0)

        self.parentPanel = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        self.parentPanel.DragAcceptFiles(True)

        gSizer2 = wx.GridSizer(1, 1, 0, 0)

        self.dropText = wx.StaticText(self.parentPanel, wx.ID_ANY, u"ここにファイルをドロップ",
                                      wx.DefaultPosition, wx.Size(550, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.dropText.Wrap(-1)

        self.dropText.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT,
                              wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BIZ UDPゴシック"))
        self.dropText.SetMinSize(wx.Size(550, 60))
        self.dropText.SetMaxSize(wx.Size(550, 300))

        gSizer2.Add(self.dropText, 0, wx.ALIGN_CENTER |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.parentPanel.SetSizer(gSizer2)
        self.parentPanel.Layout()
        gSizer2.Fit(self.parentPanel)
        gSizer1.Add(self.parentPanel, 1, wx.EXPAND | wx.ALL, 5)

        bSizer.Add(gSizer1, 4, wx.EXPAND, 5)

        self.staticline = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer.Add(self.staticline, 0, wx.EXPAND | wx.ALL, 5)

        gSizer3 = wx.GridSizer(0, 3, 0, 0)

        gSizer3.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonStart = wx.Button(
            self, wx.ID_ANY, u"文字起こし開始", wx.DefaultPosition, wx.Size(200, 50), 0)
        self.buttonStart.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BIZ UDPゴシック"))

        gSizer3.Add(self.buttonStart, 0, wx.ALL, 5)

        bSizer.Add(gSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.parentPanel.Bind(wx.EVT_DROP_FILES, self.on_drop_files)
        self.buttonStart.Bind(wx.EVT_BUTTON, self.on_button_start)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_drop_files(self, event):
        event.Skip()

    def on_button_start(self, event):
        event.Skip()
