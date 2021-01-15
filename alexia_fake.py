from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def listen_microphone():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print('Microphone...')
        audio = microphone.listen(source)
    try:
        phrase = microphone.recognize_google(audio, language = 'pt-BR')
        print('Humano: ' + phrase)
    except sr.UnkownValueError:
        print('bot: Isso não funcionou')

    return phrase

def create_audio(audio):
    tts = gTTS(audio, lang = "pt-BR")
    tts.save('bot.mp3')
    playsound('bot.mp3')

bot = ChatBot("Alexia")

conversation = [
    'Oi',
    'Olá',
    'Tudo bem?',
    'Tudo bem e você?',
    'Eu estou bem',
    'Que bom',
    'Qual meu nome?'
    'Seu nome é Leonardo'
]

trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    quest = listen_microphone()
    resp = bot.get_response(quest)
    create_audio(str(resp))
    print('Bot: ', resp)
