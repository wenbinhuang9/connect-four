player1 = 1
player2 = 2
empty = 0


maxdepth = 3

## todo adding another strategy, if the opposit will win, prevent it .

def init(row, col):
    board = [[0 for j in range(col)] for i in range(row)]

    return board


def get_total_baord():
    return total_board

def set_total_baord(board):
    total_board = board
def start(player, row, col):
    board = init(row, col)

    curPlayer = player
    while not game_over(board):
        play(board, curPlayer)
        ## convert to next player
        curPlayer = 3 - curPlayer

def play(board, player):
    if player == player1:
        r, c= maxx(board, maxdepth, player)
    if player == player2:
        r, c = mini(board, maxdepth, player)

    fillBoard(board, r, c, player)
    print_board(board)

    return (r, c)

def nextPlayer(player):
    return  3 - player

def mini(board, depth, player):
    if game_over(board) or depth == 0:
        return score(board)

    ans = 10**9
    min_r, min_c = -1, -1
    for c in getAvailCols(board):
        r =  getPlayRow(board, c)
        fillBoard(board, r, c, player)
        subans = maxx(board, depth - 1, nextPlayer(player))
        if subans < ans:
            ans = subans
            min_r, min_c = r, c
        unfillBoard(board, r, c)

    if depth == maxdepth:
        return (min_r, min_c)

    return ans

def getPlayRow(board, c):
    row = len(board)

    for i in range(row-1, -1, -1):
        if board[i][c] == empty:
            return i

    raise ValueError("column is full, can't play here|col={0}".format(c))

def maxx(board, depth, player):
    if game_over(board) or depth == 0:
        return score(board)

    ans = 0 - 10**9
    max_r, max_c = -1, -1
    for c in getAvailCols(board):
        r = getPlayRow(board, c)
        fillBoard(board, r, c, player)
        subans = mini(board, depth - 1, nextPlayer(player))
        if subans > ans:
            ans = subans
            max_r, max_c = r, c
        unfillBoard(board, r, c)

    if depth == maxdepth:
        return (max_r, max_c)
    return ans

def fillBoard(board, r, c, player):
    board[r][c] = player

def unfillBoard(board, r, c):
    board[r][c] = empty


def getAvailCols(board):
    col_list = get_col_list(board)

    ans = []
    for i, col in enumerate(col_list):
        if col[0] == empty:
            ans.append(i)

    return ans


def game_over(board):
    for line in get_row_list(board):
        if game_over_each_line(line):
            return True

    for line in get_col_list(board):
        if game_over_each_line(line):
            return True
    for line in get_diagonal_list(board):
        if game_over_each_line(line):
            return True

    return full(board)

def full(board):
    col = len(board[0])

    for c in range(col):
        if board[0][c] == empty:
            return  False

    return True

def get_row_list(board):
    row = len(board)
    return [board[i] for i in range(row)]

def get_col_list(board):
    col = len(board[0])
    row = len(board)
    return [[board[i][j] for i in range(row)] for j in range(col)]

def get_diagonal_list(board):
    col = len(board[0])
    row = len(board)
    ans = []
    for i in range(row):
        subans = get_diagonal_line_from_left_top_to_right_bottom(board, i, 0)
        ans.append(subans)
        subans = get_diagonal_line_from_right_top_to_left_bottom(board, i, col - 1)
        ans.append(subans)

    for i in range(0, col):
        if i != 0:
            subans = get_diagonal_line_from_left_top_to_right_bottom(board, 0, i)
            ans.append(subans)
        if i != col - 1:
            subans = get_diagonal_line_from_right_top_to_left_bottom(board, 0, i)
            ans.append(subans)
    return ans

def get_diagonal_line_from_left_top_to_right_bottom(board, r, c):
    row, col = len(board), len(board[0])
    ans =[]
    while r < row and c < col:
        ans.append(board[r][c])
        r+=1
        c+=1

    return ans


def get_diagonal_line_from_right_top_to_left_bottom(board, r, c):
    row, col = len(board), len(board[0])
    ans =[]
    while r < row and c < col:
        ans.append(board[r][c])
        r += 1
        c -= 1

    return ans


def game_over_each_line(arr_line):
    if len(arr_line) < 4:
        return False

    for i in range(0, len(arr_line) - 3):
        if arr_line[i] !=0 and arr_line[i] == arr_line[i + 1] == arr_line[i + 2] == arr_line[i + 3]:
            return True

    return False


def score(board):
    player1_score = get_player_score(board, player1)

    player2_score = get_player_score(board, player2)

    return player1_score - player2_score


def get_player_score(board, player):

    total_score = 0
    total_score += get_row_score(board, player)
    total_score += get_diagonal_score(board, player)
    total_score += get_col_score(board, player)

    return total_score

def get_row_score(board, player):
    totalScore = 0
    for row in get_row_list(board):
        totalScore += get_line_score(row, player)
        totalScore += get_line_score(row[::-1], player)

    return totalScore

def get_col_score(board, player):
    col_list = get_col_list(board)

    totalScore = 0
    for col in col_list:
        score = get_line_score(col, player)
        totalScore += score

    return totalScore


def get_diagonal_score(board, player):
    digonal_list = get_diagonal_list(board)
    total_score = 0
    for diagonal in digonal_list:
        total_score += get_line_score(diagonal, player)

    return total_score



def get_last_empty(one_line):
    if one_line == None or one_line[0] != empty:
        return None

    i = 1
    while i < len(one_line):
       if one_line[i] != empty:
           return i - 1

       i += 1


    return len(one_line) - 1

def get_line_score(one_line, player):
    last_empty = get_last_empty(one_line)

    if last_empty == None:
        return 0

    if last_empty + 4 < len(one_line) and player == one_line[last_empty + 1] == one_line[last_empty + 2] \
        == one_line[last_empty + 3] == one_line[last_empty + 4]:
        return 1000

    if last_empty + 3 < len(one_line) and player == one_line[last_empty + 1] == one_line[last_empty + 2] \
        == one_line[last_empty + 3]:
        return 100

    if last_empty + 2 < len(one_line) and  player == one_line[last_empty + 1] == one_line[last_empty + 2]:
        return 1

    return 0


def print_board(board):
    row_list = get_row_list(board)

    for row in row_list:
        print(row)

total_board = init(6, 7)

if __name__ == "__main__":
    start(player1, 5, 5)