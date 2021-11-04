import speech_recognition as sr
import pocketsphinx
r = sr.Recognizer()

audio_file = sr.AudioFile('C:/Users/infin/OneDrive/Desktop/Vectors/DDK/output.wav')

with audio_file as source: 
   r.adjust_for_ambient_noise(source) 
   audio = r.record(source)
#result = r.recognize_google(audio, key="AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8", language='en-US', show_all=True)
result = r.recognize_sphinx(audio, language='en-Us')

with open('test.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   print(result, "k")
   file.write(result) 
   print("ready!")



print(pocketsphinx)