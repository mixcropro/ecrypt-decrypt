from cryptography.fernet import Fernet
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

#file = open('key.key', 'rb')
f = askopenfilename() #otvaram file gdje je key za enkripciju
file = open(f, "rb")
key = file.read() # The key will be type bytes
file.close()

enc_file = askopenfilename()

with open(enc_file, 'rb') as f1:
    data = f1.read()
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

out = "enc_file.encrypted" #koji ce file biti enkriptiran
with open(out, 'wb') as f2:
    f2.write(encrypted)


