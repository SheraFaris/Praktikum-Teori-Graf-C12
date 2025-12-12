## PRAKTIKUM TEORI GRAF C12
| No | Nama                      |     NRP      |
| -- | ------------------------- | ------------ |
| 1  | Ananda Faris Ghazi R      |  5025231280  |
| 2  | Muhammad Nawfal Alfanni D |  5025241185  |
| 3  | Farrel Prastita Ramadhan  |  5025241219  |


Mahasiswa Teori Graf C diberikan 2 soal praktikum untuk dibuatkan program yang bisa berjalan sebagai bentuk implementasi dari soal tersebut. Soal dari praktikum berupa "Knight's Tour" dan "Largest Monotonically Increasing Subsequence".

Melalui praktikum ini, mahasiswa diharapkan mampu memahami konsep algoritma pencarian, mengimplementasikan algoritma tersebut ke dalam sebuah program, serta menganalisis cara kerja dan keberhasilan algoritma dalam menyelesaikan permasalahan.

****

---

## 1) Tujuan Program

Program menerima input sebuah array bilangan, lalu mencari **subsequence meningkat (strictly increasing)** terpanjang dari array tersebut, dan menampilkan hasil subsequence dan panjangnya. 

---

## 2) Struktur Kode dan Fungsinya

### a. `TreeNode`

Merepresentasikan satu node di tree pencarian subsequence:

* `value`: nilai elemen array di node
* `index`: posisi elemen di array
* `children`: daftar node lanjutan yang nilainya lebih besar
* `sequence`: subsequence dari root sampai node ini 

### b. `build_tree(arr, index, parent_sequence)`

Membangun tree subsequence meningkat mulai dari `arr[index]`:

* Membuat node baru
* `node.sequence = parent_sequence + [arr[index]]`
* Untuk setiap `i > index`, kalau `arr[i] > arr[index]`, maka `arr[i]` bisa jadi kelanjutan subsequence → dibuat child secara rekursif 

**Intinya:** fungsi ini membuat semua kemungkinan subsequence meningkat yang berawal dari elemen tertentu.

### c. `find_lmis(arr)`

Algoritma utama versi tree + DFS:

1. Jika array kosong → return `[]` 
2. Membuat “root” untuk setiap index (jadi semua kemungkinan start dicoba) 
3. DFS ke seluruh node dan menyimpan `longest` jika menemukan `node.sequence` lebih panjang 
4. Kembalikan `longest` 

### d. `print_tree(...)`

Hanya untuk visualisasi bentuk tree (opsional) dengan karakter cabang. 

### e. `main()`

* Minta input array “dipisah koma”
* Parse input jadi list int
* Panggil `find_lmis` dan cetak hasil
* Opsional tampilkan visualisasi tree untuk 5 root pertama 

### f. `find_lmis_dp(arr)` (alternatif DP)

Versi **dynamic programming** yang lebih efisien:

* `dp[i]` menyimpan subsequence meningkat terbaik yang **berakhir di i**
* Untuk setiap pasangan `j < i`, kalau `arr[j] < arr[i]` dan subsequence dari `j` membuat `dp[i]` lebih panjang, update `dp[i]` 

> Di file ini, `main()` masih memakai versi tree (`find_lmis`), bukan DP. 

---

## 3) Cara Kerja Algoritma (Mengapa Output Bisa Benar)

### Mengapa `build_tree` benar membentuk “semua” subsequence meningkat?

Untuk setiap elemen `arr[index]`, `build_tree` hanya membuat child dari posisi setelahnya (`i = index+1..`) yang nilainya **lebih besar** (`arr[i] > arr[index]`). 
Ini memastikan:

* Urutan index selalu maju → subsequence valid (tidak melanggar urutan array)
* Nilai selalu naik strict → subsequence meningkat

Karena semua kandidat `i` yang valid dicoba, maka semua kemungkinan kelanjutan subsequence dari node itu **tercakup**.

### Mengapa DFS menemukan yang terpanjang?

DFS mengunjungi **seluruh node** pada tree dari setiap root. 
Setiap node menyimpan `node.sequence` yang merupakan subsequence valid dari root ke node tersebut. 
Saat DFS, program selalu memperbarui `longest` jika menemukan sequence lebih panjang. 

Karena:

1. Semua subsequence meningkat valid dihasilkan sebagai node-node di tree, dan
2. DFS memeriksa semuanya,
   maka `longest` pada akhir DFS pasti merupakan **subsequence meningkat terpanjang**.

---

## 4) Kenapa Program “Berhasil” dan Apa Batasannya

### Alasan berhasil

* Validitas subsequence dijaga oleh syarat `arr[i] > arr[index]` dan `i > index`. 
* Tidak ada subsequence yang terlewat karena setiap root dicoba dan semua cabang valid dieksplor. 
* Seleksi hasil terpanjang dilakukan konsisten selama DFS. 

### Batasan (penting untuk ditulis di laporan)

Versi tree ini bisa **meledak** untuk input besar, karena jumlah subsequence meningkat bisa sangat banyak (mendekati eksponensial pada kasus tertentu). Itu sebabnya di file juga disediakan versi DP (`find_lmis_dp`) yang lebih aman untuk ukuran data lebih besar. 

---

## 5) Contoh Alur Eksekusi Singkat

Misal input: `4, 1, 13, 7, 0, 2, 8, 11, 3`

* Program membuat root dari 4, 1, 13, 7, 0, 2, 8, 11, 3
* Dari root `1`, ia bisa lanjut ke `13`, `7`, `2`, `8`, `11`, `3` (yang > 1 dan berada setelahnya), lalu lanjut lagi sampai tidak bisa
* DFS membandingkan seluruh jalur dan memilih yang paling panjang
* Output menampilkan subsequence meningkat terpanjang dan panjangnya. 

---

Kalau kamu kirim **kode Knight’s Tour** (atau file `.py/.c` yang dipakai untuk tugas di gambar), aku bisa bikinkan laporan dengan struktur yang sama: **algoritma (Warnsdorff/backtracking), open tour vs closed tour, bukti/argumen kenapa valid (visit semua kotak tepat sekali), serta analisis kompleksitas**.
