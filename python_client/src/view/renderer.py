import pygame
import os
from typing import List, Tuple
from model.piece import Piece  

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Dobutsu Shogi")
        self.images = self.load_piece_images()

    def load_piece_images(self):
        """Load images for each piece from the assets folder."""
        assets_path = os.path.join(os.path.dirname(__file__), "assets")
        
        images = {
            "Charman": pygame.image.load(os.path.join(assets_path, "charman.png")),
            "Clefairy": pygame.image.load(os.path.join(assets_path, "clefairy.png")),
            "Goldqueen": pygame.image.load(os.path.join(assets_path, "goldqueen.png")),
            "Mime": pygame.image.load(os.path.join(assets_path, "mime.png")),
            "Monkey": pygame.image.load(os.path.join(assets_path, "monkey.png")),
            "Sighducky": pygame.image.load(os.path.join(assets_path, "sighducky.png")),
        }
        for key in images:
            images[key] = pygame.transform.scale(images[key], (80, 80))
        return images

    def render_board(self, board, valid_moves: List[Tuple[int, int]] = None, selected_piece: Piece = None):
        """Renders the board with optional highlights for valid moves"""
        self.screen.fill((255, 255, 255))  # Background color

        for y, row in enumerate(board.grid):
            for x, piece in enumerate(row):
                rect = pygame.Rect(x * 100, y * 100, 100, 100)
                
                # print(f"Valid Moves: {valid_moves}")
                # print(f"x:{x}, y:{y}")
                if valid_moves and (y, x) in valid_moves:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)  
                    inner_rect = rect.inflate(-4, -4)  
                    pygame.draw.rect(self.screen, (0, 255, 0), inner_rect)  
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)  # Normal border color

                # # Draw the piece's first letter at its position if it's not None
                # if piece:
                #     font = pygame.font.Font(None, 36)
                #     text = font.render(piece.name[0], True, (0, 0, 0))  # Display piece's first letter
                #     self.screen.blit(text, (x * 100 + 35, y * 100 + 35))

                if piece:
                    image = self.images.get(piece.name)  # Get the corresponding image for the piece
                    if image:
                        self.screen.blit(image, (x * 100 + 10, y * 100 + 10)) 

        pygame.display.flip()
    
    def render_winner(self, winner: str):
        """
        Renders a "Player _ wins" message with a semi-transparent white background.

        Args:
            winner (str): The name of the winning player (e.g., "Player 1" or "Player 2").
        """
        print(f"Rendering winner: {winner}")  
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 153))
        font = pygame.font.Font(None, 72)
        text = font.render(f"{winner} wins!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        #pygame.display.update()
