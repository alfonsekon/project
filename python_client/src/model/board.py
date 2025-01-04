from model.piece import Piece, Mime, Goldqueen, Sighducky, Clefairy

class Board:
    def __init__(self):
        # 3x4 board with initial positions
        self.grid = [[None for _ in range(3)] for _ in range(4)]
        self.initialize_pieces()
        self.captured_pieces_player1 = []
        self.captured_pieces_player2 = []

    def initialize_pieces(self):
        # Add initial pieces (e.g., Mime, Chick, Sighducky, etc.)
        self.grid[0][0] = Goldqueen("Player 1")
        self.grid[3][0] = Goldqueen("Player 2")
        self.grid[0][1] = Mime("Player 1")
        self.grid[3][1] = Mime("Player 2")
        self.grid[0][2] = Sighducky("Player 1")
        self.grid[3][2] = Sighducky("Player 2")
        self.grid[1][1] = Clefairy("Player 1")
        self.grid[2][1] = Clefairy("Player 2")
        # Add other pieces...

    def move_piece(self, start, end):
        print("entered real move_piece")
        print(f"start[0]: {start[0]}, start[1]: {start[1]}")
        print(f"end[0]: {end[0]}, end[1]: {end[1]}")
        piece = self.grid[start[0]][start[1]]
        if piece is not None:
            target_piece = self.grid[end[0]][end[1]]
            if target_piece is not None and target_piece.owner != piece.owner:
                # Capture the opponent's piece
                if piece.owner == "Player 1":
                    self.captured_pieces_player1.append(target_piece)
                else:
                    self.captured_pieces_player2.append(target_piece)
                
                # Remove the captured piece from the board
                self.grid[end[0]][end[1]] = None
            self.grid[end[0]][end[1]] = piece
            self.grid[start[0]][start[1]] = None
    
    def get_captured_pieces(self, player):
        if player == "Player 1":
            return self.captured_pieces_player1
        else:
            return self.captured_pieces_player2
        #return []
    
    def print_captured_pieces(self):
        print("Captured pieces for Player 1:")
        for piece in self.captured_pieces_player1:
            print(piece)
        print("Captured pieces for Player 2:")
        for piece in self.captured_pieces_player2:
            print(piece)

    # def check_for_winner(self):
        # Check for win conditions
        # return None  # Placeholder
