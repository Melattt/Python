import word_set as ws
import table as tbl
import divide_text_into_words_new as dvi
import os
import matplotlib.pyplot as plt

name = os.getcwd()
name += "/holy_grail.txt" #holy_grail, eng_news_100K-sentences
names = dvi.read_words(name)
# names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Måns", "Amer", "David"] # 17 persons


word_set = ws.new_empty_set()
root = tbl.new_empty_root()
u_w = ws.count(word_set)

for s in names:
    ws.add(word_set,s)

# deleting non-words.
delete = ["'"]
x = 0
a = "abcdefghijklmnopqrstuvwxyz"
while x < 2:
    for i in a:
        if i == "I":
            pass
        else:
            delete.append(i)
    a = a.upper()
    x += 1
# print(delete)
for i in delete:   
    ws.remove(word_set,i)

words = []
nmb = []
l = 0
longest = 0
g = ""
k = ""
for i in word_set:
    for n in i:
        for x in names:
            if n == "":
                pass
            else: 
                if n == x:
                    g = x
                    l += 1 
                if longest < l:
                    longest = l
                    k = x
        words.append(g)    
        nmb.append(l)
        l = 0 
u_w = ws.count(word_set)
# print(k)
# print(longest)
# print(words)
# print(nmb)    
# print(u_w)

j = 0
while j < u_w:
    tbl.add(root, words[j], nmb[j])
    j += 1


# pairs = tbl.get_all_pairs(root)              
# print("All pairs: ",pairs)   
bins = []
for i in range(1, longest + round(longest/10)):
    i += -0.5
    bins.append(i)




u = os.getcwd()
plt.xlabel("Count")
plt.ylabel("Frequency")

name = name.replace(u, "")
plt.hist(nmb, bins=bins, edgecolor="black", log=True)
plt.title(f"Histogram of Frequency/count in {name}")
plt.show()

pairs = tbl.get_all_pairs(root)     
# print("All pairs: ",pairs)
# print("To_string: ",tbl.to_string(root))   



j = 0
k = tuple()
t = 0
while t < 10:
    for i in pairs:
        if longest + -1*j in i:
            k += i
            t +=1
    j +=1 

print(k)
