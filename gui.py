import tkinter as tk

window = tk.Tk()


moves = [" X ", " 0 "]

def clean():
    for i in range(3):
        for j in range(3):
            field[i][j]['text'] = "   "
    global move
    move = 1


def is_win():
    flag = True
    for i in range(3):
        el = field[i][0]["text"]
        flag = True
        for j in range(3):
            if field[i][j]["text"] != el or field[i][j]["text"] == "   ":
                flag = False
    if flag:
        return True

    flag = True
    for i in range(3):
        el = field[0][0]["text"]
        if field[i][i]["text"] != el or field[i][i]["text"] == "   ":
            flag = False
    if flag:
        return True

    flag = True
    el = field[0][2]
    for i in range(3):
        if field[i][2 - i]["text"] != el or field[i][2 - i]["text"] == "   ":
            flag = False

    return flag


def winner():
    global move
    if is_win():
        if move == 1:
            tk.Label(window, text="Игрок Х выйграл",
                   bg="#00c4a8",
                   fg="white",
                   font=("Arial", 15),
                   ).grid(row=6, column=0, columnspan=4)
            tk.Button(window, text="Начать новую игру?",
                      font=("Arial", 15),
                      command=clean(),
                      borderwidth=0,
            ).grid(row=7, column=0, columnspan=4)
        else:
            tk.Label(window, text="Игрок 0 выйграл",
                     bg="#00c4a8",
                     fg="white",
                     font=("Arial", 15),
                     ).grid(row=6, column=0, columnspan=4)
            tk.Button(window, text="Начать новую игру?",
                      font=("Arial", 15),
                      command=clean(),
                      borderwidth=0,
                      ).grid(row=7, column=0, columnspan=4)

def choise(button_name):
    global move
    if move == 1:
        btn1["underline"] = 0
        btn2["underline"] = 1
    else:
        btn2["underline"] = 0
        btn1["underline"] = 1

move = 1
def main(r, c):
    global move
    if move == 1:
        if field[r][c]["text"] == "   ":
            field[r][c].config(text=f"{moves[move - 1]}")
            winner()
            move = 2

    else:
        if field[r][c]["text"] == "   ":
            field[r][c].config(text=f"{moves[move - 1]}")
            winner()
            move = 1



photo = tk.PhotoImage(file="folder/controller.png")
window.iconphoto(False, photo)

window.title("Крестики нолики")

window.geometry("600x500+100+200")
window.resizable(False, False)
window.config(bg="#00c4a8")

label_1_text = "Начните игру или выберите игрока"
label_1 = tk.Label(window, text=label_1_text,
                   bg="#00c4a8",
                   fg="white",
                   font=("Arial", 12),
                   pady=10,
                   )

btn1 = tk.Button(window, text="x",
                 # command=lambda: choise("x"),
                 bg="grey",
                 fg="white",
                 font=("Arial", 15),
                 width=7,
                 background="#3d534e",
                 borderwidth=0,
                 underline=0
                 )
btn2 = tk.Button(window, text="0",
                 # command=lambda: choise("0"),
                 bg="grey",
                 fg="white",
                 font=("Arial", 15),
                 width=7,
                 background="#3d534e",
                 borderwidth=0,
                 )

label_1.grid(row=0, column=0, columnspan=5)
btn1.grid(row=0, column=6)
btn2.grid(row=0, column=7)

field = []

for i in range(3):
    swop = []
    for j in range(3):
        row = 2 + i
        column = 2 + j
        btn = tk.Button(window, text=f"   ",
                        command=lambda r=row, c=column: main(r - 2, c - 2),
                        width=4,
                        height=3,
                        borderwidth=1,
                        )
        btn.grid(row=row, column=column, stick="we")
        swop.append(btn)
    field.append(swop)

window.mainloop()
