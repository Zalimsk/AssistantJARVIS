import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr
from mpl_toolkits.mplot3d import Axes3D

class ScienceModelGenerator:
    def __init__(self):  # Corrected the constructor name
        self.models_created = []
        self.recognizer = sr.Recognizer()

    def create_molecular_structure(self):
        # Water molecule (H2O) ka 3D representation
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Oxygen aur Hydrogen ke coordinates
        oxygen = np.array([0, 0, 0])  # O origin par
        hydrogen1 = np.array([0.76, 0, 0])  # H1
        hydrogen2 = np.array([-0.76, 0, 0])  # H2

        # Plotting
        ax.scatter(*oxygen, color='red', s=100, label='Oxygen (O)')
        ax.scatter(*hydrogen1, color='blue', s=100, label='Hydrogen (H1)')
        ax.scatter(*hydrogen2, color='blue', s=100, label='Hydrogen (H2)')

        # Bonds ko represent karne wale lines
        ax.plot([oxygen[0], hydrogen1[0]], [oxygen[1], hydrogen1[1]], [oxygen[2], hydrogen1[2]], color='black')
        ax.plot([oxygen[0], hydrogen2[0]], [oxygen[1], hydrogen2[1]], [oxygen[2], hydrogen2[2]], color='black')

        ax.set_title('3D Molecular Structure of Water (H2O)')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        plt.legend()
        plt.savefig('molecular_structure.png')
        plt.close()
        self.models_created.append('3D Molecular Structure of Water created.')

    def save_explanation(self, file_name):
        explanation = """
        3D Model:
        Yeh model water (H2O) ka molecular structure dikhata hai.
        Ismein ek oxygen atom aur do hydrogen atoms hain.
        Laal sphere oxygen ko represent karta hai, aur neele spheres hydrogen atoms hain.
        Lines atoms ke beech ke bonds ko dikhate hain.
        """
        try:
            with open(file_name, 'w') as f:
                f.write(explanation)
                self.models_created.append(f'Explanation saved to {file_name}.')
        except Exception as e:
            self.models_created.append(f"Error saving explanation: {e}")

    def generate_models(self):
        self.create_molecular_structure()
        self.save_explanation('molecular_explanation.txt')

    def display_results(self):
        for result in self.models_created:
            print(result)

    def listen_for_commands(self):
        with sr.Microphone() as source:
            print("Listening for commands...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                print("Could not request results; check your network connection.")
                return ""

# Main loop
model_generator = ScienceModelGenerator()
while True:
    command = model_generator.listen_for_commands()
    if command:
        if "generate model" in command:
            model_generator.generate_models()
            model_generator.display_results()
        elif "exit" in command:
            print("Exiting the program.")
            break
