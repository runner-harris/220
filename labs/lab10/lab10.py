"""
Name: Walker Harris
lab10.py
"""


def board():
    positionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return positionList


def display_board(positionList):
    print("----------")
    acc = 0
    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(positionList[acc], end='|')
            acc += 1
        print("\n" + "-" * 10)


def place_spot(positionList, spot, marker):
    positionList[spot - 1] = marker


def legal_spot(board, spot):
    if (board[spot - 1] == 'x' or board[spot - 1] == 'o') or (spot < 1 or spot > 9):
        return False
    else:
        return True


def won(board):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
    for condition in winCon:
        counter = 0
        counter_o = 0
        for spot in condition:
            if board[spot - 1] == 'x':
                counter += 1
            if counter == 3:
                return 'x wins'
        for spot in condition:
            if board[spot - 1] == 'o':
                counter_o += 1
            if counter_o == 3:
                return 'o wins'


def game_over(board, turnCount):
    if (won(board) == 'x wins' or won(board) == 'o wins') or (turnCount >= 9):
        return True
    else:
        return False


def play_game():
    positionList = board()
    turnCount = 0
    display_board(positionList)
    while not game_over(positionList, turnCount):
        x_spot = eval(input("player 1, enter a spot "))
        if legal_spot(positionList, x_spot):
            place_spot(positionList, x_spot, 'x')
        turnCount += 1
        display_board(positionList)
        if won(positionList):
            print("player 1, you won!")
            break
        o_spot = eval(input("player 2, enter a spot "))
        if legal_spot(positionList, o_spot):
            place_spot(positionList, o_spot, 'o')
        turnCount += 1
        if won(positionList):
            print("player 2, you won!")
            break
        display_board(positionList)
    else:
        print('tie')





def main():
    # add other function calls here
    play_game()
    pass


main()
