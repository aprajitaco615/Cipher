message=input('Enter message to decrypt')

while True:
    try:
        back=int(input('Enter value to go back \n(i.e, the key value for the encryption)'))
        break
    except ValueError:
        print('Please enter a valid numerical value')
        

back=back%26
    
dummy_var=''
un_rever=''
for i in range(len(message)):
    if message[i].isalpha():
        dummy_var+=message[i]
    
    else:
        un_rever=un_rever+dummy_var[-1::-1]
        dummy_var=''
        un_rever=un_rever+message[i]
    
    if i==len(message)-1:
        un_rever=un_rever+dummy_var[-1::-1]
        



list_decry_mes=[]
    
for i in un_rever:
    if i.isalpha():
        x=ord(i)
        y=x-back
        
        if i.isupper():
            if y<65:
                y=y+26
        
        if i.islower():
            if y<97:
                y=y+26
                
        list_decry_mes.append(chr(y))
        
    else:
        list_decry_mes.append(i)
    
decrypt=''    
for i in list_decry_mes:
    decrypt+=i

print(decrypt)

