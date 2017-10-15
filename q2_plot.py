import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('backers_hist_data.csv',sep=',',index_col=0)

data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('Backers')
plt.title('Histogram of Backers')

plt.show()
