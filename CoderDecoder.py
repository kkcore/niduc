

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

    def calcNumberOfRedundantBits(self, packet):
        r=0
        while 2**r < len(packet) + r + 1:
            r+=1
        return r

    def codeHamming(self, packet):
        numberOfRedundantBits = self.calcNumberOfRedundantBits(packet)
        bitpositions = []
        for bit in range(0,numberOfRedundantBits):
            bitpos = 2**bit - 1
            bitpositions.append(bitpos)
            packet = packet[:bitpos] + ' ' + packet[(bitpos+1):]
        return self.setParrityBitValues(packet,bitpositions)

    def setParrityBitValues(self, packet, bitpositions):
        #helper do poteg
        helper = 0
        for bit in bitpositions:
            xor = 0
            for i in range(1, len(packet)+1):
                if (i & (1<<(helper))):
                    if (packet[i-1] != ' '):
                        xor^=int(packet[i-1])
            if (xor == 0):
                packet = packet[:bit] + '0' + packet[(bit+1):]
            if (xor == 1):
                packet = packet[:bit] + '1' + packet[(bit+1):]
            helper+=1
        return packet
                

class Decoder:
    def getReduntantbits(self, packet):
        r=0
        reduntantbits = []
        x = 2**r
        while x <= len(packet) + r + 1:
            r+=1
            reduntantbits.append(x)
            x = 2**r
        return reduntantbits

    def decodeParrity(self, packet):
        xor = 0
        for i in packet[:-1]:
            xor^= int(i)
        if (xor == packet[-1]):
            return True
        else:
            return False
    
    def decodeHamming(self, packet):
        reduntantbits = self.getReduntantbits(packet)
        return self.correctCode(packet,reduntantbits)

    def correctCode(self, packet, reduntantbits):
        #Do dodania kod podmieniajacy bity parzystosci, przynajmniej dla pierwszego nie dziala
        #To samo co w setParrityBitValues- redundacja, mozna zrefaktoryzowac
        helper = 0
        failedBit = 0
        for bit in reduntantbits:
            xor = 0
            for i in range(1, len(packet)+1):
                if (i & (1<<(helper))):
                    if (packet[i-1] != helper):
                        xor^=int(packet[i-1])
                failedBit+=bit
            helper+=1
        if (failedBit != 0):
            if (int(packet[failedBit]) == 0):
                packet = packet[:failedBit] + '1' + packet[(failedBit+1): ]
            else:
                packet[failedBit] = packet[:failedBit] + '0' + packet[(failedBit+1):]
        return packet


