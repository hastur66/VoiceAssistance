import speech_recognition as sr

class Sttengine:
    '''
    Speech-to-text conversion
    '''

    def __init__(self) -> None:
        pass


    def recordAudiotoString():
        """
        convert audio to string

        Returns
        ----------
        string
            text output
        """

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Say something')
            audio = r.listen(source)

        text = ''
        try:
            text = r.recognize_google(audio)
            print('You said ' + text)
        except sr.UnknownValueError:
            print('Audio cannot be recognized!')
        except sr.RequestError as e:
            print('Service error')

        return text
        

    def invokeWord(word):
        """
        special word for invocation

        Parameters
        ----------
        word
            input word
        Returns
        ----------
        string
            text output
        """

        data = recordAudiotoString() 

        # for w in data:
        #     if word in w:
        #         return True
        return [ word in w for w in data]