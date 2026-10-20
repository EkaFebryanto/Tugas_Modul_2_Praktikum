# diskon_biaya.py

def baca_float(pesan, minimum, maksimum):
    while True:
        try:
            nilai = float(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"  Nilai harus antara {minimum} dan {maksimum}.")
        except ValueError:
            print("  Input harus berupa angka.")


def baca_yn(pesan):
    while True:
        jawab = input(pesan).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Masukkan 'y' atau 'n'.")


def hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu):
    rincian = []
    total_persen = 0

    if anak_karyawan:
        rincian.append(("Anak karyawan", 25))
        total_persen += 25

    if ipk >= 3.8:
        rincian.append(("IPK >= 3.8", 20))
        total_persen += 20
    elif ipk >= 3.5:
        rincian.append(("IPK >= 3.5", 15))
        total_persen += 15
    elif ipk >= 3.0:
        rincian.append(("IPK >= 3.0", 10))
        total_persen += 10

    if tepat_waktu:
        rincian.append(("Bayar tepat waktu", 5))
        total_persen += 5

    potongan = spp * total_persen / 100
    biaya_final = spp - potongan
    return rincian, total_persen, potongan, biaya_final


def tampilkan_hasil(spp, rincian, total_persen, potongan, final):
    print("\n" + "=" * 45)
    print("RINCIAN DISKON BIAYA KULIAH".center(45))
    print("=" * 45)
    print(f"Biaya SPP awal : Rp {spp:,.0f}")
    print("-" * 45)
    if rincian:
        print("Diskon yang berlaku:")
        for nama, persen in rincian:
            print(f"  - {nama:<25}{persen:>3}%")
    else:
        print("Tidak ada diskon yang berlaku.")
    print("-" * 45)
    print(f"Total diskon   : {total_persen}%")
    print(f"Potongan biaya : Rp {potongan:,.0f}")
    print(f"BIAYA FINAL    : Rp {final:,.0f}")
    print("=" * 45)


def main():
    print("=== KALKULATOR DISKON BIAYA KULIAH ===")
    spp = baca_float("Biaya SPP (Rp)            : ", 1, 1_000_000_000)
    anak = baca_yn("Anak karyawan? (y/n)      : ")
    ipk = baca_float("IPK (0.0-4.0)            : ", 0.0, 4.0)
    waktu = baca_yn("Bayar tepat waktu? (y/n)  : ")
    hasil = hitung_diskon(spp, anak, ipk, waktu)
    tampilkan_hasil(spp, *hasil)


if __name__ == "__main__":
    main()