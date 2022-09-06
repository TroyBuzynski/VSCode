import os
from termcolor import colored


def cond_color_print(line, i):
    if i != 8:
        print(colored(line, 'red'))
    else:
        print(colored(line,"green"))
        
        
        

    

#Read in the File
fin = open("H:\AIMG-362\myfile.txt", "r" )

#Create an index file for DIP
if os.path.exists("Index.txt"):
    os.remove("Index.txt")
fout = open("Index.txt","a")

#Create a list of all the Keywords on the DocType
keyWordList = ["SUBUNIT","USER_EXTERNAL_ID","COURSE_ID","PERIOD","SURVEY","LAST_NAME","FIRST_NAME"]

#Iterate throught the input file line by line 


for line in fin:
    line = line.removesuffix(".pdf\n")
    print(line)
    
    if os.path.exists("Index.txt"):
    os.remove("Index.txt")
if os.path.exists("Error_Index.txt"):
    os.remove("Error_Index.txt")
fout = open("Index.txt","a")
fout2 = open("Error_Index.txt","a")