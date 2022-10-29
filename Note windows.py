import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def main():
    try:
        
        with sr.Microphone() as mic:
            f = open('note.txt','a+')
            r.adjust_for_ambient_noise(mic,duration = 2)
            audio = r.listen(mic)
            print("Listining")
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
                print("running the program again)")
                main()
    except sr.UnknownValueError():

        r = sr.Recognizer()
        main()
main()
        
        
        
