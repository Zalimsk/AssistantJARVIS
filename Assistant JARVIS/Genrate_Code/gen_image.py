import requests
from Body.Advance_speak import speak
from Body.Recognizing import takecommand
from PIL import Image
from io import BytesIO


def generate_image(text):
    speak("Sir, I generate the image in 3D. You just tell the name of the image.")
    Image_Name = takecommand()
    url = 'https://api.airforce/v1/imagine2'
    params = {'prompt': Image_Name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        speak("What do you call saving this 3D image?")
        path1name = takecommand() + ".png"
        path1 = "J:\\Assistant JARVIS\\Data Provided by JARVIS\\ScreenShot By JARVIS\\Genrate_Image\\"+ path1name
        image.save(path1)
        #image.show('J:\\Assistant JARVIS\\generated_image.png')
        speak(f"Sir, The generated 3D image named {path1name} has been successfully saved.")
        #print('Image saved as generated_image.png')
        
    else:
        print(f'Failed to retrieve image. Status code: {response.status_code}')
