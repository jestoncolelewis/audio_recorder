# select audio input
# save to mp3
# monitor levels
# monitor elapsed time

import sounddevice as sd
import numpy as np
import wave
from tkinter import (
    filedialog as fd,
    ttk,
    StringVar,
    IntVar,
    Tk,
    OptionMenu
)

# Global Variables
chunk = 1024
channels = 1
samplerate = 44100
filename = "sample.wav"
record = bool

def start():
    record = True

    if record == True:
        print("Recording")

        frames = []

        print("Finished")

        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
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
devices = sd.query_devices()
var.set(devices[0]["name"])
options = OptionMenu(mainframe, var, *devices).grid(column=0, row=0)
ttk.Button(mainframe, text="START", command=start).grid(column=0, row=1)
ttk.Button(mainframe, text="STOP", command=stop).grid(column=0, row=2)

window.mainloop()
