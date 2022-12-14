#Programmer: Troy Buzynski       

class Batch:
    def __init__(self):
        self.documents = []
        #files that are formated correctly
        self.cleanFiles = []
        #fileNames that are formated incorrectly
        self.dirtyFiles = []
        
    def get_cleanFiles(self):
        return self.cleanFiles
   
    def add_document(self,document):
        self.documents.append(document)
    
    def add_cleanFile(self,fileName):
        self.cleanFiles.append(fileName)
    
    def add_dirtyFile(self,fileName):
        self.dirtyFiles.append(fileName)
    
    def print_cleanFiles(self):
        for fileName in self.cleanFiles:
            print(fileName) 
            
    def print_dirtyFiles(self):
        for fileName in self.dirtyFiles:
            print(fileName)
            
    def print_docNames(self):
        for document in self.documents:
            for keyword in document.get_keyWords():
                print(keyword.get_type(), keyword.get_value())
                
           
    def create_index_file(self, path, arg):
        """Constructs a .txt file that can be interpereted by OnBase Document Import Processor (DIP)

        Args:
            path (String): Location and Name of the file. Ex: C:\Documents\myFile.txt
            arg (char): w - to overwrite existing file
                        a - to append to existing file
        """
        print("Constructing Index File.\n")
        fout = open(path, arg)
        for document in self.documents:
            fout.write("\nBEGIN:\n")
            for keyword in document.get_keyWords():
                fout.write(f"{keyword.get_type()}:{keyword.get_value()}\n" )
        fout.close
        print("Index file Location: " + path + "\n\n")
        
    def write_cleanFiles(self, path, arg):
        fout = open(path, arg)
        for fileName in self.cleanFiles:
            fout.write(fileName) 
        fout.close()
        
    def write_dirtyFiles(self, path, arg):
        fout = open(path, arg)
        for fileName in self.dirtyFiles:
            fout.write(fileName)
        fout.close()  
        
        
class Document:
    def __init__(self):
        self.keyWords = []
        
    def add_keyWord(self,keyWord):
        self.keyWords.append(keyWord)
        
    def get_keyWords(self):
        return self.keyWords
        
      
class Keyword:
    def __init__(self,type,value = None):
        self.type = type
        self.value = value
    
    def get_type(self):
        return self.type
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
        
        
class File:
    
    @staticmethod
    def handle_errors( str, sub_str, replacemnet_str):
        """
        Searches a string for a substring, if substring is found then it is replaced

        Args:
            str (String): The string to search through.
            sub_str (String): The string to be found and replaced.
            replacemnet_str (String): The replacement string.

        Returns:
            String: The modified sting if substring is found or the original string if substring is not found. 
        """
        if sub_str in str:
            str = str.replace(sub_str, replacemnet_str)
            return str
        else:
            return str
        
    def __init__(self,fileName):
        self.fileName = fileName
        
    def get_fileName(self):
        return self.fileName
    
    def get_length(self):
        return len(self.fileName.split("$"))
    
    
    def format(self):
        """ 
        Modifies the fileName to fit the following format:
        HR_ORGANIZATION$FACULTY_UID$TERM$SUBJECT$CATALOG_NUMBER$SECTION$DESCRIPTION$PATH
        """
        str = self.fileName
        str = str.removesuffix(".pdf\n") 
        str = self.handle_errors(str, "_" , " ")
        str = self.handle_errors(str,"-Extended", "")
        str = self.handle_errors(str,"  ", " & ")
    
        li = str.split("-")
        # Selecting the needed Keywords and adding a unique separator
        str = li[0] + "$" + li[1] + "$" + li[3] + "$" + li[5] + "$" + li[6] + "$" + li[7] + "$" + li[8]
        #add the file name to the end of the string
        str = str + "$" + self.fileName + "\n"
        self.fileName = str
















































class Survey:
    
    __errorList = None
    @staticmethod
    def get_errorList():
        if Survey.__errorList == None:
            Survey.__errorList = []
        return Survey.__errorList
        
    
    def __init__(self,docName,filePath):
        self.docName = docName
        self.path = filePath
        self.error = False

    def formatName(self):
        def handle_errors( str, sub_str, replacemnet_str):
            if sub_str in str:
                str = str.replace(sub_str, replacemnet_str)
                return str
            else:
                return str
        self.docName = self.docName.replace("-", " ")
        self.docName = self.docName.removesuffix(".pdf\n")
        self.docName = handle_errors(self.docName," Extended", "_Extended")
        self.docName = handle_errors(self.docName, "2213 Spring", "2213_Spring")
        self.docName = handle_errors(self.docName,"First Year","First_Year")
        self.docName = handle_errors(self.docName,"K 8", "K_8")
        
     
     
    def splitName(self):
        li = self.docName.split(" ")
        if len(li) == 10:
            pass
        elif len(li) > 10 and li[-1].isalpha() and li[-3].isalpha():
            separator = "-"
            lastName = separator.join(li[-3:-1])
            li.pop(-2)
            li.pop(-2)
            li.insert(-1,lastName)
        else:
            self.error = True
            




    def get_subunit(self):
        return self.subunit

    def set_subunit(self,aStr):
        self.subunit = aStr

    def get_userEternalID(self):
        return self.userExternalID

    def set_userExternalID(self,aStr):
        self.userExternalID = aStr

    def get_period(self):
        return self.period

    def set_period(self,aStr):
        self.period = aStr
        
    def get_courseID(self):
        return self.courseID

    def set_courseID(self,aStr):
        self.courseID = aStr
        
    def get_survey(self):
        return self.survey

    def set_survey(self,aStr):
        self.survey = aStr
    
    def get_lastName(self):
        return self.lastName

    def set_lastName(self,aStr):
        self.lastName = aStr

    def get_firstName(self):
        return self.firstName

    def set_firstName(self,aStr):
        self.firstName = aStr
class DIP:
    def __init__(self,fileOut,keyWordList,valuesList):
        self.fileOut = fileOut
        self.keyWordList = keyWordList
        self.valuesList = valuesList
        
    def createIndexFile(self):
        
        self.fileOut.write("\nBEGIN\n")
        #Initialize a count variable
        i = 0
        #Iterate through the list of values
        for value in self.valuesList:
            #Tag each value with a KeywordType
            self.fileOut.write(self.keyWordList[i] + " : " + value + "\n")
            i+=1