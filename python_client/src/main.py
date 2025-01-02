from model.game import Game
from view.renderer import Renderer
from controller.flow import GameController

def main():
    # Initialize components
    game = Game()
    renderer = Renderer()
    controller = GameController(game, renderer)
    
    # Start the game loop
    controller.run_game()

if __name__ == "__main__":
    main()
