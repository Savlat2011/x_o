board = [" " for i in range(9)]

print('|1 | 2| 3|')
print('|4 | 5| 6|')
print('|7 | 8| 9|')

def print_board():
    rad1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    rad2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    rad3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(rad1)
    print(rad2)
    print(rad3)
    print()


def spelare_drag(ikon):
    if ikon == "X":
        nummer = 1
    elif ikon == "O":
        nummer = 2

    print("Det är spelare {} tur".format(nummer))
    val = int(input("Välj en position (1-9): ").strip())
    if board[val - 1] == " ":
        board[val - 1] = ikon
    else:
        print()
        print("Den positionen är upptagen!")


def är_vinst(ikon):
    if (board[0] == ikon and board[1] == ikon and board[2] == ikon) or \
            (board[3] == ikon and board[4] == ikon and board[5] == ikon) or \
            (board[6] == ikon and board[7] == ikon and board[8] == ikon) or \
            (board[0] == ikon and board[3] == ikon and board[6] == ikon) or \
            (board[1] == ikon and board[4] == ikon and board[7] == ikon) or \
            (board[2] == ikon and board[5] == ikon and board[8] == ikon) or \
            (board[0] == ikon and board[4] == ikon and board[8] == ikon) or \
            (board[2] == ikon and board[4] == ikon and board[6] == ikon):
        return True
    else:
        return False


def är_oavgjort():
    if " " not in board:
        return True
    else:
        return False


while True:
    print_board()
    spelare_drag("X")
    if är_vinst("X"):
        print_board()
        print("Spelare X har vunnit!")
        break
    elif är_oavgjort():
        print_board()
        print("Det blev oavgjort!")
        break

    print_board()
    spelare_drag("O")
    if är_vinst("O"):
        print_board()
        print("Spelare O har vunnit!")
        break

