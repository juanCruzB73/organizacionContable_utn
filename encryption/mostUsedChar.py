ascii_chars = ''.join(chr(i) for i in range(256))

def countLetters(content):
    mostUsedLetters={}
    for char in range(len(content)):
        mostUsedLetters[content[char]]=1+mostUsedLetters.get(content[char],0)
        sorted_dic=sorted(mostUsedLetters.items(), key=lambda x: x[1], reverse=True)
    return sorted_dic

def getChar(lis):
    return lis[1][0]

def makePassword(char):
    password=(ascii_chars.find(char))-(ascii_chars.find("e")%256)
    return password

text="13164sfnaibada"
text_dic=countLetters(text)
print(text_dic)
char=getChar(text_dic)
print(char)