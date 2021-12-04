entries = open('input').read().splitlines()

sequence = entries[0].split(",")

boards = []
for i in range(2, len(entries), 6):
    board = []
    for j in range(5):
        board.append(entries[i + j].split())
    boards.append(board)

def play_number(number, board):
    for i in range(5):
        for j in range(5):
            if(board[i][j] == number): board[i][j] = ""
    return board

def is_row_complete(row):
    for i in range(len(row)):
        if row[i] != "": return False
    return True

def is_winner(board):
    #checking rows
    for i in range(5):
        if(is_row_complete(board[i])): return True
    #checking columns

    #transposing the matrix
    t_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] #zip(*board)
    for i in range(5):
        if(is_row_complete(t_board[i])): return True
    return False
def get_unplayed_sum(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if(board[i][j] != ""):
                sum += int(board[i][j])
    return sum

is_there_winner = False
for number in sequence:
    for board in boards:
        board = play_number(number, board)
        winner = is_winner(board)
        if(winner):
            print("***winner board***")
            print(board)
            sum = get_unplayed_sum(board)
            print(sum)
            score = sum * int(number)
            print(f"The final score is {score}")
            is_there_winner = True
            break
    if(is_there_winner): break
