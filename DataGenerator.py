import numpy as np
import matplotlib.pyplot as plt
import random

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
        