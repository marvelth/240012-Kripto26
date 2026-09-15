'''
Nama: Marvel Evan Theofani
NPM: 140810240012
Kelas: A
Nama Program: hill-cipher.py
'''

def convertAlphabetToNumber(huruf):
    return ord(huruf.upper())-ord('A')

def convertNumberToAlphabet(angka):
    return chr((angka%26)+ord('A'))

def determinan(matriks):
    return ((matriks[0][0]*matriks[1][1])-(matriks[0][1]*matriks[1][0]))
    
def inversMod(angka):
    angka %= 26
    for i in range(1, 26):
        if(angka*i)%26 == 1:
            return i
    return None

def inversMatriks(matriks):
    a = matriks[0][0]
    b = matriks[0][1]
    c = matriks[1][0]
    d = matriks[1][1]
    det = determinan(matriks)
    invers_det = inversMod(det)
    if invers_det is None:
        print("Nilai determinan tidak koprima dengan 26")
        return None
    adj = [[d, -b], [-c, a]]
    inversed_matriks = [
        [(invers_det*adj[0][0])%26, (invers_det*adj[0][1]%26)],
        [(invers_det*adj[1][0])%26, (invers_det*adj[1][1]%26)],
    ]
    return inversed_matriks

def encryptHill(p, key):
    plaintext = p.upper().replace(" ", "")
    if len(plaintext)%2 != 0:
        plaintext += "X"
    angka = [convertAlphabetToNumber(a) for a in plaintext]
    ciphertext = ""
    for i in range(0, len(angka), 2):
        p1, p2 = angka[i], angka[i+1]
        c1 = (key[0][0]*p1 + key[0][1]*p2)%26
        c2 = (key[1][0]*p1 + key[1][1]*p2)%26
        ciphertext += convertNumberToAlphabet(c1)+convertNumberToAlphabet(c2)
    return ciphertext

def decryptHill(c, key):
    inversed_key = inversMatriks(key)
    if inversed_key is None:
        return None
    ciphertext = c.upper().replace(" ", "")
    angka = [convertAlphabetToNumber(a) for a in ciphertext]
    plaintext = ""
    for i in range(0, len(angka), 2):
        c1, c2 = angka[i], angka[i+1]
        p1 = (inversed_key[0][0]*c1 + inversed_key[0][1]*c2)%26
        p2 = (inversed_key[1][0]*c1 + inversed_key[1][1]*c2)%26
        plaintext += convertNumberToAlphabet(p1)+convertNumberToAlphabet(p2)
    return plaintext

def keyHill(p, c):
    plaintext = p.upper().replace(" ", "")
    ciphertext = c.upper().replace(" ", "")
    if len(plaintext) < 4 or len(ciphertext) < 4:
        return None
    angka_p = [convertAlphabetToNumber(a) for a in plaintext[:4]]
    angka_c = [convertAlphabetToNumber(a) for a in ciphertext[:4]]
    matriks_p = [[angka_p[0], angka_p[2]], [angka_p[1], angka_p[3]]]
    matriks_c = [[angka_c[0], angka_c[2]], [angka_c[1], angka_c[3]]]
    inversed_matriks_p = inversMatriks(matriks_p)
    if inversed_matriks_p is None:
        return None
    key = [
        [(matriks_c[0][0]*inversed_matriks_p[0][0]+matriks_c[0][1]*inversed_matriks_p[1][0])%26, 
         (matriks_c[0][0]*inversed_matriks_p[0][1]+matriks_c[0][1]*inversed_matriks_p[1][1])%26],
        [(matriks_c[1][0]*inversed_matriks_p[0][0]+matriks_c[1][1]*inversed_matriks_p[1][0])%26, 
         (matriks_c[1][0]*inversed_matriks_p[0][1]+matriks_c[1][1]*inversed_matriks_p[1][1])%26]
    ]
    return key

def inputKunci():
    nilai = input("Masukkan 4 angka kunci (a b c d): ").split()
    if len(nilai) != 4:
        print("Kunci harus terdiri dari tepat 4 angka.")
    key = [[int(nilai[0]) % 26, int(nilai[1]) % 26],
           [int(nilai[2]) % 26, int(nilai[3]) % 26]]
    if inversMatriks(key) is None:
        print("Kunci tidak memiliki invers modulo 26.")
    return key

def main():
    print("=== Hill Cipher 2x2 ===")
    while True:
        print("\n1. Enkripsi\n2. Dekripsi\n3. Cari Kunci\n4. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "4":
            print("Program selesai.")
            break
        if pilihan not in ("1", "2", "3"):
            print("Pilihan tidak tersedia.")
            continue
        try:
            if pilihan == "3":
                pt = input("Masukkan plaintext: ")
                ct = input("Masukkan ciphertext: ")
                kunci = keyHill(pt, ct)
                if kunci is not None:
                    print("Kunci matriks 2x2 yang ditemukan:")
                    print(f"[{kunci[0][0]}  {kunci[0][1]}]")
                    print(f"[{kunci[1][0]}  {kunci[1][1]}]")
            else:
                key = inputKunci()
                teks = input("Masukkan teks: ")
                if pilihan == "1":
                    hasil = encryptHill(teks, key)
                    print("Ciphertext:", hasil)
                elif pilihan == "2":
                    hasil = decryptHill(teks, key)
                    print("Plaintext:", hasil)        
        except (ValueError, TypeError) as error:
            print("Error:", error)

if __name__ == "__main__":
    main()