import wx
from ui.user_interface import AppBaseFrame


class AppFrame(AppBaseFrame):
    def __init__(self, parent):
        AppBaseFrame.__init__(self, parent)

    def on_button_start(self, event):
        print("on_button_start")

    def on_drop_files(self, event):
        files = event.GetFiles()
        file_count = event.GetNumberOfFiles()
        print(f"file_count: {file_count}:")
        for file in files:
            print(f"  file: {file}")


if __name__ == '__main__':
    app = wx.App(False)
    frame = AppFrame(None)
    frame.Show(True)
    app.MainLoop()
