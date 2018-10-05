import matplotlib.pyplot as plt
from funs import get_zero_center_vs_rouche_stat


stat = get_zero_center_vs_rouche_stat(10 ** 4, 10, 100)
print('max ratio =', max(stat))
plt.hist(stat, bins=100)
plt.show()

# mean = sum(stat) / len(stat)
# print('mean ratio =', mean)
