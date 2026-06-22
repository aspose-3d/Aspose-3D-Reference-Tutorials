---
date: 2026-03-26
description: Pelajari cara membuat silinder dan mengekspor file OBJ menggunakan Aspose.3D
  untuk .NET. Panduan ramah pemula ini mencakup pengaturan adegan 3D dan ekspor OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cara Membuat Silinder dengan Dasar Geser – Aspose.3D untuk .NET
url: /id/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Membuat Silinder dengan Shear Bottom – Aspose.3D untuk .NET

## Perkenalan
Jika Anda bertanya-tanya **bagaimana cara membuat silinder** dengan shear bottom yang disesuaikan dalam lingkungan .NET, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan membahas setiap langkah—dari menyiapkan adegan 3‑D hingga mengekspor model akhir sebagai file OBJ—sehingga Anda dapat meningkatkan keterampilan *pemodelan 3D pemula* Anda menggunakan **Aspose.3D untuk .NET**.

## Jawaban Cepat
- **Apa kelas utama untuk memulai model 3D?** `Scene` membuat kontainer akar untuk semua geometri.
- **Metode mana yang mengekspor model ke OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.
- **Apakah saya memerlukan lisensi untuk pengujian?** Versi percobaan gratis tersedia—lihat tautan percobaan di FAQ.
- ** mendorong saya mengubah sudut geser?** Ya, ubah `ShearBottom` dengan nilai `Vector2`.
- **Apakah ini cocok untuk pemula?** Tentu saja; API penyampaian penanganan mesh tingkat rendah.

## Apa itu Adegan 3D?
*Pemandangan 3D* adalah kontainer hierarkis yang menyimpan semua entitas geometri, cahaya, kamera, dan transformasi. Dalam Aspose.3D kelas `Scene` menyediakan cara bersih untuk mengorganisir dan kemudian mengekspor model Anda.

## Mengapa Mengekspor OBJ?
OBJ adalah format berbasis teks yang didukung secara luas dan dapat diimpor oleh banyak aplikasi 3‑D (Blender, Maya, Unity). Mengekspor ke OBJ memungkinkan Anda berbagi atau mengedit lebih lanjut model silinder Anda di luar .NET.

## Prasyarat
Sebelum kita mulai, pastikan Anda memiliki:

- Pengetahuan dasar tentang C# dan pengembangan .NET.
- **Aspose.3D untuk .NET** terpasang – Anda dapat mengunduhnya **[di sini](https://releases.aspose.com/3d/net/)**.
- IDE .NET (Visual Studio, Rider, atau VS Code) siap untuk coding.

## Impor Namespace
Pertama, bawa namespace yang diperlukan ke dalam ruang lingkup sehingga tipe API dikenali.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Langkah 1: Buat Adegan 3D
Objek `Scene` berfungsi sebagai akar hierarki model Anda.

```csharp
Scene scene = new Scene();
```

## Langkah 2: Buat Silinder1
Kami menghasilkan silinder pertama dengan radius 2, tinggi 10, dan 20 segmen radial.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Langkah 3: Sesuaikan Bagian Bawah Geser untuk Silinder1
Terapkan transformasi shear, aktifkan pembuatan fan‑cylinder, dan sesuaikan properti lain untuk mencapai bentuk yang diinginkan.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Langkah 4: Tambahkan Silinder1 ke Adegan
Tempatkan silinder pertama di lokasi yang nyaman menggunakan transformasi translasi.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Langkah 5: Buat Silinder2
Silinder kedua dibuat dengan dimensi dasar yang sama tetapi tanpa shear khusus—sempurna untuk perbandingan berdampingan.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Langkah 6: Tambahkan Silinder2 ke Adegan
Kami cukup menempelkan silinder kedua ke grafik adegan.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Langkah 7: Ekspor Adegan sebagai File OBJ
Akhirnya, kami menyimpan seluruh adegan ke file OBJ sehingga dapat dibuka di penampil 3‑D standar mana pun.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Masalah Umum dan Solusinya
| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **File OBJ Kosong** | Adegan tidak memiliki geometri yang terlampir. | Pastikan kedua silinder ditambahkan ke `scene.RootNode`. |
| **Geser terlihat salah** | `ShearBottom` mengharapkan nilai tangen dari sudut. | Gunakan `Math.Tan(angleInRadians)` atau nilai `0.83` yang disediakan untuk ~47,5°. |
| **Kesalahan jalur file** | Direktori tidak valid atau tidak ada. | Gunakan `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Pertanyaan yang Sering Diajukan
### Apakah Aspose.3D untuk .NET cocok untuk pemula?
Tentu saja! Aspose.3D untuk .NET menawarkan API tingkat tinggi yang melibatkan bagian matematika berat dari pemodelan 3‑D, sehingga dapat diakses oleh pengembang dengan tingkat keahlian apa pun.

### Bisakah saya menerapkan sudut geser yang berbeda pada silinder?
Ya, setiap instance `Cylinder` memiliki properti `ShearBottom`‑nya sendiri, sehingga Anda dapat mengatur sudut unik untuk setiap objek.

### Apakah ada versi percobaan yang tersedia?
Ya, Anda dapat menjelajahi versi percobaan gratis **[di sini](https://releases.aspose.com/) **.

### Di mana saya dapat menemukan dukungan tambahan?
Kunjungi **[forum Aspose.3D](https://forum.aspose.com/c/3d/18) ** untuk bantuan komunitas, contoh kode, dan diskusi.

### Bagaimana cara mendapatkan lisensi sementara?
Dapatkan lisensi sementara Anda **[di sini](https://purchase.aspose.com/temporary-license/) **.

**Tanya Jawab Tambahan**

**Q: Bagaimana cara mengekspor model dalam format yang berbeda, seperti STL?**
A: Ganti `FileFormat.WavefrontOBJ` dengan `FileFormat.STL` pada pemanggilan `scene.Save`.

**Q: Bisakah saya menganimasikan silinder setelah dibuat?**
A: Ya, Anda dapat menambahkan animasi key‑frame ke transformasi node menggunakan kelas `Animation` yang disediakan oleh Aspose.3D.

**Q: Apakah API mendukung .NET Core?**
A: Perpustakaan ini sepenuhnya kompatibel dengan .NET Core, .NET 5+, dan .NET 6+.

---

**Terakhir Diperbarui:** 26-03-2026
**Diuji Dengan:** Aspose.3D untuk .NET (rilis terbaru)
**Penulis:** Beranggapan  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}