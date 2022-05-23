from gtts import gTTS
import os

class TTSengine:

    def __init__(self) -> None:
        pass

    def response(inputtext):
        obj = gTTS(text=inputtext, lang='en', slow=False)
        obj.save('assistant_response.mp3')
        os.system('afplay assistant_response.mp3')