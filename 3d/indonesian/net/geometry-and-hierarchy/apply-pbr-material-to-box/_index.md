---
date: 2026-04-12
description: Pelajari cara menerapkan material PBR pada sebuah kotak menggunakan Aspose.3D
  untuk .NET, membuat material PBR, dan mengekspor file STL ASCII dengan rendering
  berbasis fisika.
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: Menerapkan Material PBR pada Kotak
second_title: Aspose.3D .NET API
title: Cara Menerapkan Material PBR pada Kotak
url: /id/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menerapkan Material PBR ke Kotak

## Pendahuluan

Selamat datang di dunia grafis 3D yang memukau! Dalam tutorial langkah‑demi‑langkah ini, **Anda akan belajar cara menerapkan material pbr** pada sebuah kotak menggunakan Aspose.3D for .NET. Kami akan membahas cara membuat material PBR, menambahkannya ke mesh, dan akhirnya **mengekspor STL ASCII** sehingga Anda dapat menggunakan model tersebut dalam alur kerja selanjutnya. Baik Anda sedang membangun prototipe game, visualisasi produk, atau prototipe cepat untuk pencetakan 3D, menguasai alur kerja ini membuka pintu ke rendering berbasis fisika (PBR) yang realistis dalam aplikasi .NET Anda.

## Jawaban Cepat
- **Apa tujuan utama?** Menerapkan material PBR ke sebuah kotak dan mengekspornya sebagai STL ASCII.  
- **Perpustakaan mana yang digunakan?** Aspose.3D for .NET (cara menggunakan aspose).  
- **Apakah saya memerlukan lisensi?** Ya, lisensi sementara atau penuh diperlukan untuk produksi.  
- **Format output yang didukung?** STL ASCII (export stl ascii) dan banyak format 3D lainnya.  
- **Berapa lama waktu yang dibutuhkan?** Sekitar 10‑15 menit untuk implementasi dasar.

## Apa itu Material PBR?
Physically Based Rendering (PBR) adalah model shading yang mensimulasikan bagaimana cahaya berinteraksi dengan permukaan dunia nyata. Dengan menyesuaikan properti seperti faktor metallic dan roughness, Anda dapat mencapai hasil yang sangat realistis tanpa harus mengatur shader yang kompleks secara manual.

## Mengapa Menggunakan Physically Based Rendering (PBR)?
- **Realisme:** Material bereaksi terhadap pencahayaan dengan cara yang sesuai dengan fisika nyata.  
- **Konsistensi:** Material yang sama terlihat tepat di lingkungan pencahayaan apa pun.  
- **Efisiensi:** GPU modern dioptimalkan untuk perhitungan PBR, memberikan kinerja gratis.

## Prasyarat

Sebelum kita masuk ke kode, pastikan Anda memiliki hal berikut:

### Unduh dan Instal Aspose.3D for .NET
Kunjungi [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) untuk petunjuk detail tentang mengunduh dan menginstal perpustakaan.

### Dapatkan Lisensi
Untuk membuka potensi penuh Aspose.3D, dapatkan lisensi yang valid. Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) atau membeli lisensi penuh [di sini](https://purchase.aspose.com/buy).

## Impor Namespace
Pertama, pastikan untuk mengimpor namespace yang diperlukan guna memanfaatkan kemampuan Aspose.3D for .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Panduan Langkah‑demi‑Langkah

### Langkah 1: Inisialisasi Scene
Mulailah dengan membuat scene 3D kosong. Kontainer ini akan menampung semua geometri, material, dan cahaya yang akan Anda tambahkan nanti.

```csharp
Scene scene = new Scene();
```

### Langkah 2: Buat Material PBR
Sekarang kita **membuat material pbr** yang akan memberikan tampilan realistis pada kotak kita. Kelas `PbrMaterial` menyediakan semua parameter yang Anda perlukan untuk physically based rendering.

```csharp
PbrMaterial mat = new PbrMaterial();
```

### Langkah 3: Atur Properti Material
Sesuaikan properti material secara detail. Pada contoh ini kami membuat permukaan hampir metallic dan sangat kasar—sempurna untuk kotak berlapis logam sikat.

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### Langkah 4: Buat Mesh Kotak
Hasilkan geometri kotak sederhana. Ini adalah langkah **create box mesh** yang menjadi referensi kata kunci utama.

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### Langkah 5: Terapkan Material PBR ke Kotak
Tetapkan **add pbr material** yang telah dikonfigurasi sebelumnya ke node kotak yang baru saja kami buat.

```csharp
boxNode.Material = mat;
```

### Langkah 6: Ekspor STL ASCII (Cara Mengekspor STL)
Akhirnya, **export stl ascii** sehingga model dapat dibuka di viewer 3D standar atau slicer apa pun. Menggunakan `FileFormat.STLASCII` menjamin file yang dapat dibaca manusia.

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## Kesalahan Umum & Tips
- **Lisensi tidak ditemukan:** Pastikan file lisensi dimuat *sebelum* panggilan Aspose apa pun; jika tidak, perpustakaan akan berjalan dalam mode evaluasi.  
- **Path file tidak tepat:** Gunakan `Path.Combine` untuk menghindari kehilangan pemisah path pada sistem operasi yang berbeda.  
- **Keseimbangan Roughness vs. Metallic:** Menetapkan kedua faktor terlalu tinggi dapat membuat permukaan tampak datar; bereksperimenlah dengan nilai antara `0.5‑0.9` untuk tampilan seimbang.  
- **Tip kinerja:** Gunakan kembali satu instance `PbrMaterial` jika Anda perlu menerapkan material yang sama ke beberapa mesh; ini mengurangi beban memori.

## Pertanyaan yang Sering Diajukan

**Q1: Apakah Aspose.3D kompatibel dengan format file 3D lainnya?**  
A1: Ya, Aspose.3D mendukung berbagai format file 3D, memastikan fleksibilitas dalam proyek Anda.

**Q2: Dapatkah saya menggunakan Aspose.3D untuk aplikasi komersial?**  
A2: Tentu saja! Aspose.3D menyediakan lisensi komersial untuk integrasi mulus ke dalam perangkat lunak produksi.

**Q3: Apakah ada versi percobaan yang tersedia?**  
A3: Ya, Anda dapat menjelajahi kemampuan Aspose.3D dengan mengunduh trial gratis [di sini](https://releases.aspose.com/).

**Q4: Di mana saya dapat menemukan dukungan komunitas dan diskusi?**  
A4: Bergabunglah dengan komunitas Aspose.3D di [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

**Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A5: Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.

## Kesimpulan
Menjelajahi grafis 3D dengan Aspose.3D for .NET membuka pintu ke kemungkinan kreatif yang tak terbatas. Dengan API yang intuitif dan fitur yang kuat, membuat adegan visual yang menakjubkan menjadi pengalaman yang menyenangkan bagi pengembang. Sekarang Anda telah mengetahui **cara menerapkan pbr** material ke sebuah kotak dan **mengekspor STL ASCII**, cobalah mengganti kotak dengan mesh yang lebih kompleks atau bereksperimen dengan peta tekstur untuk melihat bagaimana cahaya bereaksi secara real time.

---

**Terakhir Diperbarui:** 2026-04-12  
**Diuji Dengan:** Aspose.3D 24.11 for .NET  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}