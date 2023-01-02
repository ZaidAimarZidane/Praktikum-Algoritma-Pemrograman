total = 0
barang = []
harga = []

while True:
    print("""Daftar Barang\n
    1. kopi\t 3000
    2. Es jeruk\t 7000
    3. pop es\t 8000
    4. mie goreng\t 11000
    5. nasi goreng\t 15000
    """)
    
    kode = int(input("Masukan kode barang : "))
    if kode == 1:
        barang.append('Kopi')
        harga.append(3000)
        total += 3000
    elif kode == 2:
        barang.append('Es jeruk')
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append('pop es')
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append('mie goreng')
        harga.append(11000)
        total += 11000
    elif kode == 5:
        barang.append('nasi goreng')
        harga.append(15000)
        total += 15000
    else:
        print('kode tidak valid')
    
    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't':
        print("")
        break
    
print('Barang yang dibeli : ', barang)
print('harga barang :', harga)
print('total yang harus dibayar :',total,'\n')

uang = int( input('Masukan uang pembayaran : ') )
if uang > total:
    print('Kembalian :',uang - total)
elif uang == total:
    print('Uang anda cukup')
else : 
    print ('Mohon maaf duit ade kurang : ', uang - total)
