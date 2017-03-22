from tournament import seq_tournament, parallel_tournament

import numpy as np

N = 20
q = 0.2
k = 3

histogram_of_winners = np.zeros(2**k)
for run in range(1000):
    winner = parallel_tournament(k, q, strength_distrib='uniform')
    histogram_of_winners[winner] += 1
print(histogram_of_winners)
