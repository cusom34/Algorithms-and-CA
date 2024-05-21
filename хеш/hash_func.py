def heshf(x, prev):
    return (3*prev+ord(x))%8

#print(heshf('k', 7))

string="London is the capital of Great Britain "

answer=[[] for i in range(8)]
prev=0
temp_word=""
for elem in string:
    if elem ==" ":
        answer[prev]+=[temp_word]
        prev=0
        temp_word=""
        continue
    else:
        prev=heshf(elem, prev)
        temp_word+=elem


for elem in answer:
    print(elem)
    
for i in range(8):
        #print(i, end='')
    print(len(answer[i]), end='')