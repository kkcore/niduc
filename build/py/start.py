import sys
from DataGenerator import DataGenerator
from Channel import Channel
from CoderDecoder import Coder, Decoder
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parrityBitTest(sin):
        channel = Channel()
        decoder = Decoder()
        coder = Coder()
        sentAgain = 0
        sent = 0 
        i = 0
        originalSin = []
        timeOut = 0
        err = 0
        resent = False
        while i < len(sin):
                sent+=1
                originalPacket = sin[i]
                sin[i] = coder.codeParrity(sin[i])
                if resent is False:
                        originalSin.append(sin[i])
                sin[i] = channel.distort_packet(sin[i], errorRate)
                resent = False
                if(not decoder.decodeParrity(sin[i])):
                        sentAgain+=1
                        resent = True
                        timeOut+=1
                        if timeOut >= 100:
                                resent = False
                                timeOut = 0
                                i+=1
                                continue
                        sin[i] = originalPacket                        
                        continue
                else:
                        i+=1
                        continue
        k = 0
        while k < len(sin):
                if sin[k] != originalSin[k]:
                        err+=1
                k+=1        
        res = dict()
        res['numberOfErrors'] = err
        res['percentageOfErrors'] = (err/ len(originalSin)) * 100
        res['sent'] = sent
        res['sentAgain'] = sentAgain
        return res

def hammingCodeTest(sin):
        channel = Channel()
        decoder = Decoder()
        coder = Coder()
        sentAgain = 0
        sent = 0 
        i = 0
        timeOut = 0
        originalSin = []
        resent = False
        err = 0
        while i  < len(sin):
                sent+=1
                originalPacket = sin[i]
                sin[i] = coder.codeHamming(sin[i])
                if resent is False:
                        originalSin.append(sin[i])
                sin[i] = channel.distort_packet(sin[i], errorRate)
                resent = False
                if (not decoder.decodeHamming(sin[i])):
                        sentAgain+=1
                        timeOut+=1
                        resent = True
                        if timeOut >= 100:
                                resent = False
                                timeOut = 0
                                i+=1
                                continue
                        sin[i] = originalPacket
                        continue
                else:
                        i+=1
                        continue
        k = 0
        while k < len(sin):
                if sin[k] != originalSin[k]:
                        err+=1
                k+=1   
        res = dict()
        res['numberOfErrors'] = err
        res['percentageOfErrors'] = (err/ len(originalSin)) * 100
        res['sent'] = sent
        res['sentAgain'] = sentAgain
        return res

def crcCodeTest(sin):
        channel = Channel()
        decoder = Decoder()
        coder = Coder()
        sentAgain = 0
        sent = 0 
        i = 0
        timeOut = 0
        originalSin = sin[:]
        while i < len(sin):
                sent+=1
                originalPacket = sin[i]
                remainder = coder.crc_remainder(sin[i], '1011', '0')
                sin[i] = channel.distort_packet(sin[i], errorRate)
                if (not decoder.crc_check(sin[i], '1011', remainder)):
                        sin[i] = originalPacket
                        sentAgain+=1
                        timeOut+=1
                        if timeOut >= 100:
                                timeOut = 0
                                i+=1
                        continue
                else:
                        i+=1
                        continue
        k = 0
        err = 0
        while k < len(sin):
                if sin[k] != originalSin[k]:
                        err+=1
                k+=1  
        res = dict()
        res['numberOfErrors'] = err
        res['percentageOfErrors'] = (err/ len(originalSin)) * 100
        res['sent'] = sent
        res['sentAgain'] = sentAgain
        return res

def generateData(n, fs, f):
        sin = datagen.create_sin(n, fs, f)
        sin = datagen.convert_y_to_bin(sin)
        return sin

if __name__ == '__main__':
        # Odebranie argumentów z javascriptu (zakomentuj jeśli używasz samego Pythona)
        # ----------------------------
        n = int(sys.argv[1])
        fs = int(sys.argv[2])
        f = int(sys.argv[3])
        codingType = sys.argv[4]
        errorRate = int(sys.argv[5])
        packetLength = int(sys.argv[6])
        appType = sys.argv[7]
        # -------------------------
        # Przypisanie argumentów w Pythonie (zakomentuj jeśli używasz klienta)
        # -----------------------------------------
        # n = 10
        # fs = 25
        # f = 25
        # codingType = 'Bit kontrolny'
        # errorRate = 30
        # packetLength = 15
        # appType = 'Test'
        # --------------------------------------------------------
        datagen = DataGenerator()
        res = dict()
        res['sent'] = 0
        res['sentAgain'] = 0
        res['numberOfErrors'] = 0
        if appType == 'Test':
                sin = generateData(n ,fs, f)
                sin = datagen.divideToPackets(sin, packetLength)
                if codingType == 'Bit kontrolny': 
                        res = parrityBitTest(sin)
                if codingType == 'Kod Hamminga':        
                        res = hammingCodeTest(sin)
                if codingType == 'Kod CRC':
                        res = crcCodeTest(sin)
                print(str(res['sent'])+' '+str(res['sentAgain'])+' '+str(res['numberOfErrors']))
        else:
                n = 100
                pbResults = 0
                hammingResults = 0
                crcResults = 0
                nArr = []
                kArr = []
                pbArr = []
                hcArr = []
                crcArr = []
                # while n <= 500:       z tego można zrobić dobry wykres 2d.
                #         nArr.append(n)
                #         packetLength = 2
                #         sin = generateData(n, fs, f)
                #         while packetLength <= 128:
                #                 kArr.append(packetLength)
                #                 diffPacketLenSin = datagen.divideToPackets(sin, packetLength)
                #                 copy = diffPacketLenSin[:]
                #                 pbResults = parrityBitTest(diffPacketLenSin)
                #                 pbArr.append(pbResults['percentageOfErrors'])
                #                 diffPacketLenSin = copy[:]
                #                 hammingResults = hammingCodeTest(diffPacketLenSin)
                #                 hcArr.append(hammingResults['percentageOfErrors'])
                #                 diffPacketLenSin = copy[:]
                #                 crcResults = crcCodeTest(diffPacketLenSin)
                #                 crcArr.append(crcResults['percentageOfErrors'])
                #                 packetLength *= 2
                #         n += 100
                packetLength = 2                
                while n <= 200: #oryginalnie 500
                        nArr.append(n)
                        sin = generateData(n, fs, f)
                        kArr.append(packetLength)
                        diffPacketLenSin = datagen.divideToPackets(sin, packetLength)
                        copy = diffPacketLenSin[:]
                        pbResults = parrityBitTest(diffPacketLenSin)
                        pbArr.append(pbResults['percentageOfErrors'])
                        diffPacketLenSin = copy[:]
                        hammingResults = hammingCodeTest(diffPacketLenSin)
                        hcArr.append(hammingResults['percentageOfErrors'])
                        diffPacketLenSin = copy[:]
                        crcResults = crcCodeTest(diffPacketLenSin)
                        crcArr.append(crcResults['percentageOfErrors'])
                        packetLength *= 2
                        n += 100
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(nArr, kArr, pbArr, c='r', marker='^', label='Bit parzystości')
                ax.scatter(nArr, kArr, hcArr, c='g', marker='o', label='Kod Hamminga')
                ax.scatter(nArr, kArr, crcArr, c='b', marker='X', label='Kod CRC')
                ax.set_xlabel('Liczba bitów')
                ax.set_ylabel('Długość pakietu')
                ax.set_zlabel('Efektywność')
                plt.legend(loc='best')
                plt.savefig('wykres.png')
                plt.show()
                        