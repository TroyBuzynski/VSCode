


from myObjects import Batch

# Takes in a string and modifies it to fit the following format:
# HR_ORGANIZATION$FACULTY_UID$TERM$SUBJECT$CATALOG_NUMBER$SECTION$DESCRIPTION
def format_name(str):
    # Replace a substring with replacement string
    def handle_errors( str, sub_str, replacemnet_str):
        if sub_str in str:
            str = str.replace(sub_str, replacemnet_str)
            return str
        else:
            return str

    str = str.removesuffix(".pdf\n") 
    str = handle_errors(str, "_" , " ")
    str = handle_errors(str,"-Extended", "")
    str = handle_errors(str,"  ", " & ")
    
    li = str.split("-")
    # Selecting the needed Keywords and adding a unique separator
    str = li[0] + "$" + li[1] + "$" + li[3] + "$" + li[5] + "$" + li[6] + "$" + li[7] + "$" + li[8]
    return str
         
# Read in File
fin = open("H:\AIMG-362\myfile.txt", "r")
# instantiate Batch obj
batch = Batch()
# Loop through the file
for line in fin:
    #formate each line
    str = format_name(line)
    #add the file name to the end of the string
    str = str + "$" + line
    # verify the string contains exactly 8 keywords
    if len(str.split("$")) == 8:
        batch.add_cleanFile(str)
    else:
        print(str)
        batch.add_dirtyFile(str)
        
#write the strings to a file
batch.write_cleanFiles("H:\AIMG-362\clean_files.txt", "w")  
batch.write_dirtyFiles("H:\AIMG-362\dirty_files.txt", "w")
# Close the read in file.
fin.close()