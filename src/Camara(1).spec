# -*- mode: python -*-
a = Analysis(['Camara.py'],
             pathex=['E:\\ideauto\\workspace\\Enrolador\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Camara.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='icono.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='Camara')
