import speech_recognition as sr
import pyttsx3

# 1. Initialize the Text-to-Speech Engine
engine = pyttsx3.init()

# OPTIONAL: Change Voice (0 = Male, 1 = Female usually)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Changing index to 1 often selects a female voice
engine.setProperty('rate', 170) # Speed of speech

def speak(text):
    """Makes the computer speak the text."""
    print(f"🤖 Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the microphone and returns text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎤 Listening... (Speak now)")
        # Adjust for ambient noise (wait 1 sec to measure background silence)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Listen for audio
            audio = recognizer.listen(source, timeout=5)
            print("⏳ Recognizing...")
            
            # Convert audio to text using Google's API
            query = recognizer.recognize_google(audio)
            print(f"👤 You: {query}")
            return query.lower()
            
        except sr.WaitTimeoutError:
            return "" # No speech detected
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError:
            print("❌ Internet connection failed")
            return ""

# --- MAIN LOOP ---
if __name__ == "__main__":
    speak("Hello! I am ready. Say something.")

    while True:
        command = listen()

        if command:
            if "hello" in command:
                speak("Hi there! How can I help?")
            
            elif "who are you" in command:
                speak("I am Jarvis Lite, your Python assistant.")

            elif "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            
            else:
                speak(f"You said: {command}")