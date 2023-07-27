# select audio input
# save to mp3
# monitor levels
# monitor elapsed time

import pyaudio
import wave
from tkinter import (
    filedialog as fd,
    ttk,
    StringVar,
    IntVar,
    Tk,
    OptionMenu
)
from threading import Event

# Global Variables
chunk = 1024
bitrate = pyaudio.paInt16
channels = 1
samplerate = 44100
filename = "sample.wav"
record = bool
p = pyaudio.PyAudio()

def start():
    record = True

    if record == True:
        print("Recording")

        stream = p.open(
            format=bitrate,
            channels=channels,
            rate=samplerate,
            frames_per_buffer=chunk,
            input=True
        )

        frames = []

        while record == True:
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Finished")

        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(bitrate))
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))
        wf.close()
    

def stop():
    record = False

# UI
window = Tk()
window.title("Simple Recorder")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
mainframe = ttk.Frame(window, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky='N S E W')

var = StringVar()
vals = ["obj1", "obj2", "obj3"]
options = OptionMenu(mainframe, variable=var, value="test").grid(column=0, row=0)
ttk.Button(mainframe, text="START", command=start).grid(column=0, row=1)
ttk.Button(mainframe, text="STOP", command=stop).grid(column=0, row=2)

window.mainloop()
