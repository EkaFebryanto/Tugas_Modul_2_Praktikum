# peringatan_stok.py

INVENTARIS = [
    {"kode": "B001", "nama": "Kertas A4 (rim)",    "stok": 120, "minimum": 30, "harga": 55000},
    {"kode": "B002", "nama": "Tinta Printer",      "stok": 25,  "minimum": 20, "harga": 90000},
    {"kode": "B003", "nama": "Spidol Whiteboard",  "stok": 8,   "minimum": 20, "harga": 12000},
    {"kode": "B004", "nama": "Stapler",            "stok": 0,   "minimum": 10, "harga": 35000},
    {"kode": "B005", "nama": "Map Folder",         "stok": 200, "minimum": 50, "harga": 3000},
    {"kode": "B006", "nama": "Kabel HDMI",         "stok": 4,   "minimum": 10, "harga": 45000},
    {"kode": "B007", "nama": "Flashdisk 32GB",     "stok": 18,  "minimum": 15, "harga": 70000},
    {"kode": "B008", "nama": "Baterai AA (pak)",   "stok": 0,   "minimum": 12, "harga": 25000},
    {"kode": "B009", "nama": "Penghapus Papan",    "stok": 60,  "minimum": 15, "harga": 8000},
]

PRIORITAS = {"HABIS": 1, "RENDAH": 2, "PERINGATAN": 3, "AMAN": 4}
LABEL_PRIORITAS = {1: "KRITIS", 2: "TINGGI", 3: "SEDANG", 4: "NORMAL"}


def evaluasi_status(item):
    stok, minimum = item["stok"], item["minimum"]
    if stok == 0:
        return "HABIS"
    elif stok <= minimum * 0.5:
        return "RENDAH"
    elif stok <= minimum:
        return "PERINGATAN"
    return "AMAN"


def proses_inventaris(data):
    hasil = []
    for item in data:
        status = evaluasi_status(item)
        hasil.append({**item, "status": status,
                      "prioritas": PRIORITAS[status],
                      "nilai": item["stok"] * item["harga"]})
    return sorted(hasil, key=lambda x: x["prioritas"])


def tampilkan_laporan(data=INVENTARIS):
    hasil = proses_inventaris(data)
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

    total_nilai = sum(h["nilai"] for h in hasil)
    jumlah = len(hasil)
    print(f"Total nilai inventaris : Rp {total_nilai:,}")

    print("\nRINGKASAN STATISTIK")
    print("-" * 40)
    for status in PRIORITAS:
        n = sum(1 for h in hasil if h["status"] == status)
        print(f"  {status:<12}: {n} item ({n / jumlah * 100:.1f}%)")
    rata_stok = sum(h["stok"] for h in hasil) / jumlah
    termahal = max(hasil, key=lambda x: x["nilai"])
    perlu_restock = [h["nama"] for h in hasil if h["status"] != "AMAN"]
    print(f"  Jumlah item          : {jumlah}")
    print(f"  Rata-rata stok       : {rata_stok:.1f}")
    print(f"  Nilai stok terbesar  : {termahal['nama']} (Rp {termahal['nilai']:,})")
    print(f"  Perlu restock        : {len(perlu_restock)} item")
    print("=" * 88)


if __name__ == "__main__":
    tampilkan_laporan()