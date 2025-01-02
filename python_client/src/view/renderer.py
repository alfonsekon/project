import pygame

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Dobutsu Shogi")

    def render_board(self, board):
        self.screen.fill((255, 255, 255))
        for y, row in enumerate(board.grid):
            for x, piece in enumerate(row):
                rect = pygame.Rect(x * 100, y * 100, 100, 100)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)
                if piece:
                    font = pygame.font.Font(None, 36)
                    text = font.render(piece.name[0], True, (0, 0, 0))
                    self.screen.blit(text, (x * 100 + 35, y * 100 + 35))
        pygame.display.flip()
