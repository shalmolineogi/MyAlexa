import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def speak(answer):
    print('Alexa : ', answer)
    alexa.say(answer)
    alexa.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Alexa listening...")
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            if 'alexa' in query.lower():
                return query
            else:
                return "Please place your query by addressing me as 'Alexa'"
    except:
        return "Sound can't be captured . Please adjust your microphone"


def chatWithAlexa():
    query = listen()
    print('Me : ', query)
    if query == "Please place your query by addressing me as 'Alexa'":
        speak(query)
        return
    elif query == "Sound can't be captured . Please adjust your microphone":
        speak(query)
        return
    elif 'play' in query:
        print("In play if")
        song = query.replace('play ', '')
        speak("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in query:
        print("In time if")
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("It's " + time + " now")
        speak("It's " + time + " now")
    elif 'who' in query:
        print("In question if")
        question = query.split('is')[1]
        info = wikipedia.summary(question, 1)
        speak(info)
    elif 'what' in query:
        print("In question if")
        question = query.split('is')[1]
        info = wikipedia.summary(question, 1)
        speak(info)
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif 'do you love me' in query:
        speak('Yes, I love you')
    elif 'I love you' in query:
        speak('I love you too')
    elif 'bye' in query:
        speak("Okay bye! Have a nice day ahead!")
        exit()
    else:
        speak("Sorry ! I didn't get you . Please repeat!")


while True:
    chatWithAlexa()
