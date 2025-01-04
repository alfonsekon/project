from model.piece import Piece, Mime, Goldqueen, Sighducky, Clefairy
from typing import Sequence, Tuple

class PieceInitializer:
    @staticmethod
    def initialize_pieces() -> Sequence[Tuple[int, int, Piece]]:
        pieces = [
            (0, 0, Goldqueen("Player 1")),
            (3, 0, Goldqueen("Player 2")),
            (0, 1, Mime("Player 1")),
            (3, 1, Mime("Player 2")),
            (0, 2, Sighducky("Player 1")),
            (3, 2, Sighducky("Player 2")),
            (1, 1, Clefairy("Player 1")),
            (2, 1, Clefairy("Player 2")),
        ]
        return pieces
