from assistant.basic_commands import execute_basic_commands
from assistant.nlp_processing import process_nlp
from assistant.task_automation import perform_task

def start_voice_assistant():
    print("Voice Assistant: Ready for commands...")

    while True:
        user_input = input("Type 'exit' to quit or say something: ")
        
        if user_input.lower() == 'exit':
            break

        # Simulate speech recognition for simplicity
        user_command = user_input.lower()

        # Basic Commands
        if "hello" in user_command:
            print("Voice Assistant: Hello there!")
        else:
            # NLP Processing
            processed_query = process_nlp(user_command)
            print(processed_query)

            # Task Automation
            task_result = perform_task(processed_query)
            print(task_result)
