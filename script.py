#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt

print('Number of arguments: %i arguments' % len(sys.argv))
print('Argument List:' + str(sys.argv))

data = pd.read_csv(sys.argv[1])
data.dropna(inplace = True)
data.plot(kind = 'scatter', x='Hits', y='Salary')
plt.savefig('output.jpg')


