from DataGenerator import DataGenerator
from Channel import Channel
from CoderDecoder import Coder, Decoder

datagen = DataGenerator()
channel = Channel()
coder = Coder()
decoder = Decoder()
sin = datagen.create_sin()
sin = datagen.convert_y_to_bin(sin) 
sin = datagen.convert_y_from_bin(sin)
# datagen.show_data(sin)
sin = datagen.convert_y_to_bin(sin)
sin = datagen.divideToPackets(sin, 128)
#kod parzystosci, przeslanie jezeli bit sie nie zgadza to odeslanie pakietu 
# for i in range(len(sin)):
#     sin[i][1] = coder.codeParrity(sin[i][1])
#     sin[i][1] = channel.distort_packet(sin[i][1], 4)
#     if(not decoder.decodeParrity(sin[i][1])):
#         i-=1
#         continue
#kod hamminga, jezeli jakis bit sie nie zgadza korekcja pakietu, error_rate ustawiony na 4% zeby
#zostal zepsuty tylko 1 bit
for i in sin:
        i[1] = coder.codeHamming(i[1])
        i[1] = channel.distort_packet(i[1], 4)
        i[1] = decoder.decodeHamming(i[1])
#Zakodowanie dla roznej dlugosci pakietow
sin = datagen.convert_y_from_bin(sin)
datagen.show_data(sin)

# distortedrandomly = channel.distort_randomly(sin,50)
# datagen.show_data(distortedrandomly)
