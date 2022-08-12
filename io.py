'''
%s - String
%d - Integers
%f - Bilangan Desimal
%.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
%x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)
'''

# meminta input
user = input('masukan pass: ')
if (user == 'kuda ganteng'):
    print('u can access all th web')
else:
    print('ur access denied!')


# command line arg
''' INI SMUA DIJALANKAN DI CMD BUKAN LGSG DI TEXT EDITOR
$ python test.py arg1 arg2 arg3
import sys
print('Jumlah arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print(sys.argv[1])


Duck Typing
Python juga sering diafiliasikan dengan metode duck typing, yang merefleksikan pada frase: 
“if it walks like a duck and it quacks like a duck, then it must be a duck”
(Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek, maka kemungkinan besar ia adalah bebek). 
Duck typing adalah sebuah konsep, tipe atau kelas dari sebuah objek tidak lebih penting daripada metode yang menjadi perilakunya. 
'''
print('')
# method yg penting
print('ini iwan    '.rstrip()) # lstrip juga analog sama halnya dia ngilangin yg dikiri tapi
# kalo utk kanan kiri dia pake strip
# ngecek depan belakang mnghasilkan bool pake STARTSIWTH n ENDSWITH

# misah n gabungin string
print(' '.join(['Ridwan','Akmal']))
print(' 🚀 '.join(['mari naik','ke bulan']))
# kalo mau pisahin brdsrkan suatu delimiter trntu kita pake split
print('iwang**ganteng**bettt'.split('**'))


