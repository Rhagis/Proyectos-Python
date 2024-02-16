import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


#opcion de idioma
id1 ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

#escuchar mi voz y transcribir lo que digo

def transformar_audio_en_texto():
    
    #almacenar recognizer en una variable
    r = sr.Recognizer()
    
    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8
        
        #informar que comenzo la grabacion
        print("Esta grabando")
        
        #guardiar lo que escuche como audio
        audio = r.listen(origen)
        
        try:
            #buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")
            
            #prueba de que pudo ingresar
            print("dijiste: " + pedido)
            
            #devolver pedido
            return pedido
        except sr.UnknownValueError:
            #en caso de que no comprenda el audio
            
            print("no entendi ni goma")
            
            #devolver algo
            return "sigo esperando"
        except sr.RequestError:
            #en caso de no resolver el pedido
            print("no entendi ni goma")
            
            #devolver algo
            return "sigo esperando"
        except:
            print("no entendi ni goma")
            
            #devolver algo
            return "sigo esperando"
        
#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):    
    
          
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    
    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():
    
    #crear variable con datos hoy
    dia = datetime.date.today()
    print(dia)
    
    #crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    
    #diccionario con nombres de dias
    calendario = {0:'lunes',
                  1: 'martes',
                  2:'miércoles',
                  3:'jueves',
                  4:'viernes',
                  5:'sábado',
                  6:'domingo'}
    
    #decir dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

def pedir_hora():
    
    hora = datetime.datetime.now()
    print(f"{hora.hour}:{hora.minute}")
    
    hablar(f"Son las {hora.hour} y {hora.minute}")

def saludar():
    
    hora = datetime.datetime.now()
    #decir el saludo
    if hora.hour > 21 or hora.hour < 6:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour <13:
        momento = "Buenos dias"
    else:
        momento = "Buenas tardes"
    hablar(f"{momento}, que necesita el día de hoy")

#funcion central del asistente

def pedir_cosas():
    
    #activar el saludo inicial
    saludar()
    
    #variable de corte
    comenzar = True
    
    while comenzar:
        
        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        
        if "abrir youtube" in pedido:
            hablar('Como ordene amo')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Como ordene')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Como ordene')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
pedir_cosas()



