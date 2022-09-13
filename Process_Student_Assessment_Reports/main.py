
from myObjects import Batch
from myObjects import Document
from myObjects import Keyword


PATH = "H:\AIMG-362\clean_files.txt"
fin = open(PATH, "r")

batch = Batch()
keyWordList = ["SUBUNIT","USER_EXTERNAL_ID","PERIOD","COURSE_ID","SURVEY","LAST_NAME","FIRST_NAME", "PATH"]

for fileName in fin:
    
    doc = Document()
    valuesList = fileName.split(" ")
    if len(valuesList) == 11:
        valuesList = [ valuesList[0] , valuesList[2] , valuesList[3], f"{valuesList[5]}{valuesList[6]}" , f"{valuesList[7]}" , valuesList[8] , valuesList[9], valuesList[10] ]
        i=0
        for value in valuesList:
            keyword = Keyword(keyWordList[i],value)
            doc.add_keyWord(keyword)
            i+=1
        batch.add_document(doc)
    else:
        raise Exception("valulist index is off") 

batch.create_index_file("H:\AIMG-362\index_student_assessment_reports.txt", "w")
    

fin.close()
