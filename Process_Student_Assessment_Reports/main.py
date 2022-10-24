"""
Programmer: Troy Buzynski
This script reads in a .txt file that has been formated by the Preprocessor
"""

from myObjects import Batch
from myObjects import Document
from myObjects import Keyword


IN_PATH = "H:\AIMG-362\clean_files.txt"
OUT_PATH = "H:\AIMG-362\index_student_assessment_reports.txt"
KEYWORD_TYPE_LIST = ["HR_ORGANIZATION", "FACULTY_UID", "TERM","SUBJECT","CATALOG_NUMBER" ,"SECTION", "DESCRIPTION", "PATH"]

# Read in File
fin = open(IN_PATH, "r")
# Instantiate Batch obj
batch = Batch()

# Loop though the file, Add all the keywords to the documents and add the document to the batch
for fileName in fin:
    doc = Document()
    valuesList = fileName.split("$")
    if len(valuesList) == len(KEYWORD_TYPE_LIST):
        i=0
        for keyword_value in valuesList:
            keyword = Keyword(KEYWORD_TYPE_LIST[i],keyword_value)
            doc.add_keyWord(keyword)
            i+=1
        batch.add_document(doc)
    else:
        raise Exception("valueList index is off") 
    
# Create index file for Document Import Processor (DIP)
batch.create_index_file(OUT_PATH, "w")

fin.close()
