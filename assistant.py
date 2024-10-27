import os
import time
import subprocess
from datetime import datetime
from playsound import playsound
from vosk import Model, KaldiRecognizer

# Set the path to the model directory
model_path = '/Users/valentinavasiliu/PycharmProjects/AIASSIS/smallmodel'

# Load the Vosk model
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Function to play a start sound
def play_start_sound():
    start_sound_path = '/Users/valentinavasiliu/PycharmProjects/AIASSIS/start.mp3'
    if os.path.exists(start_sound_path):
        playsound(start_sound_path)

# Function to determine greeting based on the time of day
def get_time_based_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Function to introduce Max and his protective nature
def introduce_yourself():
    # Start with greeting and introduction
    play_start_sound()
    time.sleep(2)
    greeting = get_time_based_greeting()
    speak(greeting)

    intro_message = (
        "Hey there! I'm Max, your cybersecurity assistant. "
        "I was created with the purpose to help people with little to no knowledge of cybersecurity, "
        "so you can feel more safe while using the internet. "
        "With all the current breaches, we all just want to browse online without being compromised."
    )
    speak(intro_message)

    # Demonstrate Brave search for current data breaches
    search_current_breaches()

    # Demonstrate email check functionality
    demo_email = "john@gmail.com"
    check_email_compromised(demo_email)

    # Close Brave after both demonstrations
    os.system("pkill 'Brave Browser'")
    print("Closed Brave.")

    # Demonstrate VPN opening and description
    open_proton_vpn()

    # Demonstrate Malwarebytes opening and description
    open_malwarebytes()

    # Conclude introduction
    conclusion_message = (
        "Feel free to ask me questions or give me commands anytime. "
        "Thank you for using my services"
    )
    speak(conclusion_message)

# Function to speak text using system TTS
def speak(text):
    try:
        subprocess.call(["say", "-v", "Daniel", text])
    except Exception as e:
        print(f"Error in speech synthesis: {e}")

# Function to open a URL in Brave browser for demonstrations
def open_url_in_brave(url, message):
    try:
        print(f"Opening Brave to search: {url}...")
        subprocess.Popen(
            ["/Applications/Brave Browser.app/Contents/MacOS/Brave Browser", "--new-tab", url],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        time.sleep(0.5)
        speak(message)
        time.sleep(3)
    except Exception as e:
        print(f"Error opening Brave: {e}")

# Function to demonstrate Brave search for current data breaches
def search_current_breaches():
    url = "https://www.google.com/search?q=current+data+breaches"
    message = (
        "I’m capable of checking current online breaches so I can always implement new ways to protect you."
    )
    open_url_in_brave(url, message)

# Function to open ProtonVPN for secure browsing
def open_proton_vpn():
    try:
        print("Opening ProtonVPN for secure browsing...")
        subprocess.Popen(["/Applications/ProtonVPN.app/Contents/MacOS/ProtonVPN"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.5)
        speak("I can launch a VPN for you. It helps keep your online activities private.")
        time.sleep(2)
        os.system("pkill 'ProtonVPN'")
        print("Closed ProtonVPN.")
    except Exception as e:
        print(f"Error opening or closing ProtonVPN: {e}")

# Function to check if an email has been compromised
def check_email_compromised(email):
    try:
        print(f"Checking if {email} has been compromised...")
        url = f"https://haveibeenpwned.com/account/{email}"
        message = (
            f"I can check if your email, {email}, has been involved in any breaches. "
            "It's a smart way to stay alert."
        )
        open_url_in_brave(url, message)
    except Exception as e:
        print(f"Error checking email {email}: {e}")

# Function to open Malwarebytes for malware protection
def open_malwarebytes():
    try:
        print("Opening Malwarebytes for malware protection...")
        subprocess.Popen(
            ["/Applications/Malwarebytes.app/Contents/MacOS/Malwarebytes"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        time.sleep(1)
        speak("I can check your device for malware to keep it clean and safe.")
        time.sleep(3)
        os.system("pkill 'Malwarebytes'")
        print("Closed Malwarebytes.")
    except Exception as e:
        print(f"Error opening or closing Malwarebytes: {e}")

# Function to listen for terminal commands
def listen_for_terminal_commands():
    while True:
        command = input("Type a command: ").strip().lower()
        if command == "max introduce yourself":
            introduce_yourself()
        elif command.startswith("max check email"):
            email = command.split(" ")[-1]
            check_email_compromised(email)
        elif command == "max open vpn":
            open_proton_vpn()
        elif command == "max open malwarebytes":
            open_malwarebytes()
        elif command in ["stop", "exit", "max exit"]:
            print("Stopping the assistant...")
            speak("Goodbye! Remember, I'm here to help whenever you need me.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    # Start listening for terminal commands
    listen_for_terminal_commands()