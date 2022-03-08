# Kalkulator Konversi Suhu

def start():
    Scale = (input('\n===== Kalkulator Suhu =====\n' + 
        'Masukan Skala yang ingin digunakan\n' + 
        '1. Celcius\n' +
        '2. Reamur\n' +
        '3. Fahrenheit\n'+
        '4. Kelvin\n'))
    if Scale == '1':
        sCelcius = (float(input('\nMasukkan Angka Suhu\n')))
        cReamur = round((4/5)*sCelcius, 2)
        cFahrenheit = round(((9/5)*sCelcius)+32, 2)
        cKelvin = round(sCelcius+273, 2)
        print ('\n===== Hasil =====\n'+
            'Suhu saat ini   : '+str(sCelcius)+' Celcius.\n'+ 
            'Dalam Reamur    : '+str(cReamur)+' Reamur.\n'+
            'Dalam Fahrenheit: '+str(cFahrenheit)+' Fahrenheit.\n'+ 
            'Dalam Kelvin    : '+str(cKelvin)+' Kelvin.\n')
        back()
    if Scale == '2':
        sReamur = (float(input('\nMasukkan Angka Suhu\n')))
        cCelcius = round((5/4)*sReamur, 2)
        cFahrenheit = round(((9/4)*sReamur)+32, 2)
        cKelvin = round((5/4)*sReamur+273, 2)
        print ('\n===== Hasil =====\n'
            'Suhu saat ini   : '+str(sReamur)+' Reamur.\n'+ 
            'Dalam Celcius   : '+str(cCelcius)+' Celcius.\n'+
            'Dalam Fahrenheit: '+str(cFahrenheit)+' Fahrenheit.\n'+ 
            'Dalam Kelvin    : '+str(cKelvin)+' Kelvin.\n')
        back()
    if Scale == '3':
        sFahrenheit = (float(input('\nMasukkan Angka Suhu\n')))
        cCelcius = round((5/9*(sFahrenheit-32)), 2)
        cReamur = round((4/9*(sFahrenheit-32)), 2)
        cKelvin = round((5/9*(sFahrenheit-32))+273, 2)
        print ('\n===== Hasil =====\n'
            'Suhu saat ini   : '+str(sFahrenheit)+' Fahrenheit.\n'+ 
            'Dalam Celcius   : '+str(cCelcius)+' Celcius.\n'+
            'Dalam Reamur    : '+str(cReamur)+' Reamur.\n'+ 
            'Dalam Kelvin    : '+str(cKelvin)+' Kelvin.\n')
        back()
    if Scale == '4':
        sKelvin = (float(input('\nMasukkan Angka Suhu\n')))
        cCelcius = round(sKelvin-273, 2)
        cReamur = round((4/5*(sKelvin-273)), 2)
        cFahrenheit = round((9/5*(sKelvin-273))+32, 2)
        print ('\n===== Hasil =====\n'
            'Suhu saat ini   : '+str(sKelvin)+' Kelvin.\n'+ 
            'Dalam Celcius   : '+str(cCelcius)+' Celcius.\n'+
            'Dalam Reamur    : '+str(cReamur)+' Reamur.\n'+ 
            'Dalam Fahrenheit: '+str(cFahrenheit)+' Fahrenheit.\n')
        back()
def back():
    after_back = input('==========\n1. Kembali\n2. Keluar\n')
    if after_back == '1':
        start()
    else:
        print('\n===== LOG OUT =====')

start()