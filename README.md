# 📘 Perkalian Matriks 5x5 di Python

Program ini melakukan **perkalian dua matriks 5x5** Matriks dikalikan menggunakan perulangan `for` dan disimpan menggunakan `append`.

---

## 🧮 Matriks Input

### Matriks A:

```
|  1   2   3   4   5   |
|  6   7    8   9  10  |
|  11  12  13  14  15  |
|  16  17  18  19  20  |
|  21  22  23  24  25  |
```

### Matriks B:

```
| 1   0   0   0   1 |
| 0   1   0   1   0 |
| 0   0   1   0   0 |
| 0   1   0   1   0 |
| 1   0   0   0   1 |
```

---

## 🔧 Cara Kerja Kode

### Inisialisasi Matrix

```python
hasil = []
```

### Penjelasan:

- Melakukan Inisalisasi untuk hasil dari matrix

---

### Perhitungan Kali Dalam Matrix

```python
hasil = []  # Matriks hasil kosong

for i in range(5):         # Untuk setiap baris di A
    baris = []
    for j in range(5):     # Untuk setiap kolom di B
        total = 0
        for k in range(5): # Perkalian elemen baris A dengan kolom B
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)
```

### Penjelasan:

- Mengambil **baris ke-i dari A** dan **kolom ke-j dari B**.
- Mengalikan elemen yang bersesuaian lalu menjumlahkannya.
- Hasilnya adalah elemen `[i][j]` pada matriks `hasil`.

---

### Menampilkan Hasil

```python
print("Hasil perkalian matriks A x B:")
for row in hasil:
    print(row)
```

### Penjelasan:

- Menampilkan Output dari hasil perkalin matrix

---

## ✅ Contoh Perhitungan Elemen `hasil[0][0]`

Baris pertama A: `[1, 2, 3, 4, 5]`  
Kolom pertama B: `[1, 0, 0, 0, 1]`

```
= 1×1 + 2×0 + 3×0 + 4×0 + 5×1
= 1 + 0 + 0 + 0 + 5
= 6
```

---

## 📊 Matriks Hasil

Hasil dari `A x B` adalah:

```
[6, 6, 9, 6, 6]
[16, 16, 24, 16, 16]
[26, 26, 39, 26, 26]
[36, 36, 54, 36, 36]
[46, 46, 69, 46, 46]
```

---

## 🔍 Ringkasan

- Tidak menggunakan library eksternal seperti `numpy`.
- Operasi dilakukan sepenuhnya dengan nested loops dan list native Python.
- Cocok untuk pembelajaran dasar matriks dan algoritma perkalian manual.
