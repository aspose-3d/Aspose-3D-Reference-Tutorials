---
date: 2026-03-23
description: Pelajari cara membuat ekstrusi menggunakan Aspose.3D untuk .NET, mengubah
  profil 2D menjadi mesh 3D, dan mengekspor ke Wavefront OBJ. Ikuti panduan langkah
  demi langkah ini.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Cara Membuat Ekstrusi di Aspose.3D untuk .NET – Langkah demi Langkah
url: /id/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Melakukan Ekstrusi Linear

## Pendahuluan:

Mulailah perjalanan menegangkan ke dalam dunia grafik 3D dengan Aspose.3D untuk .NET, sebuah kekuatan yang meningkatkan kemampuan pengembangan Anda. Dalam tutorial ini, **Anda akan belajar cara membuat ekstrusi** – teknik menarik yang mengubah profil 2‑D menjadi mesh 3‑D lengkap. Kami akan membimbing Anda melalui setiap langkah, mulai dari menginstal Aspose.3D hingga mengekspor hasilnya sebagai file Wavefront OBJ, sehingga Anda dapat **membuat 3D dari bentuk 2D** dengan percaya diri.

## Jawaban Cepat
- **Apa itu ekstrusi linear?** Memperpanjang bentuk 2‑D sepanjang jalur lurus untuk membentuk objek 3‑D.  
- **Perpustakaan mana yang digunakan tutorial ini?** Aspose.3D untuk .NET.  
- **Bagaimana cara menyimpan OBJ?** Gunakan `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Apakah saya dapat mengekspor Wavefront OBJ?** Ya – format ini didukung sepenuhnya.  
- **Apakah saya memerlukan lisensi?** Lisensi sementara sudah cukup untuk pengujian; lisensi komersial diperlukan untuk produksi.

## Prasyarat:

Sebelum menyelami dunia memukau manipulasi 3D, pastikan Anda memiliki prasyarat berikut ini:

1. **Instalasi Aspose.3D** – *install aspose 3d*  
   - Mulailah dengan mengunduh dan menginstal Aspose.3D untuk .NET dari [here](https://releases.aspose.com/3d/net/).  
   - Ikuti petunjuk instalasi yang disediakan dalam dokumentasi [here](https://reference.aspose.com/3d/net/).

2. **Menyiapkan Lingkungan Pengembangan Anda**  
   - Pastikan lingkungan pengembangan Anda dikonfigurasi dengan benar dengan namespace yang diperlukan untuk Aspose.3D.

Sekarang Anda sudah siap, mari melompat ke dalam keajaiban Aspose.3D!

## Impor Namespace:

Sertakan namespace penting untuk memulai petualangan 3D Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Namespace ini membentuk dasar perjalanan pemrograman 3D Anda, memberikan akses ke alat yang diperlukan untuk integrasi mulus fungsionalitas Aspose.3D.

## Melakukan Ekstrusi Linear:

Mari buat objek 3D yang memukau melalui Ekstrusi Linear menggunakan Aspose.3D. Ikuti langkah-langkah berikut:

### Cara Membuat Ekstrusi – Langkah 1: Inisialisasi Profil Dasar
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Langkah ini menyiapkan profil 2‑D yang akan menjadi dasar karya 3‑D kami. Sesuaikan parameter sesuai kebutuhan untuk mencapai bentuk dan struktur yang diinginkan.

### Cara Membuat Ekstrusi – Langkah 2: Ekstrusi Linear
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Di sini, Ekstrusi Linear dilakukan, mengambil profil 2‑D dan memperluasnya ke dimensi ketiga. Bereksperimenlah dengan parameter seperti **Slices**, **Twist**, dan **TwistOffset** untuk **menghasilkan variasi mesh 3D** yang sesuai dengan maksud desain Anda.

### Cara Membuat Ekstrusi – Langkah 3: Membuat Scene
```csharp
Scene scene = new Scene();
```

Kanvas kosong dibuat – sebuah scene di mana objek 3‑D Anda akan menjadi hidup.

### Cara Membuat Ekstrusi – Langkah 4: Menambahkan Ekstrusi ke Scene
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Karya ekstrusi Anda ditambahkan sebagai node anak ke scene.

### Cara Membuat Ekstrusi – Langkah 5: Menyimpan Scene 3D
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Akhirnya, **cara menyimpan OBJ** – kami menyimpan hasilnya dalam format Wavefront OBJ yang populer, yang dapat dibuka oleh sebagian besar editor 3‑D.

Sekarang, saksikan keajaiban 3D Anda!

## Mengapa ini penting

Ekstrusi linear adalah cara cepat untuk **membuat 3D dari sketsa 2D**, sempurna untuk prototyping cepat, pemodelan arsitektural, atau menghasilkan mesh yang dapat dicetak. Dengan menguasai teknik ini, Anda membuka alur kerja serbaguna yang menghemat waktu dan mengurangi kebutuhan akan alat pemodelan yang kompleks.

## Jebakan Umum & Tips

- **Nilai Twist terlalu tinggi** dapat menyebabkan self‑intersections. Jaga twist di bawah 720° untuk kebanyakan bentuk sederhana.  
- **Slices tidak cukup** dapat menghasilkan tampilan berfacets. Tingkatkan properti `Slices` untuk hasil yang lebih halus.  
- **Ingat untuk mengatur `Center = true`** jika Anda ingin ekstrusi terpusat di sekitar asal profil – ini sering mempermudah penempatan nanti.

## Kesimpulan:

Selamat! Anda baru saja menggaruk permukaan potensi Aspose.3D. Tutorial ini hanya memberi petunjuk tentang lanskap luas yang menunggu eksplorasi Anda. Selami dokumentasi, bereksperimen dengan berbagai bentuk, dan buka spektrum penuh kemungkinan dengan Aspose.3D untuk .NET.

## FAQ:

### Q1: Apakah Aspose.3D cocok untuk pemula?
A1: Tentu saja! Aspose.3D menawarkan lingkungan yang ramah pengguna, dan tutorial kami membimbing Anda melalui dasar-dasarnya.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?
A2: Ya, Aspose.3D memiliki opsi lisensi untuk penggunaan pribadi maupun komersial. Periksa [here](https://purchase.aspose.com/buy) untuk detail.

### Q3: Bagaimana saya dapat memperoleh lisensi sementara untuk pengujian?
A3: Kunjungi [this link](https://purchase.aspose.com/temporary-license/) untuk mendapatkan lisensi sementara untuk keperluan pengujian.

### Q4: Di mana saya dapat menemukan dukungan komunitas?
A4: Bergabunglah dengan [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) untuk terhubung dengan komunitas yang dinamis dan mencari bantuan.

### Q5: Apakah ada percobaan gratis yang tersedia?
A5: Tentu! Unduh versi percobaan gratis [here](https://releases.aspose.com/) untuk merasakan kemampuan Aspose.3D secara langsung.

---

**Terakhir Diperbarui:** 2026-03-23  
**Diuji Dengan:** Aspose.3D for .NET (latest release)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}