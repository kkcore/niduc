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
datagen.show_data(sin)
sin = datagen.convert_y_to_bin(sin) 
for i, item in enumerate(sin):  
    item[1] = coder.codeParrity(item[1])
    item[1] = channel.distort_packet(item[1], 50)
    if(not decoder.decodeParrity(item[1])):
        i-=1
        continue
sin = datagen.convert_y_from_bin(sin)
datagen.show_data(sin)

# distortedrandomly = channel.distort_randomly(sin,50)
# datagen.show_data(distortedrandomly)
