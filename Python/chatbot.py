import webbrowser
import os,glob
import random
helloIntent =["hey","hi","hello","wassup","hi"]
byeIntent =["bye","tata","see you","take care"]
chat = True
while chat == True:
    msg = input("enter message")
    if msg in helloIntent:
        print("hello..")
    elif msg in byeIntent:
        print("bye..")
        chat=False
    elif  msg.startswith("open"):    
        webbrowser.open(msg.split()[-1]+".com")
    elif msg.startswith("play"):
        #chdir - change directory
        os.chdir(r"C:\Users\Asus\Downloads")
        files = glob.glob("*.jpg")
        file=random.choice(files)
        os.startfile(file)
    else:
        print ("sry i dint'n understand")
