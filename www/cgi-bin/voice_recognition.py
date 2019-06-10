import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('say keyword to open portal')
    audio = r.listen(source)


try:
    x =  r.recognize_google(audio)
    print x
    webbrowser.open_new_tab('http://192.168.43.228/a.html')
    
except:
    pass
