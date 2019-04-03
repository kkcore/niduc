import numpy as np
import struct
import wave
import matplotlib.pyplot as plt
import random

class DataGenerator:
    def create_sin(self): 
        n = random.randint(100,100001)
        fs = random.randint(100,10001)
        f = random.randint(1,50)
        x = np.arange(n)
        y = np.sin(2* np.pi * f * (x/fs))
        return (x,y)
    
    def show_data(self, sin):
        plt.plot(sin[0], sin[1])
        plt.show()
        