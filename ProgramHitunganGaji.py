def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    jam_normal = 8
    total_gaji = 0   
    for i in range(hari_kerja):
        jam_kerja_hari = float(input(f"Masukan jam kerja untuk hari ke-{i + 1}: "))
        if jam_kerja_hari > jam_normal:
            lembur = jam_kerja_hari - jam_normal
            gaji_hari = (jam_normal * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            gaji_hari = jam_kerja_hari * tarif_per_jam
        total_gaji += gaji_hari
    return total_gaji
def main():
    try:
        tarif_per_jam = float(input("Masukan tarif gaji per jam: "))
        hari_kerja = int(input("Masukan jumlah hari kerja dalam sebulan: "))
        total_gaji = hitung_gaji(tarif_per_jam, 8, hari_kerja)
        print(f"\nTotal gaji bulanan: Rp {total_gaji:.2f}")
    except ValueError:
        print("Silakan masukan angka yang valid.")
if __name__ == "__main__":
    main()