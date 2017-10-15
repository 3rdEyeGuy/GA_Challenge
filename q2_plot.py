import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


x,y = np.loadtxt('backers_hist_data.csv', unpack=True, delimiter=',')

plt.hist(x, y, histtype='bar',rwidth = 1.0)
plt.ylabel('Frequency')
plt.xlabel('Backers')
plt.title('Histogram of Backers')

plt.show()
