---
date: 2026-03-23
description: Pelajari cara membuat ekstrusi dengan putaran menggunakan Aspose.3D untuk
  .NET. Panduan langkah demi langkah ini mencakup teknik putaran ekstrusi linear.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Cara Membuat Ekstrusi dengan Putaran pada Ekstrusi Linear
url: /id/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Membuat Ekstrusi dengan Putaran pada Ekstrusi Linear

## Perkenalan

Jika Anda membangun aplikasi .NET yang memerlukan visual 3D yang menarik, Anda akan segera menemukan bahwa **cara membuat ekstrusi** adalah keterampilan dasar. Aspose.3D untuk .NET menyediakan API yang bersih dan berperforma tinggi untuk mengubah profil 2‑D sederhana menjadi model 3‑D yang canggih—terutama ketika Anda menambahkan putaran. Dalam tutorial ini kami akan membimbing Anda melalui setiap langkah, mulai dari menyiapkan adegan hingga menyimpan file OBJ akhir, sehingga Anda dapat melihat kekuatan putaran ekstrusi linier secara langsung.

## Jawaban Cepat
- **Apa kelas utama untuk ekstrusi?** `LinearExtrusion`
- **Properti mana yang menambahkan rotasi?** `Twist`
- **Berapa banyak irisan yang memberikan hasil halus?** Sekitar 100 irisan (sesuaikan bila perlu)
- **Apakah saya dapat menggunakan bentuk lain?** Ya, setiap `IProfile` seperti lingkaran, poligon, atau kurva kustom
- **Format file apa yang digunakan dalam contoh?** Wavefront OBJ (`.obj`)

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki hal‑hal berikut:

- Aspose.3D untuk .NET terpasang. Jika belum mengunduhnya, dapatkan **[di sini](https://releases.aspose.com/3d/net/)**.
- Lingkungan pengembangan .NET yang berfungsi (Visual Studio, VS Code, atau IDE lain yang Anda sukai).
- Familiaritas dasar dengan sintaks C# dan konsep berorientasi objek.

## Impor Namespace

Dalam proyek .NET apa pun, penggunaan namespace yang tepat sangat penting. Mulailah dengan mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D secara efektif. Berikut cuplikan kode untuk memandu Anda:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Panduan Langkah-demi-Langkah

### Langkah 1: Inisialisasi Profil Dasar

Kita mulai dengan mendefinisikan bentuk yang akan diekstrusi. Pada contoh ini kami menggunakan persegi panjang dengan radius pembulatan kecil untuk memberi sedikit tepi lengkungan.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Langkah 2: Membuat Adegan 3D

Objek `Scene` berfungsi sebagai kanvas tempat semua entitas 3‑D berada. Anggaplah ini sebagai panggung untuk ekstrusi Anda.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Langkah 3: Tambahkan Node Kiri dan Kanan

Node memungkinkan Anda mengatur objek secara hierarkis. Kami akan membuat dua node saudara—satu untuk ekstrusi lurus dan satu lagi untuk versi berputar.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Langkah 4: Lakukan Ekstrusi Linier dengan Twist pada Node Kiri

Properti `Twist` mengontrol seberapa banyak profil berputar selama proses ekstrusi. Menekannya ke **0** menghasilkan ekstrusi lurus klasik.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Langkah 5: Lakukan Ekstrusi Linier dengan Memutar pada Node Kanan

Sekarang kami menerapkan putaran 90‑derajat pada profil yang sama. Ini menampilkan efek **linear extrusion twist** dengan jelas.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Langkah 6: Simpan Adegan 3D

Akhirnya, ekspor adegan ke format yang dapat Anda lihat di penampil 3‑D apa pun. Contoh ini menggunakan Wavefront OBJ, tetapi Aspose.3D mendukung banyak format lain juga.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Mengapa Menggunakan Ekstrusi Linier dengan Putaran?

- **Prototyping cepat:** Ubah sketsa 2‑D menjadi bagian 3‑D tanpa pemodelan manual.
- **Fleksibilitas desain:** Sesuaikan nilai `Twist` untuk membuat spiral, rib helical, atau fitur dekoratif.
- **Ramah performa:** Parameter `Slices` memungkinkan Anda menyeimbangkan ketelitian visual dan kecepatan runtime.

## Masalah & Tip Umum

- **Terlalu banyak irisan:** Meskipun 100 irisan terlihat halus, nilai yang sangat tinggi dapat memperlambat rendering. Uji dengan jumlah lebih rendah jika kinerja menjadi masalah.
- **Nilai twist negatif:** `Twist` negatif memutar ke arah berlawanan—berguna untuk desain yang dicerminkan.
- **Path file:** Pastikan direktori output ada dan Anda memiliki izin menulis; jika tidak, `scene.Save` akan dilemparkan.

## Kesimpulan

Dalam tutorial ini kami telah menunjukkan **cara membuat ekstrusi** dengan putaran menggunakan Aspose.3D untuk .NET. Dengan menyesuaikan properti `Twist` dan `Slices` Anda dapat menghasilkan berbagai bentuk, mulai dari batang berputar sederhana hingga struktur heliks yang kompleks, semuanya hanya dengan beberapa baris kode.

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menerapkan ekstrusi linier dengan putaran pada bentuk lain?**
J: Tentu saja! Setiap kelas yang mengimplementasikan `IProfile`—seperti `CircleShape`, `PolygonShape`, atau spline kustom—dapat diekstrusi dengan putaran.

**Q: Apa yang sebenarnya terhenti oleh properti `Twist`?**
A: Properti ini menentukan sudut rotasi total (dalam derajat) yang diterapkan pada profil sepanjang ekstrusi.

**Q: Apakah menambah jumlah irisan akan mempengaruhi penggunaan memori?**
A: Ya, lebih banyak irisan menghasilkan lebih banyak vertex dan face, yang mengonsumsi memori tambahan dan dapat memengaruhi performa pada perangkat dengan spesifikasi rendah.

**Q: Dapatkah saya menggabungkan ekstrusi linier dengan fitur Aspose.3D lainnya?**
A: Pastinya. Anda dapat menerapkan material, tekstur, atau bahkan operasi Boolean setelah ekstrusi untuk menciptakan model yang lebih kaya.

**Q: Di mana saya bisa mendapatkan bantuan atau berdiskusi dengan pengembang lain?**
A: bersinggungan dengan komunitas Aspose.3D di **[Aspose Forum](https://forum.aspose.com/c/3d/18)** untuk dukungan, contoh, dan diskusi.

---

**Terakhir Diperbarui:** 23-03-2026
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET
**Penulis:** Beranggapan 

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}