from tkinter import *


root = Tk()
root.title('Simple Calculator')
root.geometry("300x150")

expression = ""

def press(key):
    global expression
    expression += str(key)
    display.set(expression)


def equal():
    global expression

    try:
        result = str(eval(expression))
        display.set(result)
        expression = ""

    except:
        display.set("ERROR")
        expression = ''


def clear():
    global expression
    expression = ''
    display.set("")



if __name__ == '__main__':

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=10)

    key1 = Button(root, text='1', command=lambda: press(1), height=1, width=7)
    key1.grid(row=2, column=0)

    key2 = Button(root, text='2', command=lambda: press(2), height=1, width=7)
    key2.grid(row=2, column=1)

    key3 = Button(root, text='3', command=lambda: press(3), height=1, width=7)
    key3.grid(row=2, column=2)

    key4 = Button(root, text='4', command=lambda: press(4), height=1, width=7)
    key4.grid(row=3, column=0)

    key5 = Button(root, text='5', command=lambda: press(5), height=1, width=7)
    key5.grid(row=3, column=1)

    key6 = Button(root, text='6', command=lambda: press(6), height=1, width=7)
    key6.grid(row=3, column=2)

    key7 = Button(root, text='7', command=lambda: press(7), height=1, width=7)
    key7.grid(row=4, column=0)

    key8 = Button(root, text='8', command=lambda: press(8), height=1, width=7)
    key8.grid(row=4, column=1)

    key9 = Button(root, text='9', command=lambda: press(9), height=1, width=7)
    key9.grid(row=4, column=2)

    key0 = Button(root, text='0', command=lambda: press(0), height=1, width=7)
    key0.grid(row=5, column=0)



    clear_ = Button(root, text='Clear', command=lambda: clear(), height=1, width=7)
    clear_.grid(row=5, column=1)

    equal_ = Button(root, text='=', command=lambda: equal(), height=1, width=7)
    equal_.grid(row=5, column=2)

    dot = Button(root, text='.', command=lambda: press('.'), height=1, width=7)
    dot.grid(row=6, column=0)



    plus = Button(root, text='+', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(root, text='-', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=3)

    mult = Button(root, text='x', command=lambda: press('*'), height=1, width=7)
    mult.grid(row=4, column=3)

    div = Button(root, text='/', command=lambda: press('/'), height=1, width=7)
    div.grid(row=5, column=3)




    root.mainloop()