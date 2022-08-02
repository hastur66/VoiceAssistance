import sttengine
import ttsengine
from googlesearch import search
import wikipedia

text = sttengine.Sttengine.recordAudiotoString()

def google(text):
    result = search('text', num_results=3)

def wiki(text):
    result = wikipedia.search(text)

def select_source(text):
    utter = sttengine.Sttengine.invokeWord(text)

    if utter[0] == 'google':
        output = google(text)
    elif utter[0] == 'wikipedia':
        output = wiki(text)
    else:
        pass

    return output

def speak_output(text):
    output = select_source(text)
    voice = ttsengine.TTSengine.response(output)
    return voice

def main():
    return speak_output(text)

if __name__=='__main__':
    main()