import numpy

pythonArray = [[1, 2, 3], [9, 9, 7]]
npArray = numpy.array(pythonArray)
print(npArray.shape)
print(npArray[0])
print(npArray[:, 1])

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [5,10,15,20])
plt.title("Linear relationship", fontsize=20)
plt.xlabel("X Axis", fontsize=20)
plt.ylabel("Y Axis", fontsize=20)
plt.show()

import pandas as pd
data = {
    'cars': [5,4,1,7],
    'boats': [2,6,0,2]
}

vehicles = pd.DataFrame(data, index=['Peter', 'Sara', 'Ali', 'John'])
print(vehicles.info())
print(vehicles.loc['Ali'])
print(vehicles.head())
