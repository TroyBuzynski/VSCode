import os
from termcolor import colored


def new_func(line, i):
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
    line1 = line
    
    line1 = line1.split("-")
    while  line1[0] != '2213':
        line1.pop(0)
        

    
    i = len(line1)
    new_func(line1, i)
    
    
