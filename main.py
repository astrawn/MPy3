import pyaudio
import wave
import os
import keyboard
import time
from pydub import AudioSegment

# files
src = "C:/Users/Alex Strawn/Desktop/Misc/We_Are_The_In_Crowd/Weird_Kids_[Explicit]/B0754LBQBT_(disc_1)_03_-_Manners.mp3"
dst = "C:/Users/Alex Strawn/Desktop/Manners.wav"

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

# Set chunk size of 1024 samples per data frame
chunk = 1024

# Open the sound file
wf = wave.open(dst, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    # allows pausing via keyboard spacebar press
    if keyboard.is_pressed('space') and stream.is_active():
        time.sleep(0.3)
        stream.stop_stream()
    elif keyboard.is_pressed('space') and stream.is_stopped():
        time.sleep(0.3)
        stream.start_stream()
        
    if stream.is_active():
        stream.write(data)
        data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
os.remove(dst)
p.terminate()
