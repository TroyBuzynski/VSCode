

class Frank:
    def find_intersection(self,list1,list2):
        return  

class File:
    def __init__(self,path = None):
        self.path = path
        self.list = []
        if self.path != None:
            fin = open(self.path,"r")
            fin.readline()
            for line in fin:
                line=line.upper().strip("\"\n")
                self.list.append(line)
            fin.close()
        

            
        
    def get_list(self):
        return self.list
 
 
 
def write(list,out_path):
    fout = open(out_path, "w")
    for item in list:
        item += "\n"
        fout.write(item) 
    fout.close() 
    
           
current_OnBase_users = File(r"Document_Imaging_SRS\current_OnBase_users.txt")
users_no_active_roles = File(r"Document_Imaging_SRS\users_no_active_roles.txt")
users_email_list = File(r"Document_Imaging_SRS\users_email_list.txt")

users_to_delete = list(set(users_no_active_roles.get_list()) & set(current_OnBase_users.get_list()))
users_to_delete.sort()
write(users_to_delete,r"Document_Imaging_SRS\users_to_delete.txt")


email_list = list(set(users_email_list.get_list()) & set(current_OnBase_users.get_list()))


email_list.sort()
write(email_list,r"Document_Imaging_SRS\new_email_list.txt")