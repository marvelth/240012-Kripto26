'''
Nama: Marvel Evan Theofani
NPM: 140810240012
Kelas: A
Nama Program: vigenere-cipher.py
'''

def convertAlphabetToNumber(huruf):
    return ord(huruf.upper())-ord('A')

def convertNumberToAlphabet(angka):
    return chr((angka%26)+ord('A'))

def encryptVigenere(p, k):
    plaintext = p.upper().replace(" ", "")
    key = k.upper().replace(" ", "")
    ciphertext = ""
    for i in range(len(plaintext)):
        p_angka = convertAlphabetToNumber(plaintext[i])
        k_angka = convertAlphabetToNumber(key[i%len(key)])    # Pengulangan string key apabila panjang plaintext melebihi panjang key
        encrypt = (p_angka+k_angka)%26
        ciphertext += convertNumberToAlphabet(encrypt)
    return ciphertext

def decryptVigenere(c, k):
    ciphertext = c.upper().replace(" ", "")
    key = k.upper().replace(" ", "")
    plaintext = ""
    for i in range(len(ciphertext)):
        c_angka = convertAlphabetToNumber(ciphertext[i])
        k_angka = convertAlphabetToNumber(key[i%len(key)])
        decrypt = (c_angka-k_angka)%26
        plaintext += convertNumberToAlphabet(decrypt)
    return plaintext

def main():
    print("=== Vigenere Cipher ===")
    while True:
        print("\n1. Enkripsi\n2. Dekripsi\n3. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "3":
            print("Program selesai.")
            break
        if pilihan not in ("1", "2"):
            print("Pilihan tidak tersedia.")
            continue
        teks = input("Masukkan teks (Plaintext/Ciphertext): ")
        key = input("Masukkan key (Teks): ")
        if not key.replace(" ", "").isalpha():
            print("Error: Key harus berupa huruf alfabet.")
            continue
        if pilihan == "1":
            hasil = encryptVigenere(teks, key)
            print("Ciphertext:", hasil)
        elif pilihan == "2":
            hasil = decryptVigenere(teks, key)
            print("Plaintext:", hasil)

if __name__ == "__main__":
    main()