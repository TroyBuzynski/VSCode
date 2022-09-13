
from myObjects import Batch
from myObjects import Document
from myObjects import Keyword


PATH = "H:\AIMG-362\good_file.txt"
fin = open(PATH, "r")

batch = Batch()
keyWordList = ["SUBUNIT","USER_EXTERNAL_ID","COURSE_ID","PERIOD","SURVEY","LAST_NAME","FIRST_NAME"]

for fileName in fin:
    
    doc = Document()
    valuesList = fileName.split(" ")
    if len(valuesList) == 10:
        valuesList = [ valuesList[0] , valuesList[2] , valuesList[3], f"{valuesList[4]}_{valuesList[5]}_{valuesList[6]}" , f"{valuesList[7]}" , valuesList[8] , valuesList[9] ]
        i=0
        for value in valuesList:
            keyword = Keyword(keyWordList[i],value)
            doc.add_keyWord(keyword)
            i+=1
        batch.add_document(doc)
    else:
        raise Exception("valulist index is off") 

batch.create_index_file("H:\AIMG-362\index.txt", "w")
    

fin.close()
