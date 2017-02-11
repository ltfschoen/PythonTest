#import numpy as np
#
#def get_rank_when_digit(rank, number_ranks):
#    if rank.isdigit() == True:
#        if int(rank) in number_ranks:
#            return True
#        else:
#            return False
#
#def custom_people_rank_sort(people_rank_values, people_ranks_and_weightings):
#    return sorted(people_rank_values, key=lambda x:people_ranks_and_weightings[x[0]])
#
#def get_people_ranks_sorted_from_highest(ranks, people_ranks, ranks_np, people_ranks_and_weightings):
#    people_rank_indices = [i for i in range(len(ranks)) if ranks[i] in people_ranks]
#    if people_rank_indices:
#        people_rank_indices_np = np.array(people_rank_indices)
#        people_rank_values = ranks_np[people_rank_indices_np]
#        people_rank_values_custom_sorted = custom_people_rank_sort(people_rank_values, people_ranks_and_weightings)
##        people_rank_values_custom_sorted_replaced = [people_rank_values_custom_sorted
##                     .replace('A', '14')
##                     .replace('K', '13')
##                     .replace('Q', '12')
##                     .replace('J', '11') for rank in ranks]
#        return people_rank_values_custom_sorted
#    else:
#        return []
#
#def get_number_ranks_sorted_from_highest(ranks, number_ranks, ranks_np):
#    number_rank_indices = [i for i in range(len(ranks)) if get_rank_when_digit(ranks[i], number_ranks)]
#    if number_rank_indices:
#        number_rank_indices_np = np.array(number_rank_indices)
#        number_rank_values = ranks_np[number_rank_indices_np]
#        number_rank_values_sorted_desc = sorted(number_rank_values, reverse=True)
#        return number_rank_values_sorted_desc
#    else:
#        return []
#
#def card_ranks(cards):
#    # Return list of ranks, sorted from highest to lowest
#
#    # Break down the tuple from element in cards into rank and suit
#    # Create a list from just collecting the ranks
#    ranks = [rank for rank, suit in cards]
#    people_ranks = ['A', 'K', 'Q', 'J']
#    # dictionary that allows mapping every first element to its "weight"
#    # for checking the dictionary inside the sorting function
#    people_ranks_and_weightings = {'A': 1,'K': 2,'Q': 3,'J': 4}
#    number_ranks = np.arange(0, 11)
#    ranks_np = np.array(ranks)
#
#    people_ranks_sorted_from_highest = get_people_ranks_sorted_from_highest(ranks, people_ranks, ranks_np, people_ranks_and_weightings)
#
#    number_ranks_sorted_from_highest = get_number_ranks_sorted_from_highest(ranks, number_ranks, ranks_np)
#
#    people_ranks_sorted_from_highest = people_ranks_sorted_from_highest + number_ranks_sorted_from_highest
#
#    return people_ranks_sorted_from_highest
##    elements = [10, 11, 12, 13, 14, 15]
##    indices = (1,1,2,1,5)
##    indices = ['A','K','Q','J']
##
##    result_list = [ranks[i] for i in indices]
#
#
##    ranks.sort(reverse=True)
##    return ranks_mod
#
##poker([['TD', 'JD', 'QD', 'KD', 'AD'], ['6C', '7C', '8C', '9C', 'TC']])
##test_winning_hand()
#
#cards = ['AC', '3D', '4S', 'KH']
##print ( ("Card ranks {} is: {}".format(cards, card_ranks(cards))) ) #should output [14, 13, 4, 3]
#
#ordered_cards_by_first_index = card_ranks(cards)
#
#print ("Card ranks {} is: {}".format(cards, ordered_cards_by_first_index) )
