def setRotVal(value):
    if value == 'I':
        return ['''ABCDEFGHIJKLMNOPQRSTUVWXYZ''','''EKMFLGDQVZNTOWYHXUSPAIBRCJ''','''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
    elif value == 'II':
        return ['''ABCDEFGHIJKLMNOPQRSTUVWXYZ''','''AJDKSIRUXBLHWTMCQGZNPYFVOE''','''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
    elif value == 'III':
        return ['''ABCDEFGHIJKLMNOPQRSTUVWXYZ''','''BDFHJLCPRTXVZNYEIWGAKMUSQO''','''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
    elif value == 'IV':
        return ['''ABCDEFGHIJKLMNOPQRSTUVWXYZ''','''ESOVPZJAYQUIRHXLNFTGKDCMWB''','''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
    elif value == 'V':
        return ['''ABCDEFGHIJKLMNOPQRSTUVWXYZ''','''VZBRGITYUPSDNHLXAWMJQOFECK''','''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
    elif value == 'B':
        return '''YRUHQSLDPXNGOKMIEBFZCWVJAT'''
    elif value == 'C':
        return '''FVPJIAOYEDRZXWGCTKUQSBNMHL'''
#--------------------------------------------------------------------------------------

# Details
ETW = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
rotors = {'I':setRotVal('I'),"II":setRotVal('II'),"III":setRotVal('III'),"IV":setRotVal('IV'),"V":setRotVal('V'),"B":setRotVal('B'),"C":setRotVal('C')}
notch  = {'I':'Q',"II":'E',"III":'V',"IV":'J',"V":'Z'}

class M3:
    Plugboard = dict()
    R1,R2,R3,r1,r2,r3,plugBoard,reflector,iI,iII,iIII = "","","","","","","","","","",""
    R,r,i,S = [],[],[],[]
    
    #setter
    def setter(self,RI='I',RII='II',RIII='III',rI='A',rII='A',rIII='A',plugboard='',reflector='B',iI='A',iII='A',iIII='A'):
        self.R1,self.R2,self.R3,self.sr1,self.sr2,self.sr3,self.r1,self.r2,self.r3,self.plugBoard,self.reflector,self.i1,self.i2,self.i3 = setRotVal(RI),setRotVal(RII),setRotVal(RIII),setRotVal(RI),setRotVal(RII),setRotVal(RIII),rI,rII,rIII,plugboard,rotors[reflector],iI,iII,iIII
        self.S = ['',self.sr1,self.sr2,self.sr3]
        self.R = [self.reflector,self.R1,self.R2,self.R3]
        self.r = ['',self.r1,self.r2,self.r3]
        self.i = ['',self.i1,self.i2,self.i3]

        self.Plugboard = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}

        #check_plugboard for errors
        self.plugBoard = self.plugBoard.split(" ")
        k = ''.join(self.plugBoard)
        for i in k:
            if k.count(i) > 1:
                exit()

        #set_plugboard
        for i in self.plugBoard:
            if len(i) == 2:
                self.Plugboard[i[0].upper()] = i[1].upper()
                self.Plugboard[i[1].upper()] = i[0].upper()
            elif len(i) > 2 or len(i) == 1:
                exit()
        
        #set_ringsettings
        for i in range(1,4):
            self.R[i][2] = self.rotate(self.R[i][2],self.R[i][2].index(self.r[i]))

        #set_initialSettings
        for j in range(1,4):
            self.R[j][0] = self.rotate(self.R[j][0],self.R[j][2].index(self.i[j]))
            self.R[j][1] = self.rotate(self.R[j][1],self.R[j][2].index(self.i[j]))
            self.R[j][2] = self.rotate(self.R[j][2],self.R[j][2].index(self.i[j]))
    
    #getter
    def getter(self):
        valuePack = (self.getKeys(rotors,self.sr1),self.getKeys(rotors,self.sr2),self.getKeys(rotors,self.sr3),self.r1,self.r2,self.r3,self.plugBoard,self.getKeys(rotors,self.reflector),self.i1,self.i2,self.i3)
        return valuePack
    
    #rotorPositions
    def getRotorPosition(self):
        valuePack = (self.R[1][2][0],self.R[2][2][0],self.R[3][2][0])
        return valuePack

    #get_keys from values
    def getKeys(self,dic,val):
        for key,value in dic.items():
            if val==value:
                return key

    #rotate_rotors
    def rotate(self,val,amt):
        v = val[amt:]+val[:amt]
        return v

    #run_the_given_letter_through_rotors
    def run_rotor(self,no,val):
        if no == 0 :
            x = self.reflector[val]
            return ETW.index(x)
        else: 
            x = self.R[no][1][val]
            matchIndex = self.R[no][0].index(x)
            val = self.run_rotor(no-1,matchIndex)
            x = self.R[no][0][val]
            matchIndex = self.R[no][1].index(x)
            return matchIndex

    #mainFunction
    def startMachine(self,Value):
        self.autoRotate(3)
        encryptedMessage = self.Plugboard[ETW[self.run_rotor(3,ETW.index(self.Plugboard[Value]))]]
        return encryptedMessage

    #autoRotate
    def autoRotate(self,val):
        k = False
        for i in range(3,1,-1):
            if self.R[i][2][0] == notch[self.getKeys(rotors,self.S[i])]:
                k = True
        if k:
            for i in range(3):
                self.R[val][i] = self.rotate(self.R[val][i],1)
            self.autoRotate(val-1)
        else:
            for i in range(3):
                self.R[val][i] = self.rotate(self.R[val][i],1)
    
#SampleCode
if __name__ == '__main__':
    r = M3()
    r.setter('III','II','V','J','S','C','QH WP ES AY DX RC TF VB ZG UJ NM IK OL','B','C','S','E')
    x = input("Enter a message : ").upper()
    s = ''
    for i in x:
        s += r.startMachine(i)
    print(s)
