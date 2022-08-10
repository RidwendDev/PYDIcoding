# utk number ada 3 yaitu: int,float, dan complex lain2nya kaya str, bool dkk itu udah biasalah
a = 10 
x = 3.2
y = 1j
print(f'tipe data dari a adalah {type(a)}, tipe data dari x adalah {type(x)}, dan tipe data dari y adalah {type(y)}')

print('')
# list
wadah = [1,2,3,4,5,6]
# ngambil index ke 1 sampe ke 3
print(wadah[1:4]) #prinsipnya ingat inc:excl
# ngambil index dari awal smp sblum 5
print(wadah[:5])
# mbuat elemen dari index 2 dst
print(wadah[2:]) 
# buat list dg kebalikan(reverse)
print(wadah[::-1])
# itu kaidahnya adalah make step -1
print('')

# ngedit list jg gampang tinggal kita deklarasikan aja sama indexnya misal wadah[1] = 'hai'
# ngahpus di list gmn caranya? pake del kalo mau index
print(f'list awal :{wadah}')
del wadah[5] 
print(f'list stelah dihapus : {wadah}')
# melakukan slicing
xy = 'uiadoiajakuzyt'
xz = 'nfhgacintaidsao'
zz = 'caweqcmamakuiudapaid'
# mau ngambil ssuatu yg gud
print(xy[8:11]+' '+xz[5:10]+' '+zz[6:12])

print('')
# Berikutnya itu ada tuple() sifatnya imutable, terus set{} ini dia unique datanya
# DICTIONARY
kamusIndoJawa = {
                    'kidul' : 'utara',
                    'kulon' : 'selatan',
                    'ngetan' : 'timur',
                    'madyang' : 'makan' 
}

a = kamusIndoJawa.keys()
print(f'key dari dict tsb: {a}')
# ada juga method get yg fungsinya  memperoleh nilai dari setiap elemen yang terdapat di dalam dict
# kita cari elemenya
x = kamusIndoJawa.get('ngetan') 
print(x)