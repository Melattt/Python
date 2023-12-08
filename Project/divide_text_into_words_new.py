import re 

def read_words(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        words = re.sub("[^a-zA-Z-']+", " ", content)
        words = re.split('\ |\.|\/|\n', words)
        return words


# Program

#f=read_words("/Users/melat/OneDrive/Desktop/Python/Python_project/holy_grail.txt")
#print(f)
f=read_words("/Users/melat/OneDrive/Desktop/Python/Python_project/eng_news_100K-sentences.txt")
#print(f)