# status_mahasiswa.py

def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    elif ipk < 2.0:
        return "Peringatan"
    elif sks >= 18:
        return "Aktif"
    else:
        return "Peringatan"  # IPK >= 2.0 tapi SKS < 18


def baca_float(pesan, minimum, maksimum):
    while True:
        try:
            nilai = float(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"  Nilai harus antara {minimum} dan {maksimum}.")
        except ValueError:
            print("  Input harus berupa angka.")


def baca_int(pesan, minimum, maksimum):
    while True:
        try:
            nilai = int(input(pesan))
            if minimum <= nilai <= maksimum:
                return nilai
            print(f"  Nilai harus antara {minimum} dan {maksimum}.")
        except ValueError:
            print("  Input harus berupa bilangan bulat.")


def baca_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        print("  Input tidak boleh kosong.")


def main():
    jumlah = 5
    daftar = []
    print("=== INPUT DATA 5 MAHASISWA ===")
    for i in range(1, jumlah + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = baca_teks("  NIM  : ")
        nama = baca_teks("  Nama : ")
        ipk = baca_float("  IPK (0.0-4.0) : ", 0.0, 4.0)
        sks = baca_int("  SKS (0-24)    : ", 0, 24)
        daftar.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks,
                       "status": tentukan_status(ipk, sks)})

    print("\n" + "=" * 68)
    print("LAPORAN STATUS MAHASISWA".center(68))
    print("=" * 68)
    print(f"{'No':<4}{'NIM':<14}{'Nama':<20}{'IPK':<6}{'SKS':<6}{'Status':<12}")
    print("-" * 68)
    for no, m in enumerate(daftar, 1):
        print(f"{no:<4}{m['nim']:<14}{m['nama']:<20}{m['ipk']:<6.2f}{m['sks']:<6}{m['status']:<12}")
    print("=" * 68)


if __name__ == "__main__":
    main()