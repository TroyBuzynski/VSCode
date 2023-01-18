import os
import sys
from myObjects import Batch
from myObjects import Document
from myObjects import Keyword
from myObjects import File


PATH = input("Enter the path: ")
KEYWORD_TYPE_LIST = ["HR_ORGANIZATION", "FACULTY_UID", "TERM","SUBJECT","CATALOG_NUMBER" ,"SECTION", "DESCRIPTION", "PATH"]

def construct_documents(KEYWORD_TYPE_LIST, batch):
    """ Loop though the files, Add all the keywords to the documents and add the document to the batch.

    Args:
        KEYWORD_TYPE_LIST (List): List of Keyword Types.
        batch (Batch): Custom Batch Object
    """
    for fileName in batch.get_cleanFiles():
        doc = Document()
        valuesList = fileName.split("$")
        i=0
        for keyword_value in valuesList:
            keyword = Keyword(KEYWORD_TYPE_LIST[i],keyword_value)
            doc.add_keyWord(keyword)
            i+=1
        batch.add_document(doc)


def main():
    
    
    #Construct a list of all the fileNames in the IN_Path directory.
    fileList = os.listdir(PATH)

    # instantiate Batch obj
    batch = Batch()
    
    # Loop through the fileList
    for fileName in fileList:
        file = File(fileName)
        file.format()#format fileName
        # verify the string contains exactly 1 value for every keyword type
        if file.get_length() == len(KEYWORD_TYPE_LIST):
            batch.add_cleanFile(file.get_fileName())
        else:
            batch.add_dirtyFile(file.get_fileName())
    
    if len(batch.dirtyFiles) > 0:
        print("All the files are not formated correctly.\nBelow are the incorrect files:\n\n")
        batch.print_dirtyFiles()
        #write the strings to a file
        batch.write_cleanFiles(PATH + "\clean_files.txt", "w")  
        batch.write_dirtyFiles(PATH + "\dirty_files.txt", "w")
    else:
        print("All the file are correctly formated.\n")
        construct_documents(KEYWORD_TYPE_LIST, batch)
        # Create index file for Document Import Processor (DIP)
        batch.create_index_file(PATH + "\index_student_assessment_reports.txt", "w")
        
    
main()