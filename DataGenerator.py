import numpy as np
import matplotlib.pyplot as plt
import random
import struct

class DataGenerator:
    def create_sin(self): 
        n = random.randint(100,5001)
        fs = random.randint(100,5001)
        f = random.randint(1,50)
        x = np.arange(n)
        y = np.sin(2* np.pi * f * (x/fs))
        signal = [list(x) for x in list(zip(x,y))]
        return signal
    
    def show_data(self, signal):
        plt.plot(*zip(*signal))
        plt.show()

    def convert_y_to_bin(self, signal):
        for i in signal:
            i[1] = format(struct.unpack('!I', struct.pack('!f', i[1]))[0], '032b')
        return signal


    def convert_y_from_bin(self, signal):
        for i in signal:
            i[1] = struct.unpack('!f',struct.pack('!I', int(i[1], 2)))[0]
        return signal
        