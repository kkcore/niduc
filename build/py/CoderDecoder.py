
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
            packet = packet[:bitpos] + ' ' + packet[(bitpos):]
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

    # Zrodlo: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    # Kodowanie CRC
    def crc_remainder(self,input_bitstring, polynomial_bitstring, initial_filler = 0):
        '''
        Calculates the CRC remainder of a string of bits using a chosen polynomial.
        initial_filler should be '1' or '0'.
        '''
        polynomial_bitstring = polynomial_bitstring.lstrip('0')
        len_input = len(input_bitstring)
        initial_padding = initial_filler * (len(polynomial_bitstring) - 1)
        input_padded_array = list(input_bitstring + initial_padding)
        while '1' in input_padded_array[:len_input]:
            cur_shift = input_padded_array.index('1')
            for i in range(len(polynomial_bitstring)):
                input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
        return ''.join(input_padded_array)[len_input:]
                

class Decoder:
    def getReduntantbits(self, packet):
        i = 0
        redundantbits = []
        power = 0
        while power < len(packet):
            redundantbits.append(power)
            i+=1
            power = 2**i - 1
        return redundantbits

    def decodeParrity(self, packet):
        xor = 0
        for i in packet[:-1]:
            xor^= int(i)
        if (xor == int(packet[-1])):
            return True
        else:
            return False
    
    def decodeHamming(self, packet):
        reduntantbits = self.getReduntantbits(packet)
        return self.checkForFailedHamming(packet,reduntantbits)

    # Funkcja do wykrywania nieprawidłowych bitów w kodzie Hamminga, jeżeli codeToCorrect jest ustawiony
    # na True to poprawia i zwraca pakiet, jeżeli jest ustawiony na false to zwraca, czy w pakiecie
    # znajdowały się błędne bity
    def checkForFailedHamming(self, packet, reduntantbits, codeToCorrect = False):
        #Do dodania kod podmieniajacy bity parzystosci, przynajmniej dla pierwszego nie dziala
        #To samo co w setParrityBitValues- redundacja, mozna zrefaktoryzowac
        helper = 0
        failedBit = 0
        xor = 0
        for helper in  range(len(reduntantbits)):
            for i in  range(1, (len(packet) + 1)):
                if (i != (1 << helper) and i & (1 << helper)):
                    xor^=int(packet[i-1])
            if xor != int(packet[helper]):
                failedBit += 1 << helper
        if (failedBit != 0):
            if codeToCorrect:
                if (int(packet[failedBit - 1]) == 0):
                    packet = packet[:failedBit - 1] + '1' + packet[failedBit: ]
                else:
                    packet[failedBit - 1] = packet[:failedBit - 1] + '0' + packet[failedBit:]
                return packet
            else:
                return False
        return True

# Zrodlo: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
# Obliczanie sumy kontrolnej CRC
    def crc_check(self, input_bitstring, polynomial_bitstring, check_value):
        '''
        Calculates the CRC check of a string of bits using a chosen polynomial.
        '''
        polynomial_bitstring = polynomial_bitstring.lstrip('0')
        len_input = len(input_bitstring)
        initial_padding = check_value
        input_padded_array = list(input_bitstring + initial_padding)
        while '1' in input_padded_array[:len_input]:
            cur_shift = input_padded_array.index('1')
            for i in range(len(polynomial_bitstring)):
                input_padded_array[cur_shift + i] = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
        return ('1' not in ''.join(input_padded_array)[len_input:])


