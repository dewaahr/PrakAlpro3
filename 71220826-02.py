dadu_satu=int(input('Masukan Dadu 1:'))
dadu_dua=int(input('Masukan Dadu 2:'))
dadu_tiga=int(input('Masukan Dadu 3:'))
dadu=[1,2,3,4,5,6]

if dadu_satu not in dadu or dadu_dua not in dadu or dadu_tiga not in dadu:
    print('Harap Masukan Nilai dadu yang benar 1-6')
elif dadu_satu+dadu_dua+dadu_tiga==18:
    print('Royal')
elif dadu_satu==dadu_dua==dadu_tiga:
    print('Triple')
elif dadu_satu==4 and dadu_dua==5 and dadu_tiga==6:
    print('Flush')
elif dadu_satu==dadu_dua or dadu_satu==dadu_tiga or dadu_dua==dadu_tiga:
    print('Doubel')
elif dadu_satu!=dadu_dua and dadu_satu!=dadu_tiga and dadu_tiga!=dadu_dua:
    print('Single')
