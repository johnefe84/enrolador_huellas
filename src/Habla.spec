# -*- mode: python -*-
a = Analysis(['Habla.py'],
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
          name='Habla.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='icono.ico')
