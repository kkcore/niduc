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

    def distort_packet(self, packet, error_rate):  
        numberOfErrors = int((len(packet) * error_rate)/100)
        randomindexes = random.sample(range(len(packet)), numberOfErrors)
        for i in randomindexes:
            if (int(packet[i]) == 1):
                packet = packet[:i] + packet[i].replace('1', '0') + packet[(i+1):]
            else:
                packet = packet[:i] + packet[i].replace('0', '1') + packet[(i+1):]
        return packet
        





