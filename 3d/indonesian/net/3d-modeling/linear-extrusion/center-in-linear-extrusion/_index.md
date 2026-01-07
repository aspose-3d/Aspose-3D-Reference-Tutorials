---
date: 2026-01-07
description: Pelajari cara menambahkan bidang dasar saat melakukan ekstrusi linear
  dengan Aspose.3D untuk .NET dan mengekspor file Wavefront OBJ. Kuasai teknik memusatkan
  dan menempatkan dasar dalam pemodelan 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Tambahkan Bidang Dasar dan Pusat pada Ekstrusi Linear
url: /id/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tambahkan Ground Plane dan Pusatkan pada Linear Extrusion

## Pendahuluan

Selamat datang di panduan komprehensif tentang menguasai linear extrusion menggunakan Aspose.3D untuk .NET. Jika Anda ingin **menambahkan ground plane** ke model Anda dan **mengekspor file Wavefront OBJ** sambil menjaga ekstrusi tetap terpusat, Anda berada di tempat yang tepat. Pada tutorial ini, kita akan membahas teknik linear extrusion, khususnya fokus pada aspek pemusatan dan bagaimana ground plane membantu Anda memvisualisasikan hasil dengan lebih jelas.

## Jawaban Cepat
- **Apa yang dicapai dengan “menambahkan ground plane”?** Ini memberikan referensi visual yang memudahkan melihat di mana ekstrusi berada pada bidang X‑Z.  
- **Format apa yang digunakan untuk mengekspor model?** Scene disimpan sebagai file Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Versi percobaan gratis cukup untuk pengembangan; lisensi permanen diperlukan untuk produksi.  
- **Bisakah saya mengubah panjang ekstrusi?** Ya – ubah parameter kedua dari `LinearExtrusion`.  
- **Apakah pemusatan bersifat opsional?** Menetapkan `Center = true` memusatkan ekstrusi di sekitar profil; `false` menempatkannya ke satu sisi.

## Prasyarat

Sebelum memulai perjalanan menarik ini, pastikan Anda telah menyiapkan prasyarat berikut:

- Pemahaman dasar tentang bahasa pemrograman C#.  
- Visual Studio terpasang di mesin Anda.  
- Perpustakaan Aspose.3D untuk .NET, yang dapat Anda unduh dari [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Pastikan Anda memiliki akses ke [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) untuk referensi sepanjang tutorial.

## Impor Namespace

Untuk memulai, mari impor namespace yang diperlukan. Ini akan menjadi fondasi bagi karya masterpiece pemodelan 3D kita.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Inisialisasi Profil Dasar

Kita mulai dengan mendefinisikan profil persegi panjang yang akan diekstrusi. `RoundingRadius` menambahkan fillet halus pada sudut-sudutnya.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Langkah 2: Buat Scene 3D

Objek `Scene` berfungsi sebagai wadah untuk semua geometri, cahaya, dan kamera.

```csharp
Scene scene = new Scene();
```

## Langkah 3: Buat Node Kiri dan Kanan

Dua node saudara dibuat di bawah root. Satu akan mendemonstrasikan ekstrusi **tanpa** pemusatan, yang lainnya **dengan** pemusatan. Kami juga memindahkan node kiri sehingga dua contoh tidak saling tumpang tindih.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Langkah 4: Lakukan Linear Extrusion pada Node Kiri (Tanpa Pusat)

Di sini kami mengekstrusi profil tanpa pemusatan. Perhatikan flag `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Langkah 5: Tambahkan Ground Plane untuk Referensi (Node Kiri)

Menambahkan kotak tipis berfungsi sebagai **ground plane** sehingga Anda dapat melihat dengan jelas bagaimana ekstrusi berada di atas dasar.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Langkah 6: Lakukan Linear Extrusion pada Node Kanan (Dengan Pusat)

Sekarang kami mengekstrusi profil yang sama tetapi mengaktifkan pemusatan. Geometri akan ditempatkan secara simetris di sekitar asal profil.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Langkah 7: Tambahkan Ground Plane untuk Referensi (Node Kanan)

Ground plane kedua ditambahkan ke node kanan untuk menjaga konsistensi perbandingan visual.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Langkah 8: Ekspor File Wavefront OBJ

Akhirnya, kami **mengekspor Wavefront OBJ** sehingga hasilnya dapat dibuka di viewer 3‑D standar mana pun.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Mengapa Menambahkan Ground Plane?

Menambahkan ground plane memberikan petunjuk visual langsung tentang tinggi dan penyelarasan ekstrusi. Ini sangat membantu ketika Anda perlu membandingkan hasil yang dipusatkan vs. tidak dipusatkan, seperti yang ditunjukkan dalam tutorial ini.

## Masalah Umum & Tips

- **Ground plane tidak terlihat:** Pastikan ketebalan plane (`0.01` pada konstruktor `Box`) cukup kecil sehingga tidak menutupi ekstrusi namun cukup besar untuk dirender.  
- **Ekspor gagal:** Verifikasi direktori output ada dan Anda memiliki izin menulis.  
- **Ekstrusi yang dipusatkan tampak bergeser:** Periksa kembali properti `Center`; `true` memusatkan profil, `false` menempatkannya ke satu sisi.

## Pertanyaan yang Sering Diajukan

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung bahasa .NET seperti C# dan VB.NET.

### Q2: Di mana saya dapat menemukan dukungan untuk pertanyaan terkait Aspose.3D?

A2: Kunjungi [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) untuk dukungan khusus dan diskusi.

### Q3: Apakah ada versi percobaan gratis untuk Aspose.3D untuk .NET?

A3: Ya, Anda dapat mengakses percobaan gratis [di sini](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk .NET?

A4: Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat membeli lisensi Aspose.3D untuk .NET?

A5: Beli lisensi Anda [di sini](https://purchase.aspose.com/buy).

### Q6: Bisakah saya mengekspor scene ke format lain selain OBJ?

A6: Ya, Aspose.3D mendukung banyak format seperti STL, FBX, dan GLTF. Cukup ubah nilai enum `FileFormat` pada metode `Save`.

### Q7: Bagaimana cara mengubah jumlah slice pada ekstrusi?

A7: Sesuaikan properti `Slices` pada konstruktor `LinearExtrusion` untuk mengontrol kepadatan mesh.

---

**Terakhir Diperbarui:** 2026-01-07  
**Diuji Dengan:** Aspose.3D untuk .NET versi terbaru  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}