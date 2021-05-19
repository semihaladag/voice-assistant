import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
#gTTS kütüphanesi ile yazıyı sesli bir şekilde duymamızı sağlıyor
#playsound kütüphanesi ses dosyalarını çalmak için kullanılıyor
#random kütüphanesini random dosya ismi oluşturmak için kullanılıyor (56. satır)

r = sr.Recognizer()

#if komutlarını kullanarak komutlar girilebilir
def record(ask = False):
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
    try:
         voice=r.recognize_google(audio, language='tr-TR')
    except sr.UnknownValueError:
        speak('anlayamadım')
    except sr.RequestError:
        speak('sistem çalışmıyor')  
    return voice

def response(voice):
    if 'nasılsın' in voice:
        speak('İyiyim siz nasılsınız')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search= record('ne aramak istersin')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')

    if 'şarkı çal' in voice:
        speak('Şarkıyı açıyorum')
        url= 'https://www.youtube.com/watch?v=uliCeunCqe4&list=RDMM&start_radio=1'
        webbrowser.get().open(url)
        
    if('Neler yapabilirsin') in voice:
        speak('Sizin önceden belirlediğiniz komutları yerine getirebilirim')

    if 'kapat' in voice:
        speak('görüşürüz efendim')
        exit()


def speak(string):
   tts = gTTS(string, lang='tr')
   rand = random.randint(1,10000)
   file = 'audio-'+str(rand)+'.mp3'
   tts.save(file)
   playsound(file)
   os.remove(file)


       

speak('nasıl yardımcı olabilirim')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)


