from tkinter import *
from tkinter import ttk
import math_operator as ma

def rezult_calc():
    res = None
    second_num = float(line_input.get())
    line_input.delete(0, END)
    if operator == "+":
        res = ma.add(first_num, second_num)
    elif operator == "-":
        res = ma.subtract(first_num, second_num)
    elif operator == "*":
        res = ma.multiply(first_num, second_num)
    elif operator == "/":
        res = ma.devide(first_num, second_num)
    line_input.insert(0, res)


def choise_number(num):
    line_input.insert(END, num)


def choise_operator(oper):
    global operator, first_num
    first_num = float(line_input.get())
    operator = oper
    line_input.delete(0, END)

def clear_line():
    line_input.delete(0, END)


first_num = None
operator = None

window = Tk()
window.title("Калькулятор")
window.iconbitmap(default="calculator_icon.ico")

line_input = Entry(window, font=("Arial", 14))
line_input.grid(row=0, column=0, columnspan=4, sticky="ew")

ttk.Button(window, text="1", command=lambda: choise_number("1")).grid(row=3, column=0)
ttk.Button(window, text="2", command=lambda: choise_number("2")).grid(row=3, column=1)
ttk.Button(window, text="3", command=lambda: choise_number("3")).grid(row=3, column=2)
ttk.Button(window, text="4", command=lambda: choise_number("4")).grid(row=2, column=0)
ttk.Button(window, text="5", command=lambda: choise_number("5")).grid(row=2, column=1)
ttk.Button(window, text="6", command=lambda: choise_number("6")).grid(row=2, column=2)
ttk.Button(window, text="7", command=lambda: choise_number("7")).grid(row=1, column=0)
ttk.Button(window, text="8", command=lambda: choise_number("8")).grid(row=1, column=1)
ttk.Button(window, text="9", command=lambda: choise_number("9")).grid(row=1, column=2)
ttk.Button(window, text="0", command=lambda: choise_number("0")).grid(row=4, column=0)


ttk.Button(window, text="+", command=lambda: choise_operator("+")).grid(row=1, column=3)
ttk.Button(window, text="-", command=lambda: choise_operator("-")).grid(row=2, column=3)
ttk.Button(window, text="*", command=lambda: choise_operator("*")).grid(row=3, column=3)
ttk.Button(window, text="/", command=lambda: choise_operator("/")).grid(row=4, column=3)
ttk.Button(window, text="C", command=clear_line).grid(row=4, column=1)
ttk.Button(window, text="=", command=rezult_calc).grid(row=4, column=2)

window.mainloop()
