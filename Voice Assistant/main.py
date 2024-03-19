import speech_recognition as sr
import spacy
import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from assistant.basic_commands import process_basic_commands
from assistant.nlp_processing import process_nlp
from assistant.task_automation import perform_task
from assistant.user_interaction import start_voice_assistant

# Initialize spaCy for NLP
nlp = spacy.load("en_core_web_sm")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""

def process_advanced_commands(command):
    doc = nlp(command)
    if "send email" in command:
        send_email()
    elif "weather" in command:
        city = extract_city_from_command(doc)
        get_weather(city)
    else:
        return "Sorry, I don't understand that command."

def extract_city_from_command(doc):
    # Extract the city from the user's command using spaCy's named entity recognition (NER)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geo-Political Entity, often used for cities
            return ent.text
    return "city"  # Default city if not specified

def send_email():
    # Configure your email server and credentials
    smtp_server = "your_smtp_server"
    port = 587
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@gmail.com"
    password = "your_email_password"

    # Compose the email
    subject = "Subject: Test Email from Voice Assistant"
    body = "This is a test email sent by your voice assistant."
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain'))
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Connect to the email server and send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email sent successfully!")

def get_weather(city):
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = 'your_api_key'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    # Make the API request
    response = requests.get(base_url)
    weather_data = response.json()

    # Extract and display relevant weather information
    if weather_data['cod'] == '404':
        print(f"City not found: {city}")
    else:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Weather in {city}: {temperature}°C, {description}")

# Example usage:
user_command = recognize_speech()
if user_command:
    process_advanced_commands(user_command)
