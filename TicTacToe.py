from tkinter import *
from PIL import Image, ImageTk 

Player1 = 'X'
stop_game = False

def clicked(r, c):
    global Player1
    global stop_game

    if Player1 == "X" and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="X")
        states[r][c] = 'X'
        Player1 = 'O'
        turn_label.config(text="Player 2's turn: 'O'")

    elif Player1 == 'O' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text='O')
        states[r][c] = "O"
        Player1 = "X"
        turn_label.config(text="Player 1's turn: 'X'")

    check_if_win()


def check_if_win():
    global stop_game
    for i in range(3):

        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True
            player = "Player 1" if states[i][0] == 'X' else "Player 2"
            show_custom_popup(f"{player} won!")
            return
        
        elif states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            player = "Player 1" if states[0][i] == 'X' else "Player 2"
            show_custom_popup(f"{player} won!")
            return
        
    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        player = "Player 1" if states[0][0] == 'X' else "Player 2"
        show_custom_popup(f"{player} won!")
    elif states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        player = "Player 1" if states[0][2] == 'X' else "Player 2"
        show_custom_popup(f"{player} won!")

    elif all(states[row][col] != 0 for row in range(3) for col in range(3)):
        stop_game = True
        show_custom_popup("IT'S A TIE!")

def show_custom_popup(message):
    popup = Toplevel(root)
    popup.title("Game Result")
    popup.geometry("250x150")
    popup.resizable(False, False)

    try:
        if "TIE" in message:
            icon_path = "tie_icon.png"
        else:
            icon_path = "trophy_icon.png"
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((60, 60))
        icon_photo = ImageTk.PhotoImage(icon_image)
    except Exception as e:
        print(f"Error loading image: {e}")
        icon_photo = None

    if icon_photo:
        icon_label = Label(popup, image=icon_photo)
        icon_label.image = icon_photo 
        icon_label.pack(pady=5)

    result_label = Label(popup, text=message, font=("Helvetica", 14, "bold"))
    result_label.pack(pady=10)

def show_start_info():
    def start_game():
        start_info.destroy()
        root.deiconify()

    start_info = Toplevel(root)
    start_info.title("Game Start")
    start_info.geometry("300x200")
    start_info.resizable(False, False)

    info_label = Label(start_info, text="Game Info :-", font=("Helvetica", 16, "bold"))
    info_label.pack(pady=10)

    info_text = "\u2022 PLAYER 1 : 'X'\n\u2022 PLAYER 2 : 'O'" 
    info_message = Label(start_info, text=info_text, font=("Helvetica", 14))
    info_message.pack(pady=10)

    close_button = Button(start_info, text="Start Game", font=("Helvetica", 12), bg="lightblue", command=start_game)
    close_button.pack(pady=20)

root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

root.withdraw()
show_start_info()

def create_game_window():
    global turn_label, b, states

    turn_label = Label(root, text="Player 1's turn: 'X'", font=("Helvetica", 15))
    turn_label.grid(row=0, column=0, columnspan=3, pady=10)

    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            b[i][j] = Button(
                height=4, width=8, 
                font=("Helvetica", "20"), 
                command=lambda r=i, c=j: clicked(r, c),
                bg="lightgray",
                relief=GROOVE
            )
            b[i][j].grid(row=i+1, column=j, padx=5, pady=5)

root.update()
create_game_window()
mainloop()