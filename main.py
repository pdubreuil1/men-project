import matplotlib.pyplot as plt
import numpy as np

from tournament import seq_tournament, parallel_tournament


N = 20
q = 0.2
k = 4
n_epochs = 1000

winners_rank = np.zeros(n_epochs)
for run in range(n_epochs):
    winner_rank = parallel_tournament(k, q, strength_distrib='uniform')
    winners_rank[run] = winner_rank

plt.hist(winners_rank)
plt.title("Histogram of the rank of the tournament's winner")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.show()
