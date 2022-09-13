from myObjects import Batch
 
class Cleaner():
    def __init__(self,str):
        self.str = str
        self.verified = False

        
    def format_name(self):
        def handle_errors( str, sub_str, replacemnet_str):
            if sub_str in str:
                str = str.replace(sub_str, replacemnet_str)
                return str
            else:
                return str

        self.str = self.str.removesuffix(".pdf\n")
        self.str = handle_errors(self.str, "-" , " ")
        self.str = handle_errors(self.str," Extended", "_Extended")
        self.str = handle_errors(self.str, "2213 Spring", "2213_Spring")
        self.str = handle_errors(self.str,"First Year","First_Year")
        self.str = handle_errors(self.str,"K 8", "K_8")   
        self.str = handle_errors(self.str,"K 12", "K_12") 
        self.str = handle_errors(self.str,"5 12", "5_12")
        self.str = handle_errors(self.str,"\ ", "_")
        self.str = handle_errors(self.str,"= ", "-")
        return self.str
        

fin = open("H:\AIMG-362\myfile.txt", "r")
#fin = open("H:\AIMG-362\error_file.txt", "r")
batch = Batch()

for file in fin:
    
    cleaner = Cleaner(file)
    str = cleaner.format_name()
    str = str + " " + file
   
    if len(str.split(" ")) == 11:
        batch.add_cleanFile(str)
    else:
        batch.add_dirtyFile(str)
        

batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "w")  
batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
fin.close()