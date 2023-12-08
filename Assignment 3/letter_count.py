import os
# I wrote two programs because I divided '*' by 100 for holy grail and 
# '*' by 1000(because there are many letters compared to holy grail) for eng news 100k sentences
# But I could have written one program and divide both by 100

# Holy grail text
path = "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/holy_grail.txt" 
file = open(path ,"r",encoding="utf-8")
text = file.read()

dic = {}
byt = text.encode("ascii", "ignore")           # Removes non ascii characters and covert string to byte
string = byt.decode()                          # Convert byte to string

count = 0                                      # To count the number of letters
for character in sorted (string.lower()):      # Change to lowercase
    if character.isalpha():                    # If the character is alphabet(a-z)
            if character in dic.keys():
                dic[character] += 1            # Add 1
            else:
                dic[character] = 1 
            count += 1           
file.close()
for i in dic:
    print (i,' | ', (round(dic[i]/100)) * "*")
print("Total numbers of letters = ", count)

# English news 100k sentences
path = "/Users/melat/OneDrive/Desktop/Python/1DV501/mh225ic_assign3/eng_news_100k-sentences.txt"
file = open(path ,"r",encoding="utf-8")
text = file.read()

dic = {}
byt = text.encode("ascii", "ignore")           # Removes non ascii characters and covert string to byte
string = byt.decode()                          # Convert byte to string

count = 0                                      # To count the number of letters
for character in sorted (string.lower()):      # Change to lowercase
    if character.isalpha():                    # If the character is alphabet(a-z)
            if character in dic.keys():
                dic[character] += 1            # Add 1
            else:
                dic[character] = 1 
            count += 1           
file.close()
for i in dic:
    print (i,' | ', (round(dic[i]/1000)) * "*")
print("Total numbers of letters = ", count)
