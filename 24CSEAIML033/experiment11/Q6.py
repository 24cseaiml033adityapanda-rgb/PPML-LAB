import pandas as pd
data =[10,20,30]
labels=['a','b','c']
series = pd.Series(data,index =labels)
print("value at label 'b:",series['b'] )