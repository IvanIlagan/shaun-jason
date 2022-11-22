import keyboard
import math
from random import random
import simpleaudio


while True:
    if keyboard.is_pressed('x'):
        shaun_jason = ["Shaun", "Jason"]
        sound = simpleaudio.WaveObject.from_wave_file(f"./assets/{shaun_jason[ math.floor((random() *  2))]}{math.floor((random() *  3) + 1)}.wav")
        sound.play().wait_done()
