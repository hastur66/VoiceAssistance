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
        google(text)
    elif utter[0] == 'wikipedia':
        wiki(text)
    else:
        pass

def main():
    pass

if __name__=='__main__':
    main()