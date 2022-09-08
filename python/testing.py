import os
from termcolor import colored

def is_error(li):
    if len(li) > 11:
        return True
    else:
        return False

def handle_extended(str):
    if "_Extended" in str:
        str = str.replace("_Extended", " Extended")
        return str
    else:
        return str

def color_print(str, bool):
    if bool:
        print(colored(str, 'red'))
    else:
        print(colored(str,"green"))

def main():
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
        line = line.replace( "_" , " " )
        line = line.replace("-", "_")
        line = handle_extended(line)
        print(line)
        #li = line.split("_")
        #bool = is_error(li)
        #color_print(line, bool)


        
        
main()