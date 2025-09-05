import tkinter as tk

class View:

    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.setup_window()

        self.buttons_style = {
            "font": ("Arial", 25),
            "width": 7,
            "height": 1,
            "background": "#e7e8eb",
            "borderwidth": 0,
        }

        self.starting_player_selected = False


        self.choise_x_btn = tk.Button(self.window, text="X",
                                      **self.buttons_style,
                                      command=lambda: self.choise(1))
        self.choise_0_btn = tk.Button(self.window, text="0",
                                      **self.buttons_style,
                                      command=lambda: self.choise(2))
        self.start_buttons()

    def setup_window(self):
        window = self.window
        photo = tk.PhotoImage(file="media/controller.png")
        window.iconphoto(False, photo)
        window.title("Крестики нолики")
        window.geometry("600x500+100+200")
        window.resizable(False, False)
        window.config(bg="#00c4a8")

    def start(self):
        self.create_field()
        self.window.mainloop()

    def start_buttons(self):
        choise_label_text = "Начните игру или выберите игрока"
        choise_label = tk.Label(self.window, text=choise_label_text,
                           bg="#00c4a8",
                           fg="white",
                           font=("Arial", 15),
                           pady=10,
                           )

        choise_label.grid(row=0, column=0, columnspan=5)
        self.choise_x_btn.grid(row=0, column=6,pady=5)
        self.choise_0_btn.grid(row=0, column=7, pady=5)


    def choise(self, player):
        if self.game:
            if not self.starting_player_selected:

                self.game.current_move = player
                self.starting_player_selected = True

            if self.game.current_move == 1:
                self.choise_x_btn["fg"] = "#00c4a8"
                self.choise_0_btn["fg"] = "black"
            else:
                self.choise_x_btn["fg"] = "black"
                self.choise_0_btn["fg"] = "#00c4a8"



    def create_field(self):
        for i in range(3):
            swop = []
            for j in range(3):
                row = 2 + i
                column = 2 + j
                btn = tk.Button(self.window, text=f"   ",
                                height="3",
                                width="4",
                                font=("Arial", 20),
                                background="#e7e8eb",
                                border= 0,
                                command=lambda r=row, c=column: self.game.on_fieldbtn_click(r - 2, c - 2),
                                )
                btn.grid(row=row, column=column, stick="we")
                swop.append(btn)
            self.game.field.append(swop)
    def winner(self):
        new_game_btn = tk.Button(self.window, text="Начать новую игру?",
                                 font=("Arial", 15),
                                 border=0,
                                 height=2,
                                 width=15,
                                 background="#e7e8eb",
                                 command=lambda: self.clean_field(new_game_btn, end_label))
        end_label = tk.Label(self.window, text="",
                             height=2,
                             background="#00c4a8",
                              width=15,
                             fg="#ffffff",
                             font=("Arial", 15))
        if self.game.is_win():
            if self.game.current_move == 1:
                end_label.configure(text="Игрок X выйграл")
                end_label.grid(row=8, column=0, columnspan=5, pady=5)
                new_game_btn.grid(row=9, column=2, columnspan=4)
                self.end_game()
            else:
                end_label.configure(text="Игрок 0 выйграл")
                end_label.grid(row=8, column=0, columnspan=5, pady=5)
                new_game_btn.grid(row=9, column=2, columnspan=4, pady=5)
                self.end_game()
        else:
            if self.game.draw():
                end_label.configure(text="Ничья")
                end_label.grid(row=8, column=0, columnspan=5, pady=5, padx=5)
                new_game_btn.grid(row=9, column=2, columnspan=4, pady=5)
                self.end_game()

    def clean_field(self, button, label):
        self.choise_x_btn["fg"] = "black"
        self.choise_0_btn["fg"] = "black"
        self.game.current_move = 1
        for i in range(3):
            for j in range(3):
                self.game.field[i][j]['text'] = "   "
        self.game.current_move = 1
        button.destroy()
        label.destroy()
        self.starting_player_selected = False
        for i in range(3):
            for j in range(3):
                self.game.field[i][j].config(command=lambda r=i, c=j: self.game.on_fieldbtn_click(r, c ))

    def end_game(self):
        for row in self.game.field:
            for button in row:
                button.config(command=lambda: None)


class Game:
    field = []
    def __init__(self, viev):
        self.viev = viev
        self.current_move = 1
        self.moves = [" X ", " 0 "]

    def on_fieldbtn_click(self, r, c):
        self.viev.choise(1)
        if self.current_move == 1:
            if self.field[r][c]["text"] == "   ":
                self.field[r][c].config(text=f"{self.moves[self.current_move - 1]}")
                self.viev.winner()
                self.current_move = 2

        else:
            if self.field[r][c]["text"] == "   ":
                self.field[r][c].config(text=f"{self.moves[self.current_move - 1]}")
                self.viev.winner()
                self.current_move = 1
        self.viev.choise(0)

    def is_win(self):
        for i in range(3):
            el = self.field[i][0]["text"]
            flag = True
            for j in range(3):  # горизонтально
                if self.field[i][j]["text"] != el or self.field[i][j]["text"] == "   ":
                    flag = False
            if flag:
                return True

        for i in range(3):
            el = self.field[0][i]["text"]
            flag = True  # вертикально
            for j in range(3):
                if self.field[j][i]["text"] != el or self.field[j][i]["text"] == "   ":
                    flag = False
            if flag:
                return True

        flag = True
        for i in range(3):
            el = self.field[0][0]["text"]  # главная диагональ
            if self.field[i][i]["text"] != el or self.field[i][i]["text"] == "   ":
                flag = False
        if flag:
            return True

        flag = True
        el = self.field[0][2]["text"]
        for i in range(3):  # побочная диагональ
            if self.field[i][2 - i]["text"] != el or self.field[i][2 - i]["text"] == "   ":
                flag = False

        return flag

    def draw(self):
        flag = True
        for i in range(3):
            for j in range(3):
                if self.field[i][j]["text"] == "   ":
                    flag = False
        return flag


def main():

    view = View(None)
    game = Game(view)
    view.game = game
    view.start()

if __name__ == "__main__":
    main()