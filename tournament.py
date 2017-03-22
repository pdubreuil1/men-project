import numpy as np
from random import randint


def seq_tournament(N, q, strength_distrib='uniform'):
    '''
    Args:
        - N (integer): number of players
        - q (float in [0:1]): upset probability
        - strength_distrib (str): distribution used to select strength of
                                  each player
    Output:
        - winner_rank : the rank of the winner.
    '''
    if strength_distrib == 'uniform':
        strength_players = np.random.uniform(low=0.0, high=1.0, size=N)
    rank_players = strength_players.argsort()[::-1]
    list_rank_players = list(rank_players)
    round_id = 0
    while round_id < N-1:
        # select two players
        id_player_1, id_player_2 = np.random.choice(list_rank_players,
                                                    2,
                                                    replace=False)
        if id_player_1 > id_player_2:
            id_player_weak = id_player_2
            id_player_strong = id_player_1
        else:
            id_player_weak = id_player_1
            id_player_strong = id_player_2
        if np.random.binomial(1, 1-q) == 1:
            # weaker player stays
            list_rank_players.remove(id_player_strong)
        else:
            # stronger player stays
            list_rank_players.remove(id_player_weak)

        round_id += 1
    return list_rank_players[0]
