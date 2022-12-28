import cv2          
import numpy as np    
import time         
import serial      
 
webcam_id = 0                     
cap = cv2.VideoCapture(webcam_id)  

mensajeEnviado=False
piezaDetectada=False
 
def color_detectado(imagenHSV):
         
    # Rojo
    rojoBajo = np.array([161, 155, 84], np.uint8)      #Rango color Bajo ([H,S,V])
    rojoAlto = np.array([180, 255, 255], np.uint8)     #Rango color Alto ([H,S,V])
    #Blanco
    blancoBajo = np.array([11, 20, 20], np.uint8)
    blancoAlto = np.array([19, 155, 255], np.uint8)
    #Verde
    verdeBajo = np.array([25, 52, 72], np.uint8)
    verdeAlto = np.array([102, 255, 255], np.uint8)
  
     
    maskRojo = cv2.inRange(imagenHSV, rojoBajo, rojoAlto)       
    maskBlanco = cv2.inRange(imagenHSV, blancoBajo, blancoAlto) 
    maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)     
 
    cntsRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]      
    cntsBlanco = cv2.findContours(maskBlanco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1] 
    cntsVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1] 
 
    if len(cntsRojo)>0: color = 'Rojo'        
    elif len(cntsBlanco)>0: color = 'Blanco'  
    elif len(cntsVerde)>0: color = 'Verde'
    return color
 
def figura_detectada(approx):
     
    if len(approx)<6:
        figura='Cuadrado'
    elif len(approx)>10:
        figura='Circulo'
    return figura

try:
    while(cap.isOpened()):
        ret, image = cap.read()   
                                 
        if ret == True:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
 
            canny = cv2.Canny(image, 10, 150, 3)                                                         
         
            canny = cv2.dilate(canny, None, iterations=1) 
            canny = cv2.erode(canny, None, iterations=1)  
 
            imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
 
            pixG=gray[240,320]    
             
            if pixG < 20:        
                mensajeEnviado=False
                piezaDetectada=False
                time.sleep(0.1)
 
            if pixG > 25:       
                piezaDetectada=True        
                time.sleep(0.25)