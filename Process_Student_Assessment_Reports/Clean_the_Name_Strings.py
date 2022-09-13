from myObjects import Batch
 
class Cleaner():
    def __init__(self,fileName):
        self.fileName = fileName
        self.verified = False

        
    def format_name(self):
        def handle_errors( str, sub_str, replacemnet_str):
            if sub_str in str:
                str = str.replace(sub_str, replacemnet_str)
                return str
            else:
                return str
   
        self.fileName = self.fileName.removesuffix(".pdf\n")
        self.fileName = handle_errors(self.fileName, "-" , " ")
        self.fileName = handle_errors(self.fileName," Extended", "_Extended")
        self.fileName = handle_errors(self.fileName, "2213 Spring", "2213_Spring")
        self.fileName = handle_errors(self.fileName,"First Year","First_Year")
        self.fileName = handle_errors(self.fileName,"K 8", "K_8")   
        self.fileName = handle_errors(self.fileName,"K 12", "K_12") 
        self.fileName = handle_errors(self.fileName,"5 12", "5_12")
        self.fileName = handle_errors(self.fileName,"\ ", "_")
        self.fileName = handle_errors(self.fileName,"= ", "-")
        return self.fileName + "\n"
        

#fin = open("H:\AIMG-362\myfile.txt", "r")
fin = open("H:\AIMG-362\error_file.txt", "r")
batch = Batch()

for file in fin:
    
    cleaner = Cleaner(file)
    fileName = cleaner.format_name()
    
   
    if len(fileName.split(" ")) == 10:
        batch.add_cleanFile(fileName)
    else:
        batch.add_dirtyFile(fileName)
        

batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "a")  
batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
fin.close()