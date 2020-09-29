'''
Created on 28/07/2014

@author: johnefe
'''
#import parallel
#import time
from pynguino import PynguinoUSB 
import XMLConfig
import time

class ControlUSB:
	
	p=None
	
	def __init__(self):
		if (self.p == None):
			try:
				self.p=PynguinoUSB("v2")
			except:
				pass
	def escribir(self,comando):
		try:
			self.p.write(str(comando))  
			self.p.close()
		except Exception,e:
			print("Error: "+str(e))
			pass
	
	def send_signal(self,signal):
		try:
			if (signal == 'SEME_VERDE'):
				comando=XMLConfig.leer_datos_usb('SEME_VERDE')
				if comando.upper()==comando:
					comando2=comando.lower()
				elif comando.lower()==comando:
					comando2=comando.upper()
				self.p.write(comando)
				time.sleep(1)
				self.p.write(comando2)
			elif (signal == 'SEME_AMARILLO'):
				comando=XMLConfig.leer_datos_usb('SEME_AMARILLO')
				self.p.write(comando)    
				#p.setData(2)#amarillo
			elif (signal == 'SEME_ROJO'):
				comando=XMLConfig.leer_datos_usb('SEME_ROJO')
				self.p.write(comando)     
				#p.setData(3)#rojo
			elif (signal == 'SEMS_VERDE'):
				comando=XMLConfig.leer_datos_usb('SEMS_VERDE')
				if comando.upper()==comando:
					comando2=comando.lower()
				elif comando.lower()==comando:
					comando2=comando.upper()
				self.p.write(comando)
				time.sleep(1)
				self.p.write(comando2)
				#p.setData(4)
			elif (signal == 'SEMS_AMARILLO'):
				comando=XMLConfig.leer_datos_usb( 'SEMS_AMARILLO')
				self.p.write(comando)   
				#p.setData(5)
			elif (signal == 'SEMS_ROJO'): 
				comando=XMLConfig.leer_datos_usb('SEMS_ROJO')
				self.p.write(comando)  
				#p.setData(6)
			elif (signal == 'ABRE_PEATON'): 
				comando=XMLConfig.leer_datos_usb('ABRE_PEATON')
				self.p.write(comando)
			elif (signal == 'CIERRA_PEATON'): 
				comando=XMLConfig.leer_datos_usb('CIERRA_PEATON')
				self.p.write(comando)
			elif (signal == 'ABRE_PEATON'): 
				comando=XMLConfig.leer_datos_usb('ABRE_PARQUEADERO')
				self.p.write(comando)
			elif (signal == 'CIERRA_PEATON'): 
				comando=XMLConfig.leer_datos_usb('CIERRA_PARQUEADERO')
				self.p.write(comando)
			elif (signal == 'SEME_OFF'): 
				comando=XMLConfig.leer_datos_usb('SEME_OFF')
				self.p.write(comando)
			elif (signal == 'SEMS_OFF'): 
				comando=XMLConfig.leer_datos_usb('SEMS_OFF')
				self.p.write(comando)
			elif (signal == 'RESET'): 
				comando=XMLConfig.leer_datos_usb('RESET')
				self.p.write(comando) 
				#p.setData(0)
			else:       
				self.p.write('r') 
			self.p.close()
					#p.setData(0)
		except Exception,e:
			print("Error: "+str(e))
			pass