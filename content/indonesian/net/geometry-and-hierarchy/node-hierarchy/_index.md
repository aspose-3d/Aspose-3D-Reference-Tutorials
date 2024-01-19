---
title: Memahami Hierarki Node dalam Adegan 3D
linktitle: Memahami Hierarki Node dalam Adegan 3D
second_title: Aspose.3D .NET API
description: Buka kekuatan Aspose.3D untuk .NET! Selami manipulasi hierarki node dengan panduan langkah demi langkah ini. Buat adegan 3D yang menakjubkan dengan mudah.
type: docs
weight: 16
url: /id/net/geometry-and-hierarchy/node-hierarchy/
---
## Perkenalan

Selamat datang di dunia Aspose.3D untuk .NET, perpustakaan canggih yang memberdayakan pengembang untuk bekerja secara lancar dengan adegan dan model 3D dalam aplikasi .NET mereka. Dalam tutorial ini, kita akan mempelajari seluk-beluk pemahaman hierarki node dalam adegan 3D menggunakan Aspose.3D. Di akhir panduan ini, Anda akan memiliki pemahaman yang kuat tentang cara memanipulasi struktur pemandangan 3D melalui node, sehingga memungkinkan Anda menciptakan pengalaman visual yang menakjubkan.

## Prasyarat

Sebelum kita memulai perjalanan 3D ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk Perpustakaan .NET: Pastikan Anda memiliki perpustakaan Aspose.3D yang terintegrasi ke dalam proyek .NET Anda. Jika Anda belum melakukannya, kunjungi[dokumentasi](https://reference.aspose.com/3d/net/) untuk bimbingan.

-  Unduh Perpustakaan: Jika Anda belum mengunduh perpustakaan Aspose.3D, ambil versi terbaru dari[tautan unduhan](https://releases.aspose.com/3d/net/)dan ikuti petunjuk instalasi yang disediakan dalam dokumentasi.

-  Dapatkan Lisensi: Untuk membuka potensi penuh Aspose.3D, Anda memerlukan lisensi yang valid. Jika Anda tidak memilikinya, Anda bisa mendapatkannya[Di Sini](https://purchase.aspose.com/buy) atau memilih a[uji coba gratis](https://releases.aspose.com/) untuk mengeksplorasi kemampuannya.

-  Dukungan dan Komunitas: Bergabunglah dengan komunitas Aspose.3D di[forum dukungan](https://forum.aspose.com/c/3d/18)untuk terhubung dengan pengembang lain, mencari bantuan, dan terus mengikuti perkembangan terkini.

-  Lisensi Sementara (Opsional): Jika Anda menjelajahi Aspose.3D sebelum melakukan pembelian, pertimbangkan untuk mendapatkan a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk akses yang diperluas.

Sekarang setelah alat kita siap, mari selami dunia manipulasi hierarki node 3D yang menarik menggunakan Aspose.3D.

## Impor Namespace

Dalam proyek .NET Anda, pastikan Anda mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas yang disediakan oleh Aspose.3D. Tambahkan baris berikut ke kode Anda:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Namespace ini akan memberi Anda akses ke kelas dan metode penting untuk bekerja dengan adegan 3D.

## Langkah 1: Inisialisasi Objek Adegan

```csharp
Scene scene = new Scene();
```

 Mulailah dengan membuat adegan 3D baru menggunakan`Scene` kelas.

## Langkah 2: Buat Node Anak

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Tetapkan struktur hierarki dengan membuat hubungan induk-anak antar simpul. Dalam contoh ini,`cube1` Dan`cube2` adalah node anak dari`top` node.

## Langkah 3: Buat dan Tetapkan Mesh

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Hasilkan mesh menggunakan metode yang sesuai (di sini,`CreateMeshUsingPolygonBuilder`) dan menugaskannya ke node anak.

## Langkah 4: Atur Terjemahan

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Tentukan terjemahan untuk setiap node kubus, posisikan mereka dalam ruang 3D.

## Langkah 5: Terapkan Rotasi ke Node Induk

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Putar simpul induk (`top`), dan amati bagaimana transformasi ini memengaruhi semua node turunannya.

## Langkah 6: Simpan Adegan 3D

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Tentukan direktori keluaran dan simpan adegan 3D dalam format file yang diinginkan (di sini, FBX7500ASCII).

## Langkah 7: Tampilkan Pesan Sukses

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Beri tahu pengguna tentang keberhasilan penambahan hierarki node dan lokasi file yang disimpan.

## Kesimpulan

Selamat! Anda telah berhasil menavigasi dunia hierarki simpul 3D yang rumit di Aspose.3D untuk .NET. Tutorial ini membekali Anda dengan pengetahuan untuk membuat, memanipulasi, dan menyimpan adegan 3D dengan mudah. Saat Anda melanjutkan perjalanan, jelajahi lebih banyak fitur dan keluarkan potensi penuh Aspose.3D dalam proyek .NET Anda.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET tanpa lisensi?

A1: Meskipun lisensi membuka semua fitur, Anda dapat menjelajahi Aspose.3D dengan kemampuan terbatas menggunakan uji coba gratis.

### Q2: Apakah ada format file lain yang didukung untuk menyimpan adegan 3D?

A2: Ya, Aspose.3D mendukung berbagai format; lihat dokumentasi untuk daftar lengkap.

### Q3: Bagaimana saya bisa berkontribusi pada komunitas Aspose.3D?

A3: Bergabunglah dengan forum dukungan, bagikan pengalaman Anda, dan berkontribusi dengan membantu orang lain menjawab pertanyaan mereka.

### Q4: Apakah Aspose.3D cocok untuk pengembangan game?

A4: Tentu saja! Aspose.3D serbaguna dan dapat diintegrasikan ke dalam proyek pengembangan game.

### Q5: Apa perbedaan antara lisensi sementara dan lisensi penuh?

A5: Lisensi sementara memberikan akses jangka pendek untuk tujuan evaluasi, sedangkan lisensi penuh menawarkan penggunaan tidak terbatas.