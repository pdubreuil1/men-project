from tournament import seq_tournament

import numpy as np

N = 20
q = 0.2

histogram_of_winners = np.zeros(N)
for run in range(100000):
    winner = seq_tournament(N, q, strength_distrib='uniform')
    histogram_of_winners[winner] += 1
print histogram_of_winners
