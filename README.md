# EAS PBO Text Based RPG Game

Game RPG sederhana berbasis teks yang dibangun menggunakan Python tanpa library atau engine eksternal. Proyek ini dibuat sebagai studi kasus penerapan logika pemrograman terstruktur untuk tugas Pemrograman Berorientasi Objek (PBO).

## Fitur

- **Status pemain** melihat HP, attack, gold, dan statistik karakter lainnya
- **Pertarungan (combat)** — sistem battle dengan damage acak, mekanisme dodge/miss, serta efek khusus tiap musuh saat HP rendah (panic, enrage, self-heal, racun bertahap)
- **Inventory** — menyimpan dan menggunakan item, termasuk potion untuk memulihkan HP
- **Toko** — membeli upgrade (max HP, attack, potion) dan menjual item hasil drop musuh

## Struktur Proyek
```
EAS_PBO/
main.py        # Menu utama dan alur program
player.py      # Data dan status pemain
enemy.py       # Basis data musuh beserta efek HP rendah
combat.py      # Logika pertarungan
inventory.py   # Pengelolaan item dan potion
toko.py        # Sistem jual beli
```
## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan dari direktori proyek:

```bash
python main.py
```

Ikuti instruksi pada menu untuk memilih Status, Inventory, Battle, Toko, atau Keluar.

## Catatan Pengembangan

Struktur kode saat ini masih bersifat prosedural — data pemain dan musuh disimpan sebagai dictionary global, bukan sebagai object dari class. Untuk pengembangan lanjutan, beberapa hal yang direncanakan:

- Refactor `player.py` dan `enemy.py` menjadi class (`Player`, `Enemy`, dengan subclass per jenis musuh)
- Perbaikan bug validasi input pada `toko.py`
- Penambahan jalur upgrade untuk atribut `dodge`

## Lisensi

Proyek ini dibuat untuk keperluan tugas akademik.
