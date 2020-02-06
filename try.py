from tkinter import *
from PIL import ImageTk, Image
import nltk as mahedi

HEIGHT = 500
WIDTH = 600


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def check(x, y):
    x1 = x.split(" ")  # submitted answer
    y1 = y.split(" ")  # actual answer
    ylen = len(y1)
    if ylen == 2: #there is an additional whitespace
        ye = edits1(y1[0])
        ye.add(y1[0])
        for i in ye:
            if i in x1:
                return True
    elif ylen == 3: #there is an additional whitespace
        counter = 0
        ye = edits1(y1[0])
        ye.add(y1[0])
        ye1 = edits1(y1[1])
        ye1.add(y1[1])
        for i in ye:
            if i in x1:
                counter += 1
                break
        for j in ye1:
            if j in x1:
                counter += 1
                break
        if counter >= 1:
            return True
    else: #when ylen is more than 2
        counter = 0
        ye = edits1(y1[ylen - 2])
        ye.add(y1[ylen - 2])
        ye1 = edits1(y1[ylen - 3])
        ye1.add(y1[ylen - 3])
        for i in ye:
            if i in x1:
                counter += 1
                break
        for j in ye1:
            if j in x1:
                counter += 1
                break
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
    txtLbl = Label(lower_frame, text="")
    txtLbl.place(relwidth=1, relheight=1)
    txtLbl.config(text=str1)

    labl = Label(mid_frame, text="")
    labl.place(relwidth=1, relheight=.48)

    var = IntVar()
    button1 = Button(mid_frame, text="Next", font=40, command=lambda: var.set(1))  # jhamela
    button1.place(relx=.75, rely=.53, relwidth=0.25, relheight=.47)
    global answer
    answer = StringVar()
    global ansEntry
    global flag

    ansEntry = Entry(mid_frame, font=40, textvariable=answer)
    ansEntry.place(rely=.53, relwidth=0.65, relheight=.47)
    for ittt in range(0, num):
        tok1 = mahedi.word_tokenize(sent[ittt])
        pos = mahedi.pos_tag(tok1)
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
            flag = 0
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
                    print("____", end=" ")
                    ques = ques + "____" + " "
                    flg = 1
                ans = ans + words[itt] + " "
            itt += 1
        print("waiting")
        labl.config(text="")
        labl.config(text=ques)
        button1.wait_variable(var)  # jhamela
        uans = answer.get()
        ansEntry.delete(0, END)
        uans = uans + " "
        print("done waiting")
        tags = []
        dummy = []
        words = []
        print()
        rw = rw + 1
        if flag == 1 and check(uans.lower(), ans.lower()):
            print("correct")
            score += 1
        elif uans == ans:
            print("correct")
            score += 1
        else:
            print("wrong")

    Score = "Your score is: " + str(score)
    txtLbl.config(text="")
    labl.config(text=Score)


global screen
screen = Tk()
screen.geometry("600x500")

img = ImageTk.PhotoImage(Image.open("knowledge.jpg"))
background_label = Label(screen, image=img)
background_label.place(relwidth=1, relheight=1)

frame = Frame(screen, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.06, relwidth=0.75, relheight=0.07, anchor='n')

global tkvar
tkvar = StringVar()
global tkvar1
tkvar1 = StringVar()
choice = {'Bangladesh', 'Tajmahal', 'UNREAL', 'BCB', 'KUET'}
tkvar.set('Chose an option')
choice1 = {'5', '10', '15', '20'}
tkvar1.set('Chose an option')
popupMenu = OptionMenu(frame, tkvar, *choice)
popupMenu.place(relwidth=0.35, relheight=1)

popupMenu1 = OptionMenu(frame, tkvar1, *choice1)
popupMenu1.place(relx=0.4, relwidth=0.35, relheight=1)

button = Button(frame, text="Submit", font=40, command=select)
button.place(relx=0.8, relheight=1, relwidth=0.2)

mid_frame = Frame(screen, bg='#80c1ff', bd=5)
mid_frame.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.14, anchor='n')

lower_frame = Frame(screen, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.33, relwidth=0.75, relheight=0.6, anchor='n')


print("In")
screen.mainloop()
