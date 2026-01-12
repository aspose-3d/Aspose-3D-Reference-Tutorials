---
date: 2026-01-12
description: Pelajari cara membuat silinder dasar shear dan cara mengekspor model
  3D dalam format OBJ menggunakan Aspose.3D untuk .NET. Ikuti panduan langkah demi
  langkah ini untuk menguasai pemodelan 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cara membuat silinder dasar geser dengan Aspose.3D untuk .NET
url: /id/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Silinder Dasar Geser yang Disesuaikan

## Pendahuluan
Selamat datang di panduan komprehensif kami di mana **Anda akan belajar cara membuat model silinder dasar geser** dengan Aspose.3D untuk .NET. Baik Anda sedang membuat aset game, komponen mekanik, atau demo visual, tutorial ini menunjukkan secara tepat cara membentuk bagian bawah silinder, menerapkan geseran, dan akhirnya **mengekspor file model 3D OBJ** untuk digunakan dalam alur kerja selanjutnya. Mari kita jalani setiap langkah bersama, sehingga Anda dapat mulai menghasilkan geometri khusus dalam hitungan menit.

## Jawaban Cepat
- **Apa itu silinder dasar geser?** Silinder yang permukaan dasarnya miring (digeser) bukan datar.  
- **Pustaka mana yang digunakan?** Aspose.3D untuk .NET.  
- **Bagaimana cara mengekspor model?** Gunakan `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Apakah saya memerlukan lisensi?** Versi percobaan tersedia; lisensi komersial diperlukan untuk produksi.  
- **Prasyarat apa yang diperlukan?** Lingkungan pengembangan .NET dan paket NuGet Aspose.3D.

## Apa itu silinder dasar geser?
Silinder dasar geser adalah mesh silindris standar yang bagian bawahnya telah diubah melalui operasi geser. Ini memungkinkan Anda membuat dasar miring, ramp, atau konektor khusus tanpa harus mengedit vertex secara manual.

## Mengapa menggunakan Aspose.3D untuk tugas ini?
- **Kontrol penuh** atas parameter geometri (radius, tinggi, segmen).  
- **Dukungan geser bawaan** melalui properti `ShearBottom`, menghemat Anda dari manipulasi mesh tingkat rendah.  
- **Ekspor satu klik** ke format populer seperti OBJ, FBX, dan STL, memudahkan integrasi dengan alat lain.

## Prasyarat
- Pengetahuan dasar tentang C# dan .NET.  
- Aspose.3D untuk .NET terpasang. Anda dapat mengunduhnya **[di sini](https://releases.aspose.com/3d/net/)**.  
- IDE yang kompatibel dengan .NET (Visual Studio, Rider, atau VS Code).

## Impor Namespace
Di file C# Anda, mulai dengan mengimpor namespace yang diperlukan:

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

## Langkah 1: Buat Scene
Pertama, buat instance scene 3‑D baru yang akan menampung semua objek kita.

```csharp
Scene scene = new Scene();
```

## Langkah 2: Buat Cylinder 1
Buat silinder utama yang akan kami sesuaikan dengan dasar yang digeser.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Langkah 3: Sesuaikan Shear Bottom untuk Cylinder 1
Terapkan geseran, aktifkan pembuatan fan, dan sesuaikan properti lain untuk mencapai bentuk yang diinginkan.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Langkah 4: Tambahkan Cylinder 1 ke Scene
Tempatkan silinder yang telah disesuaikan ke dalam scene dan geser sedikit ke kanan agar kita dapat melihat kedua objek berdampingan.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Langkah 5: Buat Cylinder 2
Buat silinder kedua yang polos untuk perbandingan.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Langkah 6: Tambahkan Cylinder 2 ke Scene
Tambahkan silinder kedua tanpa geseran khusus—ini membantu memperlihatkan efek dari langkah sebelumnya.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Langkah 7: Simpan Scene
Akhirnya, ekspor seluruh scene sebagai file OBJ sehingga Anda dapat membukanya di Blender, Maya, atau penampil 3‑D lainnya.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Masalah Umum & Tips
- **Nilai shear**: `Vector2` menerima faktor shear X dan Y. Nilai `0.83` kira‑kira setara dengan 47,5°, tetapi Anda dapat menyesuaikannya untuk sudut yang berbeda.  
- **Jalur ekspor**: Pastikan folder yang Anda tentukan ada dan Anda memiliki izin menulis; jika tidak, `scene.Save` akan melempar pengecualian.  
- **Kinerja**: Untuk silinder dengan segmen sangat tinggi, pertimbangkan mengurangi jumlah segmen (`20` dalam contoh) agar ukuran file OBJ tetap dapat dikelola.

## Pertanyaan yang Sering Diajukan

### Apakah Aspose.3D untuk .NET cocok untuk pemula?
Tentu saja! Aspose.3D untuk .NET menawarkan API yang ramah pengguna, membuatnya dapat diakses baik untuk pemula maupun pengembang berpengalaman.

### Bisakah saya menerapkan sudut geser yang berbeda pada silinder?
Ya, Anda dapat menyesuaikan `ShearBottom` untuk setiap silinder secara terpisah, memungkinkan Anda mencapai efek unik.

### Apakah ada versi percobaan yang tersedia?
Ya, Anda dapat menjelajahi versi percobaan gratis **[di sini](https://releases.aspose.com/)**.

### Di mana saya dapat menemukan dukungan tambahan?
Kunjungi **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** untuk dukungan komunitas dan diskusi.

### Bagaimana saya dapat memperoleh lisensi sementara?
Dapatkan lisensi sementara Anda **[di sini](https://purchase.aspose.com/temporary-license/)**.

**Pertanyaan & Jawaban Tambahan**

**T: Bagaimana cara mengubah format ekspor ke FBX?**  
J: Ganti `FileFormat.WavefrontOBJ` dengan `FileFormat.FBX` dalam pemanggilan `scene.Save`.

**T: Apakah saya dapat menganimasikan silinder setelah mengekspor?**  
J: OBJ tidak mendukung animasi; gunakan FBX atau GLTF jika Anda memerlukan data beranimasi.

**T: Bagaimana jika saya membutuhkan radius silinder yang lebih besar?**  
J: Sesuaikan dua parameter pertama pada konstruktor `Cylinder` (misalnya, `new Cylinder(4, 4, …)`).

## Kesimpulan
Anda kini telah menguasai cara **membuat model silinder dasar geser** dan mengekspornya sebagai file OBJ menggunakan Aspose.3D untuk .NET. Bereksperimenlah dengan nilai shear yang berbeda, jumlah segmen, dan format ekspor untuk menyesuaikan kebutuhan proyek Anda. Selamat memodel!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}