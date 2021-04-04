import random
import art

board = { '7':' ', '8':' ', '9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' ',
          }

def my_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

board_keys = []
for board_key in board:
    board_keys.append(board_key)


def play():
    turn = "x"
    for i in range(10):
        if i == 9:
            print("Game Tie")
            break
        my_board(board)
        if turn == 'x':
            move = input(f"\nYour Turn '{turn}': \n")
        elif turn == 'o':
            print("**************   Opponent plays  **************\n")
            k = random.randint(1,9)
            move = str(k)
            if board[move] != ' ':
                while board[move] == " ":
                    k = random.randint(1, 9)
                    move = str(k)

        if board[move] == ' ':
            board[move] = turn
            #row wise check
            if board['7'] == board['8'] == board['9'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break
            elif board['4'] == board['5'] == board['6'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break
            elif board['1'] == board['2'] == board['3'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break

            #column wise check
            elif board['7'] == board['4'] == board['1'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break
            elif board['8'] == board['5'] == board['2'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break
            elif board['9'] == board['6'] == board['3'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break

            # 'x' wise check :)
            elif board['7'] == board['5'] == board['3'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break
            elif board['1'] == board['5'] == board['9'] != " ":
                my_board(board)
                print(f" '{turn}' won the match")
                break

            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
        else:
            print(f"### place already filled . Try another place ")
            play()

    option = input("Do you want to play again? Y or N: ").upper()
    if option == 'Y':
        for i in board_keys:
            board[i] = " "
        print(art.logo)
        play()
    else:
        exit()

print(art.logo)
play()