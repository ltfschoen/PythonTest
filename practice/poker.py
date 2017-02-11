def poker(hands):
    # Return best hand given list of hands
    return max(hands, key=hand_rank)

    # straight(ranks): returns True if the hand is a straight.
    # flush(hand):     returns True if the hand is a flush.
    # kind(n, ranks):  returns first rank the hand has exactly n of.
    #                  Given hand with 4 sevens it returns 7.
    # two_pair(ranks): Given a two pair, it returns corresponding
    #                  ranks as a tuple. i.e. Given a hand with 2 twos
    #                  and 2 fours it returns (4, 2).
    # card_ranks(hand) returns an ORDERED tuple of ranks in a hand
    #                  (ordered highest to lowest rank)

def hand_rank(hand):
    # Return value indicating rank of given hand
    ranks = card_ranks(hand)
    if royal(ranks) and flush(hand):            # royal
        return 9
    elif straight(ranks) and flush(hand):       # straight flush
        # Return tuple
        # - 1st element is single value indicating type of ranking of given hand
        # - 2nd element serves to break tied hands (of straight flushes)
        #
        # i.e. 6 7 8 9 T > 2 3 4 5 6
        #     (8, 10)    > (8, 6)
        return (8, max(ranks))
    elif kind(4, ranks):                        # 4 of kind
        # Boolean test using `kind(4, ranks)`
        # Return 3x element tuple
        # - 1st element indicates rank of hand
        # - 2nd element breaks ties of the four of a kind cards
        #   (Overloading the function 'kind' with using `kind(4, ranks)` to return a value.
        #    Note: Not an issue since cards start from 2 instead of 0, which may be interpreted as false incorrectly)
        # - 3rd element breaks ties of the fifth card
        #
        # i.e. 9 9 9 9 3
        #      (7, 9, 3)
        return (7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                           # flush
        return (5, ranks)
    elif straight(ranks):                       # straight
        return (4, max(ranks))
    elif kind(3, ranks):                        # 3 of kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                       # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                        # 2 of kind
        return (1, kind(2, ranks), ranks)
    else:                                       # high card
        return (0, ranks)

def custom_rank_sort(cards_by_rank, ranks_and_weightings):
    return sorted(cards_by_rank, key=lambda x:ranks_and_weightings[x[0]])

def card_ranks(cards):
    # Solution
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    print ("Card ranks {} is: {}".format(cards, ranks) )
    return ranks

    #    # Your code here.
    #    cards_by_rank = [card[0] for card in cards]
    #    ranks_and_weightings = {'A': 1,'K': 2,'Q': 3,'J': 4, 'T': 5, '9': 6, '8': 7,
    #                            '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
    #    card_ranks_sorted = custom_rank_sort(cards_by_rank, ranks_and_weightings)
    #
    #    for n,i in enumerate(card_ranks_sorted):
    #        if i == 'A':
    #            card_ranks_sorted[n] = 14
    #        elif i == 'K':
    #            card_ranks_sorted[n] = 13
    #        elif i == 'Q':
    #            card_ranks_sorted[n] = 12
    #        elif i == 'J':
    #            card_ranks_sorted[n] = 11
    #        elif i == 'T':
    #            card_ranks_sorted[n] = 10
    #        else:
    #            card_ranks_sorted[n] = int(card_ranks_sorted[n])
    #
    #    cards_replaced = [card for card in card_ranks_sorted]
    #
    #    print ("Card ranks {} is: {}".format(cards_by_rank, card_ranks_sorted) )
    #    return card_ranks_sorted

# Note: ranks given will be ordered from largest to smallest
def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    # Solution
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5

    #    # Your code here.
    #    return all(ranks[i] > ranks[i+1] for i in range(len(ranks)-1)) and ranks[0] <= 14 and ranks[-1] >= 2 and len(ranks) == 5

def flush(hand):
    """Return True if all the cards have the same suit."""
    # Solution
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

    #    # Your code here.
    #    return all(suit[1] is hand[0][1] for suit in hand)

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Solution
    highpair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if highpair and lowpair != highpair:
        return (highpair, lowpair)
    else:
        return None

    #    # Your code here.
    #    pairs = []
    #    for r in ranks:
    #        if ranks.count(r) == 2:
    #            pairs.append(r)
    #    unique = list(set(pairs))
    #    if len(unique) == 2:
    #        unique_sorted = unique.sort(reverse=True)
    #        return (unique[0], unique[1])
    #    else:
    #        return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there no n-of-a-kind in the hand."""
    # Solution
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None
    #    # Your code here.
    #    n_of_kind = ranks[0:n]
    #    if len(ranks) == 0:
    #        return None
    #    elif all(rank == ranks[0] for rank in n_of_kind) and ranks[n] != ranks[0]:
    #        if n == 1:
    #            if ranks[0] != ranks[1]:
    #                return ranks[0]
    #            else:
    #                return None
    #        if n == 2:
    #            if ranks[0] == ranks[1]:
    #                return ranks[0]
    #            else:
    #                return None
    #        if n == 3:
    #            if ranks[0] == ranks[1] == ranks[2]:
    #                return ranks[0]
    #            else:
    #                return None
    #        if n == 4:
    #            if ranks[0] == ranks[1] == ranks[2] == ranks[3]:
    #                return ranks[0]
    #            else:
    #                return None
    #    else:
    #        return None

# Specification of test suite sanity cases for implemented functions in poker program
def test_winning_hand():
    rf = "TD JD QD KD AD".split() # royal flush / five of a kind
    sf = "6C 7C 8C 9C TC".split() # straight flush
    fk = "9D 9H 9S 9C 7D".split() # four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    f = "2D 4D 6D TD QD".split() # flush (unordered)
    s = "6D 7D 8C 9H TS".split() # straight
    tk = "6D 6H 6S 4H 9D".split() # three of a kind
    tp = "2D 2H 4S 4H 9D".split() # two pair
    op = "2D 2H 6S 9H QC".split() # one pair
    hc = "KC 2D 4H 7C 9D".split() # high card

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    # Tests that card_ranks returns cards in order from highest card first
    # for use in tie breakers
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    # Tests normal values
    assert poker([rf, sf, fh]) == rf
    assert poker([sf, fk, fh]) == sf

    # Test extreme values
    #   - Two of the same hand
    assert poker([fh, fh]) == fh
    #   - Only one hands passed to poker function is the winner
    assert poker([fh]) == fh
    #   - No hands passed to poker function results in error as no hand to return
    #   - Large quantity of hands passed to poker function
    assert poker([fh] * 100) == fh

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(f) == (5, [12, 10, 6, 4, 2])
    assert hand_rank(s) == (4, 10)
    assert hand_rank(tk) == (3, 6, [6, 6, 6, 9, 4])
    assert hand_rank(tp) == (2, 4, 2, [9, 4, 4, 2, 2])
    assert hand_rank(op) == (1, 2, [12, 9, 6, 2, 2])
    assert hand_rank(hc) == (0, [13, 9, 7, 4, 2])

    return "tests pass"

test_winning_hand()
