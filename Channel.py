import numpy as np 
import random

class Channel:
    def distort_regularly(self, signal, error_rate):
        numberOfErrors = (len(signal) * error_rate)/100
        errorFreq = int(len(signal)/numberOfErrors)
        for i in range(0, len(signal), errorFreq):
            signal[i][1] = random.uniform(0, 1)
        return signal

    def distort_randomly(self, signal, error_rate):
        numberOfErrors = int((len(signal) * error_rate)/100)
        randomindexes = random.sample(range(0,(len(signal)-1)), numberOfErrors)
        for i in randomindexes:
            signal[i][1] = random.uniform(0, 1)
        return signal



