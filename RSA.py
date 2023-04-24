import random

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def setE(finN):
    x = random.randint(1,finN)
    count = 0
    while(gcd(x,finN) != 1):
        x = random.randint(1,finN)
        count = count+1
    return x 
   
def setD(finN,E):
    i = 1
    while(True):
        x = (i*finN) + 1
        x = x/E
        y = int(x)
        if (x-y) == 0:
            return y
        i = i+1

def isPrime(x):
    count = 0
    for i in range (1,int(x)+1):
        if x%i == 0:
            count+=1
    if count == 2:
        return True
    else:
        return False    


def setRandom():
    x = random.randint(1,1000)
    return x
   

def setPrimeNumber():
    x = setRandom()
    while(isPrime(x) != True):
        x = setRandom()
    return x

def result(num, power , sub):
    y = num ** power
    y = y % sub
    return y




plaintext = ""
ciphertext = ""


#-----
num = 1
while(num != 0):
    print("1. encryption")
    print("2. decryption")
    print("0.  exit")
    num = int(input("enter a number(0,1,2): "))
    if num == 1:
        P = 607#setPrimeNumber()
        Q = 643#setPrimeNumber()
        N = P * Q
        finN = (P - 1) * (Q - 1)
        E = 31723#setE(finN)
        D = setD(finN,E)
        #----------
        ciphertext = ""
        print("================Encryption==============")
        print(f" P = {P} , Q = {Q}\n N = {N} , finN = {finN}\n E = {E} , D = {D}")
        text = input("enter the plaintext: ")
        for i in range (0,len(text)):
            number = ord(text[i])
            number = result(number,E,N)
            txt = chr(number)
            ciphertext += txt
        print(f"ciphertext = {ciphertext}")    
        print("============")
    elif num == 2 :
        plaintext = ""
        print("================Encryption==============")
        print(f" P = {P} , Q = {Q}\n N = {N} , finN = {finN}\n E = {E} , D = {D}")
        print(f"ciphertext = {ciphertext}")
        for i in range (0,len(ciphertext)):
            number = ord(ciphertext[i])
            number = result(number,D,N)
            txt = chr(number)
            plaintext += txt
        print(f"ciphertext = {plaintext}")    
        print("============")
       


    
