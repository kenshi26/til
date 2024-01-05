"""
自然言語１００本ノック準備運動１−３
"""
#0
a = "stressed"
b = a[::-1]
print(b)

#1
a = "パタトクカシーー"
c = a[::2]
print(c)

#2
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