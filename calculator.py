import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.config(bg="black")
e = tkinter.Entry(root, width =35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10 , pady=10, ipadx=5, ipady=5)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+ str(number))

def button_clear():
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, f_num +int(second_number))
    if math=="subtraction":
        e.insert(0, f_num -int(second_number))
    if math=="multiplication":
        e.insert(0, f_num *int(second_number))
    if math=="division":
        e.insert(0, f_num /int(second_number))
   
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multi():
    first_number=e.get()
    global f_num
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_div():    
    first_number=e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)
    #define the buttons
button_1= tkinter.Button(root, text="1", padx=40 , pady=20, command=lambda: button_click(1))
button_2= tkinter.Button(root, text="2", padx=40 , pady=20, command=lambda: button_click(2))
button_3= tkinter.Button(root, text="3", padx=40 , pady=20, command=lambda: button_click(3))
button_4= tkinter.Button(root, text="4", padx=40 , pady=20, command=lambda: button_click(4))
button_5= tkinter.Button(root, text="5", padx=40 , pady=20, command=lambda: button_click(5))
button_6= tkinter.Button(root, text="6", padx=40 , pady=20, command=lambda: button_click(6))
button_7= tkinter.Button(root, text="7", padx=40 , pady=20, command=lambda: button_click(7))
button_8= tkinter.Button(root, text="8", padx=40 , pady=20, command=lambda:button_click(8))
button_9= tkinter.Button(root, text="9", padx=40 , pady=20, command=lambda: button_click(9))
button_0= tkinter.Button(root, text="0", padx=40 , pady=20, command=lambda: button_click(0))
button_add= tkinter.Button(root, text="+", padx=39 , pady=20, command=button_add)
button_equal= tkinter.Button(root, text="=", padx=89 , pady=19, command=button_equal)
button_clear= tkinter.Button(root, text="Clear", padx=79 , pady=19, command=button_clear)

button_sub= tkinter.Button(root, text="_", padx=41 , pady=20, command=button_sub)
button_div= tkinter.Button(root, text="/", padx=40 , pady=20, command=button_div)
button_multi= tkinter.Button(root, text="*", padx=41 , pady=20, command=button_multi)

#displaying the buttons
button_1.grid(row=3 , column=0, ipadx=3, ipady=3)
button_2.grid(row=3 , column=1, ipadx=3, ipady=3)
button_3.grid(row=3 , column=2, ipadx=3, ipady=3)

button_4.grid(row=2 , column=0, ipadx=3, ipady=3)
button_5.grid(row=2 , column=1, ipadx=3, ipady=3)
button_6.grid(row=2 , column=2, ipadx=3, ipady=3)

button_7.grid(row=1 , column=0, ipadx=3, ipady=10)
button_8.grid(row=1, column=1, ipadx=3, ipady=10)
button_9.grid(row=1, column=2, ipadx=3, ipady=10)

button_0.grid(row=4, column=0, ipadx=3, ipady=3)

button_add.grid(row=5 , column=0, ipadx=3, ipady=3)
button_clear.grid(row=4, column=1, columnspan=2, ipadx=3, ipady=3)
button_equal.grid(row=5, column=1, columnspan=2, ipadx=3, ipady=3)

button_sub.grid(row=6, column=0, ipadx=3, ipady=3)
button_div.grid(row=6,column=1, ipadx=3, ipady=3)
button_multi.grid(row=6, column=2, ipadx=3, ipady=3)

root.mainloop()


