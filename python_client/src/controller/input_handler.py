import pygame
from model.piece import Piece
from view.renderer import Renderer
from typing import Optional, List, Tuple, TYPE_CHECKING, cast
if TYPE_CHECKING:
    from model.game import Game

class InputHandler:
    def __init__(self):
        self.selected_piece: Optional[Piece] = None
        self.valid_moves: List[Tuple[int, int]] = [] 
        self.winner_rendered = False 
        self.renderer = Renderer()
        self.orig_coords: Optional[Tuple[int, int]]

    def handle_event(self, event: pygame.event.Event, game: "Game"):
        if game.game_over and not self.winner_rendered:
            print(f"Game over! {game.winner} wins!")
            #self.renderer.render_winner(game.winner)
            self.winner_rendered = True
            #return
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            cell_size = self.renderer.get_cell_size()
            print(cell_size)
            board_width = cell_size * self.renderer.cols
            board_height = cell_size * self.renderer.rows

            x_offset = (self.renderer.screen.get_width() - board_width) // 2
            y_offset = (self.renderer.screen.get_height() - board_height) // 2
            # board_width = self.renderer.screen.get_width() - x_offset*2
            # board_height = self.renderer.screen.get_height() - x_offset*2

            x, y = event.pos
            print(f"x: {x}")
            print(f"y: {y}")
            print(f"board width: {board_width}")
            print(f"board height: {board_height}")
            print(f"x_offset: {x_offset}")
            print(f"y_offset: {y_offset}")
            screen_height = self.renderer.screen.get_height()
            screen_width = self.renderer.screen.get_width()
            print(f"screen_height: {screen_height}")
            print(f"screen_width: {screen_width}")
            grid_x, grid_y = (y - y_offset) // cell_size, (x - x_offset) // cell_size
            print(f"row: {grid_x}")
            print(f"col: {grid_y}")
            clicked_piece = cast(Optional[Piece], game.board.grid[grid_x][grid_y])

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
                    if self.orig_coords is not None:
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
                piece = cast(Piece, game.board.grid[grid_x][grid_y])
                if piece and piece.owner == game.current_player:
                    self.selected_piece = piece
                    print(self.selected_piece)
                    # Calculate valid moves as soon as the piece is selected
                    self.valid_moves = self.selected_piece.valid_moves((grid_x, grid_y), game.board)
                    self.orig_coords = (grid_x, grid_y)
                    print(f"Valid moves: {self.valid_moves}")
                else:
                    print("No valid piece selected or wrong player!")

    def reset(self):

        self.selected_piece = None
        self.valid_moves = []
        self.winner_message_rendered = False
