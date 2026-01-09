---
date: 2026-01-09
description: Pelajari cara membuat adegan 3D .NET menggunakan Aspose.3D dan temukan
  cara memutar ekstrusi dengan teknik putaran ekstrusi linier.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Buat Adegan 3D .NET – Putaran pada Ekstrusi Linear
url: /id/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Membuat 3D Scene .NET – Twist pada Linear Extrusion

## Pendahuluan

Dalam dunia pengembangan .NET yang terus berkembang, memanfaatkan kekuatan grafis 3D merupakan sebuah tantangan yang menarik. **Aspose.3D for .NET** muncul sebagai toolkit yang berharga, memungkinkan pengembang untuk **membuat 3D scene .NET** yang imersif dan memukau secara visual. Dalam panduan komprehensif ini, kami akan menjelajahi fitur menarik — Linear Extrusion dengan Twist — dan memandu Anda melalui setiap langkah sehingga Anda dapat menambahkan twist dinamis pada model dengan percaya diri.

## Jawaban Cepat
- **Apa arti “create 3d scene .net”?** Ini merujuk pada pembuatan scene 3‑D secara programatis menggunakan pustaka Aspose.3D dalam lingkungan .NET.  
- **Bagaimana cara menambahkan twist pada sebuah extrusion?** Atur properti `Twist` pada objek `LinearExtrusion`; nilainya adalah sudut rotasi dalam derajat.  
- **Apakah saya memerlukan lisensi untuk Aspose.3D?** Versi percobaan gratis dapat digunakan untuk evaluasi; lisensi komersial diperlukan untuk penggunaan produksi.  
- **Versi .NET apa yang didukung?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6 dan yang lebih baru.  
- **Apa dampak nilai `Slices`?** Lebih banyak slice menghasilkan twist yang lebih halus tetapi meningkatkan penggunaan memori dan waktu pemrosesan.

## Apa itu Linear Extrusion dengan Twist?
Linear extrusion menggerakkan profil 2‑D sepanjang jalur lurus, sementara properti **twist** memutar profil secara bertahap, menghasilkan efek heliks. Teknik ini sangat cocok untuk memodelkan pegas, kolom berputar, atau elemen dekoratif.

## Mengapa menggunakan Aspose.3D untuk tugas ini?
- **API yang sederhana** – kelas intuitif seperti `LinearExtrusion` dan `RectangleShape`.  
- **Integrasi penuh dengan .NET** – bekerja mulus dengan C#, VB.NET, dan F#.  
- **Output lintas‑platform** – ekspor ke OBJ, STL, FBX, dan banyak format lainnya.

## Prasyarat

Sebelum memulai perjalanan 3D ini, pastikan Anda telah menyiapkan prasyarat berikut:

- Aspose.3D for .NET: Pastikan Anda telah menginstal pustaka Aspose.3D. Jika belum, Anda dapat mengunduhnya [di sini](https://releases.aspose.com/3d/net/).

- Pengetahuan Dasar Pengembangan .NET: Tutorial ini mengasumsikan pemahaman dasar tentang pengembangan .NET.

## Mengimpor Namespace

Dalam proyek .NET apa pun, penggunaan namespace yang tepat sangat penting. Mulailah dengan mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D secara efektif. Berikut cuplikan kode untuk memandu Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Cara membuat 3d scene .net dengan Linear Extrusion Twist

Berikut adalah langkah‑demi‑langkah yang menunjukkan secara tepat cara **membuat 3D scene .NET** dan menerapkan twist pada linear extrusion.

### Langkah 1: Inisialisasi Profil Dasar

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Kami memulai dengan mendefinisikan profil persegi panjang. Sesuaikan `RoundingRadius` untuk melunakkan sudut jika diinginkan.

### Langkah 2: Buat 3D Scene

```csharp
// Create a scene 
Scene scene = new Scene();
```

Objek `Scene` berfungsi sebagai kanvas tempat semua objek 3‑D akan berada.

### Langkah 3: Buat Node Kiri dan Kanan

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Node adalah wadah untuk geometri. Kami membuat dua node sehingga dapat membandingkan extrusion tanpa twist (kiri) dengan yang ber‑twist (kanan). Node kiri dipindahkan 15 satuan pada sumbu X untuk pemisahan visual.

### Langkah 4: Lakukan Linear Extrusion dengan Twist pada Node Kiri

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Di sini `Twist` diatur ke **0°**, menghasilkan extrusion lurus. Nilai `Slices` sebesar **100** memberikan permukaan yang halus.

### Langkah 5: Lakukan Linear Extrusion dengan Twist pada Node Kanan

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Menetapkan `Twist = 90` memutar profil sebesar 90 derajat sepanjang panjang extrusion, menciptakan heliks yang jelas terlihat.

### Langkah 6: Simpan 3D Scene

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Scene diekspor sebagai file OBJ, yang dapat Anda buka di sebagian besar penampil 3‑D atau impor ke pipeline lain.

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Cara Memperbaiki |
|-------|----------------|------------|
| **Twist terlihat datar** | `Slices` terlalu rendah, menghasilkan geometri kasar. | Tingkatkan `Slices` (misalnya, 200) untuk twist yang lebih halus. |
| **Performa menurun dengan `Slices` tinggi** | Lebih banyak poligon membutuhkan lebih banyak memori/CPU. | Gunakan `Slices` terendah yang masih memenuhi kualitas visual, atau aktifkan penyederhanaan geometri setelah extrusion. |
| **File tidak ditemukan saat menyimpan** | Jalur direktori output tidak valid. | Berikan jalur absolut lengkap atau pastikan direktori ada sebelum memanggil `Save`. |

## Pertanyaan yang Sering Diajukan

**T: Bisakah saya menerapkan Linear Extrusion dengan Twist pada bentuk lain?**  
J: Tentu saja! Anda dapat bereksperimen dengan berbagai profil dasar selain persegi panjang, membuka banyak kemungkinan desain.

**T: Apa peran properti 'Twist' dalam linear extrusion?**  
J: Properti 'Twist' menentukan derajat rotasi selama proses extrusion, memengaruhi bentuk 3D akhir.

**T: Apakah ada pertimbangan performa saat menggunakan banyak slice?**  
J: Semakin banyak slice menambah detail, tetapi dapat memengaruhi performa. Temukan keseimbangan berdasarkan kebutuhan aplikasi Anda.

**T: Bisakah saya menggabungkan Linear Extrusion dengan fitur Aspose.3D lainnya?**  
J: Pastinya! Aspose.3D menawarkan serangkaian fitur yang kaya. Silakan menggabungkan Linear Extrusion dengan fungsionalitas lain untuk desain yang lebih kompleks.

**T: Apakah ada komunitas untuk dukungan dan diskusi Aspose.3D?**  
J: Ya, bergabunglah dengan komunitas Aspose.3D di [Aspose Forum](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi yang menarik.

---

**Terakhir Diperbarui:** 2026-01-09  
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}