print(" \t encrypting and decrypting message .")
def encrypt_char(char,key):
    char=char.upper()
    return chr(ord('A')+((ord(char)+key)-ord('A'))%26)
def encrypt_message(sen,key):
    clone=""
    for i in sen :
        if i in " ,.;'":
            clone+=i
        else:
            clone+=encrypt_char(i, key)
    return clone
def decrypt_message(sen,key):
    clone=""
    for i in sen :
        if i in " ,.;'":
            clone+=i
        else:
            clone+=encrypt_char(i, 26-key)
    return clone
sen=input(" enter str to en/de crypt it : ")
option = int(input(" enter \n 1:encrpyt\n 2:decrypt \n: "))
key=int(input(" enter the key : "))

if(option==1):
    print(encrypt_message(sen, key))
elif(option == 2):
    print(decrypt_message(sen, key))
else:
    print(" Invalid input ")
