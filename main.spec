# -*- mode: python ; coding: utf-8 -*-

import os

venv_path = os.environ['VIRTUAL_ENV']

a = Analysis(
    ['transcrip_chan\\main.py'],
    pathex=['.\\transcrip_chan'],
    binaries=[],
    datas=[
        (os.path.join(venv_path, 'Scripts', 'whisper.exe'), '.'),
        (os.path.join(venv_path, 'Lib', 'site-packages', 'whisper'), '.\\whisper'),
    ],
    hiddenimports=['whisper', 'tqdm'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='transcrip_chan',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
