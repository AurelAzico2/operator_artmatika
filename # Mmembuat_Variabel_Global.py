# Membuat variabel global
nama = "Belajar Kode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.0"
    # mengakses variabel lokal
    print ("Nama: $s" % nama)
    print("Versi: $s" % versi)

#Mengakses variabel global
print ("Nama: $s" % nama)
print ("Versi: $s" % versi)

# Memanggil fungsi help()
help()
