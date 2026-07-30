import itertools

# Defining the poker hand: A=1, 2-10, J=11, Q=12, K=13
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = [0, 1, 2, 3]
deck = [(r, s) for r in ranks for s in suits]


straight_rank_sets = [
    {1, 2, 3, 4, 5},       # A-2-3-4-5
    {2, 3, 4, 5, 6},
    {3, 4, 5, 6, 7},
    {4, 5, 6, 7, 8},
    {5, 6, 7, 8, 9},
    {6, 7, 8, 9, 10},
    {7, 8, 9, 10, 11},
    {8, 9, 10, 11, 12},
    {9, 10, 11, 12, 13},
    {1, 10, 11, 12, 13}     # 10-J-Q-K-A
]

count = 0
for hand in itertools.combinations(deck, 5):
    hand_ranks = {card[0] for card in hand}
    if hand_ranks in straight_rank_sets:
        count += 1

print(f"The Probability of all hands including Straight ones equals {count}")
