import os
import wx
from ui.user_interface import AppBaseFrame
from faster_whisper import WhisperModel
import logging
import torch

# global settings
out_dir = "./文字起こし"
model_dir = "./models"


def init_logger(out_dir, logger_name, log_file_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_format = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_format)

    file_handler = logging.FileHandler(
        filename=os.path.join(out_dir, log_file_name))
    file_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


logger = init_logger(out_dir, 'transcrip_chan_logger', 'transcrip_chan.log')


def get_device_settings() -> tuple[str, str]:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = "float16" if torch.cuda.is_available() else "int8"
    return device, torch_dtype


def format_segment(segment):
    start = segment.start
    start_hour, start_min, start_sec, start_msec = map(
        int, (start / 3600, (start % 3600) / 60, start % 60, (start % 1) * 1000))
    end = segment.end
    end_hour, end_min, end_sec, end_msec = map(
        int, (end / 3600, (end % 3600) / 60, end % 60, (end % 1) * 1000))
    text = segment.text
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
            logger.exception(e)
            return

        try:
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
        except Exception as e:
            wx.MessageBox(
                f"出力先フォルダの作成に失敗しました。\r\n{e}", "エラー", wx.OK | wx.ICON_ERROR)
            logger.exception(e)
            return

        try:
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            model_name = self.get_selected_model()

            logger.info(
                f"\nAI モデルの読み込み中... model_name: {model_name}\n※初回のみダウンロードに時間がかかります。")
            self.update_drop_text(
                f"AI モデルの読み込み中...\r\n※初回のみダウンロードに時間がかかります。")

            device, torch_dtype = get_device_settings()

            model = WhisperModel(
                model_name, device=device, compute_type=torch_dtype, download_root=model_dir)

            logger.info(
                f"AI モデルの読み込み完了: {model_name}, device: {device}, dtype: {torch_dtype}")
        except Exception as e:
            wx.MessageBox(
                f"AI モデルの読み込みに失敗しました。\r\n{e}", "エラー", wx.OK | wx.ICON_ERROR)
            logger.exception(e)
            return

        error_count = 0
        for idx, selected_file in enumerate(selected_files):
            logger.info(
                f"'{selected_file}' の文字起こしを開始します。 ({idx+1}/{len(selected_files)})")

            try:
                filename = os.path.basename(selected_file)
                filename_wo_ext = os.path.splitext(filename)[0]

                self.update_drop_text(
                    f"{filename} を文字起こし中...({len(selected_files)} 個中 {idx+1} 個目)\r\n時間がかかりますのでしばらくお待ち下さい。 \r\n（「応答なし⌛」になっても処理は進んでいるので気長にどうぞ）")

                logger.info(
                    f"model: {model_name}\nselected_file: {selected_file}\nstart transcribe...")
                segments, info = model.transcribe(selected_file, beam_size=5)

                logger.info("Detected language '%s' with probability %f" %
                            (info.language, info.language_probability))

                transcribe_text = "\n".join(format_segment(segment)
                                            for segment in segments)

                out_file_path = os.path.join(
                    out_dir, f"文字起こし_{filename_wo_ext}.txt")

                with open(out_file_path, "w", encoding="utf-8") as f:
                    f.write(transcribe_text)
                logger.info(f"Transcription saved to {out_file_path}")
            except Exception as e:
                out_file_path = os.path.join(
                    out_dir, f"文字起こし_{filename_wo_ext}.txt")
                with open(out_file_path, "w", encoding="utf-8") as f:
                    f.write(f"文字起こし中にエラーが発生しました。\n\nエラー詳細:\n{e}")
                logger.exception(e)
                error_count += 1

        self.selected_files = []

        self.update_drop_text(
            f"ここにファイルをドロップ")

        if error_count == 0:
            wx.MessageBox(
                f"文字起こしが完了しました。\r\n結果は [{out_dir}] に保存されました。", "文字起こし完了", wx.OK | wx.ICON_INFORMATION)
        elif error_count == len(selected_files):
            wx.MessageBox(
                f"文字起こしに失敗しました。\r\nエラー詳細は [{out_dir}] の各ファイルをご確認ください。", "文字起こし失敗", wx.OK | wx.ICON_ERROR)
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
        if model_lebel == "極小":
            return "base"
        elif model_lebel == "小":
            return "small"
        elif model_lebel == "中":
            return "medium"
        elif model_lebel == "大":
            return "large-v3"
        else:
            return "small"

    def update_drop_text(self, text):
        self.dropText.SetLabel(text)


if __name__ == '__main__':
    app = wx.App(False)
    frame = AppFrame(None)
    frame.Show(True)
    app.MainLoop()
