import copy

EMPTY = '.'
WHITE = 'W'
BLACK = 'B'

def create_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = BLACK
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = WHITE
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def get_moves(board, player):
    direction = -1 if player == WHITE else 1
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c] == player:
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    if 0 <= nr < 8 and 0 <= nc < 8:
                        if board[nr][nc] == EMPTY:
                            moves.append(((r, c), (nr, nc)))
                        elif board[nr][nc] != player:
                            jump_r, jump_c = nr + direction, nc + dc
                            if 0 <= jump_r < 8 and 0 <= jump_c < 8 and board[jump_r][jump_c] == EMPTY:
                                moves.append(((r, c), (jump_r, jump_c)))
    return moves

def apply_move(board, move):
    new_board = copy.deepcopy(board)
    (r1, c1), (r2, c2) = move
    player = new_board[r1][c1]
    new_board[r1][c1] = EMPTY
    new_board[r2][c2] = player
    if abs(r2 - r1) == 2:
        mid_r, mid_c = (r1 + r2) // 2, (c1 + c2) // 2
        new_board[mid_r][mid_c] = EMPTY
    return new_board

def evaluate(board):
    w = sum(row.count(WHITE) for row in board)
    b = sum(row.count(BLACK) for row in board)
    return w - b

def minimax(board, depth, alpha, beta, maximizing_player):
    player = BLACK if maximizing_player else WHITE
    moves = get_moves(board, player)
    if depth == 0 or not moves:
        return evaluate(board), None

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            eval_score, _ = minimax(apply_move(board, move), depth - 1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            eval_score, _ = minimax(apply_move(board, move), depth - 1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def game():
    board = create_board()
    print_board(board)
    while True:
        # Player's turn
        moves = get_moves(board, WHITE)
        if not moves:
            print("No moves left. AI wins!")
            break
        print("Your available moves:")
        for i, m in enumerate(moves):
            print(f"{i}: {m}")
        idx = int(input("Choose your move: "))
        board = apply_move(board, moves[idx])
        print_board(board)

        # AI's turn
        ai_moves = get_moves(board, BLACK)
        if not ai_moves:
            print("AI has no moves left. You win!")
            break
        _, best_move = minimax(board, 4, float('-inf'), float('inf'), True)
        print(f"AI moves: {best_move[0]} -> {best_move[1]}")
        board = apply_move(board, best_move)
        print_board(board)

game()
