import numpy as np


def seq_tournament(N, q, strength_distrib="uniform", **kwargs):
    '''
    Args:
        - N (integer): number of players
        - q (float in [0:1/2]): upset probability
        - strength_distrib (str): distribution used to select strength of
        each player
        - kwargs: keyword arguments passed to the initial distribution.
    Output:
        - winner_rank : the rank of the winner.
    '''
    if strength_distrib == "uniform":
        rank_players = np.random.uniform(low=0.0, high=1.0, size=N)
    elif strength_distrib == "power":
        rank_players = np.random.power(a=kwargs.get("power"), size=N)
    else:
        raise ValueError(
            "{} is not an implemented initial distribition for ranks.".format(
                strength_distrib
            ))
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


def parallel_tournament(k, q, strength_distrib="uniform", **kwargs):
    '''
    Args:
        - k (integer): power of 2
        - q (float in [0:1/2]): upset probability
        - strength_distrib (str): distribution used to select strength of
        each player
        - kwargs: keyword arguments passed to the initial distribution.
    Output:
        - winner_rank : the rank of the winner.
    '''
    N = 2**k
    if strength_distrib == "uniform":
        rank_players = np.random.uniform(low=0.0, high=1.0, size=N)
    elif strength_distrib == "power":
        rank_players = np.random.power(a=kwargs.get("power"), size=N)
    else:
        raise ValueError(
            "{} is not an implemented initial distribition for ranks.".format(
                strength_distrib
            ))
    list_rank_players = list(rank_players)
    for round_id in range(k - 1):
        list_permuted = np.random.permutation(list_rank_players)
        rank_players_1 = list_permuted[:N // 2]
        rank_players_2 = list_permuted[N // 2:N]
        for rank_player_1, rank_player_2 in zip(
            rank_players_1, rank_players_2
        ):
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
        N = len(list_rank_players)
    return list_rank_players[0]
