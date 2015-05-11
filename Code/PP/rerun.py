import pickle
import os
def encrypt(text):
    password="Porunga"
    encrypted = []
    for i, c in enumerate(text):
        shift = password[i % len(password)]
        shift = ord(shift)
        encrypted.append((ord(c) + shift) % 256)
    return ''.join([chr(n) for n in encrypted])
infile=open('settings.txt','w')
s=['porunga','C:/PP/robot.wav']
pickle.dump(s,infile)
infile.close()
infile1=open("settings.txt")
infile2=open("Temp.txt","w")
text=infile1.read()
text=encrypt(text)
infile2.write(text)
infile1.close()
infile2.close()
os.remove("settings.txt")
os.rename("Temp.txt","settings.txt")


