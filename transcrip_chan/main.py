import os
import wx
from ui.user_interface import AppBaseFrame
import whisper


def format_segment(segment):
    start = segment["start"]
    start_hour, start_min, start_sec, start_msec = map(
        int, (start / 3600, (start % 3600) / 60, start % 60, (start % 1) * 1000))
    end = segment["end"]
    print(f"start: {start} -> end: {end}")
    end_hour, end_min, end_sec, end_msec = map(
        int, (end / 3600, (end % 3600) / 60, end % 60, (end % 1) * 1000))
    text = segment["text"]
    return f"{start_hour:02d}:{start_min:02d}:{start_sec:02d}.{start_msec:03d} --> {end_hour:02d}:{end_min:02d}:{end_sec:02d}.{end_msec:03d}\n{text}\n"


class AppFrame(AppBaseFrame):
    def __init__(self, parent):
        AppBaseFrame.__init__(self, parent)
        self.selected_files = []

    def on_button_start(self, event):
        selected_files = self.selected_files

        if len(selected_files) == 0:
            wx.MessageBox(
                "文字起こしするファイルが選択されていません。ファイルをドロップしてください。", "エラー", wx.OK | wx.ICON_ERROR)
            return

        out_dir = os.path.join(os.path.expanduser(
            "~"), "Desktop", f"文字起こし")

        try:
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
        except Exception as e:
            wx.MessageBox(
                f"出力先フォルダの作成に失敗しました。\r\n{e}", "エラー", wx.OK | wx.ICON_ERROR)
            return

        error_count = 0
        for idx, selected_file in enumerate(selected_files):
            print(
                f"selected_file: {selected_file} ({idx+1}/{len(selected_files)})")

            try:
                if not os.path.exists("./models"):
                    os.makedirs("./models")
                model_name = self.get_selected_model()
                filename = os.path.basename(selected_file)
                filename_wo_ext = os.path.splitext(filename)[0]

                self.update_drop_text(
                    f"{filename} を文字起こし中...({len(selected_files)} 個中 {idx+1} 個目)\r\n時間がかかりますのでしばらくお待ち下さい。 \r\n（「応答なし⌛」になっても処理は進んでいるので気長にどうぞ）")
                model = whisper.load_model(
                    name=model_name, download_root="./models")
                result = whisper.transcribe(model=model, audio=selected_file)

                segments = result["segments"]

                transcribe_text = "\n".join(format_segment(segment)
                                            for segment in segments)
                print(transcribe_text)

                out_file_path = os.path.join(
                    out_dir, f"文字起こし_{filename_wo_ext}.txt")

                with open(out_file_path, "w", encoding="utf-8") as f:
                    f.write(transcribe_text)
                print(f"Transcription saved to {out_file_path}")
            except Exception as e:
                out_file_path = os.path.join(
                    out_dir, f"文字起こし_{filename_wo_ext}.txt")
                with open(out_file_path, "w", encoding="utf-8") as f:
                    f.write(f"文字起こし中にエラーが発生しました。\n\nエラー詳細:\n{e}")
                error_count += 1

        self.selected_files = []

        self.update_drop_text(
            f"ここにファイルをドロップ")

        if error_count == 0:
            wx.MessageBox(
                f"文字起こしが完了しました。\r\n結果は [{out_dir}] に保存されました。", "文字起こし完了", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(
                f"文字起こしが完了しましたが、{error_count} 個のファイルでエラーが発生しました。\r\nエラー詳細は [{out_dir}] の各ファイルをご確認ください。", "文字起こし完了", wx.OK | wx.ICON_WARNING)

    def on_drop_files(self, event):
        files = event.GetFiles()
        file_count = event.GetNumberOfFiles()
        self.update_drop_text(
            f"{file_count}個のファイルがドロップされました。\r\n文字起こし開始ボタンを押してください。")
        self.selected_files = files

    def get_selected_model(self):
        model_lebel = self.radioBoxModels.GetStringSelection()
        if model_lebel == "小":
            return "small"
        elif model_lebel == "中":
            return "medium"
        elif model_lebel == "大":
            return "large-v2"
        else:
            return "small"

    def update_drop_text(self, text):
        self.dropText.SetLabel(text)


if __name__ == '__main__':
    app = wx.App(False)
    frame = AppFrame(None)
    frame.Show(True)
    app.MainLoop()
