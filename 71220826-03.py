player_satu=int(input('Masukan Nilai Pemain 1:'))
player_dua=int(input('Masukan Nilai Pemain 2:'))
player_tiga=int(input('Masukan Nilai Pemain 3:'))
if player_satu==player_dua or player_satu==player_tiga or player_tiga==player_dua:
    print("Tidak ada Pemain yang Menang")
elif player_satu==21:
    print("Pemenangnya adalah Pemain 1")
elif player_dua==21:
    print("Pemenangnya adalah Pemain 2")
elif player_tiga==21:
    print("Pemenangnya adalah Pemain 3")
elif player_satu > 21 and player_dua>21 and player_tiga>21:
    print("Tidak ada Pemain yang Menang")
elif player_satu <= 21 and abs (21 - player_satu) < abs (21 - player_dua) and abs(21 - player_satu) < abs(21 - player_tiga):
    print("Pemenangnya adalah Pemain 1")
elif player_dua <= 21 and abs (21 - player_dua) < abs (21 - player_satu) and abs(21 - player_dua) < abs(21 - player_tiga):
    print("Pemenangnya adalah Pemain 2")
elif player_tiga <= 21 and abs (21 - player_tiga) < abs (21 - player_tiga) and abs(21 - player_tiga) < abs(21 - player_dua):
    print("Pemenangnya adalah Pemain 3") 