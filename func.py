def hasil_kuadrat(x):
    return x*x

# panggil dah misal temisal misal
a = hasil_kuadrat(10)
print(f'nilai kuadrat dari 10 adalah: {a}')

print(' ')
print(' ')


# Pass by reference vs value
def ubah(listku):
    listku.append([1,2,3])
    print(f'nilai yg ada di fungsi {listku}')


# panggil fungsi pengubahnya
listku = [10,20,30]
ubah(listku)
print(f'Nilai di luar fungsi: {listku}')
