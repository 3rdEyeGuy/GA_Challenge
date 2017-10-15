import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

###style.use('ggplot')

x,y = np.loadtxt('backers_hist_data.csv', unpack=True, delimiter=',')

plt.bar(x, y, width = 90)
plt.ylabel('Frequency')
plt.xlabel('Backers')
plt.title('Histogram of Backers')

plt.show()
