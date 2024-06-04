import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"User's command: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        query = ""
    return query

def respond(query):
    if "hello" in query:
        speak("Heyy! How can I help you?")
    elif "what's the time now" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif " today's date" in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}")
    elif "search" in query:
        query = query.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    elif "exit" in query:
        speak("Goodbye  have a nice day")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Welcome to the channel How can I assist you?")
    while True:
        user_query = listen()
        respond(user_query)
