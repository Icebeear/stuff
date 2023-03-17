win_lines = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  
    [1, 5, 9],
    [3, 5, 7],  
]


cells = [" " for x in range(9)]


def board():
    print(

        f" {cells[0]} | {cells[1]} | {cells[2]}" '\n'
        "---|---|---" '\n'
        f" {cells[3]} | {cells[4]} | {cells[5]}" '\n'
        "---|---|---" '\n'
        f" {cells[6]} | {cells[7]} | {cells[8]}" 
    )


def check_win():
    for line in win_lines:
        if " " not in cells:
            board()
            print("Tie")
            return True
        
        elif " " in (cells[line[0] - 1], cells[line[1] - 1], cells[line[2] - 1]):
            pass 

        elif (cells[line[0] - 1] == cells[line[1] - 1] == cells[line[2] - 1]):
            board()
            print(f"Player {cells[line[1] - 1]} win!")
            return True


def move(name):
    while True:
        try:
            choice = int(input(f"Player {name}, enter your move (1-9): "))
            if cells[choice - 1] == " ":
                cells[choice - 1] = name
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Invalid move. Try again.")


def play():
    print("Welcome to Tic Tac Toe!")
    while True:
        board()
        move("X")
        if check_win():
            break
        board()
        move("O")
        if check_win():
            break

       
play()