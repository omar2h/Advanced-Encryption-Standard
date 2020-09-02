from constants import *
from functions import *



def g(w, i):
    l_shift = shift(w, 2, 0)
    sub = bSub(l_shift, S_BOX)
    h = hex(int(sub, 16) ^ int(RCON[i]))[2:].zfill(8)
    return h

def round(temp, key):
    for i in range(4):
        temp += hex(int(temp[i*8: i*8 + 8], 16) ^ int(key[i*8:i*8 + 8], 16)).split('x')[-1].zfill(8)
    return temp[8:]

def generateKey(key):
    roundKeys = []
    roundKeys.append(key)
    for i in range(10):
        roundKeys.append(round(g(roundKeys[i][24:32], i), roundKeys[i]))
    return roundKeys

def main():
    print(generateKey("5468617473206D79204B756E67204675"))
    #print(g("67204675"))
    #print(shift("67204675", 2, 0 ))
    #print(hex(S_BOX[251]).split('x')[-1].zfill(2))


if __name__ == "__main__":
    main()