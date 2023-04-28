from gtts import gTTS
from playsound import playsound

msg = input("Digite o que deseja que o robô fale...")
audio = gTTS(msg, lang="pt")
audio.save("msg.mp3")
playsound("msg.mp3")
