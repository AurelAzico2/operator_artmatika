# Membuat Fungsi
def salam():
    print ("Hello, Selamat Pagi")

# Pemanggilan Fungsi
salam()
salam()
salam()

#Pakai Parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi)
    print("Luas segitiga: %f" % luas)
luas_segitiga(4, 6)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
print ("Luas persegi: %d" % luas_persegi(6))

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

sisi = 3
print("luas persegi:", luas_persegi(sisi))
print("volume persegi:", volume_persegi(sisi))
