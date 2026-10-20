# validasi_data.py

def validasi_nim(nim):
    errors = []
    nim = str(nim).strip()
    if not nim.isdigit():
        errors.append("NIM harus berupa angka saja.")
    if len(nim) != 10:
        errors.append("NIM harus tepat 10 digit.")
    if nim.isdigit() and len(nim) >= 4:
        tahun = int(nim[:4])
        if not (2000 <= tahun <= 2037):
            errors.append(f"Tahun pada NIM ({tahun}) harus antara 2000-2037.")
    return errors


def validasi_ipk(ipk):
    try:
        nilai = float(ipk)
    except (ValueError, TypeError):
        return ["IPK harus berupa angka."]
    if not (0.0 <= nilai <= 4.0):
        return ["IPK harus antara 0.0 - 4.0."]
    return []


def validasi_sks(sks):
    try:
        nilai = int(sks)
    except (ValueError, TypeError):
        return ["SKS harus berupa bilangan bulat."]
    if not (0 <= nilai <= 24):
        return ["SKS harus antara 0 - 24."]
    return []


def validasi_semester(semester):
    try:
        nilai = int(semester)
    except (ValueError, TypeError):
        return ["Semester harus berupa bilangan bulat."]
    if not (1 <= nilai <= 14):
        return ["Semester harus antara 1 - 14."]
    return []


def validasi_mahasiswa(nim, ipk, sks, semester):
    """Mengembalikan list error; list kosong berarti semua data valid."""
    errors = []
    errors += validasi_nim(nim)
    errors += validasi_ipk(ipk)
    errors += validasi_sks(sks)
    errors += validasi_semester(semester)
    return errors


def main():
    print("=== VALIDASI DATA MAHASISWA ===")
    while True:
        nim = input("\nNIM (10 digit)  : ")
        ipk = input("IPK (0.0-4.0)   : ")
        sks = input("SKS (0-24)      : ")
        semester = input("Semester (1-14) : ")

        errors = validasi_mahasiswa(nim, ipk, sks, semester)
        print("\n--- HASIL VALIDASI ---")
        if errors:
            print(f"Ditemukan {len(errors)} kesalahan:")
            for no, e in enumerate(errors, 1):
                print(f"  {no}. {e}")
        else:
            print("Semua data VALID.")

        lagi = input("\nValidasi data lain? (y/n): ").strip().lower()
        if lagi != "y":
            print("Selesai.")
            break


if __name__ == "__main__":
    main()