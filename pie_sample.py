from random import random

N = 100000
N_in = 0
for i in range(N):
    x, y = random(), random()
    if x**2 + y**2 <= 1:
        N_in += 1

print((N_in / N) * 4)
