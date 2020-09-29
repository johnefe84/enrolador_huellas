'''
Created on 4/05/2014
CREATE or replace VIEW parqueo_actual AS select `vh`.`placa` AS `placa`,`pr`.`nombres_propietario` AS `nombres_propietario`,`sp`.`fecha_ingreso` AS `fecha_ingreso`,`sp`.`hora_ingreso` AS `hora_ingreso` 
from ((`servicio_parqueo` `sp` join `vehiculos` `vh`) join `propietarios` `pr`) 
where ((`sp`.`propietario` = `pr`.`id_propietarios`) and 
 (`sp`.`vehiculo` = `vh`.`idvehiculos`) and
(`sp`.`fecha_salida` is null) and
(`sp`.`hora_salida` is null) 
)


create view visitantes_actuales as select count(*) as cantidad
from ((`servicio_parqueo` `sp` join `vehiculos` `vh`) join `propietarios` `pr`) 
where ((`sp`.`propietario` = `pr`.`id_propietarios`) and 
 (`sp`.`vehiculo` = `vh`.`idvehiculos`) and
(`sp`.`fecha_salida` is null) and
(`sp`.`hora_salida` is null) and
pr.es_visitante=1);

create view propietarios_actuales as select count(*) as cantidad
from ((`servicio_parqueo` `sp` join `vehiculos` `vh`) join `propietarios` `pr`) 
where ((`sp`.`propietario` = `pr`.`id_propietarios`) and 
 (`sp`.`vehiculo` = `vh`.`idvehiculos`) and
(`sp`.`fecha_salida` is null) and
(`sp`.`hora_salida` is null) and
pr.es_visitante=0);

create view cupos_disponibles as
select par.nombre,par.cupos_propietarios - pa.cantidad as propietarios, par.cupos_visitantes - va.cantidad as visitantes 
from visitantes_actuales va,propietarios_actuales pa,parqueadero par;
@author: johnefe
'''
import MySQLdb
import time
#import os
import cv2

def realizar_consulta_base_datos(tipo,id_vehiculo,id_propietario,consulta_ext,valor_minuto,id_usuario,foto):
	conexionok=False
	try:
		infile = open('C:/xampp/htdocs/recursos/ipservidor.txt', 'r')
		ipservidor=infile.read()
		conexionDB= MySQLdb.connect(ipservidor,'consulta','johnefe187471','parqueadero'); 
		conexionok=True
		infile.close()
	except MySQLdb.Error, e:
		conexionok=False
		try:
			print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
		except IndexError:
			print "MySQL Error: %s" % str(e)
		
	if (conexionok == True):	
		count_consulta=0
		valor_a_pagar=0
		if tipo == 'insertarVehiculo':  
			#verificar que el vehiculo no este ya en el parqueadero o que no
			#sea un reprocesamiento de la camara
			consulta = 'SELECT count(*) FROM servicio_parqueo where ' + 'vehiculo="' + id_vehiculo + '" and propietario="' + str(id_propietario) + '" and fecha_salida is null and hora_salida is null;'
			valor, count_consulta, resultado= realizar_consulta_base_datos('consulta','','',consulta,'','','')
			
			if valor == 1 and count_consulta>0:
				vehiculo_en_parqueadero=resultado.fetchone()[0]
				if vehiculo_en_parqueadero==0:
					foto_resized = cv2.resize(foto, (320,240)) 
					consulta = 'SELECT rutafotos FROM parqueadero'
					valor, count_consulta, resultado= realizar_consulta_base_datos('consulta','','',consulta,'','','')
					if valor == 1 and count_consulta>0:
						rutafotos=resultado.fetchone()[0]
						rutafotos=rutafotos.replace('-','\\')
						imagen_base = 'imagen' + str(id_vehiculo) + '_' + str(id_propietario) +'_'+time.strftime("%d_%m_%y_%H_%M_%S")+'.jpg'
						ruta=rutafotos+'\\'+imagen_base
						cv2.imwrite(ruta, foto_resized)
						#ruta=ruta.replace('\\','-')
						consulta_ext = 'INSERT INTO servicio_parqueo(fecha_ingreso,hora_ingreso,vehiculo,propietario,id_usuario,foto)' + 'VALUES(CURDATE(),CURTIME(),"' + id_vehiculo + '",' + str(id_propietario) + ','+str(id_usuario)+',"'+imagen_base+'");'
						cursor = None   
						#blob_value = open('fotos\foto.jpg').read()
						#blob_value = cv2.imread('fotos\foto.jpg')
						cursor = conexionDB.cursor()
						cursor.execute(consulta_ext) 
						count_consulta=cursor.rowcount
						valor=1
						out=1
				else:
					valor=0
					count_consulta=0
					out=0
			
		elif tipo== "retirarVehiculo":
			consulta = 'SELECT fecha_ingreso,hora_ingreso,id_servicio FROM servicio_parqueo WHERE vehiculo="' + str(id_vehiculo) + '" AND propietario="' + str(id_propietario) + '" and fecha_salida is null and hora_salida is null;';
			valor, count_consulta, resultado=realizar_consulta_base_datos('consulta','','',consulta,'','','');
			if valor ==1 and count_consulta >0:
				fecha_entrada,hora_entrada,id_servicio=resultado.fetchone()
				valor_a_pagar,tiempo_parqueo=calcularPrecio(valor_minuto,fecha_entrada,hora_entrada)
				consulta_ext = 'UPDATE servicio_parqueo SET tiempo_parqueo=' + str(tiempo_parqueo) + ',valor_cancelado=' + str(valor_a_pagar) + ',fecha_salida=curdate(),hora_salida=curtime()' + 'WHERE vehiculo="'+ str(id_vehiculo) +'" AND propietario=' + str(id_propietario) +' AND id_servicio='+str(id_servicio)+';'
				cursor = None   
				cursor = conexionDB.cursor()
				cursor.execute(consulta_ext) 
				count_consulta=tiempo_parqueo
				valor=1
				out=valor_a_pagar
			else:
				valor=0
				out=0
				print('El vehiculo ya habia salido antes')
					  
		elif tipo == "consulta":
			cursor = None   
			cursor = conexionDB.cursor()
			cursor.execute(consulta_ext) 
			conexionDB.close()
			#datos=[i[0] for i in cursor.fetchall()] 
			#datos =cursor.fetchall()
			if cursor== None:
				valor=0
				out=None
				count_consulta=0
			else:
				count_consulta=cursor.rowcount
				valor=1
				out=cursor 
				
		if tipo == 'insertarVehiculo':          
			resultado=out  
		elif tipo== "retirarVehiculo":   
			resultado= valor_a_pagar
		else: 
			resultado=out     
			   
		return valor, count_consulta, resultado

def calcularPrecio(valor_minuto,fecha_entrada,hora_entrada): 
    #function [valor,tiempo_parqueo]=
    consulta = 'SELECT hour(timediff(curtime(),"'+ str(hora_entrada) +'")) as hora,minute(timediff(curtime(),"' + str(hora_entrada) + '")) as minuto,datediff(curdate(),"'+ str(fecha_entrada) +'") as dias;'
    valor, count_consulta, resultado=realizar_consulta_base_datos('consulta','','',consulta,'','','');
    if valor ==1 and count_consulta>0:
        horas,minutos,dias=resultado.fetchone()
        #pasar todo a minutos
        consulta = 'SELECT minutos_excentos from parqueadero;'
        valor2, count_consulta2, resultado2=realizar_consulta_base_datos('consulta','','',consulta,'','','');
        if valor2 ==1 and count_consulta2>0:
            minutos_excentos=resultado2.fetchone()[0]
            if minutos < minutos_excentos:
                tiempo_parqueo=0
            else:    
                tiempo_parqueo=(dias*24*60)+(horas*60)+(minutos-minutos_excentos)
    
    valor=tiempo_parqueo*float(valor_minuto)
    
    return valor,tiempo_parqueo
    