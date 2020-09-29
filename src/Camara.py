'''
Created on 11/12/2014

@author: johnefe
'''
import numpy as np
import time
import sys
from XMLConfig import leer_test_camara
from PyQt4 import QtGui, QtCore, Qt
from ventana import Ui_MainWindow
import MySQLdb
import hashlib
import os
import Consulta_BD
import Image
import cv2
import win32print #http://sourceforge.net/projects/pywin32/files/ win32 package
import win32ui #http://sourceforge.net/projects/pywin32/files/ win32 package
import win32con #http://sourceforge.net/projects/pywin32/files/ win32 package
import win32api
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab import rl_settings
import StringIO
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import Licencia
import os.path

#from NFC_escucha import modo_enrrolar,validar_administrador
from RFIDEAS import modo_enrrolar,validar_administrador

class Camara(QtGui.QMainWindow):
 
    def __init__(self,parent=None):  
        QtGui.QWidget.__init__(self,parent)
        self.licencia=Licencia.Licencia()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.ui.validar.clicked.connect(self.validar) 
        self.ui.tarjeta.clicked.connect(self.tarjeta)
        self.ui.tomarfoto.clicked.connect(self.tomarfoto) 
        self.ui.cedula.clicked.connect(self.cedula) 
        self.ui.huella.clicked.connect(self.huella) 
        self.ui.imprimir.clicked.connect(self.imprimirpdf) 
        self.ui.validar.setDisabled(False)
        self.ui.tarjeta.setDisabled(True)
        self.ui.tomarfoto.setDisabled(True)
        self.ui.cedula.setDisabled(True)
        self.ui.huella.setDisabled(True)
        self.ui.imprimir.setDisabled(True)
        infile = open('ipservidor.txt', 'r')
        ipservidor=infile.read()
        db = MySQLdb.connect(ipservidor,'consulta','johnefe187471','parqueadero');   
        cursor = None   
        infile.close()
        cursor = db.cursor()
        cedula=str(self.ui.identificacion.text())
        command = 'select nombre from empresas order by nombre asc;'
        #print (command)
        cursor.execute(command)
        db.close()
        self.ui.comboBox.activated[str].connect(self.seleccionado)
        self.ui.comboBox.addItem("")
        if cursor.rowcount > 0:
            for renglon in range(0,cursor.rowcount): 
                nombre=cursor.fetchone()[0]
                self.ui.comboBox.addItem(nombre)
            
        self.capture=[]
        self.readFrame=np.array([])         
        self.currentFrame=np.array([])
        cctv,ip= leer_test_camara()
        self.capture=cv2.VideoCapture(int(cctv))
        time.sleep(2)
        try:
            print "Validando licencia..."
            if self.licencia.validar_licencia():
                f, self.readFrame = self.capture.read()
                tam=self.readFrame.shape
                self._timer = QtCore.QTimer(self)
                self._timer.timeout.connect(self.play)
                self._timer.start(1)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle("Informacion")
                i = QtGui.QIcon()
                i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msgBox.setWindowIcon(i)
                self.ui.nombre.setText("")
                self.ui.apellido.setText("")
                msgBox.setText('Error: Licencia invalida para este equipo!')
                ret = msgBox.exec_(); 
                exit()
        except Exception,e:
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Informacion")
            i = QtGui.QIcon()
            i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msgBox.setWindowIcon(i)
            self.ui.nombre.setText("")
            self.ui.apellido.setText("")
            msgBox.setText('Error: '+str(e))
            ret = msgBox.exec_();    
            return None
        
    def seleccionado(self,item):
        infile = open('ipservidor.txt', 'r')
        ipservidor=infile.read()
        db = MySQLdb.connect(ipservidor,'consulta','johnefe187471','parqueadero');   
        cursor = None   
        infile.close()
        cursor = db.cursor()
        cedula=str(self.ui.identificacion.text())
        command = "select piso,telefono from empresas where nombre='"+str(item)+"';"
        #print (command)
        cursor.execute(command)
        db.close()
        if cursor.rowcount > 0:
            piso,telefono=cursor.fetchone()
        self.ui.piso.setText(str(piso))
        self.ui.telefono.setText(str(telefono))
        
    def convertFrame(self,imagen):
        """converts frame to format suitable for QtGui            """
        try:
            imagen=cv2.cvtColor(imagen, cv2.cv.CV_BGR2RGB, imagen)
            height,width=self.readFrame.shape[:2]
            img=QtGui.QImage(imagen,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            try:
                img=QtGui.QPixmap.fromImage(img)
                return img
            except:
                pass
                return None
        except:
            return None
    
    def captureNextFrame(self,tipoCamara):
        """                                         
        capture frame and reverse RBG BGR and return opencv image                                                                        
        """       
        apagar='0'
        saludo_propietario=''
        caracteres_detectados=''
        promedioGlobal=0
        placaDetectada=None
        mensajes=0
        exitoso=False
        minutos_pagar=0

        exitoso, self.readFrame  = self.capture.read()
            
        if(exitoso == True):
            #self.currentFrame=self.readFrame
            try:
                self.currentFrame =cv2.cvtColor(self.readFrame,cv2.COLOR_BGR2GRAY)
                height,width=self.currentFrame.shape
                placaDetectada=self.currentFrame  
            except Exception,e:
                print("except Sin imagen en: "+str(tipoCamara))
        else:  
            print("Sin imagen en: "+str(tipoCamara))
                    
        return  self.currentFrame 
    
    def imprimirpdf(self):
        
        if str(self.ui.visitaa.text()) <> "":
            visitaa=str(self.ui.visitaa.text())
        else:
            visitaa="-"
        
        if str(self.ui.comboBox.currentText()) <>"":
            visitaempresa=str(self.ui.comboBox.currentText())
        else:
            visitaempresa="-"  
            
        if str(self.ui.piso.text()) <>"":
            piso=str(self.ui.piso.text())
        else:
            piso="0"  
            
        if str(self.ui.desdeempresa.text())<>"":
            vienede=str(self.ui.desdeempresa.text())
        else:
            vienede="-"
            
        if self.ui.estaautorizado.isChecked():
            consulta = 'update propietarios set esta_autorizado=1 where cedula="'+str(self.ui.identificacion.text())+'";'
            valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')    
            
        consulta = 'insert into huellas_detectadas(cedula,fecha_entrada,hora_entrada,validar_placa,origen,visitaa,empresavisita,pisovisita,vienede) values("'+str(self.ui.identificacion.text())+'",CURDATE(),CURTIME(),0,"REG.VISITANTE","'+visitaa+'","'+visitaempresa+'",'+piso+',"'+vienede+'");'
        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
        
        if str(self.ui.identificacion.text()) <>"" and str(self.ui.identificacion.text())<> None:
            consulta = 'update propietarios set esta_autorizado=1 where cedula="'+str(self.ui.identificacion.text())+'"'
            valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
            
        imgTemp = StringIO.StringIO()
        imgDoc = canvas.Canvas(imgTemp)
        infile = open('ipservidor.txt', 'r')
        ipservidor=infile.read()  
        infile.close()
        imgPath2 = "\\\\"+ipservidor+"\personas\id_"+str(self.ui.identificacion.text())+".jpg"
        imgPath3 = "logo_cliente.png"
        packet = StringIO.StringIO()
        ancho=10
        alto=6.2
        can = canvas.Canvas(packet, pagesize=(ancho*cm,alto*cm))
        can.setFont("Times-Roman", 16)
        can.drawString(4.5*cm,3.7*cm, "VISITANTE")
        can.setFont("Times-Roman", 11)
        can.drawString(4.7*cm,2.7*cm, "Nombre: "+str(self.ui.nombre.text()))
        can.drawString(4.7*cm,2.2*cm, "Apellido: "+str(self.ui.apellido.text()))
        can.setFont("Times-Roman", 11)
        can.drawString(4.7*cm,1.8*cm, "Identificacion:"+str(self.ui.identificacion.text()))
        can.drawString(4.7*cm,1.3*cm, "De: "+str(self.ui.desdeempresa.text()))
        
        can.setFont("Times-Roman", 9)
        can.drawString(0.5*cm,1.3*cm, "Visita a: "+str(self.ui.visitaa.text()))
        can.drawString(0.5*cm,0.8*cm, "Piso: "+str(self.ui.piso.text()))
        can.drawString(0.5*cm,0.3*cm, "Empresa: "+str(self.ui.comboBox.currentText()))
        
        can.setFont("Times-Roman", 9)
        can.drawString(4.7*cm,0.8*cm, "Fecha entrada: "+time.strftime("%d/%m/%Y"))
        can.drawString(4.7*cm,0.3*cm, "Hora entrada: "+ time.strftime("%I:%M:%S %p"))
        #vendido a,factura no, fecha emision,fecha vencimiento
        #can.roundRect(x,y,ancho,alto,radio,1,0)
        can.roundRect( 0.3*cm,0*cm,9.2*cm,5*cm,10,stroke=1, fill=0)
     
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet).getPage(0)
          
        imgDoc.drawImage(imgPath2, 12,50, 110,90)    
        #imgDoc.save()
        imgDoc.drawImage(imgPath3, 215,90, 50,50) 
        imgDoc.save()
        
        page = PdfFileReader(file("sticker_limpio_10x5.pdf","rb")).getPage(0)
        overlay = PdfFileReader(StringIO.StringIO(imgTemp.getvalue())).getPage(0)
        page.mergePage(overlay)
        page.mergePage(new_pdf)
        
        output = PdfFileWriter()
        output.addPage(page)
        output.write(file("sticker.pdf","w"))
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Informacion")
        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgBox.setWindowIcon(i)
        msgBox.setText('Se genero el sticker con exito!!')
        ret = msgBox.exec_(); 
        fname= "sticker.pdf"
        win32api.ShellExecute(0, "print", fname, None,  ".",  0)
        
    def imprimir(self):   
        #Python 3.2/ windows 7
        #!/usr/bin/env python
        
        #reference snippet:http://www.daniweb.com/software-development/python/code/216640
        
        Testtext = "Impreso desde Python?"
        try:
            hDC = win32ui.CreateDC()
            #PrinterList = win32print.EnumPrinters(2,"",5) #Get all printer info
            #for dato in PrinterList:
            #    print(dato) #print all printer info
            #TargetPrinter = win32print.OpenPrinter("HP LaserJet Professional P 1102w") #Get specific printer info
            #print(TargetPrinter) # print specific printer info
            
            
            h = win32print.OpenPrinter(win32print.GetDefaultPrinter())
            t = win32print.GetPrinter(h)
            TargetPrinter = win32print.OpenPrinter(t[1])          
            print t

            fname="E:\\ideauto\\documentos\\test.pdf"
            win32api.ShellExecute(0, "print", fname, None,  ".",  0)
            '''
            resultado=hDC.StartDoc("test doc")
            hDC.StartPage()
            hDC.SetMapMode(win32con.MM_TWIPS)
            
            ulc_x=10
            ulc_y=-10
            lrc_x=2000
            lrc_y=-2000
            
            hDC.DrawText(Testtext,(ulc_x,ulc_y,lrc_x,lrc_y),win32con.DT_LEFT)
            hDC.EndPage()
            hDC.EndDoc()
            win32print.ClosePrinter(h)
            '''
            
            '''
            from win32com.client import Dispatch

            labelCom = Dispatch('Dymo.DymoAddIn')
            labelText = Dispatch('Dymo.DymoLabels')
            isOpen = labelCom.Open('test.label')
            selectPrinter = 'DYMO LabelWriter 450'
            labelCom.SelectPrinter(selectPrinter)
            
            labelText.SetField('VAR_TEXT', 'QGJ2148')
            
            labelCom.StartPrintJob()
            labelCom.Print(1,False)
            labelCom.EndPrintJob()

            '''
        except ValueError:
             
            print ValueError
            #self.ui.autorizado.setText("USUARIO O CONTRASENA INCORRECTA")
            return None
    def validar(self):
        try:
            infile = open('ipservidor.txt', 'r')
            ipservidor=infile.read()
            db = MySQLdb.connect(ipservidor,'consulta','johnefe187471','parqueadero');   
            cursor = None   
            infile.close()
            cursor = db.cursor()
            cedula=str(self.ui.identificacion.text())
            command = 'select nombres_propietario, apellidos_propietario,huella1,huella2,nfcid,esta_autorizado from propietarios where cedula="' + cedula + '";'
            #print (command)
            cursor.execute(command)
            db.close()
            if cursor.rowcount > 0:
                nombres_propietario, apellidos_propietario,huella1,huella2,nfcid,esta_autorizado=cursor.fetchone()
                self.ui.nombre.setText(str(nombres_propietario))
                self.ui.apellido.setText(str(apellidos_propietario))
                try:
                    imgPath2 = "\\\\"+ipservidor+"\personas\id_"+str(self.ui.identificacion.text())+".jpg"
    
                    if os.path.isfile(imgPath2):
                        fotoactual=self.convertFrame(cv2.imread(imgPath2))
                        self.ui.foto_final.setPixmap(fotoactual)
                        self.ui.foto_final.setScaledContents(True)
                        self.ui.efoto.setText("OK")
                        self.ui.imprimir.setDisabled(False)
                    else:
                        self.ui.efoto.setText("Sin foto")
                except:
                    self.ui.efoto.setText("Sin foto")
                    pass
                
                if huella1==None and huella2==None:
                    self.ui.ehuella.setText("Sin huella")
                elif huella1==None and huella2<>None:
                    self.ui.ehuella.setText("1 Huella")
                elif huella1<>None and huella2==None:
                    self.ui.ehuella.setText("1 Huella")
                elif huella1<>None and huella2<>None:
                    self.ui.ehuella.setText("OK")
                    
                if nfcid == None:
                    self.ui.etarjeta.setText("Sin tarj.") 
                else:
                    self.ui.etarjeta.setText("OK")
                         
                self.ui.tarjeta.setDisabled(False)
                self.ui.tomarfoto.setDisabled(False)
                self.ui.cedula.setDisabled(False)
                self.ui.huella.setDisabled(False)
                
                if esta_autorizado==1:
                    self.ui.estaautorizado.setChecked(True)
                else:
                    self.ui.estaautorizado.setChecked(False)
                    
                return True
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle("Error")
                i = QtGui.QIcon()
                i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msgBox.setWindowIcon(i)
                self.ui.nombre.setText("")
                self.ui.apellido.setText("")
                msgBox.setText('No se han registrado los datos de la persona!')
                ret = msgBox.exec_();              
                return False    
        except ValueError:
            #self.ui.autorizado.setText("USUARIO O CONTRASENA INCORRECTA")
            return None
    
    def tarjeta(self):   
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Informacion")
        i = QtGui.QIcon()
        exito=0
        exito2=0
        exito3=0
        i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgBox.setWindowIcon(i)   
           
        consulta = 'SELECT count(*) FROM propietarios where nfcid is not null and cedula ="' + str(self.ui.identificacion.text()) + '";'
        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
        if valor == 1 and count_consulta>0:
            cantidad_tarjetas=resultado.fetchone()[0]
            if cantidad_tarjetas == 0 :   
                msgBox.setText('Acerque la tarjeta en el lector dentro de los 5 segundos despues de dar clic en Aceptar, si no lo hace debera volver a hacer clic en el boton de tarjeta')
                ret = msgBox.exec_();  
                exito=modo_enrrolar(str(self.ui.identificacion.text()),'N')
                if exito==1:
                    self.ui.mensajes.setText('Tarjeta registrada con exito!')
                elif exito==3:
                    self.ui.mensajes.setText('Error: Esta tarjeta ya esta asignada y autorizada a otra persona!')
            else:
                self.ui.mensajes.setText('Acerque la tarjeta del administrador en el lector!')
                msgBox.setText('El usuario ya tiene una Tarjeta registrada, se requiere autorizacion!')
                ret = msgBox.exec_(); 
                exito2=validar_administrador(str(self.ui.identificacion.text()))
                if exito2==1:  
                    msgBox.setText('Autorizacion exitosa. Ahora retire la tarjeta y acerque la nueva tarjeta del usuario!')
                    ret = msgBox.exec_(); 
                    exito3=modo_enrrolar(str(self.ui.identificacion.text()),'N')
                    if exito3==1:
                        self.ui.mensajes.setText('Nueva Tarjeta registrada con exito!')

            '''  
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Informacion")
            i = QtGui.QIcon()
            i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msgBox.setWindowIcon(i)
            msgBox.setText('Tarjeta registrada con exito!')
            ret = msgBox.exec_(); 
            '''
    def QImageToCvMat(self,incomingImage):
        '''  Converts a QImage into an opencv MAT format  '''
    
        incomingImage = incomingImage.convertToFormat(4)
    
        width = incomingImage.width()
        height = incomingImage.height()
    
        ptr = incomingImage.constBits()
        #Mptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 3)  #  Copies the data
        #arr = np.array(ptr).reshape(width,height, 4)  #  Copies the data
        return arr

    def tomarfoto(self):
        #image = QImage(filename)
        #data = QByteArray()
        #buf = QBuffer(data)
        #imagen=QtGui.QImage(self.ui.foto.pixmap())
        infile = open('ipservidor.txt', 'r')
        ipservidor=infile.read()  
        infile.close()
        self.readFrame =cv2.cvtColor(self.readFrame,cv2.COLOR_BGR2RGB)
        imgPath2="\\\\"+ipservidor+"\personas\id_"+str(self.ui.identificacion.text())+".jpg"
        #imagen.save("C:/xampp/htdocs/recursos/ideautoweb/imagenes/personas/id_"+str(self.ui.identificacion.text())+".png", 'PNG')
        try:
            if os.path.isfile(imgPath2):
                os.remove(imgPath2)
            cv2.imwrite(imgPath2,self.readFrame)
            self.ui.mensajes.setText('Fotografia capturada y almacenada con exito!')
            self.ui.imprimir.setDisabled(False)
        except Exception,e:
            print 'Error: '+str(e)
            self.ui.mensajes.setText('Error: '+str(e))
            pass
        
        fotoactual=self.convertFrame(self.readFrame)
        self.ui.foto_final.setPixmap(fotoactual)
        self.ui.foto_final.setScaledContents(True)
        '''
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Informacion")
        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgBox.setWindowIcon(i)
        msgBox.setText('Fotografia capturada y alamacenada con exito!')
        ret = msgBox.exec_();  
        '''
    
    def cedula(self):
        print("Acerque la cedula al lector")  
        self.ui.mensajes.setText('Acerque la cedula al lector!')
          
    def huella(self):
        self.ui.mensajes.setText('Se abrira el modulo de huella por favor espere...')
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Informacion")
        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgBox.setWindowIcon(i)
        msgBox.setText('Se abrira el modulo de huella por favor espere...')
        ret = msgBox.exec_();    
        os.system("java -jar Huella.jar "+str(self.ui.identificacion.text()))
                
    def play(self):
        scale_down = 4
        contador=0
        f, self.readFrame = self.capture.read()
        tam=self.readFrame.shape
        ancho=tam[0]
        alto=tam[1]
        
        if self.readFrame <> None:
            #self.readFrame =cv2.cvtColor(self.readFrame,cv2.COLOR_COLORCVT_MAX)
            #self.readFrame=cv2.resize(self.readFrame,(480,320))
            convertida=self.convertFrame(self.readFrame)
            self.ui.foto.setPixmap(convertida)
            self.ui.foto.setScaledContents(True)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Camara()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

