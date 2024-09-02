import tkinter as tk

window = tk.Tk()

move = 1
moves = [" X ", " 0 "]


def choise(button_name):
    global move
    if move == 1:
        btn1["underline"] = 0
        btn2["underline"] = 1
    else:
        btn2["underline"] = 0
        btn1["underline"] = 1


def main(i, j):
    global move
    if move == 1:
        field[i][j].config(text=f"{moves[move - 1]}")
        move = 2
    if move == 2:
        field[i][j].config(text=f"{moves[move - 1]}")
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
        btn = tk.Button(window, text=f"   ",
                        command=lambda: main(i, j),
                        width=4,
                        height=3,
                        borderwidth=1,
                        )
        btn.grid(row=2 + i, column=2 + j, stick="we")
        swop.append(btn)
    field.append(swop)

window.mainloop()
