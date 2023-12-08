import os

def count_py_lines(dir_path):
    
    nonblank_line = 0

    tentries=os.scandir(dir_path)              # To scan directory path(scan main folder(1DV501))
    for entries in tentries:                   
        entries=os.scandir(entries)            # To scan folders inside 1DV501
    
        for entry in entries: 
            entry=os.path.join(dir_path,entry)    # To join more than one path
            
            if os.path.isfile(entry):                       # If the entry is file
                if entry.endswith(".py") and  entry!="":    # If it's a python file and not empty

                    with open (entry,"r") as file:     # Open the entry
                        for line in file:
                            
                            if line.strip() != "":     # Count if line is not empty
                                nonblank_line += 1
                    
    return nonblank_line   


#Program starts
path = "/Users/melat/OneDrive/Desktop/Python/1DV501"
print(count_py_lines(path))