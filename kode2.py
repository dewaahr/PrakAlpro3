#input
input_1 = input('Masukan Bilangan 2 digit:')
input_2 = input('Masukan Bilangan 2 digit:')

#proses-output
puluhan_1 = input_1[0]
satuan_1 = input_1[1]
puluhan_2 =input_2[0]
satuan_2 = input_2[1]

if (puluhan_1==puluhan_2 or puluhan_1==satuan_2) or (satuan_1==puluhan_2 or satuan_1 == satuan_2):
    print("Ada angka yang sama")
elif (puluhan_1!=puluhan_2 and puluhan_1!=satuan_2) or (satuan_1!=puluhan_2 and satuan_1 != satuan_2):
    print("Tidak ada angka yang sama")