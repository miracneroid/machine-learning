from assistant.utils import recognize_speech

def process_basic_commands(command):
    if "hello" in command.lower():
        return "Hello there!"
    else:
        return "Sorry, I don't understand that command."

def execute_basic_commands():
    user_command = recognize_speech()
    response = process_basic_commands(user_command)
    print(response)

