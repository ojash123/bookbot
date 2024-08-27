
def word_count(text)->int : 
    count = 0
    words = text.split()
    count = len(words)
    return count
import string
def char_count(text) :
    text_lcase = text.lower()
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for char in text_lcase:
        if char in string.ascii_lowercase:
            d[char] += 1
    return d

def gen_report(char_counts):
    l = sorted(char_counts.items(), key= lambda item:item[1], reverse= True)
    #print(l)
    for (key, value) in l:
        print(f"The '{key}' character was found {value} times")


def main():    
    with open("books/frankenstein.txt") as text:
        file_contents = text.read()
        wc = word_count(file_contents)
        print(f"The word count is {wc}")
        charcount = char_count(file_contents)
        #print(charcount)
        gen_report(charcount)
main()