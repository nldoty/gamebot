class Board:
    board = [
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
        [" ", " ", "1", " ", " ", "|", " ", " ", "2", " ", " ", "|", " ", " ", "3", " ", " "],
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
        [" ", " ", "4", " ", " ", "|", " ", " ", "5", " ", " ", "|", " ", " ", "6", " ", " "],
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
        [" ", " ", "7", " ", " ", "|", " ", " ", "8", " ", " ", "|", " ", " ", "9", " ", " "],
        [" ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " "],
    ]

    pos_1 = board[1][2]
    pos_2 = board[1][8]
    pos_3 = board[1][14]
    pos_4 = board[5][2]
    pos_5 = board[5][8]
    pos_6 = board[5][14]
    pos_7 = board[9][2]
    pos_8 = board[9][8]
    pos_9 = board[9][14]

    def __init__(self):
        pass

    def print_board(self):
        output = "\n```"

        for row in self.board:
            for char in row:
                output += char
            output += '\n'

        output += "```"
        return output

    def check_for_winner(self):
        user_vars = ['X', 'O']

        if self.pos_1 in user_vars:
            if self.pos_1 == self.pos_2 == self.pos_3:
                return True
            elif self.pos_1 == self.pos_5  == self.pos_9:
                return True
            elif self.pos_1 == self.pos_4 == self.pos_7:
                return True
        elif self.pos_2 in user_vars:
            if self.pos_2 == self.pos_5 == self.pos_8:
                return True
        elif self.pos_3 in user_vars:
            if self.pos_3 == self.pos_6 == self.pos_9:
                return True
        elif self.pos_7 in user_vars:
            if self.pos_4 == self.pos_5 == self.pos_6:
                return True
        elif self.pos_7 in user_vars:
            if self.pos_7 == self.pos_8 == self.pos_9:
                return True

        return False
