def cetak_pola(baris):
    for i in range(1, baris + 1):
        print('*' * i)
def main():
    try:
        jumlah_baris = int(input("Masukkan jumlah baris pola bintang segitiga yang diinginkan: "))
        if jumlah_baris < 1:
            print("Jumlah baris harus lebih dari 0.")
            return
        cetak_pola(jumlah_baris)
    except ValueError:
        print("Silakan masukkan angka yang valid.")

if __name__ == "__main__":
    main()