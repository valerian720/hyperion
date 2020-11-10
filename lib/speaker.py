class Speaker(object):
    def __init__( self, x=0, y=0):
      self.x = x
      self.y = y

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