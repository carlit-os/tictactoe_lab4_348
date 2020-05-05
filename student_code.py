import common


def is_tie(board):
    for box in board:
        if box == 0:
            return False
    return True


class game_stats:
    def __init__(self):
        self.outcome = None

    def is_terminal(self, board):
        status = common.game_status(board)
        # 1 if X wins, 2 if O wins, 0 else
        if status != 0 or is_tie(board):
            self.outcome = status
            return True
        else:
            return False


def minmax_tictactoe(board, turn):
    # put your code here: it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for
    # tie. use the function common.game_status(board), to evaluate a board it returns common.constants.X(1) if X wins,
    # common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished the program will keep
    # track of the number of boards evaluated result = common.game_status(board);
    minmax_stats = game_stats()
    while not minmax_stats.is_terminal(board):
        pass

    return common.constants.X


def abprun_tictactoe(board, turn):
    # put your code here: it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for
    # tie. use the function common.game_status(board), to evaluate a board it returns common.constants.X(1) if X wins,
    # common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished the program will keep
    # track of the number of boards evaluated result = common.game_status(board);
    return common.constants.NONE
