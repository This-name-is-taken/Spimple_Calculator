from tkinter import *

root = Tk()
root.title("Basic_Calculator")



def click(x):
	c = t.get()
	t.delete(0, END)
	t.insert(0, str(c)+str(x))

def add():
	global c1, flag
	c1 = t.get()
	t.delete(0, END)
	flag = 1

def sub():
	global c1, flag
	c1 = t.get()
	t.delete(0, END)
	flag = -1

def equ():
	c2 = t.get()
	t.delete(0, END)
	if flag == 1:
		t.insert(0, int(c1) + int(c2))
	elif flag == -1:
		t.insert(0, int(c1) - int(c2))

def clr():
	t.delete(0, END)





t = Entry(root, width=57, borderwidth=3)
t.grid(row=0, column=0, columnspan=3)


b0 = Button(root, text="0", padx= 50, pady=50, command=lambda: click(0))
b0.grid(row=1, column=0)

b1 = Button(root, text="1", padx= 50, pady=50, command=lambda: click(1))
b1.grid(row=1, column=1)

b2 = Button(root, text="2", padx= 50, pady=50, command=lambda: click(2))
b2.grid(row=1, column=2)

b3 = Button(root, text="3", padx= 50, pady=50, command=lambda: click(3))
b3.grid(row=2, column=0)

b4 = Button(root, text="4", padx= 50, pady=50, command=lambda: click(4))
b4.grid(row=2, column=1)

b5 = Button(root, text="5", padx= 50, pady=50, command=lambda: click(5))
b5.grid(row=2, column=2)

b6 = Button(root, text="6", padx= 50, pady=50, command=lambda: click(6))
b6.grid(row=3, column=0)

b7 = Button(root, text="7", padx= 50, pady=50, command=lambda: click(7))
b7.grid(row=3, column=1)

b8 = Button(root, text="8", padx= 50, pady=50, command=lambda: click(8))
b8.grid(row=3, column=2)

b9 = Button(root, text="9", padx= 50, pady=50, command=lambda: click(9))
b9.grid(row=4, column=0)

ba = Button(root, text="+", padx= 50, pady=50, command= add)
ba.grid(row=4, column=1)

bs = Button(root, text="-", padx= 50, pady=50, command= sub)
bs.grid(row=4, column=2)

be = Button(root, text="=", padx= 108, pady=50, command=equ)
be.grid(row=5, column=0, columnspan=2)

bc = Button(root, text="CL", padx= 45, pady=50, command=clr)
bc.grid(row=5, column=2)


root.mainloop()