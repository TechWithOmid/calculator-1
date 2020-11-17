from tkinter import *
import tkinter.messagebox

# ======================== settings ========================
root = Tk()
root.title('calculator')
root.geometry('600x400')
root.resizable(height=False, width=False)
color = 'gray'
root.config(bg=color)
# ====================== variables ======================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ======================== frames ========================
first_frame = Frame(root, width=600, height=100, bg=color)
first_frame.pack(side=TOP)

second_frame = Frame(root, width=600, height=100, bg=color)
second_frame.pack(side=TOP)

third_frame = Frame(root, width=600, height=100, bg=color)
third_frame.pack(side=TOP)

forth_frame = Frame(root, width=600, height=100, bg=color)
forth_frame.pack(side=TOP)


# ======================= Functions =======================
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'zero division error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide by 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def mult():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('zero division error')
    try:
        value = float(num1.get()) / float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


# ======================== Buttons ========================
btn_plus = Button(third_frame, text="+", width=10,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=20)

btn_minus = Button(third_frame, text="-", width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=5, pady=20)

btn_mult = Button(forth_frame, text="*", width=10,
                  highlightbackground=color, command=lambda: mult())
btn_mult.pack(side=LEFT, padx=5, pady=20)

btn_div = Button(forth_frame, text="/", width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=5, pady=20)

# ====================== Entry&Labels ======================
firstNum = Entry(first_frame, highlightbackground=color, textvariable=num1)
firstNum.pack(side=LEFT, padx=50, pady=30)

secondNum = Entry(first_frame, highlightbackground=color, textvariable=num2)
secondNum.pack(side=RIGHT, padx=50, pady=30)

result = Entry(second_frame, highlightbackground=color, textvariable=res_value)
result.pack(side=LEFT, padx=50, pady=30)

root.mainloop()