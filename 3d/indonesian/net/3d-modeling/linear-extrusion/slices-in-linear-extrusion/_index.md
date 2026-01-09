---
date: 2026-01-09
description: Pelajari cara membuat adegan 3D dan menyimpan model 3D menggunakan Aspose.3D
  untuk .NET, termasuk mengekspor Wavefront OBJ dan irisan ekstrusi linier.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Buat Adegan 3D dengan Irisan Ekstrusi Linear
url: /id/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat Adegan 3D dengan Irisan Ekstrusi Linear

## Pendahuluan

Selamat datang di dunia desain 3D menggunakan Aspose.3D untuk .NET! Dalam tutorial ini Anda akan **membuat adegan 3d** objek, menerapkan ekstrusi linear dengan jumlah irisan yang disesuaikan, dan akhirnya **menyimpan model 3d** sebagai file Wavefront OBJ. Baik Anda membuat prototipe cepat atau visualisasi siap produksi, langkah‑langkah di bawah ini akan menunjukkan **cara menggunakan Aspose** untuk menghasilkan geometri berkualitas tinggi langsung dari C#.

## Jawaban Cepat
- **Apa arti “create 3d scene”?** Itu berarti membuat objek Scene yang menampung semua entitas 3D (mesh, lampu, kamera).  
- **Format apa yang digunakan untuk ekspor?** Contoh ini mengekspor ke **Wavefront OBJ** (`export wavefront obj`).  
- **Berapa banyak irisan yang dapat saya atur?** Anda dapat mengatur nilai integer apa pun; demo menunjukkan 2 dan 10 irisan.  
- **Apakah saya memerlukan lisensi?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.  
- **Bisakah saya menjalankannya di .NET Core?** Ya, Aspose.3D mendukung .NET Framework dan .NET Core.

## Prasyarat

- **Pustaka Aspose.3D untuk .NET:** Pastikan Anda telah menginstal pustaka Aspose.3D. Anda dapat mengunduhnya dari [di sini](https://releases.aspose.com/3d/net/).
- **Integrated Development Environment (IDE):** Gunakan IDE pilihan Anda yang kompatibel dengan pengembangan .NET.
- **Pemahaman Dasar C#:** Kenali dasar-dasar bahasa pemrograman C#.
- **Keinginan untuk Menjelajahi Desain 3D:** Semangat untuk membuat model 3D yang memukau secara visual!

## Impor Namespace

Untuk memulai perjalanan desain 3D Anda dengan Aspose.3D, Anda perlu mengimpor namespace yang diperlukan. Ini memastikan kode Anda dapat mengakses kelas dan fungsionalitas yang dibutuhkan.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Cara membuat adegan 3d dengan Ekstrusi Linear

Di bawah ini kami akan menjelaskan setiap langkah yang diperlukan untuk membangun adegan, menerapkan ekstrusi, dan **menyimpan model 3d** sebagai file OBJ. Penjelasan ditulis dengan gaya percakapan sehingga Anda dapat mengikutinya dengan mudah.

### Langkah 1: Inisialisasi Profil Dasar

Pertama, kami mendefinisikan bentuk 2‑D yang akan diekstrusi. Dalam kasus ini sebuah persegi panjang dengan sudut melengkung.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Langkah 2: Buat Adegan 3D

Objek `Scene` adalah wadah untuk semua geometri, lampu, dan kamera – inti dari **pembuatan adegan 3d**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Langkah 3: Buat Node Kiri dan Kanan

Kami menambahkan dua node anak ke akar adegan. Satu akan menggunakan jumlah irisan rendah, yang lainnya jumlah irisan lebih tinggi, sehingga Anda dapat melihat perbedaan visual.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Langkah 4: Lakukan Ekstrusi Linear pada Node Kiri

Di sini kami mengekstrusi persegi panjang dengan **2 irisan**. Irisan yang lebih sedikit menghasilkan tampilan yang lebih kasar.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Langkah 5: Lakukan Ekstrusi Linear pada Node Kanan

Sekarang kami mengekstrusi profil yang sama tetapi dengan **10 irisan**, menghasilkan permukaan yang lebih halus.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Langkah 6: Simpan Adegan 3D

Akhirnya, kami mengekspor adegan ke file Wavefront OBJ. Ini menunjukkan **cara menyimpan obj** dan **mengekspor wavefront obj** menggunakan Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| File OBJ muncul kosong | Jalur output tidak benar atau tidak memiliki izin menulis. | Pastikan direktori ada dan aplikasi memiliki akses menulis. |
| Irisan tidak memengaruhi kelancaran | Nilai `Slices` terlalu rendah untuk ukuran geometri. | Tingkatkan jumlah irisan atau sesuaikan dimensi profil. |
| Pengecualian lisensi | Menjalankan tanpa lisensi yang valid pada build non‑trial. | Terapkan lisensi sementara atau permanen menggunakan `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?**  
A: Aspose.3D terutama dirancang untuk .NET, tetapi Anda dapat menjelajahi opsi interoperabilitas dengan bahasa seperti Python menggunakan binding .NET.

**Q: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?**  
A: Lihat dokumentasi [di sini](https://reference.aspose.com/3d/net/) untuk informasi mendalam tentang kemampuan dan penggunaan Aspose.3D.

**Q: Apakah ada percobaan gratis untuk Aspose.3D untuk .NET?**  
A: Ya, Anda dapat mengambil percobaan gratis [di sini](https://releases.aspose.com/) untuk menjelajahi fitur pustaka sebelum melakukan pembelian.

**Q: Bagaimana saya dapat mendapatkan dukungan teknis untuk Aspose.3D untuk .NET?**  
A: Kunjungi forum Aspose.3D [di sini](https://forum.aspose.com/c/3d/18) untuk meminta bantuan dan berinteraksi dengan komunitas.

**Q: Bisakah saya menggunakan lisensi sementara untuk Aspose.3D untuk .NET?**  
A: Ya, dapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara **membuat adegan 3d**, menerapkan ekstrusi linear dengan jumlah irisan yang disesuaikan, dan **menyimpan model 3d** sebagai file Wavefront OBJ menggunakan Aspose.3D untuk .NET. Ini baru permulaan perjalanan desain 3D Anda—silakan bereksperimen dengan profil berbeda, nilai irisan, dan format ekspor untuk memanfaatkan potensi penuh **pemodelan 3d c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2026-01-09  
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET  
**Penulis:** Aspose