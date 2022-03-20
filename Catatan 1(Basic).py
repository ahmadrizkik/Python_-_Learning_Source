
      #=========================#
      ###==== Catatan 1 ====###
      # introduction
      #=========================#

# print 'Hello World!'
print ('Hello World')


      #=========================#
      ###==== Catatan 2 ====###
      # format print
      #=========================#

nama = 'Malika' # string
umur = 17       # integer
nama, umur, tempat = 'Malika', '17', 'Jakarta'

# casting ke str
print (nama + "\n" + str(umur))

###==============
###==== metode %

''' string format
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a 
fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
  Any object which is not a string can be formatted using the %s operator
  as well. The string which returns is formatted as the string.
'''
# contoh 1
print ('%s umurnya %s' %(nama, umur))

# contoh 2
data = 1
print ('%s' % data)

# contoh 3
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

###==============
###==== metode {}.format()
# contoh 1
print ('{1} umurnya {0}'.format(nama, umur))

# contoh 2
planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390.9
# print 'Pluto weighs about 1.3e+22 kilograms (0.22% of Earth's mass).
#        It is home to 52,910,390.9 Plutonians.'
print ("""{} weighs about {:.2} kilograms ({:.2%} of Earth's mass).
      It is home to {:,} Plutonians.""".
      format(planet, pluto_mass, pluto_mass/earth_mass, population))

''' string method
.abs()
.endswith()
.index()
.isdigit()
.join()
.lower()
.replace
.split()
.startswith()
.upper()
'''

# slicing variable
data = "Hello world!"
print(data[2])      # l
print(data[-2])     # d
print(data[2:8])    # llo wo
print(data[:8])     # Hello wo
print(data[:-2])    # Hello worl
print(data[-2:])    # d!
print(data[1:10:3]) # eoo 
print(data[0:12:4]) # [0:12:4] same as [::4])
print(data[::-1])   # !dlrow olleH

# split method
claim1 = 'Pluto is a planet!'
x = claim1.split()
print (x) # print ['Pluto', 'is', 'a', 'planet!']

claim1 = 'Pluto-is-a-planet!'
a,b,c,d = claim1.split('-')
print (a) # print 'Pluto'

# join method
claim2 = ['Pluto', 'is', 'a', 'planet!']
y = ' 👏 '.join([word for word in claim2])
print (y) # print 'Pluto 👏 is 👏 a 👏 planet!'

# replace method
claim3 = 'Pluto is a planet!'
claim3Underscore = claim1.replace(' ', '_')
print (claim3Underscore) # print 'Pluto_is_a_planet!'

# isdigit method
x = '12345678x'
print (str.isdigit(x)) # print False

# quote type
print("Pluto's a planet!")       # print with one quote
print('My dog is named "Pluto"') # print with two quote


      #=========================#
      ###==== Catatan 3 ====###
      # fungsi input
      #=========================#

# input 1
nama = input("Siapa nama kamu? ")
umur = input("Berapa umur kamu? ")
print ("Salam kenal ya " + nama + " diumur kamu yang ke " + umur)

# input 2
baik = True
imut = True
tipe = 'wanita'
# if can make into branch
if baik and imut:
  if tipe == input(''):
    print ("Gas")
  else:
    print ('engga dlu')


      #=========================#
      ###==== Catatan 4 ====###
      # variabel type and if
      #=========================#

# vartype
# integer(int), float(float), string(str), boolean(bool), complex(complex)

print ("a: eh bayar utanglu sini.")
print ("b: ywdh nih gw bayar.")
print ("a: lu punya uang berapa?")

uang = input("b: ")
utang = 10000

# elif bisa ditulis lebih dari sekali
if int(uang) == utang:
  print ("a: oke lunas ya")
elif int(uang) < 5000:
  print ("a: yaampun miskin banget")
elif int(uang) < utang:
  print ("a: duitnya kurang bang")
else:
  print ("a: anjay tumben lu lebihin bayar utang")


      #=========================#
      ###==== Catatan 5 ====###
      # boolean
      #=========================#

# boolean operator
# ==, !=, >, <, >=, <=
# and = & (kalau keduanya true)
# or = | (kalau salah satunya true)
# not = != (buat bikin pernyataan jadi sebaliknya)
x = 10
y = 5
z = -3
if x > y and y < x:
  print ('keduanya benar')

if x > y or x < y:
  print ('salah satunya salah')

if not x < y:
  print ('iya itu tidak benar')


      #=========================#
      ###==== Catatan 6 ====###
      # fungsi while
      #=========================#

# while gunanya untuk bikin pengulangan
x = 1
while x < 5:
  print ("lanjut.")
  x = x + 1
else:
  print ('berhenti di' , x)

# fungsi break untuk berhenti saat mencapai nilai tertentu
x = 0
while True:
    print(x)
    x = x + 1
    if x >= 5:
        break
    
# make a Pyramid
a = 1
while a <= 5:
  b = 0
  while b < a:
    print ('*', end="") # end biar next print nyatu
    b = b + 1
    # diperlukan var baru karena jika memakai var sebelumnya
    # akan mengubah nilainya ketika diloop pertama
    # dari seharusnya 1=2=3=4 jika menggunakan 1 var akan
    # menjadi 1=2=1=2=1
  print ()
  a = a + 1
# atau
x = 1
bintang = ""
while x <= 5: 
  y = x
  while y > 0:
    bintang = bintang + "*" # dapat ditulis bintang += "*"
    y = y - 1
  bintang = bintang + "\n"
  x = x + 1 
print (bintang)


      #=========================#
      ###==== Catatan 7 ====###
      # fungsi for and tuple
      #=========================#

# fungsi for
for a in range(1,5):
  for b in range (1,5):
    c = a*b
    print (c, end=" ")
  print ()

# for x in var gunanya buat loop isi dari variabel atau list
nama = ['Ani', 'Budi', 'Cika']
nama1 = 'Budi'
for x in nama:
  print ('ini namaya ', nama)
for x in nama1:
  print (nama)

# fungsi continue to skip command
for x in range(10):
    if x % 2 == 0:
        continue
    print(x) # 1,3,5,7,9

# for loop dari modul built in
import re
for x in dir(re):
    if 'find' in x:
        print (x)

# exaFor 1 (print only uppercase letter in string)
s = 'steganograpHy is the practicE of conceaLing a fiLe Or video.'
for char in s:
    if char.isupper():      # use isupper
        print(char, end='') # HELLO

###==============
###==== Tuple

# tuple () mirip list bedanya dia immutable (gabisa pake method)
nama1 = ('Ale', 'Bidi', 'Coki')
nama2 = ['Ale', 'Bidi', 'Coki']

print (nama1[0])
print (len(nama1))  # jumlah data
print (max(nama1))  # tertinggi
print (list(nama1)) # ganti ke list
print (tuple(nama2))


      #=========================#
      ###==== Catatan 8 ====###
      # fungsi list
      #=========================#

# list tandanya pake []
nama = ['Ani', 'Budi', 'Cika']
nama1 = 'Budi'
angka = [1,2,3]

# cara akses list
x, y, z = nama
print (x, y, z, sep='_') # sep to change space between values
print (nama[0])

# method in list
nama.append ('Diki')  # nambahin
nama[0] = 'Akel'      # ganti
del nama[1]           # hapus metode 1
nama.pop(1)           # hapus metode 2
nama.index('Budi')    # akses index
len(nama)             # jumlah data di  list
sorted(nama)          # urutin list
sum(angka)            # total list
print (nama)
print (nama[0])

# list in list
nama = [['Ani', 'Budi', 'Cika'],
        ['Andi', 'Bina', 'Cita']]
x = nama[1][0]  # acces method
print (x)       # andi

###==============
###==== comprehension list

# exaCompreList 1 (print length word except 'the')
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
# basic code
word_lengths = []
for word in words:
  if word != "the":
    word_lengths.append (len(word))
# comprehen with just one code
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)

# exaCompreList 2
data1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
integer = [int(x) for x in data1 if x > 0]
print(integer)

# exaCompreList 3
squares = [n**2 for n in range(10)]
print (squares)

# exaCompreList 4
planets = ['Mercurius', 'Venus', 'Earth', 'Mars', 'Jupiter',
           'Saturnus', 'Uranus', 'Neptunus']
short_planets = [planet for planet in planets if len(planet) < 6]
print (short_planets)

# exaCompreList 5(count negative number in list)
nums = [5, -1, -2, 0, 3]
n_negative = 0
for num in nums:
    if num < 0:
        n_negative = n_negative + 1
print (n_negative)
  # can be comprehen into this
print (len([num for num in nums if num < 0]))
  # or into this
print (sum([num < 0 for num in nums]))

# exaCompreList 6 (check lucky number in list (luckNumb = 7))
nums = [1,2,3,4,5,6,7]
for num in nums:
    if num % 7 == 0:
        print (True)
    else:
        continue
  # comprehen into this
print (any([num % 7 == 0 for num in nums]))


      #=========================#
      ###=== Catatan 9 ===####
      # fungsi dictionary
      #=========================#

# dictionary pake {}, punya key dan value
data = {'nama'  : 'Aben',
        'umur'  : '17',
        'hobi'  : 'Masak',
        'gender': 'Wanita'}
print (data)

# method di dict
data['kelamin'] = 'Laki-laki' # nambahin
data['nama'] = 'Budi'         # ganti
del data['umur']              # cara delete 1
data.pop('gender')            # cara delete 2
print (data)

# loop dict
# 'for' buat dic bisa pake items() atau pake 
# satu data tpi data selanjutnya dikasih []
for x, y in data.items():
  print (x, ":", y)
  # atau ini
for x in data:
  print (x, ":", data[x])

# loop dua dict
data = {
  'data1' : {
    'nama' : 'Kai',
    'umur' : '19',
    'hobi' : 'Mancing'},
  'data2' : {
    'nama' : 'Lex',
    'umur' : '20',
    'hobi' : 'Nganggur'}}

for x, y in data.items():
  print ('\n' + 'ini ' + x)
  for x1 in y:
    print (x1 + ' : ' + y[x1])
# bisa juga pake code ini
for x, y in data.items():
  print ('\n', 'ini ', x)
  for x1, y1 in y.items():
    print (x1, ' : ', y1)

###==============
###==== comprehension dict
# contoh 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
x = {}
for planet1 in planets:
    x[planet1] = planet1[0]
print (x)
  # can comprehen into this
y = {planet: planet[0] for planet in planets}
print (y)
print (' '.join(sorted(x.values()))) # print values


      #=========================#
      ###=== Catatan 10 ===####
      # fungsi set
      #=========================#

# set mirip dict pake {} tpi gada keysnya
# set gabisa diakses pake key, atau index (misal nama[0])
# set sifatnya acak, nonduplikat
nama = {'Andi', 'Bagus', 'Cinta', 'Andi'}
print (nama) # hasil print acak dan nama andi cuma 1 kali

nama.add ('Dara')     # nambahin
nama.remove ('Bagus') # hapus
print (nama)

# sets bisa dipakai buat perhitungan 
# pakai tanda (|) (&) (-) (^)
angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}

print (angka1 ^ angka2)


      #=========================#
      ###=== Catatan 11 ===####
      # make own function
      #=========================#

###==============
###==== function bisa tanpa argumen
# contoh 1
def nilai():
  print ()
  print ('Benar')
nilai()
# contoh 2
def commaValue():
    value = 123456.789
    return '{:,}'.format(value) # to give comma in result
print (commaValue())            # 123,456.789

###==============
###==== function dengan argumen
# contoh 1
def nilai(text):
  print (text)
  print ('Iya benar')
nilai("Apakah ini benar?")

# contoh 2
def nilai(text):
    return text + 2 # return untuk mengambil nilai fungsi
                    # akan none jika tidak ada return/print
y = nilai(3)
print (y)

# contoh 3
def menu_is_boring(meals):
    '''
    this funct is to check if there's a same meal
    in a row
    '''
    # range is to iterate list so it can be compare for below code
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
x = menu_is_boring(['x','y','z','x','y','y','x'])
print (x)

# contoh 4
def is_valid_zip(zip_code):
    """
    Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) == 5:
        return str.isdigit(zip_code)
    else:
        return False
  # can comprehen into
def is_valid_zip2(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()
print (is_valid_zip('12345')) # must true
print (is_valid_zip('1234x')) # must false
print (is_valid_zip('1234')) # must false

###==============
###==== function default
def nilai (text = 0):
  print (text)
nilai() #keluar 0

###==============
###==== function >1 argumen
# contoh 1
def nilai (a, b, c):
  print ('Kalau', a, 'ditambah', b, 'jadinya', c)
nilai (2, 3, 5)

# contoh 2
def x(nama, umur, hobi):
    print ('Nama: ' + nama + 
           'Umur: ' + umur +
           "Hobi: " + hobi
          )
x('17\n', 'isan\n', 'masak')
  # di print berurut dari nama
x(umur = '17\n', nama = 'isan\n', hobi = 'masak')

# contoh 3
def data(x, y):
    '''
    This func is to print a compare list into boolean list 
    '''
    data = []
    for z in x:
        data.append(z > y)
    return data
x = data([1, 2, 3, 4], 2) # element compare
print (x) # will print = [False, False, True, True]

# contoh 4
list1 = ['Becak adalah kendaraan.', 'Sepeda adalah kendaraan.',
        'Banyak jenis kendaraan di dunia.']
key   = ['adalah', 'kendaraan']
def wordSearch(doc, keyword):
    '''
    this funct is to search one keyword in list
    '''
    count = []
    for i, j in enumerate(doc):
        tokens = j.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            count.append(i)
    return count
print (wordSearch(list1, 'kendaraan'))
def multiWordSearch(doc, keyword):
    '''
    this funct is to search more than one keyword in list
    '''
    count = {}
    for keywords in keyword:
        count[keywords] = wordSearch(doc, keyword)
    return count
print (multiWordSearch(list1, key[0]))

###==============
###==== higher-order function (fungsi didalam fungsi)
def mult_by_five(x):
    return 5 * x
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n')

# didalam fungsi dapat langsung mengakses fungsi
# dibawahnya (lihat program konversi suhu)


      #=========================#
      ###=== Catatan 12 ===####
      # fungsi lambda
      #=========================#

# lambda same like func
def add(x,y):
  return x + y
x = add(1,2)
print (x)
# if using lambda
add1 = lambda x,y : x + y
y = add1(1,2)
print (y)

# another lambda
l = [2,4,7,3,14,19]
for i in l:
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))


      #=========================#
      ###=== Catatan 13 ===####
      # args (*) dan kwargs (**)
      #=========================#

# buat fungsi jika output lebih dari parameter
# Args bisa buat list
def nama(*text):
  print (text)

nama('adel', 'beni', 'caca', 'diki')

# Kwargs bisa buat dict
def bio(**text):
  for x in text:
    print (x, ' : ', text[x])

bio(nama = 'adel', umur = '17', hobi = 'belajar')


      #=========================#
      ###=== Catatan 14 ===####
      # import module
      #=========================#

# import module dari file (import nama_module as n_m)
# atau spesifik fungsi (from nama_module import fungsi_module)
# nama_module.fungsi_module / fungsi_module buat di penamaan

# import dari build in module datetime
import datetime

now = datetime.datetime.now()
date = datetime.datetime(2001, 2, 16)

print (now)
print (date)
print (now.strftime('%d %B %Y')) # format tanggal

# cek func di module
x = dir(datetime)
print (x)


      #=========================#
      ###=== Catatan 15 ===####
      # global and local var
      #=========================#

nama = 'andi'
def x():
    global nama               # lokal berubah global
    nama = nama + ' dan beni' # var global bisa diedit
    print (nama)

#hasil print akan sama
x()
print (nama)


      #=========================#
      ###=== Catatan 16 ===####
      # error method
      #=========================#

# metode raise exception
raise Exception('Ada kesalahan dibawah')
print (alpha) # ini gak keprint

# metode try
try:
    print (alpha) # ini gak keprint
except:
    print ('ada eror di bagian ini')

# cara assert 
alpha = ['ayam', 'babi', 'cicak']
def is_it_var():
    assert('domba' in alpha),'tidak di variabel' # pake assert buat eror
is_it_var()
print ('Hello') # ini gak keprint


      #=========================#
      ###=== Catatan 17 ===####
      # compile
      #=========================#
'''
compile py ketik di terminal python (-m py_compile (nama modul))
run di terminal (.\__pycache__\(nama modul))
'''

      #=========================#
      ####==== Shortcut ====#####
      #=========================#
'''
Alt  + arrow : move linecode up and down
Ctrl + /     : insert comment
Ctrl + d     : multiple selection

Alt  + shift + arrow : copy linecode
Ctrl + Alt   + arrow : multiple selection
Ctrl + shift + k     : delete line code
Ctrl + shift + a     : python run file
'''