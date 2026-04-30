---
date: 2026-03-28
description: Pelajari cara menganimasikan kubus dalam adegan 3D menggunakan Aspose.3D
  untuk .NET dan mengekspor adegan animasi FBX. Panduan ini menunjukkan cara membuat
  kurva animasi, mengikat keyframe, dan menganimasikan properti 3D.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Cara Menganimasi Kubus dalam Adegan 3D dengan Aspose.3D untuk .NET
url: /id/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menganimasikan Kubus dalam Adegan 3D dengan Aspose.3D untuk .NET

## Pendahuluan

Jika Anda menyelami dunia pembuatan adegan 3D dan animasi di .NET, Aspose.3D adalah toolkit pilihan Anda. Dalam panduan langkah‑demi‑langkah ini, kami akan mengeksplorasi **cara menganimasikan objek kubus** dengan menganimasi properti mereka, membuat kurva animasi, dan mengikat keyframe. Pada akhir tutorial, Anda akan memiliki kubus yang sepenuhnya teranimasi yang dapat diekspor ke format 3D populer.

## Jawaban Cepat
- **Perpustakaan apa yang digunakan?** Aspose.3D untuk .NET  
- **Tugas utama apa yang dibahas tutorial ini?** Cara menganimasikan kubus dalam adegan 3D  
- **Langkah‑langkah kunci?** Mengimpor namespace, membuat adegan, mengikat keyframe, menyimpan file  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis cukup untuk belajar; lisensi komersial diperlukan untuk produksi  
- **Format output yang didukung?** FBX (ASCII 7500) dan format lain yang didukung oleh Aspose.3D  

## Apa itu “cara menganimasikan kubus” dalam Aspose.3D?
Menganimasikan sebuah kubus berarti memodifikasi properti transformasinya (seperti Translasi, Rotasi, atau Skala) seiring waktu menggunakan data keyframe. Aspose.3D menyediakan API yang bersih untuk membuat **kurva animasi**, **mengikat keyframe**, dan **menganimasi properti 3D** langsung pada node adegan.

## Mengapa menganimasikan kubus dengan Aspose.3D?
- **Integrasi .NET penuh** – bekerja dengan .NET Framework, .NET Core, dan .NET 5/6.  
- **Tanpa ketergantungan eksternal** – tidak memerlukan Unity atau mesin lain untuk animasi sederhana.  
- **Fleksibilitas ekspor** – adegan yang teranimasi dapat disimpan sebagai FBX, OBJ, GLTF, dll., untuk pipeline selanjutnya.

## Prasyarat

Sebelum memulai perjalanan menarik ini, pastikan Anda memiliki prasyarat berikut:

- Aspose.3D untuk .NET: Pastikan perpustakaan telah terpasang. Anda dapat mengunduhnya dari [situs Aspose.3D](https://releases.aspose.com/3d/net/).

- Pengetahuan tentang C#: Familiaritas dengan bahasa pemrograman C# sangat penting untuk memahami dan mengimplementasikan contoh.

- Integrated Development Environment (IDE): Gunakan IDE pilihan Anda, seperti Visual Studio, untuk menulis kode bersama contoh.

- Konsep Dasar Adegan 3D: Memahami konsep dasar adegan 3D akan membuat proses belajar lebih lancar.

## Mengimpor Namespace

Dalam kode C# Anda, pastikan mengimpor namespace yang diperlukan untuk Aspose.3D. Berikut set yang diperlukan:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Langkah 1: Inisialisasi Objek Scene

Buat adegan kosong yang akan menampung semua node dan animasi kita.

```csharp
Scene scene = new Scene();
```

## Langkah 2: Membuat Mesh Menggunakan Polygon Builder

Kami menghasilkan mesh kubus sederhana menggunakan metode bantuan `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Langkah 3: Membuat Node Kubus

Tambahkan mesh kubus ke adegan sebagai node anak dari root. Nama node **cube1** akan digunakan nanti saat mengikat keyframe.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Langkah 4: Temukan Properti Translasi

Untuk menganimasikan posisi kubus, kita perlu menemukan properti **Translation** pada transformasi node.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Langkah 5: Membuat Bind Point

`BindPoint` menghubungkan properti adegan ke kurva animasi. Di sini kami mengikat properti translasi.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Langkah 6: Mengikat Kurva Animasi pada Komponen X

Sekarang kami membuat kurva animasi untuk sumbu **X**. Ini mendemonstrasikan langkah **create animation curve** dan menunjukkan cara **bind keyframes**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Langkah 7: Mengikat Kurva Animasi pada Komponen Z

Demikian pula, kami menganimasikan sumbu **Z** untuk memberikan jalur gerak yang lebih dinamis pada kubus.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Langkah 8: Menyimpan Adegan 3D

Ekspor adegan yang teranimasi ke file FBX. Format `FBX7500ASCII` didukung secara luas oleh alat 3D.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Langkah 9: Menampilkan Pesan Sukses

Berikan umpan balik kepada pengguna bahwa animasi berhasil ditambahkan.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Mengekspor Adegan yang Teranimasi ke FBX

Salah satu tugas paling umum setelah menganimasikan kubus adalah **mengekspor adegan teranimasi ke FBX** sehingga aplikasi 3D lain dapat menggunakannya. Kode di atas sudah menyimpan adegan dalam format FBX7500ASCII, yang mempertahankan data keyframe dan bekerja mulus dengan alat seperti Autodesk Maya, Blender, dan Unity. Saat Anda membuka file `.fbx` yang dihasilkan, Anda akan melihat kubus bergerak sepanjang sumbu X dan Z persis seperti yang didefinisikan oleh urutan keyframe.

## Masalah Umum dan Solusinya

| Masalah | Penyebab | Solusi |
|-------|--------|-----|
| Tidak ada gerakan yang terlihat | Waktu keyframe tidak cocok dengan rentang pemutaran | Pastikan timeline animasi adegan mencakup waktu keyframe (0‑5 detik dalam contoh ini). |
| Jalur file tidak tepat | `output` mengarah ke direktori yang tidak ada | Buat direktori terlebih dahulu atau gunakan jalur absolut. |
| Pengecualian lisensi | Menjalankan tanpa lisensi yang valid di produksi | Terapkan lisensi Aspose.3D Anda sebelum membuat `Scene`. |

## Pertanyaan yang Sering Diajukan

### Q1: Di mana saya dapat menemukan dokumentasi Aspose.3D?

A1: Dokumentasi tersedia [di sini](https://reference.aspose.com/3d/net/).

### Q2: Bagaimana cara mengunduh Aspose.3D untuk .NET?

A2: Anda dapat mengunduhnya dari [halaman rilis](https://releases.aspose.com/3d/net/).

### Q3: Apakah ada versi percobaan gratis?

A3: Ya, Anda dapat mendapatkan percobaan gratis [di sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat mendapatkan dukungan untuk Aspose.3D?

A4: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan.

### Q5: Bisakah saya memperoleh lisensi sementara?

A5: Ya, Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

## FAQ Tambahan (AI‑Optimized)

**T: Bisakah saya menganimasikan properti lain seperti rotasi atau skala?**  
J: Tentu saja. Gunakan `cube1.Transform.FindProperty("Rotation")` atau `"Scale"` dan ikat urutan keyframe dengan cara yang sama.

**T: Apakah Aspose.3D mendukung tipe interpolasi keyframe selain Bezier dan Linear?**  
J: Ya, ia juga mendukung `Interpolation.Step` dan `Interpolation.Cubic` untuk kontrol lebih lanjut.

**T: Bagaimana cara saya melihat pratinjau animasi sebelum mengekspor?**  
J: Aspose.3D menyediakan viewer sederhana dalam API‑nya; alternatifnya, muat FBX yang diekspor ke viewer 3D seperti Autodesk FBX Review.

**T: Apakah memungkinkan untuk menganimasikan beberapa kubus secara bersamaan?**  
J: Buat node terpisah untuk setiap kubus, ambil properti masing‑masing, dan ikat urutan keyframe secara independen.

## Kesimpulan

Selamat! Anda baru saja menguasai **cara menganimasikan kubus** dalam adegan 3D menggunakan Aspose.3D untuk .NET. Anda kini tahu cara **membuat kurva animasi**, **mengikat keyframe**, dan **mengekspor adegan teranimasi ke FBX** untuk menghidupkan geometri statis. Jangan ragu bereksperimen dengan rotasi, skala, atau bahkan morph target untuk memperluas toolkit animasi Anda.

---

**Terakhir Diperbarui:** 2026-03-28  
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}