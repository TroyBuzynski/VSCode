"""
Programmer: Troy Buzynski
This script reads in a .txt file  

"""
from myObjects import Batch
from myObjects import Document
from myObjects import Keyword


IN_PATH = "H:\AIMG-362\clean_files.txt"
OUT_PATH = "H:\AIMG-362\index_student_assessment_reports.txt"
KEYWORD_LIST = ["HR_ORGANIZATION", "COURSE_ID", "USER_EXTERNAL_ID","PERIOD","SUBJECT_AREA","CATALOG_NUMBER" ,"CLASS_SECTION", "DESCRIPTION","LAST_NAME","FIRST_NAME", "PATH"]


fin = open(IN_PATH, "r")
batch = Batch()

for fileName in fin:
    doc = Document()
    valuesList = fileName.split("$")
    if len(valuesList) == len(KEYWORD_LIST):
        i=0
        for value in valuesList:
            keyword = Keyword(KEYWORD_LIST[i],value)
            doc.add_keyWord(keyword)
            i+=1
        batch.add_document(doc)
    else:
        raise Exception("valueList index is off") 

batch.create_index_file(OUT_PATH, "w")
    
fin.close()
