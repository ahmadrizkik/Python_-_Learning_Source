import pandas as pd
import numpy as np

dict = {'col1': [1, 2, 3, 4, 7],
     'col2': [4, 5, 6, 9, 5],
     'col3': [7, 8, 12, 1, 11]}

# convert into pandas dataframe
df = pd.DataFrame(data=dict)

# count column
count_column = df.shape[1]  # have to use 1
print(count_column)

# count row
count_row = df.shape[0]     # have to use 0
print(count_row)

# min method
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_min)

# max method
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_max)

# mean (average) method
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage)
