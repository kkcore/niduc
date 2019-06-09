import sys
from DataGenerator import DataGenerator
from Channel import Channel
from CoderDecoder import Coder, Decoder

if __name__ == '__main__':
        #Odebranie argumentów z javascriptu
        n=sys.argv[1]
        fx=sys.argv[2]
        f=sys.argv[3]
        codingType=sys.argv[4]
        errorRate=sys.argv[5]
        packetLength=sys.argv[6]
        datagen = DataGenerator()
        channel = Channel()
        coder = Coder()
        decoder = Decoder()
        sin = datagen.create_sin(n, fs, f)
        #sin = datagen.convert_y_to_bin(sin) 
        #sin = datagen.convert_y_from_bin(sin)
        # datagen.show_data(sin)
        sin = datagen.convert_y_to_bin(sin)
        sin = datagen.divideToPackets(sin, packetLength)
        #kod parzystosci, przeslanie jezeli bit sie nie zgadza to odeslanie pakietu
        if codingType == 'Bit kontrolny': 
                for i in range(len(sin)):
                sin[i][1] = coder.codeParrity(sin[i][1])
                sin[i][1] = channel.distort_packet(sin[i][1], errorRate)
                if(not decoder.decodeParrity(sin[i][1])):
                        i-=1
                        continue
        #kod hamminga, jezeli jakis bit sie nie zgadza korekcja pakietu, error_rate ustawiony na 4% zeby
        #zostal zepsuty tylko 1 bit
        # for i in sin:
        #         i[1] = coder.codeHamming(i[1])
        #         i[1] = channel.distort_packet(i[1], 4)
        #         i[1] = decoder.decodeHamming(i[1])
        #Zakodowanie dla roznej dlugosci pakietow
        if codingType == 'Kod Hamminga':
                for i in sin:
                        i[1] = coder.codeHamming(i[1])
                        i[1] = channel.distort_packet(i[1], errorRate)
                        
        #sin = datagen.convert_y_from_bin(sin)
        #datagen.show_data(sin)

        # distortedrandomly = channel.distort_randomly(sin,50)
        # datagen.show_data(distortedrandomly)
