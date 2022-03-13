
import pandas as pd

      #=========================#
      ###=== Catatan 1 ===####
      # Install Pandas Package
      #=========================#
'''
like the way to install peewee lib, install pandas in pip using
terminal with command
> pip install pandas,
and how to uninstall it using command
> pip uninstall pandas.
'''

      #=========================#
      ###==== Catatan 2 ====####
      # DataFrame
      #=========================#

dict1 = {"country"  : ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital"   : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area"      : [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }

# convert into pandas dataframe
brics = pd.DataFrame(dict1)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# count column
count_column = brics.shape[1]  # have to use 1
print(count_column)

# count row
count_row = brics.shape[0]     # have to use 0
print(count_row)

      #=========================#
      ###==== Catatan 2 ====####
      # CSV File
      #=========================#

x = pd.read_csv('test3.csv', header=0, sep=',')
y = pd.DataFrame(x)
print (y[0:6])

# clean data from null values and non numeric
x.dropna(axis=0, inplace=True)   # use .dropna()