import nltk as mahedi

print("1. Bangladesh\n2. Taj Mahal\n3. Unreal Engine\n4. BCB\n5. kuet")
a = int(input("Choose an option: "))
if a == 1:
    f = open("trial.txt", "r")
    str = f.read()
elif a == 2:
    f = open("tajMahal.txt", "r")
    str = f.read()
elif a == 3:
    f = open("unreal.txt", "r")
    str = f.read()
elif a == 4:
    f = open("bdckt.txt", "r")
    str = f.read()
elif a == 5:
    f = open("kuet.txt", "r")
    str = f.read()
dummy = []
tags = []
words = []
score = 0
ans = ""
tok = mahedi.sent_tokenize(str)
for t in tok:
    tok1 = mahedi.word_tokenize(t)
    pos = mahedi.pos_tag(tok1)
    flag = 0
    ans = ""
    for i in pos:
        tags.append(i[1])
        words.append(i[0])
        dummy.append(i[1])
    if "CD" not in tags:
        it = 0
        while it < len(tags):
            if tags[it] == 'NNP' or tags[it] == 'NNPS':
                itt = it + 1
                tags[it] = 'null'
                while itt < len(tags):
                    if tags[itt] == 'NNP' or tags[itt] == 'NNPS':
                        tags[itt] = 'null'
                    else:
                        break
                    itt += 1
                break
            it += 1

    else:
        it = 0
        while it < len(tags):
            if tags[it] == 'CD':
                itt = it + 1
                tags[it] = 'null'
                while itt < len(tags):
                    if tags[it] == 'CD':
                        tags[itt] = 'null'
                    else:
                        break
                    itt += 1
                break
            it += 1
    itt = 0
    flag = 0
    while itt < len(tags):
        if dummy[itt] == tags[itt]:
            print(words[itt], end=" ")
        else:
            if flag == 0:
                print("______", end=" ")
                flag = 1
            ans = ans + words[itt] + " "
        itt+=1
    tags=[]
    dummy=[]
    words=[]
    print()
    answer = input("Answer: ")
    answer = answer + " "
    if ans.upper() == answer.upper():
        print("Correct")
        score = score + 1
    else:
        print("Wrong")
    print(ans.split(" "))
    print(answer.split(" "))
print("Your score is: ")
print(score)

