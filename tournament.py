import numpy as np


def seq_tournament(N, q, strength_distrib='uniform'):
    '''
    Args:
        - N (integer): number of players
        - q (float in [0:1/2]): upset probability
        - strength_distrib (str): distribution used to select strength of
                                  each player
    Output:
        - winner_rank : the rank of the winner.
    '''
    if strength_distrib == 'uniform':
        strength_players = np.random.uniform(low=0.0, high=1.0, size=N)
    rank_players = strength_players.argsort()[::-1]
    list_rank_players = list(rank_players)
    for round_id in range(N - 1):
        # select two players
        rank_player_1, rank_player_2 = np.random.choice(
            list_rank_players,
            2,
            replace=False)
        if rank_player_1 < rank_player_2:
            rank_player_weak = rank_player_2
            rank_player_strong = rank_player_1
        else:
            rank_player_weak = rank_player_1
            rank_player_strong = rank_player_2
        if np.random.binomial(1, q) == 1:
            # weaker player stays
            list_rank_players.remove(rank_player_strong)
        else:
            # stronger player stays
            list_rank_players.remove(rank_player_weak)

    return list_rank_players[0]


def parallel_tournament(k, q, strength_distrib):
    '''
    Args:
        - k (integer): power of 2
        - q (float in [0:1/2]): upset probability
        - strength_distrib (str): distribution used to select strength of
                                  each player
    Output:
        - winner_rank : the rank of the winner.
    '''
    N = 2**k
    if strength_distrib == 'uniform':
        strength_players = np.random.uniform(low=0.0, high=1.0, size=N)
    rank_players = strength_players.argsort()[::-1]
    list_rank_players = list(rank_players)
    round_id = 0
    N1 = N
    while round_id < k-1:
        list_permuted = np.random.permutation(list_rank_players)
        players_1 = list_permuted[:int((N1)/2)]
        players_2 = list_permuted[int((N1)/2):N]
        for i in range(len(players_1)):
            if players_1[i] < players_2[i]:
                id_player_weak = players_2[i]
                id_player_strong = players_1[i]
            else:
                id_player_weak = players_1[i]
                id_player_strong = players_2[i]
            if np.random.binomial(1, q) == 1:
                # weaker player stays
                list_rank_players.remove(id_player_strong)
            else:
                # stronger player stays
                list_rank_players.remove(id_player_weak)
        round_id += 1
        N1 = N1 / 2
    return list_rank_players
