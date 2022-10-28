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


def GetChildItem(dir):
    for item in os.listdir(dir):
        print(item)
    

def main():
    GetChildItem("H:\AIMG-362\PDF_Reports_2213_final(copy)")


        
        
main()