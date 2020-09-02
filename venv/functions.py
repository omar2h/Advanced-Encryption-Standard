from constants import *

def bSub(shKey, box):
    sub=""
    for i in range(0, len(shKey), 2):
        row = int(shKey[i], 16) * 16
        col = int(shKey[i + 1], 16)
        pos = row + col
        sub += hex(box[pos]).split('x')[-1].zfill(2)
    return sub

def shift(str, bit, dir):
    return (str * 3)[len(str) + bit: 2 * len(str) + bit] if dir==0 else (str * 3)[len(str) - bit: 2 * len(str) - bit]

def add(text, key):
    res=""
    for i in range(0,len(text),2):
        res+= hex(int(text[i:i+2], 16) ^ int(key[i:i+2], 16))[2:].zfill(2)
    return res