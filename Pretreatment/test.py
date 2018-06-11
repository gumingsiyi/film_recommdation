import Pretreatment.getdata as gd
import pandas as pd
import numpy as np

arr = np.arange(25).reshape(5, 5)

ma = np.matrix(arr)
mb = ma
print(ma)
print(mb)

print(ma+mb*2)

x = np.max(ma)

print(x)