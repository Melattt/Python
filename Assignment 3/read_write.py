import os
#Number 1
def read_file(file_path):
    # Open the file
    with open(file_path, "r",encoding="utf8") as file:
        full_text= " "
        for line in file:
            full_text += line
        return full_text
       
         
#Number 2
def write_file(lines, file_path):
    # Open the file
    with open(file_path,"w",encoding="utf8") as file:
        file.writelines(lines)
        return lines



#Number 1
#Program starts  
file_path= "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/read_write.txt"       # Path pointing to directory containing the specified files
print(read_file(file_path))

#Number 2
#Program starts
file_path= "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/read_write.txt"       # Path pointing to directory containing the specified files
lines="""Darkness cannot drive out darkness;
only light can do that. Hate cannot
drive out hate; only love can do that.""" 
print(write_file(lines, file_path))