# Revolutionary AI code here

class GameManager():
    """
    Manages game (board) state for all players, and calculations for AI player.
    """
    def __init__(self):
        self.board = Board()
        self.board.display_board()


    def calculate_legal_moves(self):

        self.board.get_board_state()


class Board():
    """
    Handles the state of the tic-tac-toe board
    """


    def __init__(self):

        """Initializes starting board and variable for tracking the running board state"""

        self.key = {0: "O",
                    1: "X",
                    2: "-"}
        self.initial_board_state = [2,2,2,
                                    2,2,2,
                                    2,2,2]

        self.board_state = self.initial_board_state




    def display_board(self):

        """For displaying board state in a readable format"""

        #print("board goes here")
        print(f" {self.key[self.board_state[0]]} | {self.key[self.board_state[1]]} | {self.key[self.board_state[2]]}")
        print(f"___________")
        print(f" {self.key[self.board_state[3]]} | {self.key[self.board_state[4]]} | {self.key[self.board_state[5]]}")
        print(f"___________")
        print(f" {self.key[self.board_state[6]]} | {self.key[self.board_state[7]]} | {self.key[self.board_state[8]]}")



    def get_board_state(self):

        """Returns current state of the board"""

        return self.board_state

    def update_board_state(self, new_board_state):

        """Method for changing board state"""


        self.board_state = new_board_state


def main():
    game = GameManager()

















if __name__ == '__main__':
    main()