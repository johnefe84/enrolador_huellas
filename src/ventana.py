# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created: Tue Feb 03 16:13:26 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1119, 529)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 229, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 231, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icono.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 211, 281))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("logo_small_blanco.PNG")))
        self.label.setObjectName(_fromUtf8("label"))
        self.foto = QtGui.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(270, 70, 261, 201))
        self.foto.setFrameShape(QtGui.QFrame.Box)
        self.foto.setText(_fromUtf8(""))
        self.foto.setObjectName(_fromUtf8("foto"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.identificacion = QtGui.QLineEdit(self.centralwidget)
        self.identificacion.setGeometry(QtCore.QRect(20, 310, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.identificacion.setFont(font)
        self.identificacion.setText(_fromUtf8(""))
        self.identificacion.setObjectName(_fromUtf8("identificacion"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(270, 280, 521, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.huella = QtGui.QPushButton(self.frame)
        self.huella.setGeometry(QtCore.QRect(320, 20, 71, 61))
        self.huella.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("huella.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.huella.setIcon(icon1)
        self.huella.setIconSize(QtCore.QSize(50, 50))
        self.huella.setObjectName(_fromUtf8("huella"))
        self.cedula = QtGui.QPushButton(self.frame)
        self.cedula.setGeometry(QtCore.QRect(110, 20, 71, 61))
        self.cedula.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("cedula.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cedula.setIcon(icon2)
        self.cedula.setIconSize(QtCore.QSize(62, 62))
        self.cedula.setObjectName(_fromUtf8("cedula"))
        self.tarjeta = QtGui.QPushButton(self.frame)
        self.tarjeta.setGeometry(QtCore.QRect(10, 20, 71, 61))
        self.tarjeta.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("nfc.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tarjeta.setIcon(icon3)
        self.tarjeta.setIconSize(QtCore.QSize(50, 50))
        self.tarjeta.setObjectName(_fromUtf8("tarjeta"))
        self.tomarfoto = QtGui.QPushButton(self.frame)
        self.tomarfoto.setGeometry(QtCore.QRect(220, 20, 71, 61))
        self.tomarfoto.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("camara.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tomarfoto.setIcon(icon4)
        self.tomarfoto.setIconSize(QtCore.QSize(40, 40))
        self.tomarfoto.setObjectName(_fromUtf8("tomarfoto"))
        self.validar = QtGui.QPushButton(self.centralwidget)
        self.validar.setGeometry(QtCore.QRect(20, 340, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.validar.setFont(font)
        self.validar.setObjectName(_fromUtf8("validar"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 400, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.mensajes = QtGui.QLabel(self.centralwidget)
        self.mensajes.setGeometry(QtCore.QRect(20, 460, 761, 21))
        self.mensajes.setText(_fromUtf8(""))
        self.mensajes.setObjectName(_fromUtf8("mensajes"))
        self.imprimir = QtGui.QPushButton(self.centralwidget)
        self.imprimir.setGeometry(QtCore.QRect(700, 300, 75, 61))
        self.imprimir.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("imprimir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imprimir.setIcon(icon5)
        self.imprimir.setIconSize(QtCore.QSize(50, 50))
        self.imprimir.setObjectName(_fromUtf8("imprimir"))
        self.visita = QtGui.QLabel(self.centralwidget)
        self.visita.setGeometry(QtCore.QRect(840, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.visita.setFont(font)
        self.visita.setObjectName(_fromUtf8("visita"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 340, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(840, 410, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(840, 370, 231, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(900, 410, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 400, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 400, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 399, 771, 51))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.nombre = QtGui.QLineEdit(self.frame_2)
        self.nombre.setGeometry(QtCore.QRect(80, 20, 181, 21))
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.apellido = QtGui.QLineEdit(self.frame_2)
        self.apellido.setGeometry(QtCore.QRect(340, 20, 181, 21))
        self.apellido.setObjectName(_fromUtf8("apellido"))
        self.desdeempresa = QtGui.QLineEdit(self.frame_2)
        self.desdeempresa.setGeometry(QtCore.QRect(600, 20, 161, 21))
        self.desdeempresa.setObjectName(_fromUtf8("desdeempresa"))
        self.desdeempresa_2 = QtGui.QLineEdit(self.frame_2)
        self.desdeempresa_2.setGeometry(QtCore.QRect(820, -80, 161, 21))
        self.desdeempresa_2.setFrame(True)
        self.desdeempresa_2.setObjectName(_fromUtf8("desdeempresa_2"))
        self.visitaa = QtGui.QLineEdit(self.centralwidget)
        self.visitaa.setGeometry(QtCore.QRect(840, 300, 231, 21))
        self.visitaa.setObjectName(_fromUtf8("visitaa"))
        self.piso = QtGui.QLineEdit(self.centralwidget)
        self.piso.setGeometry(QtCore.QRect(840, 430, 41, 20))
        self.piso.setObjectName(_fromUtf8("piso"))
        self.telefono = QtGui.QLineEdit(self.centralwidget)
        self.telefono.setGeometry(QtCore.QRect(900, 430, 113, 20))
        self.telefono.setObjectName(_fromUtf8("telefono"))
        self.foto_final = QtGui.QLabel(self.centralwidget)
        self.foto_final.setGeometry(QtCore.QRect(550, 70, 261, 201))
        self.foto_final.setFrameShape(QtGui.QFrame.Box)
        self.foto_final.setText(_fromUtf8(""))
        self.foto_final.setObjectName(_fromUtf8("foto_final"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.etarjeta = QtGui.QLabel(self.centralwidget)
        self.etarjeta.setGeometry(QtCore.QRect(280, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.etarjeta.setFont(font)
        self.etarjeta.setText(_fromUtf8(""))
        self.etarjeta.setObjectName(_fromUtf8("etarjeta"))
        self.ecedula = QtGui.QLabel(self.centralwidget)
        self.ecedula.setGeometry(QtCore.QRect(380, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ecedula.setFont(font)
        self.ecedula.setText(_fromUtf8(""))
        self.ecedula.setObjectName(_fromUtf8("ecedula"))
        self.efoto = QtGui.QLabel(self.centralwidget)
        self.efoto.setGeometry(QtCore.QRect(490, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.efoto.setFont(font)
        self.efoto.setText(_fromUtf8(""))
        self.efoto.setObjectName(_fromUtf8("efoto"))
        self.ehuella = QtGui.QLabel(self.centralwidget)
        self.ehuella.setGeometry(QtCore.QRect(590, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ehuella.setFont(font)
        self.ehuella.setText(_fromUtf8(""))
        self.ehuella.setObjectName(_fromUtf8("ehuella"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(840, 10, 261, 211))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("logo_cliente.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.estaautorizado = QtGui.QCheckBox(self.centralwidget)
        self.estaautorizado.setGeometry(QtCore.QRect(840, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.estaautorizado.setFont(font)
        self.estaautorizado.setObjectName(_fromUtf8("estaautorizado"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Modulo enrolamiento", None))
        self.label_2.setText(_translate("MainWindow", "Vista previa de la cámara", None))
        self.label_3.setText(_translate("MainWindow", "Número de identificación:", None))
        self.validar.setText(_translate("MainWindow", "Validar registro del número", None))
        self.label_4.setText(_translate("MainWindow", "Nombre: ", None))
        self.visita.setText(_translate("MainWindow", "Visita a:", None))
        self.label_5.setText(_translate("MainWindow", "Empresa:", None))
        self.label_6.setText(_translate("MainWindow", "Piso:", None))
        self.label_7.setText(_translate("MainWindow", "Teléfono:", None))
        self.label_8.setText(_translate("MainWindow", "Apellido: ", None))
        self.label_9.setText(_translate("MainWindow", "Empresa: ", None))
        self.label_10.setText(_translate("MainWindow", "Foto capturada", None))
        self.estaautorizado.setText(_translate("MainWindow", "Esta autorizado?", None))

