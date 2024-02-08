import speech_recognition as sr
import subprocess
import os
import requests

r = requests.get(audiofle)

AudioFile = sr.AudioFile('example.mp4')

# open the file
with open("example.mp4", "wb") as handle:

    for data in r.inter_content():
        handle.write(mp4fil.read())

cmdline =['avconv', '-i', 'example.mp4', '-vn', '-f', 'wv', 'output.wav']
subprocess.call(cmdline)

r = sr.Recognizer()
with sr.AudioFile('example.mp4') as source:
    audio = r.record(source)

command = r.recognise_google(audio)
print(command)

