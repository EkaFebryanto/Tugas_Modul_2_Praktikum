# menu_si_mahasiswa.py

# ---------- DATA & UTILITAS ----------
INVENTARIS = [
    {"kode": "B001", "nama": "Kertas A4 (rim)",    "stok": 120, "minimum": 30, "harga": 55000},
    {"kode": "B002", "nama": "Tinta Printer",      "stok": 25,  "minimum": 20, "harga": 90000},
    {"kode": "B003", "nama": "Spidol Whiteboard",  "stok": 8,   "minimum": 20, "harga": 12000},
    {"kode": "B004", "nama": "Stapler",            "stok": 0,   "minimum": 10, "harga": 35000},
    {"kode": "B005", "nama": "Map Folder",         "stok": 200, "minimum": 50, "harga": 3000},
    {"kode": "B006", "nama": "Kabel HDMI",         "stok": 4,   "minimum": 10, "harga": 45000},
    {"kode": "B007", "nama": "Flashdisk 32GB",     "stok": 18,  "minimum": 15, "harga": 70000},
    {"kode": "B008", "nama": "Baterai AA (pak)",   "stok": 0,   "minimum": 12, "harga": 25000},
]
PRIORITAS = {"HABIS": 1, "RENDAH": 2, "PERINGATAN": 3, "AMAN": 4}
LABEL_PRIORITAS = {1: "KRITIS", 2: "TINGGI", 3: "SEDANG", 4: "NORMAL"}


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


def baca_yn(pesan):
    while True:
        jawab = input(pesan).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Masukkan 'y' atau 'n'.")


# ---------- 1. STATUS MAHASISWA ----------
def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    elif ipk < 2.0:
        return "Peringatan"
    elif sks >= 18:
        return "Aktif"
    return "Peringatan"


def menu_status_mahasiswa():
    print("\n=== CEK STATUS MAHASISWA ===")
    jumlah = baca_int("Jumlah mahasiswa yang akan dicek (1-50): ", 1, 50)
    daftar = []
    for i in range(1, jumlah + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = baca_teks("  NIM  : ")
        nama = baca_teks("  Nama : ")
        ipk = baca_float("  IPK (0.0-4.0) : ", 0.0, 4.0)
        sks = baca_int("  SKS (0-24)    : ", 0, 24)
        daftar.append((nim, nama, ipk, sks, tentukan_status(ipk, sks)))

    print("\n" + "=" * 68)
    print(f"{'No':<4}{'NIM':<14}{'Nama':<20}{'IPK':<6}{'SKS':<6}{'Status':<12}")
    print("-" * 68)
    for no, (nim, nama, ipk, sks, st) in enumerate(daftar, 1):
        print(f"{no:<4}{nim:<14}{nama:<20}{ipk:<6.2f}{sks:<6}{st:<12}")
    print("=" * 68)


# ---------- 2. DISKON BIAYA ----------
def hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu):
    rincian, total = [], 0
    if anak_karyawan:
        rincian.append(("Anak karyawan", 25)); total += 25
    if ipk >= 3.8:
        rincian.append(("IPK >= 3.8", 20)); total += 20
    elif ipk >= 3.5:
        rincian.append(("IPK >= 3.5", 15)); total += 15
    elif ipk >= 3.0:
        rincian.append(("IPK >= 3.0", 10)); total += 10
    if tepat_waktu:
        rincian.append(("Bayar tepat waktu", 5)); total += 5
    potongan = spp * total / 100
    return rincian, total, potongan, spp - potongan


def menu_diskon_biaya():
    print("\n=== HITUNG DISKON BIAYA KULIAH ===")
    spp = baca_float("Biaya SPP (Rp)            : ", 1, 1_000_000_000)
    anak = baca_yn("Anak karyawan? (y/n)      : ")
    ipk = baca_float("IPK (0.0-4.0)            : ", 0.0, 4.0)
    waktu = baca_yn("Bayar tepat waktu? (y/n)  : ")
    rincian, total, potongan, final = hitung_diskon(spp, anak, ipk, waktu)

    print("\n" + "=" * 45)
    print(f"Biaya SPP awal : Rp {spp:,.0f}")
    print("-" * 45)
    if rincian:
        for nama, persen in rincian:
            print(f"  - {nama:<25}{persen:>3}%")
    else:
        print("  Tidak ada diskon yang berlaku.")
    print("-" * 45)
    print(f"Total diskon   : {total}%")
    print(f"Potongan biaya : Rp {potongan:,.0f}")
    print(f"BIAYA FINAL    : Rp {final:,.0f}")
    print("=" * 45)


# ---------- 3. PERINGATAN STOK ----------
def evaluasi_status(item):
    stok, minimum = item["stok"], item["minimum"]
    if stok == 0:
        return "HABIS"
    elif stok <= minimum * 0.5:
        return "RENDAH"
    elif stok <= minimum:
        return "PERINGATAN"
    return "AMAN"


def menu_peringatan_stok():
    hasil = []
    for item in INVENTARIS:
        st = evaluasi_status(item)
        hasil.append({**item, "status": st, "prioritas": PRIORITAS[st],
                      "nilai": item["stok"] * item["harga"]})
    hasil.sort(key=lambda x: x["prioritas"])

    print("\n" + "=" * 88)
    print("LAPORAN PERINGATAN STOK".center(88))
    print("=" * 88)
    print(f"{'Kode':<7}{'Nama Barang':<22}{'Stok':>6}{'Min':>6}{'Harga':>10}"
          f"{'Nilai':>14}  {'Status':<12}{'Prioritas':<9}")
    print("-" * 88)
    for h in hasil:
        print(f"{h['kode']:<7}{h['nama']:<22}{h['stok']:>6}{h['minimum']:>6}"
              f"{h['harga']:>10,}{h['nilai']:>14,}  {h['status']:<12}"
              f"{LABEL_PRIORITAS[h['prioritas']]:<9}")
    print("-" * 88)
    print(f"Total nilai inventaris : Rp {sum(h['nilai'] for h in hasil):,}")
    for status in PRIORITAS:
        n = sum(1 for h in hasil if h["status"] == status)
        print(f"  {status:<12}: {n} item ({n / len(hasil) * 100:.1f}%)")
    print("=" * 88)


# ---------- MENU UTAMA ----------
def main():
    while True:
        print("\n" + "=" * 36)
        print("   SISTEM INFORMASI MAHASISWA")
        print("=" * 36)
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-3): ").strip()

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_diskon_biaya()
        elif pilihan == "3":
            menu_peringatan_stok()
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 0-3.")


if __name__ == "__main__":
    main()