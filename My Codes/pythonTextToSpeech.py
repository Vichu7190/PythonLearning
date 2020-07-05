"""
Created on Sun Jul  5 15:01:50 2020

@author: Viswanathan A
Learning Objectives
1. Recognize Speech and convert to text
2. Convert Speech to Text
3. Writing a simple function

"""

import speech_recognition as sr
import gtts
from playsound import playsound
import os

#Fuction to Convert Text to Speech

def speakOutLoad(textTOSpeak="It was Nice Talking to You",Name=''):
    toSpeak=str(textTOSpeak) +str(Name)
    tts=gtts.gTTS(toSpeak,slow = False)
    tts.save(FileName)
    playsound(FileName)
    os.remove(FileName)

#Function Convert Speech to Text
  
def virtualAssist(questionToAsk,Salutation="Hello"):
    text=''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(questionToAsk)
        #Speak out Loud the Question
        speakOutLoad(questionToAsk)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            NewText=str(Salutation) +str(text)
            print("You Said : {}".format(text))
            #Speak out Loud the Answer
            speakOutLoad(NewText)
        except:
            print("Sorry could not recognize what you said")
            speakOutLoad("Sorry could not recognize what you said")
   if text:
        return text


#Save the Speech as a Sound File and Remove Before every run of the Code
        
FileName="SoundFile.mp3"        
if os.path.exists(FileName):
    os.remove(FileName)
    
#Ask the First Question to the User..
QuestionToAsk="What is Your Name?"
UserAnswer =virtualAssist(QuestionToAsk)
if UserAnswer:
    NextQuestion="How Old are You " + str(UserAnswer)
    MyNextAnswer = virtualAssist(NextQuestion,"Your Age is ")
    if MyNextAnswer:
        speakOutLoad("Good Bye" +str(UserAnswer)+"Have a Good Day")
    else :
        speakOutLoad(Name=UserAnswer)
        print("Bye")
else :
    speakOutLoad()
    print("Bye")
