"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        countX += row.count(X)
        countO += row.count(O)

    if countX > countO:
        return O
    elif not terminal(board) and countO == countX:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is EMPTY:
                possible.add((i, j))
    return possible

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")
    elif terminal(board):
        raise Exception("Game Over")
    else:
        result_board = copy.deepcopy(board)

        i, j = action[0], action[1]
        currentPlayer = player(board)
        result_board[i][j] = currentPlayer

        return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
            
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not any(j==EMPTY for i in board for j in i):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    possibleMoves = actions(board)
    checkNowPlayer = player(board)

    if checkNowPlayer == X:
        best_move = None
        best_score = float("-inf")
        for move in possibleMoves:
            newBoard = result(board, move)
            maxVal = max_value(newBoard)
            if maxVal > best_score:
                best_score = maxVal
                best_move = move

    else:
        best_move = None
        best_score = float("inf")
        for move in possibleMoves:
            newBoard = result(board, move)
            maxVal = max_value(newBoard)
            if maxVal < best_score:
                best_score = maxVal
                best_move = move

    return best_move
        
def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = float("-inf")
    
    for move in actions(board):
        newBoard = result(board, move)
        value = max(value, min_value(newBoard))

    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = float("inf")
    
    for move in actions(board):
        newBoard = result(board, move)
        value = min(value, max_value(newBoard))

    return value