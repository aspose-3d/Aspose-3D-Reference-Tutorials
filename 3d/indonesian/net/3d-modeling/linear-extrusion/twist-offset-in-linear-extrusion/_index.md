---
date: 2026-03-23
description: Pelajari cara menambahkan putaran pada ekstrusi linear dengan Aspose.3D
  untuk .NET dan temukan cara menggunakan ekstrusi untuk proyek pemodelan 3D asp.net.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Cara Menambahkan Twist pada Ekstrusi Linear menggunakan Aspose.3D untuk .NET
url: /id/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menambahkan Twist pada Linear Extrusion menggunakan Aspose.3D untuk .NET

## Pendahuluan

Jika Anda mencari panduan langkah‑demi‑langkah yang jelas tentang **cara menambahkan twist** pada linear extrusion, Anda berada di tempat yang tepat. Pada tutorial ini kami akan menjelaskan seluruh proses dengan Aspose.3D untuk .NET, menunjukkan **cara menggunakan extrusion** untuk membuat bentuk 3D dinamis yang sempurna untuk skenario *asp.net 3d modeling*. Pada akhir tutorial Anda akan memiliki contoh yang siap dijalankan yang memperlihatkan twist offset, slices, dan menyimpan hasilnya sebagai file OBJ.

## Jawaban Cepat
- **Apa fungsi “twist offset”?** Itu menggeser titik awal twist sepanjang sumbu extrusion.  
- **Apakah saya memerlukan lisensi untuk menjalankan contoh?** Lisensi sementara cukup untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Versi .NET apa yang didukung?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Bisakah saya mengubah jumlah slices?** Ya—sesuaikan properti `Slices` untuk mengontrol kehalusan mesh.  
- **Apakah format output terbatas pada OBJ?** Tidak, Aspose.3D mendukung banyak format; OBJ dipilih di sini untuk kesederhanaan.

## Apa Itu Twist Offset pada Linear Extrusion?

Twist offset mendefinisikan pergeseran translasi yang diterapkan pada operasi twist. Alih‑alih memutar tepat di awal extrusion, geometri mulai berputar dari vektor offset yang ditentukan, memberi Anda kontrol artistik lebih besar atas bentuk akhir.

## Mengapa Menggunakan Aspose.3D untuk .NET?

- **API lengkap** – Menangani profil, transformasi, dan beragam format file.  
- **Lintas‑platform** – Berfungsi di Windows, Linux, dan macOS dengan .NET Core.  
- **Dioptimalkan untuk performa** – Menghasilkan mesh bersih tanpa perhitungan manual.  
- **Dokumentasi yang luar biasa** – Banyak contoh untuk mempercepat pengembangan.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Perpustakaan Aspose.3D untuk .NET: Unduh dan instal perpustakaan dari [halaman rilis](https://releases.aspose.com/3d/net/).  
- Lingkungan Pengembangan Anda: Visual Studio, Rider, atau IDE apa pun yang mendukung C#.

## Impor Namespace

Pertama, impor namespace yang memberi Anda akses ke kelas‑kelas 3D inti.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Pernyataan‑pernyataan ini membuat `Scene`, `LinearExtrusion`, `Vector3`, dan tipe penting lainnya tersedia dalam kode Anda.

## Panduan Langkah‑demi‑Langkah

### Langkah 1: Inisialisasi Profil Dasar

Kami memulai dengan profil persegi panjang sederhana dan memberikan radius pembulatan kecil sehingga tepinya tidak terlalu tajam.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Langkah 2: Buat Scene

`Scene` berfungsi sebagai wadah untuk semua node, lampu, kamera, dan geometri.

```csharp
Scene scene = new Scene();
```

### Langkah 3: Buat Node

Dua node anak ditambahkan ke root scene—satu untuk extrusion biasa dan satu untuk versi twisted. Node kiri digeser pada sumbu X untuk pemisahan visual.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Langkah 4: Linear Extrusion pada Node Kiri (Tanpa Twist Offset)

Di sini kami memperlihatkan extrusion dasar dengan twist penuh 360° dan 100 slices untuk kehalusan.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Langkah 5: Linear Extrusion pada Node Kanan dengan Twist Offset

Sekarang kami menerapkan twist offset `(3, 0, 0)`. Ini memindahkan awal twist tiga satuan sepanjang sumbu X, menghasilkan heliks yang bergeser secara visual.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Langkah 6: Simpan Scene 3D

Akhirnya, kami menulis scene ke file OBJ. Ubah jalur output sesuai kebutuhan lingkungan Anda.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **Twist terlihat datar** | `Slices` diatur terlalu rendah, menghasilkan mesh kasar. | Tingkatkan `Slices` (misalnya, 200) untuk rotasi yang lebih halus. |
| **Objek tidak berada di tengah** | `TwistOffset` menggunakan koordinat dunia; node mungkin sudah dipindahkan. | Terapkan offset relatif terhadap transformasi lokal node atau sesuaikan translasi node sesuai kebutuhan. |
| **File tidak tersimpan** | Jalur output salah atau izin menulis tidak ada. | Pastikan direktori ada dan aplikasi memiliki akses menulis. |
| **Pengecualian lisensi** | Menjalankan tanpa lisensi yang valid pada build non‑trial. | Muat lisensi sementara atau permanen sebelum membuat scene. |

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung bahasa .NET, tetapi Aspose menyediakan perpustakaan serupa untuk Java dan platform lainnya.

### Q2: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk .NET?

A2: Kunjungi [tautan ini](https://purchase.aspose.com/temporary-license/) untuk memperoleh lisensi sementara untuk keperluan pengujian.

### Q3: Apakah ada forum komunitas untuk Aspose.3D untuk .NET?

A3: Tentu! Bergabunglah dengan komunitas di [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) untuk berinteraksi dengan pengembang lain dan meminta bantuan.

### Q4: Apakah ada contoh dan dokumentasi tambahan yang tersedia?

A4: Jelajahi [dokumentasi](https://reference.aspose.com/3d/net/) untuk panduan dan contoh yang lengkap.

### Q5: Di mana saya dapat membeli Aspose.3D untuk .NET?

A5: Kunjungi [tautan ini](https://purchase.aspose.com/buy) untuk melakukan pembelian dan membuka potensi penuh Aspose.3D.

### Q6: Bisakah saya mengekspor model ke format selain OBJ?

A6: Ya—Aspose.3D mendukung FBX, STL, 3MF, dan banyak lagi. Cukup ubah nilai enum `FileFormat` pada pemanggilan `Save`.

### Q7: Bagaimana “cara menambahkan twist” berbeda dari rotasi biasa?

A7: Twist memutar profil secara bertahap sepanjang panjang extrusion, sedangkan rotasi biasa menerapkan sudut statis tunggal. Offset menambahkan pergeseran translasi sebelum rotasi dimulai.

---

**Terakhir Diperbarui:** 2026-03-23  
**Diuji Dengan:** Aspose.3D untuk .NET (rilis terbaru)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}