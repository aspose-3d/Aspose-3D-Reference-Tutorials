---
date: 2026-01-17
description: Pelajari cara menampilkan daftar properti material, mengubah warna difus,
  dan memodifikasi atribut material 3D menggunakan Aspose.3D untuk .NET. Contoh kode
  langkah demi langkah disertakan.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Daftar Properti Material dalam Adegan 3D dengan Aspose.3D
url: /id/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Daftar Properti Material dalam Adegan 3D dengan Aspose.3D

## Pendahuluan

Jika Anda perlu **mendaftar properti material** dari model 3D dan kemudian menyesuaikan hal‑hal seperti warna difus, Anda berada di tempat yang tepat. Aspose.3D untuk .NET menyediakan API berorientasi‑objek yang bersih yang memungkinkan Anda memeriksa, mengambil, dan memodifikasi atribut material tanpa meninggalkan kode C# Anda. Dalam tutorial ini kami akan menunjukkan cara memuat adegan, menelusuri properti materialnya, dan mengubah nilai seperti komponen difus—sehingga Anda dapat memberikan tampilan yang tepat pada model Anda.

## Jawaban Cepat
- **Apa tujuan utama?** Mendaftar properti material dan memodifikasinya (misalnya, warna difus).  
- **Perpustakaan apa yang diperlukan?** Aspose.3D untuk .NET.  
- **Apakah saya memerlukan lisensi?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.  
- **Format file yang didukung?** FBX, OBJ, STL, STL‑ASCII, 3MF, dan lainnya.  
- **Waktu implementasi tipikal?** Sekitar 10‑15 menit untuk skrip dasar yang menampilkan properti.

## Apa itu **list material properties**?
Mendaftar properti material berarti mengiterasi `PropertyCollection` sebuah material untuk membaca setiap nama properti dan nilai saat ini. Ini berguna untuk debugging, inspeksi visual, atau membangun kontrol UI yang memungkinkan pengguna menyesuaikan pengaturan material pada waktu berjalan.

## Mengapa menggunakan Aspose.3D untuk **mengakses properti material**?
- **Tanpa konverter eksternal** – bekerja langsung dengan objek .NET native.  
- **Model properti yang kaya** – mendukung atribut khusus FBX selain nilai PBR standar.  
- **Lintas‑platform** – berfungsi pada .NET Framework, .NET Core, dan .NET 5/6+.

## Prasyarat

- Aspose.3D untuk .NET terpasang dalam proyek Anda. Unduh [di sini](https://releases.aspose.com/3d/net/).
- Sebuah folder di disk untuk menyimpan file sumber 3‑D Anda (misalnya, file FBX dengan tekstur tersemat).

Setelah Anda menyiapkan hal‑hal dasar, mari masuk ke kode.

## Impor Namespace

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Langkah 1: Muat Adegan 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Langkah 2: **Akses properti material** dari node pertama

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Langkah 3: **Daftar properti material** – lihat setiap pasangan nama/nilai

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Langkah 4: **Cara mengubah difus** – modifikasi properti Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Langkah 5: **Ambil properti berdasarkan nama** – dapatkan instance bertipe kuat

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Langkah 6: Telusuri properti milik properti itu sendiri (lanjutan)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Cara **mengubah warna material 3d** selain difus
Jika Anda perlu memengaruhi warna spekular, ambient, atau emisif, cukup ganti `"Diffuse"` dengan `"Specular"` atau `"Ambient"` pada penugasan `props["..."]` di atas. Struktur `Vector3` atau `Vector4` yang sama tetap berlaku.

## Kesulitan Umum & Tips
- **Sensitivitas huruf pada nama properti** – kunci properti Aspose.3D bersifat case‑sensitive; gunakan nama persis yang ditampilkan pada output daftar.  
- **Properti tidak ada** – Tidak semua material mengekspos setiap atribut PBR. Periksa `props.ContainsKey("Specular")` sebelum mengakses.  
- **Menyimpan perubahan** – Setelah memodifikasi properti, panggil `scene.Save("output.fbx");` untuk menyimpan perubahan.

## Kesimpulan

Anda kini telah mempelajari cara **mendaftar properti material**, **mengambil properti berdasarkan nama**, dan **mengubah warna difus** (atau atribut material lainnya) menggunakan Aspose.3D untuk .NET. Bereksperimenlah dengan berbagai tipe properti untuk menyempurnakan tampilan aset 3‑D Anda.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, termasuk FBX, STL, dan banyak lagi.

### Q2: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D untuk .NET?

A2: Kunjungi [di sini](https://purchase.aspose.com/temporary-license/) untuk memperoleh lisensi sementara.

### Q3: Apakah ada forum komunitas untuk pengguna Aspose.3D?

A3: Ya, Anda dapat menemukan dukungan dan diskusi di [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Di mana saya dapat menemukan dokumentasi detail untuk Aspose.3D untuk .NET?

A4: Lihat [dokumentasi](https://reference.aspose.com/3d/net/) untuk panduan lengkap.

### Q5: Bisakah saya mencoba Aspose.3D untuk .NET secara gratis sebelum membeli?

A5: Tentu! Unduh [versi percobaan gratis](https://releases.aspose.com/) untuk menjelajahi fiturnya.

## Pertanyaan yang Sering Diajukan

**T: Apa yang dimaksud dengan `Vector3(1, 0, 1)`?**  
J: Itu menetapkan warna difus menjadi magenta (merah = 1, hijau = 0, biru = 1) dalam ruang warna linear.

**T: Apakah saya harus memanggil `scene.Save` setelah mengubah properti?**  
J: Ya, menyimpan adegan menuliskan modifikasi Anda ke disk; jika tidak, perubahan hanya berada di memori.

**T: Bisakah saya menelusuri atribut FBX khusus?**  
J: Tentu. `PropertyCollection` akan mencakup semua atribut khusus, yang dapat diakses via `GetProperty("customName")`.

**T: Apakah ada cara untuk memperbarui beberapa material secara batch?**  
J: Lakukan loop melalui `scene.RootNode.ChildNodes` dan ulangi langkah‑langkah modifikasi properti untuk setiap material.

**T: Apakah Aspose.3D mendukung .NET 6?**  
J: Ya, perpustakaan ini sepenuhnya kompatibel dengan .NET 6 dan versi selanjutnya.

---

**Terakhir Diperbarui:** 2026-01-17  
**Diuji Dengan:** Aspose.3D 24.11 untuk .NET  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}