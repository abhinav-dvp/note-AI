import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def main():
    with sr.Microphone() as mic:
        f = open('note.txt','a+')
        r.adjust_for_ambient_noise(mic,duration = 2)
        audio = r.listen(mic)
        text = r.recognize_google(audio)
        text = text.lower()       
        if 'stop' in text :
            print("terminating")
            #f.close()
        else:
            L = text + '.'+'\n'
            f.write(L)
            f.close()
            main()
main()
        
        
