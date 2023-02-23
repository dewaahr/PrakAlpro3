jarak_nilai=int(input('Masukan Jarak Antar Nilai:'))
batas_nilai=int(input('Masukan Batas nilai tertinggi:'))
nilai_nilai=int(input('Masukan Nilai Anda:'))

nilai_a=batas_nilai
nilai_a2=nilai_a-jarak_nilai
nilai_b=nilai_a2-jarak_nilai
nilai_b2=nilai_b-jarak_nilai
nilai_b3=nilai_b2-jarak_nilai
nilai_c=nilai_b3-jarak_nilai
nilai_c2=nilai_c-jarak_nilai
nilai_d=nilai_c2-jarak_nilai
nilai_e=nilai_d-jarak_nilai

print(nilai_a,nilai_b,nilai_a2,batas_nilai)

if nilai_nilai>=nilai_a:
    print('Nilai Anda Adalah : A')
elif nilai_nilai>=nilai_a2:
    print('Nilai Anda Adalah : A-')
elif nilai_nilai>=nilai_b:
    print('Nilai Anda Adalah : B+')
elif nilai_nilai>=nilai_b2:
    print('Nilai Anda Adalah : B')
elif nilai_nilai>=nilai_b3:
    print('Nilai Anda Adalah : B-')
elif nilai_nilai>=nilai_c:
    print('Nilai Anda Adalah : C+')
elif nilai_nilai>=nilai_c2:
    print('Nilai Anda Adalah : C')
elif nilai_nilai>=nilai_d:
    print('Nilai Anda Adalah : D')
else:
    print('Nilai Anda Adalah : E')
