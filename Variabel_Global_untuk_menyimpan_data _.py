# Variabel Global untuk menyimpan data buku
buku = []
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print (f"[{indeks}] {buku[indeks]}")

# Fungsi untuk menambakan data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

#Fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indexs > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indexs > len(buku):
        print("ID salah")
    else:
       buku.remove(buku[indeks])

#Fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("---------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

if input("menu") == 1:
    show_data()
elif int(menu) == 2:
    insert_data()
elif int(menu) == 3:
    edit_data()
elif int(menu) == 4:
    delete_data()
elif int(menu) == 5:
    exit()
else:
    print("Salah pilih!")

if __name__ == "__main__":
    while True:
        show_menu()