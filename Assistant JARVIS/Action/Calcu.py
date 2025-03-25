from Body.Advance_speak import speak
from Body.Speech_to_Text import listen



def calculate(command):
    try:
        # Extract calculation expression from the command and evaluate
        expression = command.split("calculate ")[1]
        result = eval(expression)
        speak(f"Result of '{expression}': {result}")
    except Exception as e:
        speak(f"Error calculating: {e}")

def calcul():
    if "calculate" in command:
        calculate(command)

if __name__ == "__main__":
    while True:
        command = listen()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            calcul(command)