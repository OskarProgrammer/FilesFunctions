import os as system


def check(filename:str)->bool:
    if system.path.exists(filename):
        return True
    else:
        return False

class FileReader(object):
    """
    Class which reads file 
    """

    def __init__(self,filename):
        if check(filename):
            print(f"File exists:", filename)
            self.filename = filename
            
        else:
            print(f"File does not exist")
            exit()
        
    def __enter__(self)->str:
        self.file = open (self.filename,"r",encoding = "utf-8")
        return self.file
    
    def __exit__(self,*args):
        print("File had been closed")




class FileWriter(object):
    """
    Class which adds text into the file
    """
    def __init__(self,filename):
        if check(filename):
            print(f"File exists:", filename)
            self.filename = filename
        
        else:
            print(f"File does not exist")
            exit()
    
    def __enter__(self):
        self.file = open (self.filename,"a")
        return self.file
    def __exit__(self,*args):
        print("File had been closed")
