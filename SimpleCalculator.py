from tkinter import * 
win=Tk() 
win.geometry("600x400" ) 
win.title("Simple Calculator") 
win.resizable(0,0) 
#functions for calling:- 
def add(): 
    n1=int(entn1.get()) 
    n2=int(entn2.get()) 
    res=n1+n2 
    lblre.config(text="Result: "+str(res)) 
def sub(): 
    n1=int(entn1.get()) 
    n2=int(entn2.get()) 
    res=n1-n2 
    lblre.config(text="Result: "+str(res)) 
def mul(): 
    n1=int(entn1.get()) 
    n2=int(entn2.get()) 
    res=n1*n2 
    lblre.config(text="Result: "+str(res))  
def div(): 
    n1=int(entn1.get()) 
    n2=int(entn2.get()) 
    res=n1/n2 
    lblre.config(text="Result: "+str(res))              
#Labels for the entry in the calc:- 
lbln1=Label(win,text="Enter first no :",fg="green" ,font=("Arial 18 bold")) 
lbln1.place(x=20,y=50) 
lbln2=Label(win,text="Enter second no:",fg="green",font=("Arial 18 bold")) 
lbln2.place(x=20,y=100) 
 
lblre=Label(win,text="Result :",fg="green",font=("Alegrian 18 bold")) 
lblre.place(x=20,y=150) 
 
#entry in the labels :- 
entn1=Entry(win,font=("Arial 15"),fg="white",bg="grey",bd="5") 
entn1.place(x=220,y=50) 
entn2=Entry(win,font=("Arial 15"),fg="white",bg="grey",bd="5") 
entn2.place(x=220,y=100) 
 
#buttons :- 
btnadd=Button(win,text="ADD",fg="grey",font=("Arial 17 bold"),command=add) 
btnadd.place(x=40,y=200) 
 
btnsub=Button(win,text="SUB",fg="grey",font=("Arial 17 bold"),command=sub) 
btnsub.place(x=150,y=200) 
 
btnmul=Button(win,text="MUL",fg="grey",font=("Arial 17 bold"),command=mul) 
btnmul.place(x=250,y=200) 
 
btndiv=Button(win,text="DIV",fg="grey",font=("Arial 17 bold"),command=div) 
btndiv.place(x=350,y=200) 
win.mainloop()
