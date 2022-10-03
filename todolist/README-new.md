# Penjelasan Tugas 4 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/todolist/login/).

## Jawaban dari Pertanyaan
### Perbedaan Inline, Internal, dan External CSS
Inline CSS adalah metode penulisan CSS pada atribut `style` elemen HTML yang bersangkutan. Internal CSS adalah metode penulisan CSS pada *tag* `style` di halaman HTML yang bersangkutan. *Tag* ini biasanya ditempatkan di bagian *header* dari *file* HTML yang bersangkutan. Sedangkan, external CSS adalah metode penulisan CSS pada file berekstensi `.css` yang terpisah dengan halaman HTML.<br>
Berikut adalah kelebihan dan kekurangannya masing-masing.
1. Inline CSS memiliki kelebihan berupa mempercepat *load website* dan memperkecil *HTTP Request*, serta bermanfaat jika kita hanya akan menguji perubahan pada tampilan HTML untuk elemen tertentu saja. Sedangkan, kelemahannya adalah kurang efisien dikarenakan kode CSS yang dimasukkan hanya berlaku pada elemen HTML tersebut saja.
2. Internal CSS memiliki kelebihan berupa tidak perlu melakukan *import file* dari luar *file* HTML, sudah bisa memanfaatkan *selector* untuk `class` dan `ID`, serta bermanfaat jika perubahan yang diinginkan hanya pada satu halaman HTML tertentu saja. Sedangkan, kelemahannya adalah akan memperlambat *load website* karena CSS yang berbeda akan perlu di-*load* ulang tiap kali mengganti halaman web, serta membuat ukuran *file* HTML menjadi lebih besar.
3. External CSS memiliki kelebihan dapat membuat *file* HTML menjadi lebih kecil, proses *load website* menjadi lebih cepat, dan satu *file* CSS tersebut dapat dimanfaatkan untuk beberapa halaman sekaligus. Sedangkan, kelemahannya adalah tidak cocok untuk halaman web yang membutuhkan halaman yang berbeda-beda antara satu dengan yang lainnya (*custom*), serta halaman web akan menjadi berantakan jika halaman HTML-nya berhasil ditampilkan tetapi CSS-nya gagal saat di-*load*.

### Tag HTML5 yang Diketahui
Berikut adalah *tag* HTML5 yang saya ketahui:
1. `<a>` untuk menambahkan *hyperlink*
2. `<b>` untuk mempertebal teks (*bold*)
3. `<body>` untuk mendefinisikan *body* dari halaman HTML
4. `<br>` untuk menambahkan *line break* (baris baru)
5. `<button>` untuk menambahkan tombol
6. `<caption>` untuk mendefinisikan *caption* dari suatu *table*
7. `<div>` untuk mendefinisikan suatu *division* atau bagian tertentu dalam suatu halaman HTML
8. `<form>` untuk mendefinisikan suatu *form* untuk mengambil input dari *user*
9. `<head>` untuk mendefinisikan bagian *head* dari suatu halaman HTML, yang berisi informasi terkait halaman HTML tersebut
10. `<h1>` sampai `<h6>` untuk membuat suatu *heading*
11. `<html>` mendefinisikan *root* dari sebuah halaman HTML
12. `<i>` untuk memiringkan teks (*italic*)
13. `<img>` untuk menambahkan gambar
14. `<input>` untuk mendefinisikan *input field* yang akan diisi oleh *user*
15. `<li>` untuk mendefinisikan tiap-tiap elemen dari suatu list *unordered* (`<ul>`) atau *ordered* (`<ol>`)
16. `<nav>` untuk mendefinisikan suatu bagian yang terdiri dari *navigation links*
17. `<p>` untuk mendefinisikan suatu teks paragraf
18. `<script>` sebagai tempat meletakkan *script* yang diperlukan
19. `<span>` untuk mendefinisikan bagian pada suatu teks menjadi *inline* dan *styless*
20. `<style>` sebagai tempat untuk mendefinisikan internal CSS dalam suatu halaman HTML
21. `<table>` untuk mendefinisikan tabel
22. `<td>` untuk mendefinisikan sebuah cell pada tabel
23. `<textarea>` untuk mendefinisikan *input field* untuk *text* yang bersifat *multiline*
24. `<th>` untuk mendefinisikan *header* tabel
25. `<title>` untuk mendefinisikan judul dokumen HTML
26. `<tr>` untuk mendefinisikan suatu baris pada tabel

### Tipe Selector CSS yang Diketahui
Berikut adalah tipe *selector* CSS yang saya ketahui:
1. Element selector, yakni *selector* yang langsung memanfaatkan *tag* HTML sebagai *selector*-nya. Untuk sintaks pada CSS-nya, langsung memanfaatkan nama dari *tag* tersebut, seperti `h1{...}`.
2. ID selector, yakni *selector* yang menggunakan ID yang sudah didefinisikan pada *tag* sebagai *selector*-nya. Untuk sintaks pada CSS-nya, memanfaatkan nama ID pada *tag* tersebut, tetapi ditambahkan `#` di awal, seperti untuk `id="nama"`, di CSS akan ditulis `#nama{...}`.
3. Class selector, yakni *selector* yang menggunakan class yang sudah didefinisikan pada *tag* sebagai *selector*-nya. Untuk sintaks pada CSS-nya, memanfaatkan nama class pada *tag* tersebut, tetapi ditambahkan `.` di awal, seperti untuk `class="nama"`, di CSS akan ditulis `.nama{...}`.

### Tahap-Tahap Implementasi Checklist
Tahapan yang saya lakukan dalam mengimplementasikan checklist:
1. Pertama-tama, saya menyediakan *static files* yang diperlukan dalam mengerjakan tugas ini, dalam hal ini adalah file CSS untuk page `login`, yaitu `login.css` dan untuk page `todolist` yaitu `todolist.css`. Selanjutnya, saya menjalankan perintah `collectstatic` untuk mengumpulkan semua *static files*.
2. Selanjutnya, saya menambahkan potongan kode untuk menjalankan Bootstrap di tiap *file* HTML yang akan saya kustomisasi. Potongan kode tersebut adalah `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` dan `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>`. Tidak lupa juga saya menambahkan `{% load static %}` dan direktori *static file* dalam atribut `href` *tag* `link` jika ada *static file* yang ingin saya masukkan ke dalam *file* HTML yang akan dikustomisasi tersebut.
3. Setelah itu, saya mulai melakukan kustomisasi untuk *file* `login.html`. Saya ingin membuat *login page* yang memanfaatkan *card* dengan *background gradient* agar terlihat menarik. Adapun pengaturan untuk *gradient* tersebut saya masukkan ke file `CSS` terpisah pada *selector* `body`. Selain itu, saya juga memanfaatkan *class selector* untuk melakukan kustomisasi teks pada class `title` dan `label-input`. Sementara itu, untuk *form*, saya menggunakan *floating label* pada *input field* agar terlihat menarik. Saya juga melakukan kustomisasi untuk *padding* dan *margin* pada elemen-elemen tersebut agar rapi.
4. Lalu, saya melakukan kustomisasi untuk *file* `todolist.html`. Saya menambahkan `navbar` pada bagian atas dari halaman yang berisi nama aplikasi, nama *user* yang *logged in*, tombol untuk menambahkan *task* baru, dan tombol untuk *logout*. Saya memanfaatkan `button` bawaan dari Bootstrap untuk itu. Selanjutnya, saya mengganti metode penampilan task dari bentuk *tabel* ke bentuk *card* agar terlihat lebih menarik. Di dalam tiap *card*, akan ada informasi terkait nama *task* yang menjadi `card-title`, deskripsi task dan tanggal pembuatan *task* yang menjadi `card-text`, informasi terkait status dari *task* apakah sudah selesai atau tidak yang ditampilkan dalam bentuk `badge` di samping nama *task*, serta dua tombol di bawah informasi tanggal pembuatan *task* yang berfungsi untuk mengubah status dari *task* dan menghapus *task*. Saya juga melakukan kustomisasi *message* yang ditampilkan dengan memanfaatkan `alert-dismissible` dari Bootstrap. Lalu, untuk mengerjakan *bonus task*, saya menambahkan `:hover` pada `todolist.css` untuk *class card* dengan mengubah `background-color` dari *card* tersebut. Saya juga menggunakan *conditionals* dari *template tags* Django untuk menampilkan teks 'No Task' jika belum ada *task* yang dibuat.
5. Selanjutnya, saya melakukan kustomisasi untuk *file* `new_task.html`. Saya tetap menggunakan `navbar` yang telah saya buat di *page* `todolist`, hanya saja saya menghilangkan tombol untuk menambah *task* baru. Setelah itu, saya merapikan halaman ini dengan menambahkan *margin* dan *padding* pada *input field* serta menambahkan dua `button` di bawah untuk *save task* dan *discard task* memanfaatkan `button` dari Bootstrap.
6. Terakhir, untuk halaman `register.html`, saya memanfaatkan kembali *card* yang telah saya buat sebelumnya pada halaman `login`, tetapi dengan mengubah isinya. Saya masih memanfaatkan `{{form.as_table}}` untuk membuat *input field* yang dibutuhkan, akan tetapi saya melakukan kustomisasi menggunakan Bootstrap dengan menghilangkan *border* dari *table* dan membuat tabel menjadi *responsive* dengan memanfaatkan *class* `table-responsive`.
7. Selanjutnya, saya melakukan `add`, `commit`, dan `push` ke GitHub, lalu melakukan *re-run jobs* agar perubahan yang telah saya buat ter-*deploy*.

### Referensi
https://mdbootstrap.com/docs/standard/extended/login/<br>
https://getbootstrap.com/<br>
https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/<br>
https://qwords.com/blog/perbedaan-internal-external-dan-inline-css/<br>
https://www.tutorialrepublic.com/html-reference/html5-tags.php