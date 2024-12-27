def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b
def main():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        if pilihan == '1':
            hasil = tambah(angka1, angka2)
            print(f"Hasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            print(f"Hasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            print(f"Hasil: {angka1} * {angka2} = {hasil}")
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
    except ValueError:
        print("Silakan masukkan angka yang valid.")

if __name__ == "__main__":
    main()