import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def speech_to_text():
    try:       
        with sr.Microphone() as mic:
            f = open('note0.txt','a+')
            r.adjust_for_ambient_noise(mic,duration = 1.3)
            print("Listining")
            audio = r.listen(mic)   
            text = r.recognize_google(audio)
            text = text.lower()       
            if 'stop' in text :
                print("terminating")
            else:
                print ("Stop not found")
                print("Writing down")
                L = text + '.'+'\n'
                f.write(L)
                f.close()
                print("running the program again")
                speech_to_text()
    except sr.UnknownValueError():
        speech_to_text()
speech_to_text()
        
        
        
