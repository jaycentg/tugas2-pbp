# Penjelasan Tugas 2 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/katalog/).

## Jawaban dari Pertanyaan
### Bagan *Request Client*
![bagan](https://user-images.githubusercontent.com/88029772/189681692-6527e06e-05f8-490f-86f6-c6c076742bd2.png)
Penjelasan terkait bagan tersebut adalah sebagai berikut.
1. Client akan melakukan *request*.
2. *Request* yang masuk akan diproses pada `urls.py` berdasarkan *routes* yang ada di `urlpatterns`.
3. *Request* lalu diproses pada `views.py` oleh fungsi-fungsi yang terkait.
4. Jika perlu untuk mengakses *database*, `views.py` ini akan memanggil *query* ke `models.py` yang terhubung dengan *database*.
5. *Database* akan memberikan respons data yang merupakan hasil pemanggilan *query* ke `views.py`.
6. Respons data yang sudah didapatkan kemudian dipetakan ke berkas HTML yang sesuai untuk kemudian siap dilakukan *render*.
7. Berkas HTML ditampilkan sebagai respons.
