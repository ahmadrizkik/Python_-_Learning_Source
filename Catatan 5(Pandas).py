# Catatan 1
# Install Pandas Package

'''
like the way to install peewee lib, install pandas in pip using
terminal with command
> pip install pandas,
and how to uninstall it using command
> pip uninstall pandas.
'''

# Catatan 2 
# Dataframe

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict) # dataframe print table in terminal
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)