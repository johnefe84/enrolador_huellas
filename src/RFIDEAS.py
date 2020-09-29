'''
Created on 27/01/2015

@author: JohnFranklin
'''
import os,string,time
import Licencia
import Consulta_BD
import numpy
#import ControlUSB
import sys

def modo_enrrolar(cedula,usuario):
    try:
        intentos=0
        parar=False
        exito=0
        listado = os.popen('cmdpcprox -list')
        s = listado.read()
        listado.close()
        devices = s.split('#')
        cantidadLectores=len(devices)-1
        print("Cantidad de lectores: "+str(cantidadLectores))
        
        licencia=Licencia.Licencia()
        if licencia.validar_licencia():
            while parar==False:
                dispositivo=0
                while dispositivo < cantidadLectores:
                    #print("Anlizando lector: "+str(revision)) 
                    codigo=""
                    fd = os.popen('cmdpcprox -getactiveid=":%s"  -waitforgetactiveid=1 -setactdev='+str(dispositivo))
                    codigo = fd.read()[:-17]
                    fd.close()
                    if codigo <> "":
                        codigo=codigo.replace(" ","")
                        codigo=codigo.replace(":","")
                        
                        if usuario=='N' and codigo <> "":  
                            consulta = 'SELECT count(*) FROM propietarios where nfcid="' + str(codigo) + '" and esta_autorizado=1;'
                            valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                            if valor == 1 and count_consulta>0:
                                yarelacionada=resultado.fetchone()[0]     
                                if yarelacionada== 0:        
                                    exito=1                 
                                    consulta = 'update propietarios set nfcid="'+str(codigo)+'" where cedula="' + str(cedula) + '";'
                                    valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
                                    print "Tarjeta asignada al usuario con exito"
                                else:
                                    exito=3
                                    consulta = 'SELECT nombres_propietario,apellidos_propietario FROM propietarios where nfcid="' + str(codigo) + '" and esta_autorizado=1;'
                                    valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                                    if valor == 1 and count_consulta>0:
                                        nombre_propietario,apellido_propietario=resultado.fetchone()
                                        print "Esta tarjeta ya esta asignada y autorizada a: "+str(nombre_propietario)+" "+str(apellido_propietario)
                        else:
                            exito=1
                        parar=True
                        revision = cantidadLectores
                        intentos=3
              
                    dispositivo=dispositivo+1
                
                intentos=intentos+1
                if intentos >3:
                    parar=True
                elif exito==1:
                    parar=True    
        return exito 
        
    except ValueError:
        print ("Error: "+str(ValueError))
    return exito
    
def validar_administrador(cedula):
    try:            
        exito=0               
        consulta = 'select cedulaadmin from parqueadero;'
        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
        if valor == 1 and count_consulta>0:
            cedulaadmin=resultado.fetchone()[0]
            exito=modo_enrrolar(cedulaadmin,'A')                                     
        
    except ValueError:
        print ("Error: "+str(ValueError))
    return exito

def modoescucha():
    control_usb=None
    try:
        licencia=Licencia.Licencia()
        if licencia.validar_licencia():
            dispositivo=0
            listado = os.popen('cmdpcprox -list')
            s = listado.read()
            listado.close()
            devices = s.split('#')
            cantidadLectores=len(devices)-1
            print("cantidad de lectores detectados: "+ str(cantidadLectores))
            
            while True and cantidadLectores>0:
                codigo=""
                #print "Leyendo lector No. "+str(dispositivo)
                fd = os.popen('cmdpcprox -getactiveid=":%s"  -waitforgetactiveid=0.25 -setactdev='+str(dispositivo))
                #codigo = fd.read()[:-11]
                codigo = fd.read()[:-17]
                fd.close()
                if codigo <> "":
                    codigo=codigo.replace(" ","")
                    codigo=codigo.replace(":","")
                    #s_nosp = string.replace(codigo, ' ', '') # remove spaces
                    #bits = eval("0x"+s_nosp[0:2])
                    #idRaw = eval("0x"+s_nosp[2:])
                    # en cchasp= id = (int)(idRaw & 0x0ffffL); 65535 es FFFFen HEX
                    #id1 = idRaw & 65535
                    #id1 = idRaw &65636
                    #fac = (idRaw>>17) & 255
                    #print "Card Bits=%d, FAC=%d, ID=%d\n" % (bits,fac,id1) 
                    
                    print "codigo tarjeta: "+str(codigo)+" en lector No. "+str(dispositivo)
                    consulta = 'SELECT cedula,nombres_propietario,validar_placa,es_visitante,esta_autorizado FROM propietarios where nfcid="' + str(codigo) + '";'
                    valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                    if valor == 1 and count_consulta>0:
                        cedula,nombres_propietario,validar_placa,es_visitante,esta_autorizado=resultado.fetchone()
                        cedula=str(cedula).split('.')[0]
                        #consulta = 'select count(*) from huellas_detectadas where cedula="'+str(cedula)+'" and fecha_entrada= CURDATE( ) AND MINUTE( TIMEDIFF( CURTIME( ) , hora_entrada ) ) <=1 and HOUR( TIMEDIFF( CURTIME( ) , hora_entrada ) ) =0 ;'
                        #valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
                        
                        #if valor == 1 and count_consulta>0:
                        #    cantidad=resultado.fetchone()[0]                 
                        #    if cantidad ==0:
                                
                        consulta = 'SELECT acceso,descripcion FROM lectores where id="'+str(dispositivo)+'"'
                        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                        if valor == 1 and count_consulta>0:                                
                            acceso,descripcion=resultado.fetchone() 
                            
                            if 'entrada' in str(descripcion).lower():
                                consulta = 'insert into huellas_detectadas(cedula,fecha_entrada,hora_entrada,validar_placa,origen) values("'+str(cedula)+'",CURDATE(),CURTIME(),'+str(validar_placa)+',"TARJETERO");'
                                valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
                                print('Ingreso: '+str(nombres_propietario))
                                if esta_autorizado==1:
                                    consulta = 'SELECT count(*) FROM signals where cedula="'+str(cedula)+'" and send="'+str(acceso)+'" and descripcion="'+str(descripcion)+'"'
                                    valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                                    cantidad=0
                                    if valor == 1 and count_consulta>0:                                
                                        cantidad=resultado.fetchone()[0] 
                                    if cantidad==0:
                                        consulta = 'insert into signals(send,descripcion,cedula) values ("'+str(acceso)+'","'+str(descripcion)+'","'+str(cedula)+'");'                                            
                                        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
                            elif 'salida' in str(descripcion).lower():
                                consulta = 'update huellas_detectadas set fecha_salida=curdate(),hora_salida=curtime() where origen="TARJETERO" and cedula="'+str(cedula)+'";'
                                valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')
                                print('Salio: '+str(nombres_propietario))
                                
                                if es_visitante==0:
                                    if esta_autorizado==1:
                                        consulta = 'SELECT count(*) FROM signals where cedula="'+str(cedula)+'" and send="'+str(acceso)+'" and descripcion="'+str(descripcion)+'"'
                                        valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                   
                                        cantidad=0
                                        if valor == 1 and count_consulta>0:                                
                                            cantidad=resultado.fetchone()[0] 
                                        if cantidad==0:
                                            consulta = 'insert into signals(send,descripcion,cedula) values ("'+str(acceso)+'","'+str(descripcion)+'","'+str(cedula)+'");'                                            
                                            valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')    
                                    consulta = 'update propietarios set esta_autorizado=0 where cedula="'+str(cedula)+'" and es_visitante=1 and esta_autorizado=1;'                                            
                                    valor, count_consulta, resultado= Consulta_BD.realizar_consulta_base_datos('consulta','','',consulta,'','','')                                                   

                dispositivo=dispositivo+1
            
                if dispositivo>=cantidadLectores:
                    dispositivo=0 
        else:
            print "Licencia no valida para este equipo"
            sys.exit()

    except Exception,e:
        print "Error "+str(e)
        