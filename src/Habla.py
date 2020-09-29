'''
Created on 18/02/2015

@author: JohnFranklin
'''
import pyttsx
import sys

def main():
    try:
        engine = pyttsx.init()
        engine.setProperty('rate', 100)
        #Se selecciona el idioma a utilizar
        #voices = engine.getProperty('voices')
        #for voice in voices:
        #   print(voice.id)
        #   engine.setProperty('voice', voice.id)
        #engine.setProperty('voice', "spanish-latin-american")
        #Se genera la voz a partir de un texto
        engine.say(sys.argv[1])
        engine.runAndWait()
          
    except ValueError:
        print "Error: " + ValueError      
    
if __name__ == '__main__':
    main()
