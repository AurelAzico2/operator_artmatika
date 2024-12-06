listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Yogyakarta', 'Semarang', 'Makassar'
]
kotaYangDicari = input('Masukan nama kota yang anda cari :')
i = 0
while i < len(listKota):
    if listKota[i].lower() == kotaYangDicari.lower():
        print('Ketemu di index, i')
        break
    print('Bukan', listKota[i])
    i += 1
else:
    print('Maaf, kota yang anda cari tidak ditemukan')