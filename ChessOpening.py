import os
import chess.pgn


class ChessOpening:
    def __init__(self, pgn_f):
        self.pgn_f = pgn_f
        self.game = load_game(self.pgn_f)

        self.pgn_string = str(self.game)
        self.pgn_string_moves_only = get_pgn_string_moves_only(self.game)
        self.eco_code = get_val_from_game_header(self.game, "Site")
        self.opening = get_val_from_game_header(self.game, "White")
        self.variation = get_val_from_game_header(self.game, "Black")
        self.half_moves_amount = get_half_moves_amount(self.game)


def load_game(pgn_f):
    return chess.pgn.read_game(pgn_f)


def get_half_moves_amount(game):
    if game is None:
        return None

    return len([move for move in game.mainline_moves()])


def get_pgn_string_moves_only(game):
    if game is None:
        return None

    return str(game.mainline_moves())


def get_val_from_game_header(game, key):
    if game is None:
        return None

    return game.headers[key]


def load_chess_openings(pgn_file_path):
    f = open(pgn_file_path)

    chess_openings = []
    while True:
        chess_opening = ChessOpening(f)
        if chess_opening.game is None:
            break  # end of file
        print("Loaded Game: {} {}, {} - Moves: {}".format(chess_opening.eco_code, chess_opening.opening,
                                                          chess_opening.variation, chess_opening.half_moves_amount))
        chess_openings.append(chess_opening)
    return chess_openings


if __name__ == '__main__':
    pgn_file_path = os.path.join(os.getcwd(), "ECO PGN", "eco.pgn")
    chess_openings = load_chess_openings(pgn_file_path)
