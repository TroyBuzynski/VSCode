import os

def createIndexFile(fileName):
    #If the file already exitsts, delete it.
    if os.path.exists(fileName):
        os.remove(fileName)
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
    


#Read in the File
fin = open("H:\AIMG-362\myfile.txt", "r" )

#Create an index file for DIP
fout1 = createIndexFile("Index.txt")
fout2 = createIndexFile("Error_Index.txt")

#Create a list of all the Keywords on the DocType
keyWordList = ["SUBUNIT","USER_EXTERNAL_ID","COURSE_ID","PERIOD","SURVEY","LAST_NAME","FIRST_NAME"]

#Iterate throught the input file line by line 
for line in fin:
    line = line.removesuffix(".pdf\n")

    #split the file name into individual values
    li = line.split("-")
    valuesList = [ li[0] , li[2] , f"{li[6]}_{li[7]}", f"{li[3]}_{li[4]}" , f"{li[5]}_{li[6]}_{li[7]}_{li[8]}" , li[9] , li[10] ]
    
    #Write to txt file
    #If there are errors, write the string to a file
    if len(li) > 11:
        fout2.write(line + "\n")
    #Else, Formate the string for indexing through DIP
    else:
        DIP_format(fout1,keyWordList,valuesList)

fin.close()       
fout1.close()
fout2.close()


    
    