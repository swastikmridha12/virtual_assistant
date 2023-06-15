import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            request = r.recognize_google(audio, language='en-in')
            print("You said:", request)
        except Exception as e:
            print(e)
            print("Sorry couldn't get it. Can you please say that again or something else.")
            speak("Sorry couldn't get it. Can you please say that again or something else.")
            return "None"
        return request


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)


def welcome():
    print("Hi it's spooderman, your virtual assistant. How may I help you?")
    speak("Hi it's spooderman, your virtual assistant. How may I help you?")


def Take_request():
    welcome()
    while True:
        request = takeCommand().lower()
        if "hello" in request:
            speak("Hi there. how may I help?")
            continue

        elif "spooderman" in request:
            speak("hey there. what may I do for you?")
            continue

        elif "open website" in request:
            speak("sure, what website will it be?")
            open_site = takeCommand().lower()
            if open_site != "none":
                search_web = "https://www." + open_site.replace(" ", "").replace("www.", "") + ".com"
                speak("Sure")
                webbrowser.open(search_web)
            continue

        elif "open google" in request:
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")
            continue

        elif "search on google" in request:
            speak("What do you want to search for?")
            search_request = takeCommand().lower()
            if search_request != "none":
                search_url = "https://www.google.com/search?q=" + search_request.replace(" ", "+")
                speak("Searching on Google for " + search_request)
                webbrowser.open(search_url)
            continue

        elif "from wikipedia" in request:
            speak("Checking Wikipedia")
            request = request.replace("wikipedia", "")
            result = wikipedia.summary(request, sentences=4)
            speak("According to Wikipedia")
            print("According to Wikipedia " + result)
            speak(result)


        elif "day" in request:
            tellDay()
            continue

        elif "time" in request:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
            continue

        elif "bye" in request:
            speak("if you need me I'm always around. Bye, and have a good day!")
            exit()

        elif "who are you" in request:
            speak("I am your virtual assistant, you can also call me spooderman")

        elif "that's it" in request:
            speak("if you need me I'm always around. Bye, and have a good day!")
            exit()


if __name__ == '__main__':
    Take_request()
