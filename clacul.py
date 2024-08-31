
# project calculator (ismail)
from tkinter import*
v = Tk()
v.title("Calculator")
v.geometry('600x800+40+120')
v.config(bg='pink')
def buttquit():
    quit()
def click(number):
    current=enter.get()
    enter.delete(0,END)
    enter.insert(END,(current)+str(number))
def egale():
    equation=enter.get()
    try:
        result=eval(equation)
        enter.delete(0,END)
        enter.insert(END,str(result))
    except:
        enter.delete(0,END)
        enter.insert(END,'Erour')
        

def delete():
    enter.delete(0,END)

frame1=Frame(v,bg='black',width=600, height=300, relief='solid')
frame1.place(x=1,y=1)


label_myname = Label(frame1, text = "ismail" , font=("Times",9,"bold"), bg="orange", bd = 6)
label_myname.place(x=0,y=0)


label=Label(frame1, text='Calculator', bg='black', fg='yellow', font=('Times',9,'bold'), bd=6)
label.place(x=180,y=10)

buttquit=Button(frame1,text='X', bg='black', fg='red',font=('Times',7,'bold'),relief='solid', command=buttquit)
buttquit.place(x=510,y=0)

enter=Entry(frame1,text=' ', bg='white',fg='black', font=('Times',12,'bold'),width=17, bd=12, relief='solid')
enter.place(x=40,y=120)

frame2=Frame(v,bg='Gray', width=600,height=500, relief='solid')
frame2.place(x=1,y=300)
π=float('3.14')

buttons=[
['1',1,1],['2',150,1],['3',300,1],['4',450,1],['5',1,100],['6',150,100],['7',300,100],['8',450,100],['9',1,200],['0',150,200],['.',300,200],['+',450,200],['*',1,300],['-',150,300],['/',450,300],['π',1,400],['(',150,400],[')',300,400]
]

                  
for button in buttons:
    butt=Button(frame2,text=button[0], bg='black',fg='white', font=('Times',7,'bold'), bd=10, command=lambda b=button[0]:click(b))
    butt.place(x=button[1],y=button[2])

buttegale=Button(frame2,text='=',bg='black',fg='white',font=('Times',7,'bold'),bd=10, command=egale)
buttegale.place(x=300,y=300)

buttc=Button(frame2,text='C',bg='black',fg='white',font=('Times',7,'bold'),bd=10,command=delete,relief='groove')
buttc.place(x=450,y=400)

v.mainloop()
