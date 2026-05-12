---
date: 2026-03-23
description: Pelajari cara ekstrusi linear dengan irisan menggunakan Aspose.3D untuk
  .NET. Buat model 3D detail dengan contoh kode langkah demi langkah.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Cara Ekstrusi Linear dengan Irisan Menggunakan Aspose.3D untuk .NET
url: /id/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Linear Extrusion dengan Slices Menggunakan Aspose.3D untuk .NET

## Perkenalan

Selamat datang di dunia desain 3D menggunakan Aspose.3D untuk .NET! Pada tutorial ini Anda akan menemukan **cara linear extrusion** dengan irisan, sebuah teknik yang memungkinkan Anda mengontrol tingkat detail pada model. Baik Anda seorang pengembang berpengalaman maupun yang baru memulai, kami akan memandu Anda melalui setiap langkah, menjelaskan alasan di balik setiap tindakan, dan memberikan tip praktis yang dapat langsung Anda terapkan.

## Jawaban Cepat
- **Apa itu ekstrusi linier dengan irisan?** Ini adalah metode memperluas profil 2D menjadi 3D sambil menentukan berapa banyak penampang menengah (irisan) yang dihasilkan.
- **Mengapa menggunakan irisan?** Lebih banyak irisan menghasilkan kelengkungan yang lebih halus; lebih sedikit irisan membuat mesh lebih ringan.
- **Prasyarat?** Aspose.3D untuk .NET, IDE yang kompatibel dengan .NET, dan pengetahuan dasar C#.
- **Waktu runtime tipikal?** Contoh ini berjalan kurang dari satu detik pada PC modern.
- **Format output?** Contoh menyimpan ke Wavefront OBJ, tetapi Aspose.3D mendukung banyak format.

## Apa itu Ekstrusi Linier dengan Irisan?

Ekstrusi linier mengambil bentuk 2‑D (sebuah profil) dan memanjangkannya sepanjang garis lurus untuk membuat padat 3‑D. Properti **Slices** menentukan berapa banyak penampang menengah yang disisipkan antara awal dan akhir ekstrusi, mempengaruhi kelancaran dan jumlah poligon.

## Mengapa Menggunakan Irisan dalam Ekstrusi Linier?

- **Control Mesh Density:** Menyetel keseimbangan antara kualitas visual dan ukuran file.
- **Optimalkan Kinerja:** Gunakan lebih sedikit irisan untuk aplikasi real‑time, lebih banyak untuk render resolusi tinggi.
- **Fleksibilitas Kreatif:** Gabungkan jumlah irisan yang berbeda pada objek terpisah untuk menonjolkan maksud desain.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Library Aspose.3D untuk .NET – unduh dari [di sini](https://releases.aspose.com/3d/net/).
- IDE yang mendukung C# (Visual Studio, Rider, VS Code, dll.).
- Familiaritas dasar dengan sintaks C# dan konsep berorientasi objek.
- Rasa ingin tahu untuk bereksperimen dengan geometri 3‑D!

## Impor Namespace

Pertama, impor namespace yang memberi Anda akses ke kelas inti Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Panduan Langkah-demi-Langkah

### Langkah 1: Inisialisasi Profil Dasar

Kami memulai dengan bentuk persegi panjang sederhana dan memberikan radius pembulatan kecil agar tepinya tidak terlalu tajam.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Langkah 2: Membuat Adegan 3D

`Scene` berfungsi sebagai wadah untuk semua node, mesh, cahaya, dan kamera.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Langkah 3: Tambahkan Node Kiri dan Kanan

Kami akan membuat dua node saudara di bawah root scene. Node kiri akan menerima jumlah irisan rendah, simpul kanan jumlah irisan tinggi, sehingga Anda dapat membandingkan perbedaan visualnya.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Langkah 4: Lakukan Ekstrusi Linier pada Node Kiri (Detail Rendah)

Di sini kami mengekstrusi persegi panjang hanya dengan **2 irisan**. Ini menghasilkan mesh kasar—ideal untuk pemandangan cepat.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Langkah 5: Lakukan Ekstrusi Linier pada Node Kanan (Detail Tinggi)

Sekarang kami menggunakan **10 irisan** untuk hasil yang jauh lebih halus. Perhatikan bagaimana geometri menjadi lebih detail.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Langkah 6: Simpan Adegan 3D

Akhirnya, tulis adegan ke file OBJ. Ganti `"Your Output Directory"` dengan jalur yang valid di mesin Anda.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Masalah dan Solusi Umum

| Masalah | Mengapa Terjadi | Perbaikan |
|-------|----------------|-----|
| **Tidak ada file yang dibuat** | Jalur output tidak valid atau tidak memiliki izin tulis. | Gunakan jalur absolut dan pastikan folder tersebut ada. |
| **Objek terlihat datar** | `Slices` diatur ke 1 atau 0. | Atur `Slices` minimal 2 untuk ekstrusi yang terlihat. |
| **Geometri yang tidak terduga** | Radius pembulatan terlalu besar untuk ukuran persegi panjang. | Sesuaikan `RoundingRadius` ke nilai yang lebih kecil dari setengah sisi terkecil persegi panjang. |

## Pertanyaan Umum Asli

### T1: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

J1: Aspose.3D terutama dirancang untuk .NET, tetapi Anda dapat menjelajahi opsi interoperabilitas dengan bahasa seperti Python menggunakan binding .NET.

### T2: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?

J2: Lihat dokumentasi [di sini](https://reference.aspose.com/3d/net/) untuk informasi mendalam tentang kemampuan dan penggunaan Aspose.3D.

### T3: Apakah tersedia uji coba gratis untuk Aspose.3D untuk .NET?

J3: Ya, Anda dapat mengambil uji coba gratis Anda [di sini](https://releases.aspose.com/) untuk menjelajahi fitur-fitur pustaka sebelum melakukan pembelian.

### T4: Bagaimana saya bisa mendapatkan dukungan teknis untuk Aspose.3D untuk .NET?

J4: Kunjungi forum Aspose.3D [di sini](https://forum.aspose.com/c/3d/18) untuk mencari bantuan dan berinteraksi dengan komunitas.

### T5: Dapatkah saya menggunakan lisensi sementara untuk Aspose.3D untuk .NET?

A5: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.

## Kesimpulan

Anda kini telah melihat **cara ekstrusi linier** dengan irisan menggunakan Aspose.3D untuk .NET, mengeksplorasi dampak dari berbagai jumlah irisan, dan mempelajari cara mengekspor hasil kerja Anda. Bereksperimenlah dengan profil lain, mainkan nilai `Slices`, serta integrasikan material atau cahaya untuk membuat aset 3‑D siap produksi.

---

**Terakhir Diperbarui:** 23-03-2026
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET (terbaru pada saat penulisan)
**Penulis:** Beranggapan  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}