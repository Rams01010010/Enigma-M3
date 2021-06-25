import M3 as enigma

rotor,rings,Rot,plugb,reflector = [],[],[],'',''
flag = 0
#Enigma Settings
def select_settings(isFullSetting=True):

    global rotor,rings,Rot,plugb,reflector
    
    if isFullSetting == True:
        
        # Getting Rotor Order
        x = input("Rotor (Eg : I III VI ): ").upper().split(" ")
        rotor = ['I','II','III'] if x == [''] else x
        
        # Getting Reflector
        x = input("Reflector (B/C) : ").upper()
        reflector = 'B' if x == '' else x
        
        #Getting RingSetting
        x = input("Ring Setting (Eg : A B C) : ").upper().split(" ")
        rings = ['A','A','A'] if x == [''] else x

        #Getting Plugboard Setting
        plugb = input("Plugboard Pairs - Eg : ab cd ef gh ij : ").upper()

        #initialSetting
        x = input("Rotor initial setting (Eg : E N I ) : ").upper().split(" ")
        Rot = ['A','A','A'] if x == [''] else x

    else:
        #initialSetting
        x = input("Rotor initial setting (Eg : E N I ) : ").upper().split(" ")
        Rot = ['A','A','A'] if x == [''] else x

    #Inputing Values
    m3.setter(rotor[0],rotor[1],rotor[2],rings[0],rings[1],rings[2],plugb,reflector,Rot[0],Rot[1],Rot[2])

#start
def start():
    plainMsg = input("Enter message : ").upper()
    encryptedMsg = ''
    for i in plainMsg:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            encryptedMsg += m3.startMachine(i)
    print("\nEncrypted Msg : ",end = '')
    k = 0
    for i in encryptedMsg:
        if k == 5:
            print(" ",end = '')
            k = 0
        print(i,end = '')
        k+=1
    print()
#displayCurrentSettings
def displayCurrentSetting():
    R1,R2,R3,r1,r2,r3,plugBoard,reflector,i1,i2,i3 = m3.getter()
    print("\nRotor Settings : ",R1,R2,R3)
    print("Ring Settings : ",r1,r2,r3)
    print("Initial Settings : ",i1,i2,i3)
    print("Plugboard : ",plugBoard)
    print("Reflector : ",reflector)

#displayRotorSettings
def displayRotorSettings():
    R1,R2,R3 = m3.getRotorPosition()
    print('\t',R1,R2,R3)
    
#--------------------------------------------------------------------------------------------#

ch,f = 0,0

m3 = enigma.M3()
m3.setter()
while ch != 5:
    try :
        print("\n\tMENU\n1.Enigma Settings\n2.Initial Setting\n3.Start\n4.Display Settings\n5.Exit")
        ch = input("Enter your choice : ")
        if ch == '1':
            select_settings()
            f = 1
        elif ch == '2':
            select_settings(False)
        elif ch == '3':
            if f == 1:
                print()
                displayRotorSettings()
                print()
                start()
            elif f ==  0:
                select_settings()
                f = 1
        elif ch == '4':
            displayCurrentSetting()
        elif ch == '5':
            break
        else:
            print('\n\t"Invalid choice"') 
    except:
        print("Input Correctly !")
