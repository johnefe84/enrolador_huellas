# -*- mode: python -*-
a = Analysis(['RFIDEAS_escucha.py'],
             pathex=['E:\\ideauto\\workspace\\Enrolador\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RFIDEAS_escucha.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='icono.ico')
