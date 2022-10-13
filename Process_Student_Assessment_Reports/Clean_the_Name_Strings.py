from myObjects import Batch
        
def format_name(str):
    def handle_errors( str, sub_str, replacemnet_str):
        if sub_str in str:
            str = str.replace(sub_str, replacemnet_str)
            return str
        else:
            return str

    str = str.removesuffix(".pdf\n")
    str = handle_errors(str, "-" , "$")
    str = handle_errors(str,"$Extended", "")
    str = handle_errors(str,"__", " & ")
    str = handle_errors(str, "$Spring_", "-Spring-")
    str = handle_errors(str,"First$Year","First-Year")
    str = handle_errors(str,"K$8", "K-8")   
    str = handle_errors(str,"K $12", "K-12") 
    str = handle_errors(str,"5$12", "5-12")
    str = handle_errors(str,"_", " ")
    #str = handle_errors(str,"- ", "-")
    print(str)
    return str
    
        

fin = open("H:\AIMG-362\myfile.txt", "r")
#fin = open("H:\AIMG-362\dirty_files.txt",, "r")
batch = Batch()

for line in fin:
    str = format_name(line)
    str = str + "$" + line
    if len(str.split("$")) == 11:
        batch.add_cleanFile(str)
    else:
        batch.add_dirtyFile(str)
        

batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "w")  
batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
fin.close()