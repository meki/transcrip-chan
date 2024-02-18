# Transcrip-chan

「文字起こしちゃん」は、 OpenAI-Whisper を使った文字起こし GUI アプリケーションです。
スタンドアロンの実行ファイルから起動でき、音声ファイルをドラッグアンドドロップするだけで文字起こしを行うことができます。
現在は Windows OS のみに対応しています。

## For developers

使用しているフレームワーク:

- UI: wxPython
- UI デザイン: wxFormBuilder

### Debugging

```bash
poetry run python ./transcrip_chan/main.py
```

### Create executable

```bash
poetry run pyinstaller main.spec --noconfirm
```
