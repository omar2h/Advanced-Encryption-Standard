from key import generateKey
from functions import *

def rowToCol(text):
    res = ""
    for i in range(0, 8, 2):
        for j in range(0, len(text), 8):
            res += text[i + j:i + j + 2]
    return res

def shift4(text,dir):
    rtext = rowToCol(text)
    shText = ""
    for i in range(4):
        shText+=shift(rtext[i*8:i*8+8], 2*i, dir)
    return rowToCol(shText)

def mix(text, mtx):
    res = 0
    z = ""
    for k in range(4):
        for i in range(4):
            p=[]
            for j in range(0,8,2):
                n = mtx[(j//2)+k*4]
                m = hex(int(text[j + i * 8:j + i * 8 + 2], 16))[2:].zfill(2)
                a = hex(int(text[j + i * 8:j + i * 8 + 2], 16))[2:].zfill(2)
                if n == 1:
                    p.append(m)
                if (n == 3):
                    p.append(bSub(m, GALOIS_MULTIP[1]))
                if n == 2:
                    p.append(bSub(m, GALOIS_MULTIP[0]))
                if n== 9:
                    p.append(bSub(m, GALOIS_MULTIP[2]))
                if n == 11:
                    p.append(bSub(m, GALOIS_MULTIP[3]))
                if n == 13:
                    p.append(bSub(m, GALOIS_MULTIP[4]))
                if n== 14:
                    p.append(bSub(m, GALOIS_MULTIP[5]))
                if (j == 0):
                    res = int(p[j], 16)
                else:
                    res ^= int(p[j // 2], 16)
            z += hex(res)[2:].zfill(2)
    return rowToCol(z)

def encrypt(text, key):
    key = generateKey(key)
    addKey = add(text, key[0])
    sub = bSub(addKey, S_BOX)
    textShift = shift4(sub, 0)
    cipher = mix(textShift, MIX_COLUMNS_MTX)
    cipher = add(cipher, key[1])
    for i in range(2,10,1):
        sub = bSub(cipher, S_BOX)
        textShift=shift4(sub, 0)
        cipher = mix(textShift, MIX_COLUMNS_MTX)
        cipher = add(cipher, key[i])
    sub = bSub(cipher, S_BOX)
    textShift = shift4(sub, 0)
    cipher = add(textShift, key[10])
    return cipher

def decrypt(text, key):
    key = generateKey(key)
    addKey = add(text, key[10])
    textShift = shift4(addKey, 1)
    plain = bSub(textShift, S_BOX_INV)
    for i in range(9, 1, -1):
        plain = add(plain, key[i])
        plain = mix(plain, INV_MIX_COLUMNS_MTX)
        plain = shift4(plain, 1)
        plain = bSub(plain, S_BOX_INV)
    plain = add(plain, key[1])
    plain = mix(plain, INV_MIX_COLUMNS_MTX)
    plain = shift4(plain, 1)
    plain = bSub(plain, S_BOX_INV)
    plain = add(plain, key[0])
    return plain





