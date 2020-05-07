import common


def is_tie(board):
    for box in board:
        if box == 0:
            return False
    return True


def possible_moves(board, player):
    blanks = [idx for idx, box in enumerate(board) if box == 0]
    result = []

    for spot in blanks:
        temp = board.copy()
        temp[spot] = player
        result.append(temp)

    return result


class game_stats:
    def __init__(self, board, turn):
        self.outcome = None
        self.turn = turn
        self.board = board
        self.value = None

    def is_terminal(self):
        status = common.game_status(self.board)
        # 1 if X wins, 2 if O wins, 0 else
        if is_tie(self.board) or status != 0:
            self.outcome = status
            return True
        else:
            return False

    def set_outcome(self):
        self.outcome = common.game_status(self.board)

    def get_board(self):
        return self.board

    def get_turn(self):
        return self.turn

    def get_outcome(self):
        return self.outcome

    def set_turn(self, fresh_turn):
        self.turn = fresh_turn

    def set_board(self, fresh_board):
        self.board = fresh_board

    def set_value(self, fresh_val):
        self.value = fresh_val

    def get_value(self):
        return self.value


def closer_to1(outcomes):
    if 1 in outcomes:
        return 1
    elif 0 in outcomes:
        return 0
    elif 2 in outcomes:
        return 2
    else:
        return float("inf")
    pass


def prune_to1(outcomes):
    # one of [1, 0, 2, inf, -inf]
    if float("inf") in outcomes:
        return float("inf")
    elif 1 in outcomes:  # xwins
        return 1
    elif 0 in outcomes:  # tie
        return 0
    elif 2 in outcomes:  # O wins
        return 2
    else:
        return float("-inf")
    pass


def v_beta(v, beta):
    value = 0

    if v == 2:
        value = -1
    return value >= beta


def v_alpha(v, alpha):
    value = 0

    if v == 2:
        value = -1
    return value <= alpha


def prune_to2(outcomes):
    if float("-inf") in outcomes:
        return float("-inf")
    elif 2 in outcomes:  # O wins
        return 2
    elif 0 in outcomes:  # tie
        return 0
    elif 1 in outcomes:  # x wins
        return 1
    else:
        return float("inf")
    pass


def closer_to2(outcomes):
    if 2 in outcomes:
        return 2
    elif 0 in outcomes:
        return 0
    elif 1 in outcomes:
        return 1
    else:
        return float("-inf")
    pass


def agentX(curr_board, stats):
    stats.set_board(curr_board)
    if stats.is_terminal():
        return stats.get_outcome()
    else:
        v = float("-inf")

        for state in possible_moves(curr_board, 1):
            v = closer_to1([v, agentO(state, stats)])
        return v


def agentO(curr_board, stats):
    stats.set_board(curr_board)
    if stats.is_terminal():
        return stats.get_outcome()
    else:
        v = float("inf")
        for state in possible_moves(curr_board, 2):
            v = closer_to2([v, agentX(state, stats)])
        return v


def minmax_tictactoe(board, turn):
    # put your code here: it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for
    # tie. use the function common.game_status(board), to evaluate a board it returns common.constants.X(1) if X wins,
    # common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished the program will keep
    # track of the number of boards evaluated result = common.game_status(board);
    minmax_stats = game_stats(board, turn)

    if turn == common.constants.X:  # x goes first
        return agentX(minmax_stats.get_board(), minmax_stats)
    else:  # o goes first
        return agentO(minmax_stats.get_board(), minmax_stats)


def pruneX(curr_board, alpha, beta, stats):
    stats.set_board(curr_board)
    if stats.is_terminal():
        return stats.get_outcome()
    else:
        v = float("-inf")
        for state in possible_moves(curr_board, 1):
            v = prune_to1([v, pruneO(state, alpha, beta, stats)])
            if v_beta(v, beta):
                return v
            alpha = prune_to1([alpha, v])
        return v


def pruneO(curr_board, alpha, beta, stats):
    stats.set_board(curr_board)
    if stats.is_terminal():
        return stats.get_outcome()
    else:
        v = float("inf")
        for state in possible_moves(curr_board, 2):
            v = prune_to2([v, pruneX(state, alpha, beta, stats)])
            if v_alpha(v, alpha):
                return v
            beta = prune_to2([beta, v])
        return v


def abprun_tictactoe(board, turn):
    # put your code here: it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for
    # tie. use the function common.game_status(board), to evaluate a board it returns common.constants.X(1) if X wins,
    # common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished the program will keep
    # track of the number of boards evaluated result = common.game_status(board);
    minmax_stats = game_stats(board, turn)

    if turn == common.constants.X:
        return pruneX(board, float("-inf"), float("inf"), minmax_stats)
    else:
        return pruneO(board, float("-inf"), float("inf"), minmax_stats)
