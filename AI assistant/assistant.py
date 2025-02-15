import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hey I am jack your assistant. Please tell me how may I help you?")


# It takes microphone input from the user and returns the string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print("Please say it again ...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartik2k1sharma@gmail.com', "flyiujeacbakxemi")
    server.sendmail('kartik2k1sharma@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Google' in query:
            webbrowser.open("google.com")

        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'good job jack' in query:
            speak("thank you sir")

        elif "open my folder" in query:
            path = "E:\\kartik"
            os.startfile(path)

        elif 'how are you jack' in query:
            speak("i am good thanks for asking, what about you?")

        elif 'i am fine jack' in query:
            speak("good to know sir, tell me how can i help you ")

        elif "open dj folder" in query:
            path = "E:\\Daizy"
            os.startfile(path)

        elif 'send email to kartik' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "kartik2k1sharma@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully!")

            except Exception:
                speak("Sorry, I am unable to send the email.")

        elif 'exit' in query:
            speak("Goodbye Have a great day.")
            exit()
