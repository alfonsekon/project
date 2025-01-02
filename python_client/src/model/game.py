from model.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "Player 1"
        self.winner = None

    def switch_player(self):
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"

    def check_winner(self):
        # Check win conditions (e.g., Lion capture)
        self.winner = self.board.check_for_winner()
