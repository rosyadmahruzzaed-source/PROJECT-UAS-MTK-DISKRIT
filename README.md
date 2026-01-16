
# NAMA : ZAED ROSYAD MAHRUZ
# NIM : 312510291
# MATA KULIAH : MTK DISKRIT
JENIS PROJECT UAS :Menggambar Pohon Biner dan Spanning Tree
Proyek ini dibuat untuk memenuhi tugas **Ujian Akhir Semester (UAS) Mata Kuliah Matematika Diskrit**.   Program ini  menggunakan bahasa pemrograman **HTML** 
Baik, saya akan menjelaskan secara detail tentang Pohon Biner dan Spanning Tree berdasarkan soal latihan tersebut.
1. POHON BINER (Binary Tree)
Apa itu Pohon Biner?
Pohon biner adalah struktur data hierarkis di mana setiap simpul (node) maksimal memiliki 2 anak (child): anak kiri dan anak kanan.
Komponen Pohon Biner:
<img width="938" height="489" alt="Screenshot 2026-01-16 104339" src="https://github.com/user-attachments/assets/0506a06a-461f-4cc4-89f2-7731bc703d5d" />




Root (Akar): Simpul paling atas (dalam contoh: A)
Parent (Induk): Simpul yang memiliki anak
Child (Anak): Simpul yang berada di bawah parent
Leaf (Daun): Simpul yang tidak memiliki anak (dalam contoh: D, E, F, G)
Edge (Sisi): Garis penghubung antar simpul

Contoh dengan 7 Simpul:
        A (root)
       / \
      B   C
     / \ / \
    D  E F  G (leaves)
Karakteristik:

Jumlah simpul: 7
Jumlah sisi: 6 (selalu n-1 untuk pohon dengan n simpul)
Tinggi: 2 (level 0, 1, 2)
Tidak ada siklus (tidak ada jalur yang kembali ke simpul awal)


2. GRAF (Graph)
Apa itu Graf?
Graf adalah struktur yang terdiri dari simpul-simpul yang dihubungkan oleh sisi, bisa memiliki siklus dan setiap simpul bisa terhubung ke banyak simpul lain.
Graf Berbobot:
Setiap sisi memiliki nilai/bobot yang merepresentasikan jarak, biaya, atau nilai lainnya.
Contoh Graf dalam soal:
<img width="999" height="533" alt="Screenshot 2026-01-16 104635" src="https://github.com/user-attachments/assets/68f7d113-5d3e-4df4-8a90-e4de652d1b08" />


5 simpul: A, B, C, D, E
7 sisi dengan bobot:

A-B: 2
A-C: 3
B-C: 1
B-D: 4
C-D: 2
C-E: 5
D-E: 3




3. SPANNING TREE
Apa itu Spanning Tree?
Spanning tree adalah subgraf dari sebuah graf yang:

Berbentuk pohon (tidak ada siklus)
Menghubungkan semua simpul dalam graf
Memiliki tepat n-1 sisi (n = jumlah simpul)

Contoh Spanning Tree dari graf di atas:
Spanning Tree 1 (Total bobot: 12):
<img width="908" height="682" alt="image" src="https://github.com/user-attachments/assets/b8c36726-1e31-4c93-a099-d8227c0b8ede" />


A-B: 2
A-C: 3
B-D: 4
D-E: 3
Total: 2+3+4+3 = 12

Spanning Tree 2 (bisa ada banyak kemungkinan):

A-B: 2
B-C: 1
C-D: 2
C-E: 5
Total: 2+1+2+5 = 10


4. MINIMUM SPANNING TREE (MST)
Apa itu MST?
MST adalah spanning tree dengan total bobot paling kecil di antara semua kemungkinan spanning tree.
Algoritma untuk Menemukan MST:
<img width="892" height="670" alt="image" src="https://github.com/user-attachments/assets/e01b1b1e-d10c-46eb-93e2-64605218005d" />


A. Algoritma Kruskal:

Urutkan semua sisi berdasarkan bobot (dari kecil ke besar)
Pilih sisi dengan bobot terkecil yang tidak membentuk siklus
Ulangi sampai semua simpul terhubung

Langkah-langkah untuk contoh:

Urutkan sisi: B-C(1), A-B(2), C-D(2), A-C(3), D-E(3), B-D(4), C-E(5)
Pilih B-C: 1 ✓
Pilih A-B: 2 ✓
Pilih C-D: 2 ✓
Pilih D-E: 3 ✓
Selesai (4 sisi untuk 5 simpul)

MST: B-C, A-B, C-D, D-E
Total bobot minimum: 1+2+2+3 = 8
B. Algoritma Prim:

Mulai dari simpul acak
Pilih sisi terkecil yang menghubungkan simpul yang sudah terpilih dengan yang belum
Ulangi sampai semua simpul terhubung


5. PERBEDAAN SPANNING TREE vs MINIMUM SPANNING TREE
AspekSpanning TreeMinimum Spanning TreeDefinisiPohon yang menghubungkan semua simpulSpanning tree dengan bobot total terkecilJumlahBisa banyak kemungkinanBisa lebih dari satu, tapi dengan bobot yang samaBobotBervariasiPaling minimumContohTotal: 12Total: 8 (paling kecil)

6. PENERAPAN DALAM KEHIDUPAN NYATA
Spanning Tree digunakan untuk:

Jaringan komputer: Mencegah broadcast storm
Perencanaan jalan: Menghubungkan semua kota
Jaringan listrik: Distribusi listrik ke semua rumah

MST digunakan untuk:

Jaringan kabel: Meminimalkan panjang kabel untuk menghubungkan semua komputer
Perencanaan transportasi: Rute termurah untuk menghubungkan semua lokasi
Desain sirkuit: Mengurangi biaya koneksi elektronik


7. KESIMPULAN
Berdasarkan soal nomor 9:

"Pohon biner dan spanning tree merupakan dua konsep penting dalam matematika diskrit yang berkaitan erat dengan graf dan struktur data."

Poin penting:

Pohon Biner = Struktur hierarkis dengan maksimal 2 anak per simpul
Spanning Tree = Pohon yang menghubungkan semua simpul dalam graf tanpa siklus
MST = Spanning tree dengan total bobot minimum
Memahami kedua konsep ini penting untuk algoritma dan aplikasi praktis dalam ilmu komputer
hasil program yang saya kerjakan 
<img width="1089" height="229" alt="Screenshot 2026-01-16 105130" src="https://github.com/user-attachments/assets/0fb286ea-4d7e-4f00-899d-878f13c57e17" />


