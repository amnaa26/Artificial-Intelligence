def alpha_beta(cards, left, right, is_max_turn, alpha, beta):
    if left > right:
        return 0

    if is_max_turn:
        # Max wants the maximum score
        pick_left = cards[left] + alpha_beta(cards, left + 1, right, False, alpha, beta)
        pick_right = cards[right] + alpha_beta(cards, left, right - 1, False, alpha, beta)
        best = max(pick_left, pick_right)
        alpha = max(alpha, best)
        if beta <= alpha:
            return best
        return best
    else:
        # Min plays greedy, always picking the lower value
        if cards[left] < cards[right]:
            return alpha_beta(cards, left + 1, right, True, alpha, beta)
        else:
            return alpha_beta(cards, left, right - 1, True, alpha, beta)

def play_game(cards):
    max_score = 0
    min_score = 0
    left, right = 0, len(cards) - 1
    turn = 'Max'

    print(f"Initial Cards: {cards}")

    while left <= right:
        if turn == 'Max':
            # Simulate both choices to decide best move
            pick_left = cards[left] + alpha_beta(cards, left + 1, right, False, float('-inf'), float('inf'))
            pick_right = cards[right] + alpha_beta(cards, left, right - 1, False, float('-inf'), float('inf'))

            if pick_left >= pick_right:
                chosen = cards[left]
                left += 1
            else:
                chosen = cards[right]
                right -= 1

            max_score += chosen
            print(f"Max picks {chosen}, Remaining Cards: {cards[left:right+1]}")
            turn = 'Min'

        else:  # Min's turn (greedy)
            if cards[left] <= cards[right]:
                chosen = cards[left]
                left += 1
            else:
                chosen = cards[right]
                right -= 1

            min_score += chosen
            print(f"Min picks {chosen}, Remaining Cards: {cards[left:right+1]}")
            turn = 'Max'

    print(f"Final Scores - Max: {max_score}, Min: {min_score}")
    if max_score > min_score:
        print("Winner: Max")
    elif min_score > max_score:
        print("Winner: Min")
    else:
        print("It's a Draw!")

# Example
cards = [4, 10, 6, 2, 9, 5]
play_game(cards)
