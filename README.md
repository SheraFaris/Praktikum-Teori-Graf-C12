# **PRAKTIKUM TEORI GRAF C12**

| No | Nama                      | NRP        |
| -- | ------------------------- | ---------- |
| 1  | Ananda Faris Ghazi R      | 5025231280 |
| 2  | Muhammad Nawfal Alfanni D | 5025241185 |
| 3  | Farrel Prastita Ramadhan  | 5025241219 |

Mahasiswa mata kuliah **Teori Graf C12** diberikan dua soal praktikum yang bertujuan untuk mengimplementasikan konsep algoritma ke dalam sebuah program. Soal yang diberikan pada praktikum ini adalah **Knight’s Tour** dan **Largest Monotonically Increasing Subsequence (LMIS)**.

Melalui praktikum ini, mahasiswa diharapkan dapat memahami konsep algoritma pencarian, menerapkannya ke dalam program, serta menjelaskan cara kerja dan alasan keberhasilan algoritma dalam menyelesaikan permasalahan yang diberikan.

---

# **Soal I

Largest Monotonically Increasing Subsequence (LMIS)**

## **1.1 Tujuan Program**

Tujuan dari program ini adalah untuk menerima sebuah array bilangan sebagai input, kemudian mencari **subsequence meningkat (strictly increasing)** terpanjang dari array tersebut. Program akan menampilkan subsequence hasil beserta panjangnya.


## **1.2 Struktur Kode dan Fungsinya**

### **1.2.1 `TreeNode`**

Kelas `TreeNode` digunakan untuk merepresentasikan satu node dalam tree pencarian subsequence. Setiap node memiliki:

* `value` sebagai nilai elemen array,
* `index` sebagai posisi elemen dalam array,
* `children` untuk menyimpan node lanjutan,
* `sequence` untuk menyimpan subsequence dari root hingga node tersebut.


### **1.2.2 `build_tree(arr, index, parent_sequence)`**

Fungsi ini digunakan untuk membangun tree subsequence meningkat dengan langkah-langkah sebagai berikut:

* Membuat node baru dari elemen array pada indeks tertentu,
* Menambahkan elemen tersebut ke subsequence sebelumnya,
* Membuat child node secara rekursif jika ditemukan elemen berikutnya yang lebih besar.

Dengan cara ini, seluruh kemungkinan subsequence meningkat dapat dibentuk.


### **1.2.3 `find_lmis(arr)`**

Fungsi ini merupakan algoritma utama untuk mencari LMIS dengan pendekatan tree dan **Depth First Search (DFS)**, dengan langkah:

1. Membuat root untuk setiap elemen array,
2. Melakukan DFS pada setiap tree,
3. Menyimpan subsequence terpanjang yang ditemukan,
4. Mengembalikan subsequence dengan panjang maksimum.


### **1.2.4 `print_tree(node)`**

Fungsi ini bersifat opsional dan digunakan untuk menampilkan struktur tree subsequence dalam bentuk visual di terminal.


### **1.2.5 `main()`**

Fungsi utama yang mengatur alur program, yaitu:

* Menerima input array dari pengguna,
* Memanggil fungsi pencarian LMIS,
* Menampilkan hasil subsequence dan panjangnya,
* Menyediakan opsi untuk menampilkan visualisasi tree.


### **1.2.6 `find_lmis_dp(arr)`**

Fungsi ini merupakan versi alternatif menggunakan **dynamic programming**.
Pendekatan ini lebih efisien karena menyimpan subsequence terbaik pada setiap indeks array dan memperbaruinya secara bertahap.


## **1.3 Cara Kerja Algoritma**

Fungsi `build_tree` hanya membentuk child dari elemen array yang memiliki indeks lebih besar dan nilai lebih besar dari elemen sebelumnya. Hal ini memastikan bahwa subsequence yang dihasilkan:

* Tidak melanggar urutan array,
* Selalu bersifat meningkat.

Dengan melakukan DFS pada seluruh node tree, program dapat membandingkan semua subsequence yang valid dan memilih subsequence dengan panjang maksimum.


## **1.4 Alasan Program Berhasil**

Program berhasil menemukan LMIS karena:

1. Setiap subsequence yang dibentuk selalu valid,
2. Seluruh kemungkinan subsequence meningkat dicoba,
3. DFS memastikan tidak ada subsequence yang terlewat,
4. Seleksi subsequence terpanjang dilakukan secara konsisten.


## **1.5 Contoh Alur Eksekusi**

Untuk input:

```
4, 1, 13, 7, 0, 2, 8, 11, 3
```

Program akan membentuk tree subsequence dari setiap elemen, kemudian mencari subsequence meningkat terpanjang melalui DFS. Hasil akhir berupa subsequence dengan panjang terbesar akan ditampilkan sebagai output.


# **Soal II

Knight’s Tour**

## **2.1 Deskripsi Program**

Program Knight’s Tour dibuat untuk menentukan lintasan pergerakan bidak kuda pada papan catur berukuran 8 × 8 sehingga seluruh petak papan dapat dikunjungi tepat satu kali sesuai aturan pergerakan kuda.

Program diimplementasikan menggunakan bahasa pemrograman Python dengan bantuan pustaka `NumPy` untuk pengolahan matriks dan `Matplotlib` untuk menampilkan visualisasi lintasan kuda.


## **2.2 Algoritma yang Digunakan**

Algoritma yang digunakan adalah **backtracking** dengan bantuan **heuristik Warnsdorff**.
Backtracking digunakan untuk mencoba setiap kemungkinan langkah, sedangkan heuristik Warnsdorff membantu memilih langkah dengan jumlah kemungkinan lanjutan paling sedikit agar pencarian lebih efisien.


## **2.3 Cara Kerja Program**

Langkah kerja program adalah sebagai berikut:

1. Program menginisialisasi papan catur 8 × 8.
2. Posisi awal kuda ditentukan.
3. Semua kemungkinan langkah kuda dihitung.
4. Langkah terbaik dipilih berdasarkan heuristik Warnsdorff.
5. Petak yang sudah dikunjungi ditandai.
6. Proses diulang hingga seluruh petak dikunjungi.
7. Jika langkah buntu, program melakukan backtracking.
8. Hasil akhir ditampilkan dalam bentuk matriks dan visualisasi lintasan.


## **2.4 Open Tour dan Closed Tour**

* **Open Tour**
  Kuda dapat berhenti di petak mana saja setelah seluruh papan dikunjungi.

* **Closed Tour**
  Posisi akhir kuda harus dapat menyerang posisi awal dengan satu langkah kuda.

Program melakukan pengecekan tambahan untuk memastikan kondisi *closed tour* terpenuhi.


# **BAB III

Analisis Keberhasilan Program**

## **3.1 Alasan Algoritma Berhasil**

Algoritma berhasil karena:

1. Gerakan kuda selalu divalidasi,
2. Tidak ada petak yang dikunjungi lebih dari satu kali,
3. Heuristik Warnsdorff mengurangi kemungkinan jalan buntu,
4. Backtracking memungkinkan pencarian solusi alternatif.

## **3.2 Keterbatasan Program**

Beberapa keterbatasan program antara lain:

1. Tidak semua posisi awal selalu menghasilkan *closed tour*,
2. Performa dapat menurun pada papan dengan ukuran lebih besar,
3. Algoritma masih bergantung pada heuristik.


# **BAB IV

Kesimpulan**

Berdasarkan hasil praktikum, dapat disimpulkan bahwa algoritma *backtracking* dengan heuristik Warnsdorff mampu menyelesaikan permasalahan Knight’s Tour dengan baik pada papan catur berukuran 8 × 8. Program berhasil menghasilkan lintasan *open tour* maupun *closed tour* serta menampilkan visualisasi pergerakan bidak kuda.

