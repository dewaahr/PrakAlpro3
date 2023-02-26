#Input
bil_satu = int(input('Masukan Bilangan 1:'))
bil_dua = int(input('Masukan Bilangan 2:'))
bil_tiga = int(input('Masukan Bilangan 3:'))
bil_empat = int(input('Masukan Bilangan 4:'))
bil_lima = int(input('Masukan Bilangan 5:'))

#proses-output
if (bil_satu<bil_dua and bil_satu>bil_tiga and bil_satu>bil_empat and bil_satu>bil_lima)or (bil_satu<bil_tiga and bil_satu>bil_dua and bil_satu>bil_empat and bil_satu>bil_lima) or (bil_satu<bil_empat and bil_satu>bil_dua and bil_satu>bil_tiga and bil_satu>bil_lima) or (bil_satu<bil_lima and bil_satu>bil_dua and bil_satu>bil_tiga and bil_satu>bil_empat):
    print('Bilangan terbesar kedua :',bil_satu)
elif (bil_dua<bil_satu and bil_dua>bil_tiga and bil_dua>bil_empat and bil_dua>bil_lima) or (bil_dua<bil_tiga and bil_dua>bil_satu and bil_dua>bil_empat and bil_dua>bil_lima) or (bil_dua<bil_empat and bil_dua>bil_satu and bil_dua>bil_tiga and bil_dua>bil_lima) or (bil_dua<bil_lima and bil_dua>bil_satu and bil_dua>bil_tiga and bil_dua>bil_empat):
    print('Bilangan terbesar kedua : ',bil_dua)
elif (bil_tiga<bil_satu and bil_tiga>bil_dua and bil_tiga>bil_empat and bil_tiga>bil_lima) or (bil_tiga<bil_dua and bil_tiga>bil_satu and bil_tiga>bil_empat and bil_tiga>bil_lima) or (bil_tiga<bil_empat and bil_tiga>bil_satu and bil_tiga>bil_dua and bil_tiga>bil_lima) or (bil_tiga<bil_lima and bil_tiga>bil_empat and bil_tiga>bil_dua and bil_tiga>bil_satu):
     print('Bilangan terbesar kedua :',bil_tiga)
elif (bil_empat<bil_satu and bil_empat>bil_dua and bil_empat>bil_tiga and bil_empat>bil_lima) or (bil_empat<bil_dua and bil_empat>bil_satu and bil_empat>bil_tiga and bil_empat>bil_lima) or (bil_empat<bil_tiga and bil_empat>bil_satu and bil_empat>bil_dua and bil_empat>bil_lima) or (bil_empat<bil_lima and bil_empat>bil_satu and bil_empat>bil_dua and bil_empat>bil_tiga):
     print('Bilangan terbesar kedua :',bil_empat)
else: 
     print('Bilangan terbesar kedua :',bil_lima)