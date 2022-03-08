# membuat list belanja di txt

text = open('test1.txt', 'a+')
def buy_list():
    choice = input(
        '\nApa yang mau dilakukan?\n' +
        '1. Menambah list\n' +
        '2. Melihat list\n' +
        '3. Keluar\n'
    )
    if choice == '1':
        add_to_list()
    elif choice == '2':
        read_list()
    else:
        stop_list()
def add_to_list():
    text.write ('\n' + input('\nMau Beli Apa?\n'))
    print('\nBerhasil Menambahkan.')
    buy_list()
def read_list():
    text.seek(0)
    print('\n' + text.read())
    buy_list()
def stop_list():
    print ('\nSelesai Membuat List.\n')
buy_list()