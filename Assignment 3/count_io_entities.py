import os
#Number 1
def count_directories(dir_path):
    
    entries=os.scandir(dir_path)    # Scans directory for a given path
    no_dir=0

    for entry in entries:

        if entry.is_dir():          # If the entry is directory
            no_dir += 1
    return no_dir



#Number 2
def count_py_files(dir_path):
     
    n=0
    lst=os.listdir(dir_path)        # Lists directory for a given path
    for s in lst:
        if s.endswith(".py"):       # If the file ends with ".py"
            n+=1
    return n
 

#Number 1
path = "/Users/melat/OneDrive/Desktop/Python/1DV501"         # Path pointing to directory containing sub-directories
n_dirs=count_directories(path)
print( "Dir Count:", n_dirs)
      
#Number 2     
path = "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3"       # Path pointing to directory containing .py files
print("Py-file Count:", count_py_files(path))
     