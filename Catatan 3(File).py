      #=========================#
      ####==== Catatan 1 ====####
      # txt
      #=========================#

# membuka file bisa dari folder yang sama
# atau memanggil absolute path
import os
# r buat ekstensi (\)
os.chdir(r'C:\Users\Rizky\Documents\My Data\File\Python')

text = open('test1.txt', 'w') # new write
text.write('Alucard Savage')
text = open('test1.txt', 'r') # read

data = text.read()
print (data)

# a+ menulis tanpa menghapus
text = open('test1.txt', 'a+') # write
text.write('\nAlucard Savage')
text.seek(0) # back to default

data = text.read()
print (data)


      #=========================#
      ####==== Catatan 2 ====####
      # csv
      #=========================#

import os
os.chdir(r'C:\Users\Rizky\Documents\My Data\File\Python')

import csv
rows = []

# lewat list
# cara biasa
csvfile = open('test1.csv', 'r')
csvreader = csv.reader(csvfile)
rows = list(csvreader)
for row in rows[:5]:
    print (row[0] + ' : ' + row[1])

# pake metode with
with open('test1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile) # pake list
    # bisa pake ini pengganti (rows = list(csvreader))
    # for row in csvreader:
    #     rows.append(row)
    rows = list(csvreader)
    print ('Total Baris: ', csvreader.line_num)
for row in rows[:5]:
    print (row[0] + ' : ' + row[1])

# lewat dict
with open('test1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile) # pake dict
    rows = list(csvreader)
    print ('Total Baris: ', csvreader.line_num)
for row in rows[1:5]:
    print (row['first_name'] + ' : ' + row['email'])

# mengedit file csv
rows = [{'nama': 'Alpha', 'skill' : 'Api',   'power' : 100},
        {'nama': 'Beta',  'skill' : 'Tanah', 'power' : 200},
        {'nama': 'Gamma', 'skill' : 'Udara', 'power' : 300}]

with open('test2.csv', 'a') as csvfile:
    fields = ['nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(rows)


      #=========================#
      ####==== Catatan 3 ====####
      # json
      #=========================#

import json

# data untuk isi file
data = {}
data['member'] = [
    {'name' : 'alpha', 'skill' : 'fly'},
    {'name' : 'beta', 'skill' : 'explode'},
    {'name' : 'gamma', 'skill' : 'cook'}]

# write file
with open('test2.txt', 'w') as file:
    json.dump(data, file) # metode write json

# read file
with open('test2.txt', 'r') as file1:
    data1 = json.load(file1) # metode read json
def text():
    for file in data1['member']:
        print ('namanya ' + file['name'] +
         ', punya skill ' + file['skill'])
text()


      #=========================#
      ####==== Catatan 4 ====####
      # jupyter notebook
      #=========================#

'''
first change directory location to open notebook
open jupyter notebook in terminal with command
py -m jupyterlab    = open jupyterlab
py -m notebook      = open jupyter notebook
'''