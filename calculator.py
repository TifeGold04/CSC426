from tkinter import *

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Simple Calculator")
root.geometry("500x600")

entry = Entry(root, width=20, font=('Arial',20))
entry.pack(pady=10)

buttons = [
'7','8','9','/',
'4','5','6','*',
'1','2','3','-',
'0','.','+','%',
'^','C','=','//'
]

frame = Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    if button == "=":
        Button(frame,text=button,width=5,height=2,
               command=calculate).grid(row=row,column=col)
    elif button == "C":
        Button(frame,text=button,width=5,height=2,
               command=clear).grid(row=row,column=col)
    elif button == "^":
        Button(frame,text=button,width=5,height=2,
               command=lambda: click("**")).grid(row=row,column=col)
    elif button == "//":
        Button(frame,text="\\",width=5,height=2,
               command=lambda: click("//")).grid(row=row,column=col)
    else:
        Button(frame,text=button,width=5,height=2,
               command=lambda b=button: click(b)).grid(row=row,column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()