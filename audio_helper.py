import pyttsx3

class PlayAudio:
    def __init__(self,voice='male',speakstatus=True):
        self.voice='male'
        self.speakstatus=speakstatus
        self.speakWords={
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',
            '0':'zero',
            '+':'plus',
            '-':'minus',
            '*':'multiply',
            '/':'divide',
            '=':'equal to'

        }
        self.engine=pyttsx3.init()
        v=self.engine.getProperty('voices')
        self.engine.setProperty('voices',v[0].id)

    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()





if __name__=='__main__':
    ob=PlayAudio()
    ob.speak('1')