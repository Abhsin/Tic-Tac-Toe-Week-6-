from logic import check_winner
def get_empty_board():
    return [
        ["None", "None","None"],
        ["None", "None", "None"],
        ["None","None", "None"],
    ]



def get_player_input(current_player):
    """"
    input : row, col
    return:
        row -> int -> the index of Row 
        col -> int -> the index of Column
    """
    prompt = f"player {current_player}, Please inpute your move, e.g. row,col \n"
    player_input = input(prompt) # This is a string 
    # 1,1.split (",") --> ["1","1"]
    row_col_list = player_input.split(',')
    row,col = [int(x) for x in row_col_list]
    return row,col

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'


def print_board(board):
    for row in board: 
        print(row)# Print will the variable in a new line


if __name__ == '__main__':
    #get a empty board 
    current_player = 'X'
    board= get_empty_board()
    winner = None

    while winner is None:
        print_board(board)
    #ask user input
        row,col = get_player_input(current_player)

    # mark the board 
        board[row][col] = current_player
        winner = check_winner(board)
        current_player = switch_player(current_player)


    #check for winner
    # Check if game is draw 
    #Print the winner

