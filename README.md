# second-project
Voice Assistant 
Jarvis A.I. Voice Assistant
Jarvis is a Python-based virtual assistant inspired by Iron Man's AI. It uses speech recognition to take commands, a text-to-speech engine to respond, and the OpenAI GPT-3.5-Turbo model to handle complex conversations and generate intelligent content.

🚀 Features
Voice Interaction: Recognizes speech via Google Speech Recognition and responds using pyttsx3.

Conversational AI: Remembers the context of your current conversation for a natural chat experience.

Smart Content Generation: Ask Jarvis to write something "Using artificial intelligence," and it will save the full response to a text file in a local folder.

Web Automation: Quick voice commands to open YouTube, Google, and Wikipedia.

System Controls: Open the camera, Notepad, or play music directly via voice command.

Time Reporting: Provides the current time on demand.

Memory Management: Reset the AI's conversation memory at any time by saying "Reset chat."

🛠 Prerequisites
Before running the project, ensure you have:

Python 3.8+ installed.

An OpenAI API Key.

A working Microphone and Speakers.

📦 Installation
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
Install required libraries:

Bash

pip install speechrecognition pyttsx3 openai
Note: Depending on your OS, you may also need to install pyaudio. For Windows, use pip install pipwin then pipwin install pyaudio.

Setup Configuration: Create a file named config.py in the root directory and add your OpenAI API key:

Python

apikey = "YOUR_OPENAI_API_KEY_HERE"
🎮 Usage
Run the main script:

Bash

python main.py
Common Voice Commands:
Chatting: Just speak naturally to chat with the AI.

Websites: "Open YouTube", "Open Google", "Open Wikipedia".

Apps: "Open Notepad", "Open FaceTime" (Opens Windows Camera).

AI Writing: "Using artificial intelligence, write an essay on [topic]" (Saves to Openai/ folder).

Control: "Reset chat", "What's the time", "Jarvis Quit".

📂 Project Structure
main.py: The core logic for speech recognition, command processing, and AI interaction.

config.py: Stores your sensitive API keys (ensure this is in your .gitignore).

Openai/: Automatically generated directory where AI-written text files are saved.

⚠️ Important Note for Windows Users
The music player feature is currently set to a default Windows sound path: C:\Windows\Media\tada.wav. To play your own music, update the musicPath variable in main.py to point to your local .mp3 or .wav files.
