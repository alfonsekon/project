from model.board import Board
from model.piece import Mime, Charman
from view.renderer import Renderer
from controller.input_handler import InputHandler

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "Player 1"
        self.counter = 0
        self.max_moves = 3
        self.winner = None
        self.game_over = False
        self.renderer = Renderer()
        self.input_handler = InputHandler()

    def switch_player(self):
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
    
    def increment_counter(self):
        self.counter += 1
        if self.counter >= self.max_moves:
            self.switch_player()
            self.counter = 0
        print(self.counter)

    def get_counter(self) -> int:
        return self.counter

    def check_winner(self):
        print("entered check_winner")
        if self.checkmate():
            self.winner = self.current_player
            self.game_over = True
            print(f"{self.winner} wins by checkmate!")

            return self.winner

        # opponent = "Player 1" if self.current_player == "Player 2" else "Player 2"
        # captured_pieces = self.board.get_captured_pieces(self.current_player)
        # print(self.current_player)
        # print(captured_pieces)

        # for piece in captured_pieces:
        #     if isinstance(piece, Mime):
        #         self.winner = self.current_player
        #         self.game_over = True
        #         print(f"{self.winner} wins by capturing the opponent's Mime!")

        #         return self.winner
                

        #self.winner = self.board.check_for_winner()
    
    def get_available_pieces_and_moves(self):
        all_moves = {}
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[row])):
                piece = self.board.grid[row][col]
                if piece and piece.owner == self.current_player:
                    position = (row, col)
                    valid_moves = piece.valid_moves(position, self.board)
                    all_moves[position] = valid_moves
        return all_moves

    def print_all_moves(self):
        all_moves = self.get_available_pieces_and_moves()
        print("Valid moves for all pieces of the current player:")
        for position, moves in all_moves.items():
            print(f"Piece at {position}: {moves}")

    def checkmate(self):
        opponent = "Player 1" if self.current_player == "Player 2" else "Player 2"

        # List to store protected opponent pieces (Mime and Charman)
        protected_pieces = []

        # Iterate over the opponent's pieces to find Mime and Charman
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[row])):
                piece = self.board.grid[row][col]
                if piece and piece.owner == opponent and piece.protected:
                    protected_pieces.append((piece, (row, col)))  # Store the piece and its position

        # Get the current player's valid moves
        current_player_moves = self.get_available_pieces_and_moves()

        # Track how many protected pieces are threatened
        threatened_count = 0

        for position, moves in current_player_moves.items():
            for move in moves:
                # Check if the move threatens any of the protected pieces
                for protected_piece, protected_pos in protected_pieces:
                    if move == protected_pos:
                        print(f"Piece at {position} can move to {move}, which is an opponent's protected {protected_piece.__class__.__name__}.")
                        threatened_count += 1

        # Print the number of protected pieces threatened for debugging
        print(f"Number of protected pieces threatened: {threatened_count}")

        # Return True if both protected pieces are threatened, otherwise False
        if threatened_count == len(protected_pieces):
            return True
        else:
            return False


    def reset(self):
        self.board = Board() 
        self.current_player = "Player 1"  
        self.counter = 0 
        self.max_moves = 3  
        self.winner = None  
        self.game_over = False
