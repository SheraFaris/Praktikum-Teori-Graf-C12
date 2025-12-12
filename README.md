## PRAKTIKUM TEORI GRAF C12
| No | Nama                      |     NRP      |
| -- | ------------------------- | ------------ |
| 1  | Ananda Faris Ghazi R      |  5025231280  |
| 2  | Muhammad Nawfal Alfanni D |  5025241185  |
| 3  | Farrel Prastita Ramadhan  |  5025241219  |


Mahasiswa Teori Graf C diberikan 2 soal praktikum untuk dibuatkan program yang bisa berjalan sebagai bentuk implementasi dari soal tersebut. Soal dari praktikum berupa "Knight's Tour" dan "Largest Monotonically Increasing Subsequence".

Melalui praktikum ini, mahasiswa diharapkan mampu memahami konsep algoritma pencarian, mengimplementasikan algoritma tersebut ke dalam sebuah program, serta menganalisis cara kerja dan keberhasilan algoritma dalam menyelesaikan permasalahan.


## SOAL 1 : Largest Monotonically Increasing Subsequence


## 1) Tujuan Program

Program menerima input sebuah array bilangan, lalu mencari **subsequence meningkat (strictly increasing)** terpanjang dari array tersebut, dan menampilkan hasil subsequence dan panjangnya. 


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


## 4) Kenapa Program “Berhasil” dan Apa Batasannya

### Alasan berhasil

* Validitas subsequence dijaga oleh syarat `arr[i] > arr[index]` dan `i > index`. 
* Tidak ada subsequence yang terlewat karena setiap root dicoba dan semua cabang valid dieksplor. 
* Seleksi hasil terpanjang dilakukan konsisten selama DFS. 


## 5) Contoh Alur Eksekusi Singkat

Misal input: `4, 1, 13, 7, 0, 2, 8, 11, 3`

* Program membuat root dari 4, 1, 13, 7, 0, 2, 8, 11, 3
* Dari root `1`, ia bisa lanjut ke `13`, `7`, `2`, `8`, `11`, `3` (yang > 1 dan berada setelahnya), lalu lanjut lagi sampai tidak bisa
* DFS membandingkan seluruh jalur dan memilih yang paling panjang
* Output menampilkan subsequence meningkat terpanjang dan panjangnya.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## SOAL 2 : Knight's Tour

Baik 👍
Karena kamu **sudah mengirim kode Knight’s Tour (`Knight.ipynb`)**, berikut aku buatkan **laporan inti yang formal dan akademik**, mencakup:

* **Deskripsi kode**
* **Cara kerja algoritma**
* **Alasan algoritma berhasil**
* **Open tour vs closed tour**
* **Analisis singkat kompleksitas**

Bahasanya siap **langsung masuk laporan praktikum**.

---

## **BAB II

DESKRIPSI PROGRAM DAN ALGORITMA**

### **2.1 Deskripsi Program**

Program yang dibuat bertujuan untuk menyelesaikan permasalahan *The Knight’s Tour* pada papan catur berukuran 8 × 8. Program ini mengimplementasikan algoritma pencarian lintasan untuk menentukan urutan pergerakan bidak kuda sehingga seluruh petak papan catur dapat dikunjungi tepat satu kali sesuai dengan aturan pergerakan kuda.

Program dikembangkan menggunakan bahasa pemrograman Python dengan bantuan pustaka `NumPy` untuk pengelolaan data matriks serta `Matplotlib` untuk memvisualisasikan rute perjalanan bidak kuda. Hasil akhir program berupa papan catur yang berisi urutan langkah bidak kuda serta visualisasi lintasan pergerakan.

---

### **2.2 Algoritma yang Digunakan**

Algoritma utama yang digunakan dalam program ini adalah **algoritma backtracking dengan heuristik Warnsdorff**.

1. **Backtracking**
   Digunakan untuk menelusuri kemungkinan pergerakan bidak kuda secara rekursif. Jika pada suatu langkah tidak ditemukan pergerakan yang valid, algoritma akan kembali ke langkah sebelumnya dan mencoba alternatif gerakan lain.

2. **Heuristik Warnsdorff**
   Untuk meningkatkan efisiensi pencarian, algoritma memilih langkah berikutnya berdasarkan jumlah kemungkinan langkah lanjutan paling sedikit. Petak dengan derajat (*degree*) terkecil diprioritaskan untuk dikunjungi terlebih dahulu.

Pendekatan ini secara signifikan mengurangi kemungkinan terjebak pada kondisi buntu (*dead end*).

---

### **2.3 Cara Kerja Program**

Langkah kerja program secara umum adalah sebagai berikut:

1. Program menginisialisasi papan catur 8 × 8 dengan nilai awal kosong.
2. Posisi awal bidak kuda ditentukan dan ditandai sebagai langkah pertama.
3. Program menghitung seluruh kemungkinan gerakan bidak kuda dari posisi saat ini.
4. Gerakan yang valid dipilih berdasarkan heuristik Warnsdorff, yaitu petak dengan jumlah kemungkinan lanjutan paling sedikit.
5. Setiap petak yang dikunjungi ditandai agar tidak dikunjungi kembali.
6. Proses berlanjut hingga seluruh 64 petak berhasil dikunjungi.
7. Jika tidak ditemukan langkah lanjutan yang valid, algoritma melakukan *backtracking*.
8. Setelah solusi ditemukan, program menampilkan hasil dalam bentuk matriks langkah dan visualisasi lintasan.

---

### **2.4 Open Tour dan Closed Tour**

Program ini mendukung dua jenis solusi:

* **Open Tour**
  Perjalanan bidak kuda dapat berakhir di petak mana saja setelah seluruh papan dikunjungi.

* **Closed Tour**
  Setelah seluruh papan dikunjungi, posisi akhir bidak kuda harus dapat menyerang posisi awal dengan satu langkah kuda.

Untuk *closed tour*, program melakukan pengecekan tambahan pada langkah terakhir untuk memastikan bahwa posisi akhir memiliki hubungan gerak kuda dengan posisi awal.

---

## **BAB III

ANALISIS KEBERHASILAN PROGRAM**

### **3.1 Alasan Algoritma Berhasil**

Algoritma berhasil menyelesaikan permasalahan *The Knight’s Tour* karena beberapa alasan berikut:

1. **Validitas Gerakan Terjamin**
   Setiap langkah bidak kuda selalu diperiksa agar berada di dalam batas papan catur dan belum pernah dikunjungi sebelumnya.

2. **Tidak Ada Pengulangan Petak**
   Setiap petak ditandai setelah dikunjungi sehingga tidak mungkin dikunjungi lebih dari satu kali.

3. **Efisiensi Heuristik Warnsdorff**
   Dengan memilih petak dengan kemungkinan lanjutan paling sedikit, algoritma meminimalkan risiko terjebak pada kondisi buntu.

4. **Backtracking sebagai Mekanisme Pemulihan**
   Jika suatu jalur gagal, algoritma dapat kembali ke langkah sebelumnya dan mencoba jalur lain, sehingga solusi tetap dapat ditemukan.

---

### **3.2 Analisis Kompleksitas**

Secara teori, kompleksitas masalah *The Knight’s Tour* dengan *backtracking* bersifat eksponensial karena banyaknya kemungkinan lintasan. Namun, dengan penerapan heuristik Warnsdorff, kompleksitas praktis dapat ditekan secara signifikan sehingga solusi dapat ditemukan dalam waktu yang relatif singkat untuk papan 8 × 8.

---

### **3.3 Keterbatasan Program**

Beberapa keterbatasan dari program ini antara lain:

1. Heuristik Warnsdorff tidak selalu menjamin solusi untuk semua konfigurasi papan yang lebih besar.
2. Program masih bergantung pada pemilihan posisi awal.
3. Untuk ukuran papan yang lebih besar, waktu eksekusi dapat meningkat.

---

## **BAB IV

KESIMPULAN**

Program *The Knight’s Tour* berhasil diimplementasikan menggunakan algoritma *backtracking* dengan heuristik Warnsdorff. Program mampu menghasilkan rute perjalanan bidak kuda yang mengunjungi seluruh petak papan catur tepat satu kali, baik dalam bentuk *open tour* maupun *closed tour*. Pendekatan heuristik terbukti efektif dalam meningkatkan efisiensi pencarian dan mengurangi kegagalan pencarian solusi.

---

Kalau kamu mau, aku bisa:

* Menyesuaikan bahasa **sesuai gaya laporan ITS 100%**
* Membuat **BAB V (Lampiran Kode)**
* Menambahkan **flowchart algoritma**
* Mengubah ini ke format **DOCX / LaTeX**

Tinggal bilang mau lanjut ke bagian mana 👌

