import sounddevice as sd
import numpy as np
import soundfile as sf
import os
filename = r"C:\Users\Owner\Documents\Sound recordings\hello.wav"
data,fs=sf.read(filename,dtype='float')
sd. play(data,fs)
sd.wait()
