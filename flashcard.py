from tkinter import *
from sys import argv
script,n=argv
import random

def get_words(word_file=n):
    good_word = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            words =len(word.split())
            cunt=int(words)
            #print(words)
            if int(len(word.split())) < 3:
                good_word.append(word)
    word =random.choice(good_word)
    return word


def nClick(press):
    if press==1:
        global counter
        counter = 1
    elif press==2:
        counter = 2
    return counter

def first_guess_points(counter):
    global right
    global wrong     
    if counter==1:
        right+=1
    elif counter==2:        
        wrong+=1
    elif counter==3:
        right=0
        wrong=0
        
    return (counter,right ,wrong)


def main():

    turn=0
    if turn==0:
        q=first_guess_points(3)
        turn+=1
    for i in range(5):
        
        window =Tk()
        window.geometry("500x350")

        #label for question
        var_1=StringVar()
        label =Label(window, font="Times 22 bold",textvariable=var_1)
        label.place(x=15,y=45)
        word=get_words()
        h=word.split()
        var_1.set(h[0])

        #label for wrong point        
        var_4=StringVar()
        label =Label(window, font="Times 22 bold",textvariable=var_4)
        label.place(x=100,y=160)
        var_4.set(wrong)

        #label for right point
        var_5=StringVar()
        label =Label(window, font="Times 22 bold",textvariable=var_5)
        label.place(x=50,y=160)
        var_5.set(right)

        def answer_window(h):
            var_1=StringVar()
            label =Label(window, font="Times 22 bold",textvariable=var_1)
            label.place(x=50,y=130)
            var_1.set(h[1])

        
        #button for see answer
        but1=Button(window, text="see answer",command=lambda:answer_window(h))
        but1.place(x = 10,y = 90)

        #button for right point 
        but2=Button(window, text="am right",command=lambda:nClick(press=1))
        but2.place(x = 10,y =200)

        #button for wrong point
        but3=Button(window, text="am wrong",command=lambda:nClick(press=2))
        but3.place(x = 100,y =200)

        def close_window():
            window.destroy()

        button=Button(text = "next question", command = close_window)
        button.place(x=150,y=300)
        window.mainloop()
        
        c=first_guess_points(counter)
      

if __name__ == "__main__":
    main()
