import speech_recognition as sr
import pyttsx3
import smtplib
import requests

# Initialize the recognizer and synthesizer
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    synthesizer.say(text)
    synthesizer.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Function to send an email
def send_email(to_address, subject, body):
    from_address = "mansid.aiml21@sbjit.edu.in"
    password = "Pass@12345"
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(from_address, to_address, message)
        server.quit()
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email.")

# Function to get weather updates
def get_weather(city):
    api_key = "8d5f1da7a0a45365e83b13e5758fdfc0"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(base_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_description = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature - 273.15:.2f} degrees Celsius with {weather_description}.")
    else:
        speak("City not found.")

# Function to handle user commands
def handle_command(command):
    if "send email" in command:
        speak("To whom should I send the email?")
        to_address = listen()
        speak("What should be the subject?")
        subject = listen()
        speak("What should I say in the email?")
        body = listen()
        send_email(to_address, subject, body)
    
    elif "weather" in command:
        speak("Which city's weather would you like to know?")
        city = listen()
        get_weather(city)
    
    elif "set reminder" in command:
        # Implementation for setting reminder
        speak("This feature is not yet implemented.")
    
    elif "control" in command and "device" in command:
        # Implementation for controlling smart home devices
        speak("This feature is not yet implemented.")
    
    else:
        speak("Sorry, I can't help with that.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you today?")
    
    while True:
        command = listen()
        if command:
            handle_command(command)
