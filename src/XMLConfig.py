'''
Created on 22/08/2014

@author: johnefe
'''

from xml.dom import minidom

    
p1=''
p2=''
p3=''
p4=''  
    
def leer_datos_puntos(tipoCamara):      
    xmldoc = minidom.parse('config.xml') 
    if tipoCamara=='entrada':    
        camaras=xmldoc.getElementsByTagName('camara1')
    elif tipoCamara=='salida':    
        camaras=xmldoc.getElementsByTagName('camara2')
    
    for node in camaras:  # visit every node <bar />
        conf_name=node.getAttribute('name')
        
        alist=node.getElementsByTagName('coordenada')
        for a in alist:
            tipo= a.childNodes[0].nodeValue
            if (conf_name == 'X1'):
                x1 = tipo
            elif (conf_name == 'X2'):    
                x2 = tipo   
            elif (conf_name == 'X3'):    
                x3 = tipo
            elif (conf_name == 'X4'):    
                x4 = tipo   
            elif (conf_name == 'Y1'):    
                y1 = tipo   
            elif (conf_name == 'Y2'):    
                y2 = tipo     
            elif (conf_name == 'Y3'):    
                y3 = tipo
            elif (conf_name == 'Y4'):    
                y4 = tipo
            elif (conf_name == 'REDMX'):    
                redmx = tipo
            elif (conf_name == 'REDMY'):    
                redmy = tipo        
            elif (conf_name == 'UMBRAL'):    
                umbral = tipo                  
                
    return x1,x2,x3,x4,y1,y2,y3,y4,redmx,redmy ,umbral 

def leer_datos_usb(signal):      
    xmldoc = minidom.parse('usbconfig.xml') 
    camaras=xmldoc.getElementsByTagName('signals')
    comando=''
    
    for node in camaras:  # visit every node <bar />
        conf_name=node.getAttribute('name')
        
        alist=node.getElementsByTagName('signal')
        for a in alist:
            tipo= a.childNodes[0].nodeValue
            if (conf_name == signal):
                comando = tipo
                
    return str(comando)  

def leer_test_camara():      
    xmldoc = minidom.parse('test.xml') 
    camaras=xmldoc.getElementsByTagName('testcamara')
    
    for node in camaras:  # visit every node <bar />
        conf_name=node.getAttribute('name')   
        alist=node.getElementsByTagName('direccion')
        
        for a in alist:
            tipo= a.childNodes[0].nodeValue
            if (conf_name == 'CCTV'):
                cctv = tipo
            elif (conf_name == 'IP'):    
                ip = tipo   
                
    return str(cctv),str(ip) 
                