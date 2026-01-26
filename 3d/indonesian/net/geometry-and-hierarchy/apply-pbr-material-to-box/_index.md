---
date: 2026-01-17
description: Pelajari cara menerapkan material PBR pada kotak menggunakan Aspose.3D
  untuk .NET, buat material PBR, dan ekspor file STL ASCII dengan rendering berbasis
  fisika.
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: Cara Menerapkan Material PBR pada Kotak
url: /id/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menerapkan Material PBR pada Kotak

## Pendahuluan

Selamat datang di dunia grafis 3D yang menakjubkan! Dalam panduan langkah demi langkah ini, Anda akan belajar **cara menerapkan material pbr** pada sebuah kotak menggunakan Aspose.3D untuk .NET. Kami akan memandu Anda membuat material PBR, menambahkannya ke mesh, dan akhirnya **mengekspor STL ASCII** sehingga Anda dapat menggunakan model tersebut dalam alur kerja apa pun. Baik Anda sedang membangun prototipe game atau visualisasi produk, menguasai alur kerja ini membuka pintu ke rendering berbasis fisika (PBR) yang realistis dalam aplikasi .NET Anda.

## Jawaban Cepat
- **Apa tujuan utama?** Menerapkan material PBR pada kotak dan mengekspornya sebagai STL ASCII.  
- **Perpustakaan apa yang digunakan?** Aspose.3D untuk .NET (how to use aspose).  
- **Apakah saya memerlukan lisensi?** Ya, lisensi sementara atau penuh diperlukan untuk produksi.  
- **Format output yang didukung?** STL ASCII (export stl ascii) dan banyak format 3D lainnya.  
- **Berapa lama waktu yang dibutuhkan?** Sekitar 10‑15 menit untuk implementasi dasar.

## Apa Itu Material PBR?
Physically Based Rendering (PBR) adalah model shading yang mensimulasikan bagaimana cahaya berinteraksi dengan permukaan dunia nyata. Dengan menyesuaikan properti seperti faktor metallic dan roughness, Anda dapat mencapai hasil yang sangat realistis tanpa harus men-tuning shader yang kompleks secara manual.

## Mengapa Menggunakan Physically Based Rendering (PBR)?
- **Realisme:** Material bereaksi terhadap pencahayaan dengan cara yang sesuai dengan fisika nyata.  
- **Konsistensi:** Material yang sama terlihat tepat di lingkungan pencahayaan apa pun.  
- **Efisiensi:** GPU modern dioptimalkan untuk perhitungan PBR, memberikan kinerja ekstra tanpa usaha tambahan.

## Prasyarat

Sebelum kita masuk ke kode, pastikan Anda memiliki hal‑hal berikut:

### Unduh dan Instal Aspose.3D untuk .NET
Kunjungi [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) untuk petunjuk detail tentang cara mengunduh dan menginstal perpustakaan.

### Dapatkan Lisensi
Untuk membuka potensi penuh Aspose.3D, dapatkan lisensi yang valid. Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) atau membeli lisensi penuh [di sini](https://purchase.aspose.com/buy).

## Impor Namespace
Pertama, pastikan untuk mengimpor namespace yang diperlukan agar dapat memanfaatkan kemampuan Aspose.3D untuk .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Langkah 1: Inisialisasi Scene
Mulailah dengan menginisialisasi scene 3D menggunakan cuplikan kode berikut:

```csharp
Scene scene = new Scene();
```

## Langkah 2: Buat Material PBR
Sekarang kita **create pbr material** yang akan memberikan tampilan realistis pada kotak kita:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Langkah 3: Atur Properti Material
Sesuaikan properti material, menjadikannya hampir metallic dan sangat kasar—sempurna untuk kotak bertekstur logam sikat:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Langkah 4: Buat Kotak
Hasilkan kotak yang akan diberi material PBR:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Langkah 5: Tambahkan Material PBR ke Kotak
Tetapkan **add pbr material** yang telah dikonfigurasi sebelumnya ke node kotak yang dibuat:

```csharp
boxNode.Material = mat;
```

## Langkah 6: Simpan Scene 3D sebagai STL ASCII
Akhirnya, **export stl ascii** sehingga model dapat dibuka di viewer 3D standar atau slicer apa pun:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Selamat! Anda telah berhasil menerapkan material PBR pada kotak dalam scene 3D menggunakan Aspose.3D untuk .NET.

## Kesalahan Umum & Tips
- **Lisensi tidak ditemukan:** Pastikan file lisensi dimuat sebelum panggilan Aspose apa pun; jika tidak, perpustakaan akan berjalan dalam mode evaluasi.  
- **Path file salah:** Gunakan `Path.Combine` untuk menghindari kehilangan pemisah path pada OS yang berbeda.  
- **Roughness vs. Metallic:** Menetapkan kedua faktor terlalu tinggi dapat membuat permukaan tampak datar; coba nilai antara 0.5‑0.9 untuk tampilan yang seimbang.

## Kesimpulan
Menyelami grafis 3D dengan Aspose.3D untuk .NET membuka pintu ke kemungkinan kreatif yang tak terbatas. Dengan API yang intuitif dan fitur yang kuat, menciptakan scene yang memukau secara visual menjadi pengalaman yang menyenangkan bagi pengembang. Selanjutnya, coba ganti kotak dengan mesh yang lebih kompleks atau bereksperimen dengan tekstur PBR yang berbeda untuk melihat bagaimana cahaya bereaksi.

## Pertanyaan yang Sering Diajukan

**Q1: Apakah Aspose.3D kompatibel dengan format file 3D lainnya?**  
A1: Ya, Aspose.3D mendukung berbagai format file 3D, memastikan fleksibilitas dalam proyek Anda.

**Q2: Bisakah saya menggunakan Aspose.3D untuk aplikasi komersial?**  
A2: Tentu! Aspose.3D menyediakan lisensi komersial untuk integrasi mulus ke dalam aplikasi Anda.

**Q3: Apakah ada versi percobaan yang tersedia?**  
A3: Ya, Anda dapat menjelajahi kemampuan Aspose.3D dengan mengunduh trial gratis [di sini](https://releases.aspose.com/).

**Q4: Di mana saya dapat menemukan dukungan komunitas dan diskusi?**  
A4: Bergabunglah dengan komunitas Aspose.3D di [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

**Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A5: Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) untuk keperluan evaluasi.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---