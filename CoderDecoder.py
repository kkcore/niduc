

class Coder:
    def codeParrity(self, packet):
        xor = 0
        for i in packet:
            xor ^= int(i)
        if (xor == 0):
            packet+='0'
        else:
            packet+='1'
        return packet

class Decoder:
    def decodeParrity(self, packet):
        xor = 0
        for i in packet[:-1]:
            xor^= int(i)
        if (xor == packet[-1]):
            return True
        else:
            return False

