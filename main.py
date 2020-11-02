# этап 1 - voice to text
# этап 2 - text to voice
# этап 3 - запуск макроса
# 
# этап 4 - выделение незнакомых системе слов
# этап 5 - сохранение новых слов
# этап 6 - разбор сложных команд
# 

# #################################
from lib import listener, speaker
# #################################
# class Listener(object):
#   """
#   docstring
#   """
#   def listen_message(args):
#      return "adasd"
# # 

# ear = Listener()
# print (ear.listen_message() )

import speech_recognition as sr

import pyttsx3
from gtts import gTTS

from io import BytesIO
from pygame import mixer

import time
# Initialize the recognizer  
r = sr.Recognizer()  

mp3_name = "tmp.mp3"
mixer.init(48000, -16, 1, 1024)
# Function to convert text to 
# speech 
def SpeakText(command): 
    # https://cloud.google.com/text-to-speech/docs/voices
    # ru-ru ru-RU-Wavenet-D	MALE
    command = 'тест тест тест, эта штука работает, не так ли? configuring audio module'
    tts = gTTS(command, lang='ru')

    tts.save(mp3_name)
    # Проигрываем полученный mp3 файл
    mixer.music.load(mp3_name)
    mixer.music.play()
    # while mixer.music.get_busy():
    #     time.sleep(0.1)
    print ("done")

def SpeakTextLocalhost(command): 
      
    # Initialize the engine 
    # https://www.microsoft.com/en-us/download/details.aspx?id=27224
    engine = pyttsx3.init()
    # engine.setProperty('voice', male_voice)
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.name == 'Pavel':
            print(voice.name)
            engine.setProperty('voice', voice.id)
    engine.say(command)  
    engine.runAndWait()       
      
# Loop infinitely for user to 
# speak 
  
SpeakText("тест тест тест, эта штука работает? configuring audio module");

while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
  
            print("Did you say "+MyText) 
            SpeakText(MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 