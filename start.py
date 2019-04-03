from DataGenerator import DataGenerator
from Channel import Channel
datagen = DataGenerator()
channel = Channel()
sin = datagen.create_sin()
datagen.show_data(sin)
distortedrandomly = channel.distort_randomly(sin,50)
datagen.show_data(distortedrandomly)
