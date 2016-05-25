import sys,time
allcorrect=False
runningcode=input('enter x to close files and code')
if runningcode!='x':
    if allcorrect==False:
        file=open('en(rypt storage.txt','r+')
        filecontent=file.readline()
        filecontent=str(filecontent)
        print(filecontent)
        if filecontent=='blank':
            print('Welcome to Python Password and General Storage')
            passwordincorrect=True
            while passwordincorrect==True:
                password=input('Please enter a password (please note the maximum length of 16 characters):')
                passwordcheck=input('Please enter your password again:')
                if password==passwordcheck:
                    passwordincorrect==False
                    file.write('working')
                    print('Please close the program and then re-open it')
                    time.sleep(10000000)
        entrypassword=input('please enter your password to logon:')
        print('calculating...')
        allcorrect=True
        entrypasswordstring=str(entrypassword)
        passwordletterzero=entrypasswordstring[0]
        passwordletterone=entrypasswordstring[1]
        passwordlettertwo=entrypasswordstring[2]
        passwordletterthree=entrypasswordstring[3]
        passwordletterfour=entrypasswordstring[4]
        passwordletterfive=entrypasswordstring[5]
        passwordlettersix=entrypasswordstring[6]
        passwordletterseven=entrystring[7]
        passwordlettereight=entrypasswordstring[8]
        passwordletternine=entrypasswordstring[9]
        passwordletterten=entrypasswordstring[10]
        passwordlettereleven=entrypasswordstring[11]
        passwordlettertwelve=entrypasswordstring[12]
        passwordletterthirteen=entrypasswordstring[13]
        passwordletterfourteen=entrypasswordstring[14]
        passwordletterfifteen=entrypasswordstring[15]
        typetoencrypt=input('please enter the name for the password you wish to encrypt(e.g my game):')
        print('calculating...')
        typetoencryptstring=str(typetoencrypt)
        typetoencryptletterzero=typetoencryptstring[0]
        typetoencryptletterone=typetoencryptstring[1]
        typetoencryptlettertwo=typetoencryptstring[2]
        typetoencryptletterthree=typetoencryptstring[3]
        typetoencryptletterfour=typetoencryptstring[4]
        typetoencryptletterfive=typetoencryptstring[5]
        typetoencryptlettersix=typetoencryptstring[6]
        typetoencryptletterseven=typetoencryptstring[7]
        typetoencryptlettereight=typetoencryptstring[8]
        typetoencryptletternine=typetoencryptstring[9]
        typetoencryptletterten=typetoencryptstring[10]
        typetoencryptlettereleven=typetoencryptstring[11]
        typetoencryptlettertwelve=typetoencryptstring[12]
        typetoencryptletterthirteen=typetoencryptstring[13]
        typetoencryptletterfourteen=typetoencryptstring[14]
        typetoencryptletterfifteen=typetoencryptstring[15]
        passwordtoencrypt=input('please enter the  you wish to encrypt:')
        print('calculating...')
        passwordtoencryptstring=str(passwordtoencrypt)
        passwordtoencryptletterzero=passwordtoencryptstring[0]
        passwordtoencryptletterone=passwordtoencryptstring[1]
        passwordtoencryptlettertwo=passwordtoencryptstring[2]
        passwordtoencryptletterthree=passwordtoencryptstring[3]
        passwordtoencryptletterfour=passwordtoencryptstring[4]
        passwordtoencryptletterfive=passwordtoencryptstring[5]
        passwordtoencryptlettersix=passwordtoencryptstring[6]
        passwordtoencryptletterseven=passwordtoencryptstring[7]
        passwordtoencryptlettereight=passwordtoencryptstring[8]
        passwordtoencryptletternine=passwordtoencryptstring[9]
        passwordtoencryptletterten=passwordtoencryptstring[10]
        passwordtoencryptlettereleven=passwordtoencryptstring[11]
        passwordtoencryptlettertwelve=passwordtoencryptstring[12]
        passwordtoencryptletterthirteen=passwordtoencryptstring[13]
        passwordtoencryptletterfourteen=passwordtoencryptstring[14]
        passwordtoencryptletterfifteen=passwordtoencryptstring[15]
        print('encrypting...')
        typenumberletterzero=ord(passwordtoencryptletterzero)
        typenumberletterone=ord(passwordtoencryptletterone)
        typenumberlettertwo=ord(passwordtoencryptlettertwo)
        typenumberletterthree=ord(passwordtoencryptletterthree)
        typenumberletterfour=ord(passwordtoencryptletterfour)
        typenumberletterfive=ord(passwordtoencryptletterfive)
        typenumberlettersix=ord(passwordtoencryptlettersix)
        typenumberletterseven=ord(passwordtoencryptletterseven)
        typenumberlettereight=ord(passwordtoencryptlettereight)
        typenumberletternine=ord(passwordtoencryptletternine)
        typenumberletterten=ord(passwordtoencryptletterten)
        typenumberlettereleven=ord(passwordtoencryptlettereleven)
        typenumberlettertwelve=ord(passwordtoencryptlettertwelve)
        typenumberletterthirteen=ord(passwordtoencryptletterthirteen)
        typenumberletterfouteen=ord(passwordtoencryptletterfourteen)
        typenumberletterfifteen=ord(passwordtoencryptletterfifteen)
        passwordnumberletterzero=ord(passwordtoencryptletterzero)
        passwordnumberletterone=ord(passwordtoencryptletterone)
        passwordnumberlettertwo=ord(passwordtoencryptlettertwo)
        passwordnumberletterthree=ord(passwordtoencryptletterthree)
        passwordnumberletterfour=ord(passwordtoencryptletterfour)
        passwordnumberletterfive=ord(passwordtoencryptletterfive)
        passwordnumberlettersix=ord(passwordtoencryptlettersix)
        passwordnumberletterseven=ord(passwordtoencryptletterseven)
        passwordnumberlettereight=ord(passwordtoencryptlettereight)
        passwordnumberletternine=ord(passwordtoencryptletternine)
        passwordnumberletterten=ord(passwordtoencryptletterten)
        passwordnumberlettereleven=ord(passwordtoencryptlettereleven)
        passwordnumberlettertwelve=ord(passwordtoencryptlettertwelve)
        passwordnumberletterthirteen=ord(passwordtoencryptletterthirteen)
        passwordnumberletterfouteen=ord(passwordtoencryptletterfourteen)
        passwordnumberletterfifteen=ord(passwordtoencryptletterfifteen)
        #the rest of the code will create a single password vairable, multiply it by the passowrd and type, put these numbers in the file and will also contain a function to view the encrypted items
        file.close()
    file.close()
else:
    file.close()
