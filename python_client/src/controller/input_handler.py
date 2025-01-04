import pygame
from model.board import Board
from model.piece import Piece
# from model.game import Game
from view.renderer import Renderer

class InputHandler:
    def __init__(self):
        self.selected_piece = None
        self.valid_moves = [] 
        self.winner_rendered = False 
        self.renderer = Renderer()

    def handle_event(self, event, game):
        if game.game_over and not self.winner_rendered:
            print(f"Game over! {game.winner} wins!")
            self.renderer.render_winner(game.winner)
            self.winner_rendered = True
            #return
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            x, y = event.pos
            print(x)
            print(y)
            grid_x, grid_y = y // 100, x // 100
            print(f"row: {grid_x}")
            print(f"col: {grid_y}")
            clicked_piece = game.board.grid[grid_x][grid_y]

            if clicked_piece and clicked_piece.owner == game.current_player:
                # reselect new piece if misclicked/change of mind
                self.selected_piece = clicked_piece
                self.valid_moves = self.selected_piece.valid_moves((grid_x, grid_y), game.board)
                self.orig_coords = (grid_x, grid_y)
                print(f"Switched to new piece: {self.selected_piece}")
                print(f"Valid moves: {self.valid_moves}")
                    
            elif self.selected_piece:
                print(self.selected_piece)
                # Check if the clicked position is a valid move
                if (grid_x, grid_y) in self.valid_moves:
                    print(grid_x)
                    print(grid_y)
                    print("entered movepiece")
                    game.board.move_piece(self.orig_coords, (grid_x, grid_y))
                    game.check_winner()
                    game.increment_counter()
                    game.board.print_captured_pieces()
                    self.selected_piece = None
                    self.valid_moves = []  # Reset valid moves after the move
                    self.orig_coords = None
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

    def reset(self):
        """Reset the input handler state."""
        self.selected_piece = None
        self.valid_moves = []
        self.winner_message_rendered = False
