import tkinter as tk
from sys import flags

window = tk.Tk()
move = 1
moves = [" X ", " 0 "]
field = []


def draw():
    flag = True
    for i in range(3):
        for j in range(3):
            if field[i][j]["text"] == "   ":
                flag = False
    return flag

def clean(button, label):
    for i in range(3):
        for j in range(3):
            field[i][j]['text'] = "   "
    global move
    move = 1
    button.destroy()
    label.destroy()


def is_win():
    for i in range(3):
        el = field[i][0]["text"]
        flag = True
        for j in range(3):         #горизонтально
            if field[i][j]["text"] != el or field[i][j]["text"] == "   ":
                flag = False
        if flag:
            return True

    for i in range(3):
        el = field[0][i]["text"]
        flag = True                #вертикально
        for j in range(3):
            if field[j][i]["text"] != el or field[j][i]["text"] == "   ":
                flag = False
        if flag:
            return True

    flag = True
    for i in range(3):
        el = field[0][0]["text"]   #главная диагональ
        if field[i][i]["text"] != el or field[i][i]["text"] == "   ":
            flag = False
    if flag:
        return True

    flag = True
    el = field[0][2]["text"]
    for i in range(3):             #побочная диагональ
        if field[i][2 - i]["text"] != el or field[i][2 - i]["text"] == "   ":
            flag = False

    return flag


def winner():
    global move
    if is_win():
        if move == 1:
            end_label = tk.Label(window, text="Игрок X выйграл",
                                 bg="#00c4a8",
                                 fg="white",
                                 font=("Arial", 15),
                                 )
            end_label.grid(row=7, column=0, columnspan=4)

            new_game_btn = tk.Button(window, text="Начать новую игру?",
                                     font=("Arial", 15),
                                     command=lambda: clean(new_game_btn, end_label),
                                     borderwidth=0,
                                     )
            new_game_btn.grid(row=8, column=0, columnspan=4)
        else:
            end_label = tk.Label(window, text="Игрок 0 выйграл",
                    bg="#00c4a8",
                     fg="white",
                     font=("Arial", 15),
                     )
            end_label.grid(row=7, column=0, columnspan=4)

            new_game_btn = tk.Button(window, text="Начать новую игру?",
                      font=("Arial", 15),
                      command=lambda: clean(new_game_btn, end_label),
                      borderwidth=0,
                      )
            new_game_btn.grid(row=8, column=0, columnspan=4)
    else:
        if draw():
            draw_label = tk.Label(window, text="Ничья",
                                  bg="#00c4a8",
                                  fg="white",
                                  font=("Arial", 15),
                                  )
            draw_label.grid(row=7, column=0, columnspan=4)

            new_game_btn = tk.Button(window, text="Начать новую игру?",
                                     font=("Arial", 15),
                                     command=lambda: clean(new_game_btn, draw_label),
                                     borderwidth=0,
                                     )
            new_game_btn.grid(row=8, column=0, columnspan=4)


def choise(button_name):
    global move
    if move == 1:
        btn1["underline"] = 0
        btn2["underline"] = 1
    else:
        btn2["underline"] = 0
        btn1["underline"] = 1


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
