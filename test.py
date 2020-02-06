from tkinter import *
import nltk as mahedi

'''def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)'''

def check(x,y):
    x1 = x.split(" ") #submitted answer
    y1 = y.split(" ") #actual answer
    xlen = len(x1)
    ylen = len(y1)
    if ylen == 2:
        if y1[0] in x1:
            return True
    elif ylen == 3:
        counter = 0
        if y1[0] in x1:
            counter += 1
        if y1[1] in x1:
            counter += 1
        if counter >= 1:
            return True
    else:
        counter = 0
        if y1[ylen-2] in x1:
            counter += 1
        if y1[ylen-3] in x1:
            counter += 1
        if counter == 2:
            return True
    return False

def select():
    if tkvar.get() == "Bangladesh":
        f = open("trial.txt", "r")
        str1 = f.read()
        print(str1)
    elif tkvar.get() == "Tajmahal":
        f = open("tajMahal.txt", "r")
        str1 = f.read()
        print(str1)
    elif tkvar.get() == "UNREAL":
        f = open("unreal.txt", "r")
        str1 = f.read()
        print(str1)
    elif tkvar.get() == "BCB":
        f = open("bdckt.txt", "r")
        str1 = f.read()
        print(str1)
    elif tkvar.get() == "KUET":
        f = open("kuet.txt", "r")
        str1 = f.read()
        print(str1)
    num = int(tkvar1.get())
    dummy = []
    tags = []
    words = []
    score = 0
    sent = mahedi.sent_tokenize(str1)
    rw = 0
    txtLbl = Label(screen, text="")
    txtLbl.grid(column=3,row=0,rowspan=7)
    txtLbl.config(text=str1)
    labl = Label(screen, text="")
    labl.grid(row=5, sticky=W, columnspan=2)
    var = IntVar()
    button1 = Button(screen, text="Next", command=lambda: var.set(1))
    button1.grid(row=7, sticky=W)
    global answer
    answer = StringVar()
    global ansEntry
    global flag
    ansEntry = Entry(screen, textvariable=answer)
    ansEntry.grid(row=6, sticky=W)
    for ittt in range(0,num):
        tok1 = mahedi.word_tokenize(sent[ittt])
        pos = mahedi.pos_tag(tok1)
        flag = 0
        ans = ""
        ques = ""
        for i in pos:
            tags.append(i[1])
            words.append(i[0])
            dummy.append(i[1])
        if "CD" not in tags:
            flag = 1
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
        flg = 0
        while itt < len(tags):
            if dummy[itt] == tags[itt]:
                print(words[itt], end=" ")
                ques = ques + words[itt] + " "
            else:
                if flg == 0:
                    print("______", end=" ")
                    ques = ques + "______" + " "
                    flg = 1
                ans = ans + words[itt] + " "
            itt += 1
        print("waiting")
        labl.config(text="")
        labl.config(text=ques)
        button1.wait_variable(var)
        uans = answer.get()
        ansEntry.delete(0, END)
        uans = uans + " "
        print("done waiting")
        tags = []
        dummy = []
        words = []
        print()
        rw = rw + 1
        '''if uans.upper() == ans.upper():
            score+=1'''
        if flag == 1 and check(uans.lower(), ans.lower()):
            print("correct")
            score += 1
        elif uans == ans:
            print("correct")
            score += 1
    Score = "Your score is: " + str(score)
    txtLbl.config(text="")
    labl.config(text=Score)


global screen
screen = Tk()
screen.geometry("460x240")
global tkvar
tkvar = StringVar()
global tkvar1
tkvar1 = StringVar()
choice = {'Bangladesh', 'Tajmahal', 'UNREAL', 'BCB', 'KUET'}
tkvar.set('Chose an option')
choice1 = {'5', '10', '15', '20'}
tkvar1.set('Chose an option')
label = Label(screen, text="Topic: ")
label1 = Label(screen, text="Marks: ")
popupMenu = OptionMenu(screen, tkvar, *choice)
popupMenu1 = OptionMenu(screen, tkvar1, *choice1)
button = Button(screen, text="Submit", command=select)
while True:
    print("In")
    label.grid(row=0)
    popupMenu.grid(row=0, column=1, sticky=W)
    label1.grid(row=1)
    popupMenu1.grid(row=1, column=1, sticky=W)
    button.grid(row=2, column=1, sticky=W)
    screen.mainloop()