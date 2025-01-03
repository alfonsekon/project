import pygame
from model.board import Board
from model.piece import Piece

class InputHandler:
    def __init__(self):
        self.selected_piece = None
        self.valid_moves = []  # Store valid moves

    def handle_event(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x)
            print(y)
            grid_x, grid_y = y // 100, x // 100
            print(f"row: {grid_x}")
            print(f"col: {grid_y}")

            if self.selected_piece:
                print(self.selected_piece)
                # Check if the clicked position is a valid move
                if (grid_x, grid_y) in self.valid_moves:
                    print(grid_x)
                    print(grid_y)
                    print("entered movepiece")
                    game.board.move_piece(self.orig_coords, (grid_x, grid_y))
                    self.selected_piece = None
                    self.valid_moves = []  # Reset valid moves after the move
                else:
                    print("Invalid move!")
            else:
                # Select the piece if it belongs to the current player
                piece = game.board.grid[grid_x][grid_y]
                if piece and piece.owner == game.current_player:
                    self.selected_piece = piece
                    print(self.selected_piece)
                    # Calculate valid moves as soon as the piece is selected
                    self.valid_moves = self.selected_piece.valid_moves((grid_x, grid_y), game.board)
                    self.orig_coords = [grid_x, grid_y]
                    print(f"Valid moves: {self.valid_moves}")
                else:
                    print("No valid piece selected or wrong player!")
