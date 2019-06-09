import sys
from CoderDecoder import Coder, Decoder
from DataGenerator import DataGenerator
from Channel import Channel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    # coder = Coder()
    # decoder = Decoder()
    # coder.codeHamming('10011010')
    # wError = '011100101110'
    # decoder.decodeHamming(wError)
    # a = [1,2,3,4,15,13,5]
    # b = [3,2,3,5,2,14,12]
    # c = [1,2,3,4,52,5,7]
    # d = [2,4,5,3,3,26,3]
    # e = [3,2,5,3,3,2,5]
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(a, b, c, c='r', marker='^')
    # ax.scatter(a, b, d, c='g', marker='o')
    # ax.scatter(a, b, e, c='b', marker='X')
    # ax.set_xlabel('Liczba bitów')
    # ax.set_ylabel('Długość pakietu')
    # ax.set_zlabel('Efektywność')
    # plt.show()

    n=sys.argv[1]
    fx=sys.argv[2]
    f=sys.argv[3]
    codingType=sys.argv[4]
    errorRate=sys.argv[5]
    packetLength=sys.argv[6]
    appType=sys.argv[7]
    print(n+' '+fx+' '+f+' '+codingType+' '+errorRate+' '+packetLength + ' '+ appType)
    
