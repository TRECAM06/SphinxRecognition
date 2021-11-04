import pyaudio
import wave
import sys
import shutil
from scipy.io.wavfile import write


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "C:/Users/infin/OneDrive/Desktop/Vectors/DDK/output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

play=pyaudio.PyAudio()
stream_play=play.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      output=True)
for data in frames: 
    stream_play.write(data)
    

stream_play.stop_stream()
stream_play.close()
play.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
"""
with wave.open('C:/Users/infin/OneDrive/Desktop/Vectors/DDK/output.wav') as fd:
    params = fd.getparams()
    frames = fd.readframes(1000000) # 1 million frames max
with wave.open('C:/Users/infin/OneDrive/Desktop/Vectors/DDK/Comp.wav') as nd:
    params2 = nd.getparams()
    frames2 = nd.readframes(100000) 

print(frames-frames2)"""