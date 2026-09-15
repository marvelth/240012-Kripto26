# Program Hill Cipher 2x2

* **Nama:** Marvel Evan Theofani
* **NPM:** 140810240012
* **Kelas:** A

---

## Deskripsi Program
Program ini merupakan implementasi dari algoritma kriptografi klasik Hill Cipher menggunakan matriks kunci berordo $2 \times 2$.

Program menyediakan tiga fitur utama:
1. **Enkripsi:** Mengubah Plaintext menjadi Ciphertext menggunakan matriks kunci.
2. **Dekripsi:** Mengembalikan Ciphertext menjadi Plaintext menggunakan invers dari matriks kunci.
3. **Cari Kunci:** Menemukan matriks kunci yang digunakan berdasarkan pasangan Plaintext dan Ciphertext yang diketahui (Kriptanalisis).

---

## Penjelasan Alur Program dan Fungsi

### 1. Fungsi Utilitas Dasar
* **`convertAlphabetToNumber(huruf)` & `convertNumberToAlphabet(angka)`**
  Berfungsi untuk mengonversi karakter huruf (A-Z) menjadi angka indeks (0-25) dan sebaliknya dengan memanfaatkan nilai ASCII melalui fungsi bawaan `ord()` dan `chr()`.

### 2. Fungsi Operasi Matriks & Modulo 26
* **`determinan(matriks)`**
  Menghitung nilai determinan dari matriks $2 \times 2$ menggunakan rumus standar aljabar linier: $(a \times d) - (b \times c)$.
* **`inversMod(angka)`**
  Mencari nilai invers modulo 26 dari determinan matriks. Fungsi ini menggunakan perulangan dari 1 hingga 25 untuk mencari angka yang jika dikalikan dengan determinan lalu dimodulo dengan 26, hasilnya adalah 1.
* **`inversMatriks(matriks)`**
  Mencari matriks invers (modulo 26). Prosesnya meliputi: mencari adjoin dari matriks awal (menukar posisi $a$ dan $d$, serta mengalikan $b$ dan $c$ dengan -1), lalu mengalikan setiap elemen adjoin tersebut dengan nilai `inversMod` determinannya. Hasil akhirnya dimodulokan dengan 26.

### 3. Fungsi Inti Kriptografi
* **`encryptHill(p, key)`**
  Fungsi enkripsi teks. Jika panjang teks ganjil, akan ditambahkan huruf "X" di akhir teks sebagai *padding*. Teks kemudian dipecah menjadi blok berisi 2 angka berurutan. Setiap blok direpresentasikan sebagai vektor kolom $2 \times 1$ dan dikalikan dengan matriks kunci berordo $2 \times 2$. Hasil perkalian di-modulo 26 dan diubah kembali menjadi teks Ciphertext.
* **`decryptHill(c, key)`**
  Fungsi dekripsi teks. Alur kerjanya mirip dengan `encryptHill`, namun vektor blok 2 huruf dikalikan dengan **matriks invers kunci** yang didapatkan dari fungsi `inversMatriks()`.
* **`keyHill(p, c)`**
  Fungsi pencarian matriks kunci (dikenal sebagai *Known-Plaintext Attack*). Fungsi ini mengambil tepat 4 karakter pertama dari Plaintext dan Ciphertext masukan. Karakter tersebut disusun dari atas ke bawah untuk membentuk masing-masing matriks ordo $2 \times 2$. Matriks kunci ($K$) ditemukan menggunakan rumus $K = C \cdot P^{-1} \pmod{26}$.

---

## Screenshot Running Program

**1. Screenshot Enkripsi & Dekripsi**
`![Screenshot Enkripsi](link-gambar-atau-path-gambar-disini)`

**2. Screenshot Pencarian Kunci**
`![Screenshot Cari Kunci](link-gambar-atau-path-gambar-disini)`