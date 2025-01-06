import pygame
from typing import Dict

class AudioRenderer:
    def __init__(self):
        pygame.mixer.init()
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.piece_sound = pygame.mixer.Sound("src/view/assets/piece1.mp3")

    def load_sound(self, name: str, filepath: str):
        self.sounds[name] = pygame.mixer.Sound(filepath)

    def play_sound(self, name: str):
        if name in self.sounds:
            self.sounds[name].play()