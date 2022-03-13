import numpy as np

      #=========================#
      ###==== Catatan 1 ====###
      # install numpy package
      #=========================#

'''
like the way to install peewee lib, install numpy in pip using
terminal with command
> pip install numpy,
and how to uninstall it using command
> pip uninstall numpy.
'''

      #=========================#
      ###==== Catatan 2 ====###
      # array func in numpy
      #=========================#

# array like list but more eficient
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = list(np_weight / np_height ** 2)
for x in bmi:
    if x > 23:
        print(round(x, 2))

# access method array in array
nama = [['Ani', 'Budi', 'Cika'],
        ['Andi', 'Bina', 'Cita']]
nama1 = np.array(nama)
print (nama1[1,0])