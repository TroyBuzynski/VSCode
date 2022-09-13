#from curses.ascii import isalpha
import os

def createIndexFile(fileName):
    #If the file already exitsts, delete it.
    #if os.path.exists(fileName):
     #   os.remove(fileName)
    return open(fileName, "a")

def DIP_format(fout, keyWordList, valuesList):
    fout.write("\nBEGIN\n")
    #Initialize a count variable
    i = 0
    #Iterate through the list of values
    for value in valuesList:
        #Tag each value with a KeywordType
        fout.write(keyWordList[i] + " : " + value + "\n")
        i+=1
    
def handle_errors( str, sub_str, replacemnet_str):
    if sub_str in str:
        str = str.replace(sub_str, replacemnet_str)
        return str
    else:
        return str

def create_values_list(li):
        valuesList = [ li[0] , li[2] , li[3], f"{li[4]}_{li[5]}_{li[6]}" , f"{li[7]}" , li[8] , li[9] ]
        return valuesList


def main():
    #Read in the File
    file = input("Enter 1 or 2: ") 
    if file == "1":
        path = "H:\AIMG-362\myfile.txt"
    elif file == "2":
        path = "H:\AIMG-362\error_file.txt"
    else: 
        print("Invalid input")
    fin = open(path, "r" )

    #Create an index file for DIP
    fout1 = open("H:\AIMG-362\Index.txt", "a")
    fout2 = open("H:\AIMG-362\error_file.txt", "w")

    #Create a list of all the Keywords on the DocType
    keyWordList = ["SUBUNIT","USER_EXTERNAL_ID","PERIOD","COURSE_ID","SURVEY","LAST_NAME","FIRST_NAME"]
    

    for str in fin:
        str = str.replace("-", " ")
        str = str.removesuffix(".pdf\n")
        str = handle_errors(str," Extended", "_Extended")
        str = handle_errors(str, "2213 Spring", "2213_Spring")
        str = handle_errors(str,"First Year","First_Year")
        str = handle_errors(str,"K 8", "K_8")

        #split the file name into individual values
        li = str.split(" ")
            

        #Write to txt file
        #If there are no errors, Format the string for indexing through DIP and create index file 
        if len(li) == 10:
            DIP_format(fout1,keyWordList,create_values_list(li))

        elif len(li) > 10 and li[-1].isalpha() and li[-2].isalpha() and li[-3].isalpha():
            separator = "-"
            x = separator.join(li[-3:-1])
            li.pop(-2)
            li.pop(-2)
            li.insert(-1,x)
            DIP_format(fout1,keyWordList,create_values_list(li))

        #Else, write string to error file
        else:
            fout2.write(str + "\n")
            
            

    fin.close()       
    fout1.close()
    fout2.close()


main()