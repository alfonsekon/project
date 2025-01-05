import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.piece_sound = pygame.mixer.Sound("src/view/assets/piece1.mp3")
        self.bgm = pygame.mixer.Sound("src/view/assets/bgm.mp3")

    def load_sound(self, name, filepath):
        self.sounds[name] = pygame.mixer.Sound(filepath)

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()