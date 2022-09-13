from myObjects import Batch
        
def format_name(str):
    def handle_errors( str, sub_str, replacemnet_str):
        if sub_str in str:
            str = str.replace(sub_str, replacemnet_str)
            return str
        else:
            return str

    str = str.removesuffix(".pdf\n")
    str = handle_errors(str, "-" , " ")
    str = handle_errors(str," Extended", "_Extended")
    str = handle_errors(str, "2213 Spring", "2213_Spring")
    str = handle_errors(str,"First Year","First_Year")
    str = handle_errors(str,"K 8", "K_8")   
    str = handle_errors(str,"K 12", "K_12") 
    str = handle_errors(str,"5 12", "5_12")
    str = handle_errors(str,"_ ", "_")
    str = handle_errors(str,"- ", "-")
    
    li = str.split(" ")
    if len(li) == 10:
        li = [ f"{li[0]} "  , f"{li[2]} " , f"{li[3]} ", f"{li[5]}{li[6]} " , f"{li[7]} " , 
                f"{li[8]} " , f"{li[9]}" ]
        str = ""
        for item in li:
            str = str + item
        print(str)
        return str
    else:
        print(str)
        return str
        

fin = open("H:\AIMG-362\myfile.txt", "r")
#fin = open("H:\AIMG-362\dirty_files.txt",, "r")
batch = Batch()

for file in fin:
    str = format_name(file)
    str = str + " " + file
    if len(str.split(" ")) == 8:
        batch.add_cleanFile(str)
    else:
        batch.add_dirtyFile(str)
        

batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "w")  
batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
fin.close()