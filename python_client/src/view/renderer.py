import pygame
import os
from typing import List, Tuple
from model.piece import Piece  

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 700), pygame.RESIZABLE)
        pygame.display.set_caption("Dobutsu Shogi")
        self.images = self.load_piece_images()
        self.rows = 8  # Number of rows on the board
        self.cols = 7
        self.captured_piece_positions = {
            "Player 1": [],
            "Player 2": []
        }
        #self.cell_size = 100

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

    def calculate_cell_size(self):
        """Calculate the cell size dynamically based on the window size."""
        screen_width, screen_height = pygame.display.get_window_size()
        
        cell_width = screen_width // self.cols
        cell_height = screen_height // self.rows
        self.cell_size = min(cell_width, cell_height)
        # print(screen_width)
        # print(screen_height)
        # print(cell_width)
        # print(cell_height)
        # print(self.cell_size)
    
    def get_cell_size(self):
        """Ensure cell size is calculated and return it."""
        self.calculate_cell_size()  # Recalculate before returning, in case the window size changed.
        return self.cell_size

    def render_captured_pieces(self, board):
        """Renders captured pieces for both players and tracks their positions for interaction."""
        # Coordinates for rendering captured pieces
        top_y_offset = 50
        bottom_y_offset = self.screen.get_height() - 260
        x_offset = 10
        piece_spacing = 80
        row_spacing = 80
        max_pieces_per_row = 6
        font = pygame.font.Font(None, 36)

        # Player 1's captured pieces
        p1_captured_label = font.render("Player 1 Captured Pieces", True, (0, 0, 0))
        self.screen.blit(p1_captured_label, (x_offset, top_y_offset - 30))
        # print("Player 1's Captured Pieces Positions:")
        for i, piece in enumerate(board.captured_pieces_player1):
            row = i // max_pieces_per_row
            col = i % max_pieces_per_row
            image = self.images.get(piece.name)
            if image:
                image = pygame.transform.scale(image, (70, 70))
                rect = self.screen.blit(image, (x_offset + col * piece_spacing, top_y_offset + row * row_spacing))
                self.captured_piece_positions["Player 1"].append((piece, rect))
                # Print the piece name and its position
                # print(f"  {piece.name}: {rect.topleft}")

        # Player 2's captured pieces
        p2_captured_label = font.render("Player 2 Captured Pieces", True, (0, 0, 0))
        self.screen.blit(p2_captured_label, (x_offset, bottom_y_offset - 30))
        # print("Player 2's Captured Pieces Positions:")
        for i, piece in enumerate(board.captured_pieces_player2):
            row = i // max_pieces_per_row
            col = i % max_pieces_per_row
            image = self.images.get(piece.name)
            if image:
                image = pygame.transform.scale(image, (70, 70))
                rect = self.screen.blit(image, (x_offset + col * piece_spacing, bottom_y_offset + row * row_spacing))
                self.captured_piece_positions["Player 2"].append((piece, rect))
                # Print the piece name and its position
                # print(f"  {piece.name}: {rect.topleft}")

    def render_board(self, board, valid_moves: List[Tuple[int, int]] = None, selected_piece: Piece = None, captured_pieces: List[Piece] = None, current_player = "Player 1"):
        """Renders the board with optional highlights for valid moves, centered on the screen."""
        self.calculate_cell_size()
        self.screen.fill((255, 255, 255))  # Background color

        board_width = self.cell_size * self.cols
        board_height = self.cell_size * self.rows

        x_offset = (self.screen.get_width() - board_width) // 2
        y_offset = (self.screen.get_height() - board_height) // 2
        

        for y, row in enumerate(board.grid):
            for x, piece in enumerate(row):
                starting_x = x * self.cell_size + x_offset
                starting_y = y * self.cell_size + y_offset
                rect = pygame.Rect(
                    starting_x,
                    starting_y,
                    self.cell_size,
                    self.cell_size
                )

                # Highlight valid moves
                if piece and piece.protected: #lalagyan ko pa ng or opponent.piece.protected
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)  # Default border for the cell
                elif valid_moves and (y, x) in valid_moves:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)
                    inner_rect = rect.inflate(-4, -4)
                    pygame.draw.rect(self.screen, (0, 255, 0), inner_rect)
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)
                # Draw the piece if present
                if piece:
                    image = self.images.get(piece.name)
                    if image:
                        image_size = self.cell_size - 20
                        image = pygame.transform.scale(image, (image_size, image_size))
                        self.screen.blit(
                            image,
                            (x * self.cell_size + x_offset + (self.cell_size - image_size) // 2,
                            y * self.cell_size + y_offset + (self.cell_size - image_size) // 2)
                        )

        self.render_captured_pieces(board)
        self.render_current_player(current_player)

        pygame.display.flip()

    def render_current_player(self, current_player):
        """Renders the current player label on the right side of the screen."""
        font = pygame.font.Font(None, 36)
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        # Render the "Current Player:" label
        label_text = "Current Player:"
        current_player_label = font.render(label_text, True, (0, 0, 0))
        label_width = current_player_label.get_width()
        
        # Calculate position for the label (top-right corner)
        label_x = screen_width - label_width - 200  # Add some padding from the right edge
        label_y = screen_height * 0.2  # 20% down from the top

        self.screen.blit(current_player_label, (label_x, label_y))

        # Render the current player's name below the label
        player_text = "Player 1" if current_player == "Player 1" else "Player 2"
        current_player_name = font.render(player_text, True, (0, 0, 0))
        name_width = current_player_name.get_width()

        # Position the player's name centered below the label
        name_x = screen_width - name_width - 100  # Align with label_x
        name_y = label_y 

        self.screen.blit(current_player_name, (name_x, name_y))

            

    
    def render_winner(self, winner: str):
        """
        Renders a "Player _ wins" message with a semi-transparent white background.

        Args:
            winner (str): The name of the winning player (e.g., "Player 1" or "Player 2").
        """
        print(f"Rendering winner: {winner}")  
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 153))
        font = pygame.font.Font(None, 50)
        text = font.render(f"{winner} wins!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        #pygame.display.update()

    def render_play_again_button(self):
        button_width, button_height = 200, 50
        button_x = (self.screen.get_width() - button_width) // 2
        button_y = (self.screen.get_height() // 2) + 30  

        self.play_again_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(self.screen, (0, 128, 0), self.play_again_button_rect) 

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Play Again", True, (255, 255, 255))  
        text_rect = text_surface.get_rect(center=self.play_again_button_rect.center)
        self.screen.blit(text_surface, text_rect)

