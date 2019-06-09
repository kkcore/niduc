

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

