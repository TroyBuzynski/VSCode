#from myObjects import Batch
def handle_errors( str, sub_str, replacemnet_str):
    if sub_str in str:
        str = str.replace(sub_str, replacemnet_str)
        return str
    else:
        return str  
def format_name(str):

    #str = str.removesuffix(".pdf\n")
    str = handle_errors(str, "-" , "$")
    str = handle_errors(str,"$Extended", "")
    str = handle_errors(str,"__", " & ")
    str = handle_errors(str, "$Spring_", "-Spring-")
    str = handle_errors(str,"First$Year","First-Year")
    str = handle_errors(str,"K$8", "K-8")   
    str = handle_errors(str,"K$12", "K-12") 
    str = handle_errors(str,"5$12", "5-12")
    str = handle_errors(str,"_", " ")
    #str = handle_errors(str,"- ", "-")
    return str
    
        

fin1 = open("H:\\ver_rep.txt", "r")
fin2 = open("H:\\myfile.txt", "r")
li = []
for line in fin2:
    li.append(line)
i = 0    
for line in fin1:
    if line in li:
        i+=1
    else:
        print(line)
print(i)       

        
    

#batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "w")  
#batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
