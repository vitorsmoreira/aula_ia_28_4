from gtts import gTTS # Converte texto em voz
import speech_recognition as sr # Converte voz em texto
from playsound import playsound
import os

reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

while True:
    try:
        with microfone as mic:
            reconhecedor.adjust_for_ambient_noise(mic)
            print("Você deseja ouvir uma música?")
            audio = gTTS("Você deseja ouvir uma música?", lang="pt")
            audio.save("pergunta.mp3")
            playsound("pergunta.mp3")
            print("Aguardando resposta...")
            resposta = reconhecedor.listen(mic)
            print("Aguarde... reconhendo áudio...")
            texto = reconhecedor.recognize_google(resposta, language="pt")
            if texto.upper() == "SIM":
                print("Ok, abrindo a música...")
                audio = gTTS("Ok, abrindo a música...", lang="pt")
                audio.save("ok.mp3")
                playsound("ok.mp3")
                os.system("musica.mp3")
            elif texto.upper() == "Cancelar":
                break
            else:
                print("Beleza, estou encerrando...")
                audio = gTTS("Beleza, estou encerrando...", lang="pt")
                audio.save("tchau.mp3")
                playsound("tchau.mp3")
    except:
        print("Bugou!")
