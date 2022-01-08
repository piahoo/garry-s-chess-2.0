import conf


def get_legal_captures(piece):
    potential_captures = piece.get_potential_captures()
    legal_captures = []

    for potential_capture in potential_captures:
        if is_occupied_by_enemy(piece, potential_capture):
            legal_captures.append(potential_capture)

    return legal_captures


def is_occupied_by_enemy(piece, square):
    for piece in conf.all_pieces:
        if piece.square == square and piece.color is not piece.color:
            return True
    return False


def get_legal_moves(piece):
    potential_moves = piece.get_potential_moves()
    legal_moves = []

    for potential_move in potential_moves:
        if is_not_occupied(potential_move):
            legal_moves.append(potential_move)

    return legal_moves


def is_not_occupied(square):
    for piece in conf.all_pieces:
        if piece.square == square:
            return False
    return True
