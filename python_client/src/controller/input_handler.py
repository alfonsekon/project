import pygame

class InputHandler:
    def __init__(self):
        self.selected_piece = None

    def handle_event(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x, grid_y = x // 100, y // 100
            if self.selected_piece:
                game.board.move_piece(self.selected_piece, (grid_x, grid_y))
                self.selected_piece = None
            else:
                self.selected_piece = (grid_x, grid_y)
