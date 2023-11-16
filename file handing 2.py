import os
import sys
def fi():
    print("choose your option\n 1.creat the file\n 2.list the file\n 3.edit the file\n 4.delet the file\n 5.read the file\n 6.stop the file\n")
    d=int(input(""))
    a=d
    match a:
        case 1:
            print("------------------------")
            print("CREATING FILE\n")
            print("enter your file name\n: ")
            f=input("")
            h=f+".txt"
            with open(h,'x')as file:
                print(f,"file is created succesfully")
        case 5:
            print("*******************************")
            print("reading file\n")
            f=input("enter the file name that you want to read")
            with open(f+".txt","r")as file:
                print(file.read())
        case 2:
            print("_______________________")
            print("listing all file\n")
            path='E:\dolly'
            file=os.listdir(path)
            for file in file:
                print(file)
            print("these are the list of files\n")
        case 3:
            print("______________________________")
            print("ENTER THE FILE NAME\n")
            f=input("")
            with open(f+".txt",'a')as file:
                print(file.write("HELLO WORLD"))
            print("the file is edited successfully \n")
        case 4:
            print("____________________________________")
            print("DELETED THE FILE\n")
            f=input("")
            file=os.remove(f+'.txt')
            print("DELETED THE FILE SUCCESSFULLY\n")
        case 6:
            print("_*-*-*-*-*-*-*-*-*-*-*-*-**--*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("STOP THE PROGRAM\n")
            sys.exit(0)

while 1:
    fi()
    
        

