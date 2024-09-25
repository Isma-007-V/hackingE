import pyttsx3 as voz 
import speech_recognition as sr 
import subprocess as sub 
from datetime import datetime
import pyaudio 

#configuracion de la voz de asistente virtual. 
voice=voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)
voice.setProperty('rate', 140)

def say (text):
    voice.say(text)
    voice.runAndWait()

while True:
    recognizer=sr.Recognizer()
    #activar microfono
    with sr.Microphone() as source:
        print("Escuchando...")
        audio=recognizer.listen(source, phrase_time_limit=3)

        try:#Si entiende nuestra peticion entramos a la logica principal
            comando = recognizer.recognize_google(audio, language='es-MX')
            print(f'Creo que dijiste "{comando}"')

            comando = comando.lower()
            comando = comando.split(' ')

            if 'computadora' in comando:

                if 'abre' in comando or 'abrir' in comando:
                    #diccionario de sitios
                    sites={
                        'google':'google.com',
                        'youtube':'youtube.com',
                        'facebook':'facebook.com',
                        'instagram':'instagram.com',
                        'twitter':'twitter.com',
                        'github':'github.com',
                        'spotify':'spotify.com',
                        'xnxx':'xnxx.com'
                    }

                    for i in list(sites.keys()):
                        if i in comando:
                            sub.call(f'start opera.exe {sites[i]}', shell=True)
                            say(f'Abriendo {i}')
                elif 'hora' in comando:
                    time = datetime.now().strftime('%H:%M')
                    say(f'Son las {time}')

                if 'termina' in comando or 'terminar' in comando or 'término' in comando or 'terminó' in comando:
                    say('Sesión finalizada')
                    break


        except:
            print('No te entendí, podrías repetirlo de nuevo por favor')

            