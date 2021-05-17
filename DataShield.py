import pyAesCrypt

from os import stat, remove
print("****************************************************************************")
print("\t \t \t MENU")
print("***************************************************************************")
print("\t \t 1. Data XOR Encryption and Decryption ")
print("\t \t 2. Data  AES Encryption and Decryption ")
print("***************************************************************************")
a=int(input("Enter your choice"))
if a==1:
    print("*************************************")
    print("1.Press 1 for Encryption")
    print("1.Press 2 for Dencryption")
    b=int(input("Enter your choice"))
    if b==1:
        
        try:
        	
        	path = input(r'Enter path of data: ')
        	
        	
        	key = int(input('Enter Key for encryption of data : '))
        	
        	
        	
        	print('The path of file : ', path)
        	print('Key for encryption : ', key)
        	
        	
        	fin = open(path, 'rb') #Reading Binary value of fetched file/image
        	
        	
        	image = fin.read()
        	fin.close()
        	
        	
        	
        	image = bytearray(image)#typecasting
        
        	
        	for index, values in enumerate(image):
        		image[index] = values ^ key
        
        	
        	fin = open(path, 'wb') #Writing Binary value of fetched file/image
        	
        	
        	fin.write(image)
        	fin.close()
        	print('Encryption Done...')
        
        	
        except Exception:
        	print('Error caught : ', Exception.__name__)
    if b==2:
                
        try:
        
        	path = input(r'Enter path of data : ')
        	
        	
        	key = int(input('Enter Key for encryption of data : '))
        	
        	
        	print('The path of file : ', path)
        	print('Note : Encryption key and Decryption key must be same.')
        	print('Key for Decryption : ', key)
        	
        	
        	fin = open(path, 'rb') #Reading Binary value of fetched file/image
        	
        	
        	image = fin.read()
        	fin.close()
        	
        	
        	image = bytearray(image)
        
        	
        	for index, values in enumerate(image):
        		image[index] = values ^ key
        

        	fin = open(path, 'wb')
        	
        	
        	fin.write(image)
        	fin.close()
        	print('Decryption Done...')
        
        
        except Exception:
        	print('Error caught : ', Exception.__name__)

    else:
        print("Please enter the Right choice")
if a==2:
    print("**********************************************************************************************")    
    print("1 for Encryption" )
    print("2 for Decryption")
    print("##############################################################################################")
    h=int(input("Enter the Choice"))
    jh=input("Enter the file location with extension")
    bufferSize = 64 * 1024 #by default 512 (max value 64*1024)
    password = input("Enter the password")
    koi=f'{jh}.aes'

    if h==1:
        
        
    
        with open(jh, "rb") as fIn:
         with open(koi, "wb") as fOut:
             pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        print("Encryption done")
   
    
    if h==2:
    #DEcrypt................
        encFileSize = stat(jh).st_size
        print(encFileSize)
        
        with open(jh, "rb") as fIn:
            try:
                aso=input("decrrypted file name")
                with open(aso, "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                    
            except ValueError:
                
                print("Value Error please give less buffer Size Block")
        
