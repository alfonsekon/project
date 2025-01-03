import pygame
from typing import List, Tuple
from model.piece import Piece  # Assuming piece.py is in the same directory

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Dobutsu Shogi")

    def render_board(self, board, valid_moves: List[Tuple[int, int]] = None, selected_piece: Piece = None):
        """Renders the board with optional highlights for valid moves"""
        self.screen.fill((255, 255, 255))  # Background color

        for y, row in enumerate(board.grid):
            for x, piece in enumerate(row):
                rect = pygame.Rect(x * 100, y * 100, 100, 100)
                
                # Draw background for each cell
                if valid_moves and (x, y) in valid_moves:
                    # Highlight valid moves in green
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)  # Normal border color

                # Draw the piece's first letter at its position if it's not None
                if piece:
                    font = pygame.font.Font(None, 36)
                    text = font.render(piece.name[0], True, (0, 0, 0))  # Display piece's first letter
                    self.screen.blit(text, (x * 100 + 35, y * 100 + 35))

        pygame.display.flip()
