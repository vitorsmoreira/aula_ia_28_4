import pyttsx3

robo = pyttsx3.init()
robo.setProperty("volume", 1.0)
robo.setProperty("rate", 150)

msg = input("O que deseja que o robô fale?")

robo.say(msg)
robo.runAndWait()
