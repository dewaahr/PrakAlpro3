bil_satu=input('Masukan Bilangan 1  : ')
bil_dua=input('Masukan Bilangan 2  : ')
bil_tiga=input('Masukan Bilangan 3  : ')

x=bil_satu[1]
y=bil_dua[1]
z=bil_tiga[1]
x=int(x)
y=int(y)
z=int(z)
bil_satu=int(bil_satu)
bil_dua=int(bil_dua)
bil_tiga=int(bil_tiga)

if x >= 5:
    bil_satu=bil_satu-x+10
else: bil_satu=bil_satu-x

if y >= 5:
    bil_dua=bil_dua-y+10
else: bil_dua=bil_dua-y

if z >= 5:
    bil_tiga=bil_tiga-z+10
else: bil_tiga=bil_tiga-z
print(bil_satu,bil_dua,bil_tiga)
print(f'Jumlah dari tiga bilangan setelah dibulatkan adalah :{bil_satu+bil_dua+bil_tiga}')