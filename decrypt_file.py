from cryptography.fernet import Fernet
from tkinter import Tk
from tkinter.filedialog import askopenfilename

f = askopenfilename() #otvaram file gdje je key za enkripciju
file = open(f, "rb")
key = file.read() # The key will be type bytes
file.close()


output_file = 'decrypted_file.txt'

dec_file = askopenfilename()
with open(dec_file, 'rb') as f1:
    data = f1.read()
fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f2:
    f2.write(encrypted)


