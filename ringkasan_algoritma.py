# ringkasan_algoritma.py

# ---------- DATA CONTOH ----------
MAHASISWA = [
    {"nim": "2023010001", "nama": "Andi",  "ipk": 3.60, "sks": 20},
    {"nim": "2023010002", "nama": "Budi",  "ipk": 2.50, "sks": 18},
    {"nim": "2023010003", "nama": "Citra", "ipk": 1.80, "sks": 15},
    {"nim": "2023010004", "nama": "Dewi",  "ipk": 1.20, "sks": 12},
    {"nim": "2023010005", "nama": "Eko",   "ipk": 3.90, "sks": 24},
]

# anak_karyawan, ipk, tepat_waktu
DATA_DISKON = [
    {"spp": 5_000_000, "anak": True,  "ipk": 3.85, "waktu": True},
    {"spp": 5_000_000, "anak": False, "ipk": 3.60, "waktu": True},
    {"spp": 5_000_000, "anak": False, "ipk": 3.10, "waktu": False},
    {"spp": 5_000_000, "anak": True,  "ipk": 2.50, "waktu": False},
    {"spp": 5_000_000, "anak": False, "ipk": 2.40, "waktu": False},
]

INVENTARIS = [
    {"nama": "Kertas A4 (rim)",   "stok": 120, "minimum": 30},
    {"nama": "Tinta Printer",     "stok": 25,  "minimum": 20},
    {"nama": "Spidol Whiteboard", "stok": 8,   "minimum": 20},
    {"nama": "Stapler",           "stok": 0,   "minimum": 10},
    {"nama": "Map Folder",        "stok": 200, "minimum": 50},
    {"nama": "Kabel HDMI",        "stok": 4,   "minimum": 10},
    {"nama": "Flashdisk 32GB",    "stok": 18,  "minimum": 15},
    {"nama": "Baterai AA (pak)",  "stok": 0,   "minimum": 12},
]


# ---------- FUNGSI ALGORITMA ----------
def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    elif ipk < 2.0:
        return "Peringatan"
    elif sks >= 18:
        return "Aktif"
    return "Peringatan"


def total_persen_diskon(anak, ipk, waktu):
    total = 25 if anak else 0
    if ipk >= 3.8:
        total += 20
    elif ipk >= 3.5:
        total += 15
    elif ipk >= 3.0:
        total += 10
    if waktu:
        total += 5
    return total


def perlu_restock(item):
    return item["stok"] <= item["minimum"]  # habis, rendah, atau peringatan


# ---------- PERHITUNGAN ----------
def main():
    # (a) Mahasiswa aktif vs tidak aktif
    status = [tentukan_status(m["ipk"], m["sks"]) for m in MAHASISWA]
    total_mhs = len(status)
    aktif = status.count("Aktif")
    peringatan = status.count("Peringatan")
    tidak_aktif = status.count("Tidak Aktif")

    # (b) Rata-rata diskon
    daftar_diskon = [total_persen_diskon(d["anak"], d["ipk"], d["waktu"])
                     for d in DATA_DISKON]
    rata_diskon = sum(daftar_diskon) / len(daftar_diskon)
    rata_potongan = sum(d["spp"] * p / 100
                        for d, p in zip(DATA_DISKON, daftar_diskon)) / len(DATA_DISKON)

    # (c) Persentase item perlu restock
    total_item = len(INVENTARIS)
    jumlah_restock = sum(1 for i in INVENTARIS if perlu_restock(i))

    # ---------- TAMPILAN TABEL ----------
    garis = "+" + "-" * 38 + "+" + "-" * 10 + "+" + "-" * 14 + "+"
    print("\n" + "RINGKASAN ALGORITMA SISTEM INFORMASI MAHASISWA".center(66))
    print(garis)
    print(f"| {'Indikator':<36} | {'Jumlah':>8} | {'Persentase':>12} |")
    print(garis)
    print(f"| {'(a) Mahasiswa Aktif':<36} | {aktif:>8} | {aktif / total_mhs * 100:>11.1f}% |")
    print(f"| {'    Mahasiswa Peringatan':<36} | {peringatan:>8} | {peringatan / total_mhs * 100:>11.1f}% |")
    print(f"| {'    Mahasiswa Tidak Aktif':<36} | {tidak_aktif:>8} | {tidak_aktif / total_mhs * 100:>11.1f}% |")
    print(garis)
    print(f"| {'(b) Rata-rata diskon diberikan':<36} | {len(DATA_DISKON):>8} | {rata_diskon:>11.1f}% |")
    print(f"| {'    Rata-rata potongan (Rp)':<36} | {'-':>8} | {rata_potongan:>12,.0f} |")
    print(garis)
    print(f"| {'(c) Item perlu restock':<36} | {jumlah_restock:>8} | {jumlah_restock / total_item * 100:>11.1f}% |")
    print(f"| {'    Item stok aman':<36} | {total_item - jumlah_restock:>8} | {(total_item - jumlah_restock) / total_item * 100:>11.1f}% |")
    print(garis)
    print(f"Catatan: Aktif vs Tidak Aktif = {aktif / total_mhs * 100:.1f}% : {tidak_aktif / total_mhs * 100:.1f}%")


if __name__ == "__main__":
    main()