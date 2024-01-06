
"""
#5
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def nGram(sentence, num):

    result = []

    for i in range(len(sentence)- num + 1):
        result.append([sentence[i:i + num]])

    return result

a = "I am an NLPer"
print(nGram(a, 2))

word = a.split()
print(nGram(word, 2))