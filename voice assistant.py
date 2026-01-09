import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI  # Updated import for new library
from config import apikey
import datetime
import random
import pyttsx3

# --- INITIALIZATION ---
client = OpenAI(api_key=apikey)  # New OpenAI Client
chatStr = ""

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Try to set a specific voice (usually index 0 is male, 1 is female on Windows)
engine.setProperty('voice', voices[0].id)


def say(text):
    """Speaks the text using the pyttsx3 engine (Windows compatible)."""
    engine.say(text)
    engine.runAndWait()


def chat(query):
    """Handles conversational AI using GPT-3.5-Turbo."""
    global chatStr
    print(chatStr)

    # Update the conversation history
    chatStr += f"User: {query}\nJarvis: "

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        reply = response.choices[0].message.content
        say(reply)
        chatStr += f"{reply}\n"
        return reply

    except Exception as e:
        print(f"Error in chat: {e}")
        say("I apologize, I encountered an error connecting to the server.")
        return "Error"


def ai(prompt):
    """Generates a text file response for a specific prompt."""
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        reply = response.choices[0].message.content
        text += reply

        # Create directory if it doesn't exist
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # logic to create a safe filename
        try:
            # Try to split by "intelligence" if the user said it
            filename_part = prompt.split('intelligence')[1].strip()
        except IndexError:
            # Fallback if "intelligence" wasn't in the specific string
            filename_part = prompt[:20]

            # sanitize filename (remove characters that are illegal in Windows filenames)
        safe_filename = "".join([c for c in filename_part if c.isalpha() or c.isdigit() or c == ' ']).strip()

        with open(f"Openai/{safe_filename}.txt", "w") as f:
            f.write(text)

        say("I have saved the response to the OpenAI folder.")

    except Exception as e:
        print(f"Error in AI function: {e}")
        say("I could not save the file due to an error.")


def takeCommand():
    """Listens to microphone input."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I initialized")

    while True:
        query = takeCommand()

        # Stop processing if the listener failed
        if "Some Error Occurred" in query:
            continue

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # Feature: Play Music
        if "open music" in query.lower():
            # IMPORTANT: Change this path to a real MP3 file on YOUR computer
            musicPath = r"C:\Windows\Media\tada.wav"
            try:
                os.startfile(musicPath)  # Windows command to open file
            except Exception:
                say("I could not find the music file.")

        # Feature: Tell Time
        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {min} minutes")

        # Feature: Open Camera (Replaced FaceTime for Windows)
        elif "open facetime".lower() in query.lower():
            say("Opening Camera")
            os.system("start microsoft.windows.camera:")

        # Feature: Open Passky (Replaced with Notepad for testing)
        elif "open pass".lower() in query.lower():
            say("Opening Notepad")
            os.system("notepad")

        # Feature: Specific AI Prompt saving
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        # Feature: Quit
        elif "Jarvis Quit".lower() in query.lower():
            say("Goodbye sir")
            exit()

        # Feature: Reset Chat Memory
        elif "reset chat".lower() in query.lower():
            chatStr = ""
            say("Chat memory reset")

        # Default: Chat with AI
        else:
            print("Chatting...")
            chat(query)