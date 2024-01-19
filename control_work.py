import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

# data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
# data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
# data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
# data.loc[data['whoAmI'] == 'human', 'human'] = '1'
# print(data.head())  

# data.loc[data['whoAmI'] == 'robot', 'whoAmI'] = '0'
# data.loc[data['whoAmI'] == 'human', 'whoAmI'] = '1'
# print(data.head())

lst2 = []
for item in data['whoAmI']:
    if item == 'human':
        lst2.append(1)
    elif item == 'robot':
        lst2.append(0)
data = pd.DataFrame({'whoAmI':lst2})   
print(data.head())