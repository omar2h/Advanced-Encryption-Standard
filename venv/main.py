from text import encrypt, decrypt
from key import generateKey
from tkinter import *

root = Tk()

def showCipher():
    key = entry1.get()
    text = entry2.get()
    label1 = Label(root, text=encrypt(text, key))
    canvas1.create_window(200, 190, window=label1)

def showPlain():
    key = entry1.get()
    text = entry3.get()
    label2 = Label(root, text=decrypt(text, key))
    canvas1.create_window(200, 350, window=label2)

root.title("AES Encryption & Decryption")
canvas1 = Canvas(root, width=400, height=500)
canvas1.pack()

key_label = Label(root, text="Key")
canvas1.create_window(200, 20, window=key_label)

entry1 = Entry(root)
canvas1.create_window(200, 40, width=250, window=entry1)

enc_label = Label(root, text="Encryption", font='calibri 14 bold')
canvas1.create_window(200, 80,window=enc_label)

plain_label = Label(root, text="Plaintext")
canvas1.create_window(200, 110, window=plain_label)

entry2 = Entry(root)
canvas1.create_window(200, 130,width=250, window=entry2)

button1 = Button(text='Encrypt', command=showCipher)
canvas1.create_window(200, 160, window=button1)

dec_label = Label(root, text="Decryption", font='calibri 14 bold')
canvas1.create_window(200, 240,window=dec_label)

cipher_label = Label(root, text="Ciphertext")
canvas1.create_window(200, 270, window=cipher_label)

entry3 = Entry(root)
canvas1.create_window(200, 290,width=250, window=entry3)

button2 = Button(text='Decrypt', command=showPlain)
canvas1.create_window(200, 320, window=button2)

root.mainloop()
