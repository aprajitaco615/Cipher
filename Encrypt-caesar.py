print('Welcome to Cipher! \n')

print('Your message will be encrypted first using a caesar cipher, and then individual words will be reversed for further encryption \nExample: "Hello World!" with a jump value of 2 will become "qnngJ fntqY!"')
print('Note: Only alphabets will be shifted using caesar cipher, and only alphabets will be considered in a word to be reversed')


message=input('Enter message to encrypt')

while True:
    try:
        jump=int(input('Enter value to jump'))
        break
    except ValueError:
        print('Please enter a valid numerical value')
        

    
    
jump=jump%26
    
list_enc_mes=[]

for i in message:
    if i.isalpha():
        x=ord(i)
        y=x+jump
        
        if i.isupper():
            if y>90:
                z=y-90
                y=65+z
        
        if i.islower():
            if y>122:
                z=y-122
                y=97+z
        
        list_enc_mes.append(chr(y))
        
    else:
        list_enc_mes.append(i)
    
encr_mess=''    
for i in list_enc_mes:
    encr_mess+=i

dummy_var=''
rever_mes=''
for i in range(len(encr_mess)):
    if encr_mess[i].isalpha():
        dummy_var+=encr_mess[i]
    
    else:
        rever_mes+=dummy_var[-1::-1]
        dummy_var=''
        rever_mes+=encr_mess[i]
    
    if i==len(encr_mess)-1:
        rever_mes+=dummy_var[-1::-1]
        
print(rever_mes)


        
    