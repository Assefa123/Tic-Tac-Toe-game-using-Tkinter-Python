from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.resizable(False, False)


def clicked(b):
    global count, x_turn
    if b["text"] == " " and x_turn:
        b["text"] = "X"
        x_turn = False
        count += 1
        checkifwon()
    elif b['text'] == " " and not x_turn:
        b['text'] = 'O'
        x_turn = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe!", "You can't take this position!")


def disableallbuttons():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    global won
    won = False
    current_config = [
        # Horizontal
        b1["text"] + b2["text"] + b3["text"],
        b4["text"] + b5["text"] + b6["text"],
        b7["text"] + b8["text"] + b9["text"],
        # Vertical
        b1["text"] + b4["text"] + b7["text"],
        b2["text"] + b5["text"] + b8["text"],
        b3["text"] + b6["text"] + b9["text"],
        # Diagonal
        b1["text"] + b5["text"] + b9["text"],
        b3["text"] + b5["text"] + b7["text"],
    ]
    if "XXX" in current_config:
        won = True
        messagebox.showinfo("Tic Tac Toe!", "Congratulations! X won!")
        disableallbuttons()
    elif "OOO" in current_config:
        won = True
        messagebox.showinfo("Tic Tac Toe!", "Congratulations! O won!")
        disableallbuttons()
    elif count == 9:
        messagebox.showinfo("Tic Tac Toe!", "It is a tie!")
        disableallbuttons()


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global x_turn
    global count
    global won
    x_turn = True
    if random.randint(0, 1):
        x_turn = False

    count = 0
    won = False
    b1 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b1))
    b2 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b2))
    b3 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b3))

    b4 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b4))
    b5 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b5))
    b6 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b6))

    b7 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b7))
    b8 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b8))
    b9 = Button(root, text=" ", height=5, width=10, bg='black', fg='white', font=("Helvetica", 15), command=lambda: clicked(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


won = False
x_turn = True
if random.randint(0, 1):
    x_turn = False

count = 0


mainMenu = Menu(root)
root.config(menu=mainMenu)

optionsMenu = Menu(mainMenu, tearoff=0)

mainMenu.add_cascade(menu=optionsMenu, label="Options")
optionsMenu.add_command(label='Reset', command=reset)
optionsMenu.add_command(label='Exit', command=root.quit)


reset()
root.mainloop()
