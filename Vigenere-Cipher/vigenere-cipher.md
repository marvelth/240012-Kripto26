# Program Vigenere Cipher

* **Nama:** Marvel Evan Theofani
* **NPM:** 140810240012
* **Kelas:** A

---

## Deskripsi Program
Program ini merupakan implementasi dari algoritma kriptografi klasik Vigenere Cipher.

Program menyediakan dua fitur utama:
1. **Enkripsi:** Mengubah Plaintext menjadi Ciphertext menggunakan string kunci.
2. **Dekripsi:** Mengembalikan Ciphertext menjadi Plaintext menggunakan string kunci.
---

## Penjelasan Alur Program dan Fungsi

### 1. Fungsi Utilitas Dasar
* **`convertAlphabetToNumber(huruf)` & `convertNumberToAlphabet(angka)`**
  Berfungsi untuk mengonversi karakter huruf (A-Z) menjadi angka indeks (0-25) dan sebaliknya dengan memanfaatkan nilai ASCII melalui fungsi bawaan `ord()` dan `chr()`.

### 2. Fungsi Inti Kriptografi
* **`encryptVigenere(p, k)`**
  Fungsi enkripsi teks. Jika panjang plaintext melebihi panjang key, maka dilakukan perulangan dengan mengambil elemen huruf pada key tersebut hingga menyamai panjang plaintext.
* **`decryptHill(c, k)`**
  Fungsi enkripsi teks. Jika panjang plaintext melebihi panjang key, maka dilakukan perulangan dengan mengambil elemen huruf pada key tersebut hingga menyamai panjang plaintext.
---

## Screenshot Running Program

**1. Screenshot Enkripsi & Dekripsi**


**2. Screenshot Pencarian Kunci**