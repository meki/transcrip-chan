# Transcrip-chan

「文字起こしちゃん」は、 OpenAI-Whisper を使った文字起こし GUI アプリケーションです。
スタンドアロンの実行ファイルから起動でき、音声ファイルをドラッグアンドドロップするだけで文字起こしを行うことができます。
現在は Windows OS のみに対応しています。

## ダウンロード

- [リリースページ](https://github.com/meki/transcrip-chan/releases) から最新版の zip をダウンロードして解凍。
- 解凍先のフォルダ内にある transcrip_chan_[バージョン番号].exe を起動します。

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
