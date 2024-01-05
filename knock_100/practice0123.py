"""
自然言語１００本ノック準備運動１−３
"""
"""
#TODO 0
a = "stressed"
b = a[::-1]
print(b)

#TODO 1
a = "パタトクカシーー"
c = a[::2]
print(c)

#TODO 2
p = "パトカー"
t = "タクシー"
combined: str = ''
i = 0
while i < len(p): 
    #w = p[i]
    #print(w)
    tmp_combine_text = f"{p[i]}{t[i]}"
    combined += tmp_combine_text
    i += 1
print(combined)
"""
#TODO 3
origin_word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#a[] = origin_word.split()
words = origin_word.replace(",", " ").replace(".", " ").split()
words_length = [len(i) for i in words]
#print(words_length)

#TODO 4
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
    New Nations Might Also Sign Peace Security Clause. Arthur King Can." 

words = sentence.replace(".", " ").split()
one_letter_number = {1, 5, 6, 7, 8, 9, 15, 16, 19}
symbol = {}
for i, word in enumerate(words, 1):
    if i in one_letter_number:
        symbol[word[:1]] = i
    else:
        symbol[word[:2]] = i

for element, number in symbol.items():
    print(f"{element},{number}")
