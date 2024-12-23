import speech_recognition as sr

# Task list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted successfully.")
    else:
        print(f"Task '{task}' not found.")

def show_tasks():
    if tasks:
        print("Here are your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("You have no tasks.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
        return ""

def process_command(command):
    if "add task" in command:
        task = command.replace("add task", "").strip()
        add_task(task)
    elif "delete task" in command:
        task = command.replace("delete task", "").strip()
        delete_task(task)
    elif "show tasks" in command:
        show_tasks()
    elif "exit" in command:
        print("Exiting Task Manager. Goodbye!")
        return False
    else:
        print("Command not recognized. Please try again.")
    return True

def main():
    print("Welcome to Voice-Activated Task Manager!")
    print("Commands: 'Add task [task]', 'Delete task [task]', 'Show tasks', 'Exit'")
    
    running = True
    while running:
        command = recognize_speech()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()
