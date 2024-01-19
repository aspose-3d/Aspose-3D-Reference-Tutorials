---
title: Membuat Adegan dengan Tekstur Tertanam
linktitle: Membuat Adegan dengan Tekstur Tertanam
second_title: Aspose.3D .NET API
description: Buat pemandangan 3D yang memukau dengan tekstur tertanam menggunakan Aspose.3D untuk .NET. Ikuti panduan langkah demi langkah kami untuk hasil yang menakjubkan.
type: docs
weight: 10
url: /id/net/materials/create-scene-embedded-texture/
---
## Perkenalan
Selamat datang di dunia grafis 3D yang menarik dengan Aspose.3D untuk .NET! Dalam tutorial komprehensif ini, kami akan memandu Anda melalui proses pembuatan pemandangan 3D yang menakjubkan dengan tekstur tertanam menggunakan Aspose.3D, perpustakaan yang kuat dan serbaguna untuk pengembang .NET.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
- Pemahaman dasar tentang pemrograman C# dan .NET.
- Visual Studio diinstal pada mesin Anda.
-  Aspose.3D untuk perpustakaan .NET, yang dapat Anda unduh[Di Sini](https://releases.aspose.com/3d/net/).
- Keakraban dengan konsep grafik 3D dan pembuatan pemandangan.
## Impor Namespace
Mulailah dengan mengimpor namespace yang diperlukan ke dalam proyek Anda. Namespace ini akan memberi Anda alat dan fungsi yang diperlukan untuk manipulasi grafis 3D.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Langkah 1: Membuat Adegan
Mulailah dengan membuat adegan 3D baru menggunakan Aspose.3D untuk .NET. Ini akan berfungsi sebagai kanvas untuk karya 3D Anda.
```csharp
// Buat file FBX dengan tekstur tertanam
Scene scene = new Scene();
```
## Langkah 2: Membuat Tekstur Tertanam
Sekarang, mari tambahkan kesan visual pada pemandangan Anda dengan menyematkan tekstur. Kami akan membuat tekstur dengan konten khusus dan memberinya nama file.
```csharp
// Buat tekstur tertanam
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // Nama file diperlukan jika tekstur tersemat digunakan.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Langkah 3: Membuat Materi
Selanjutnya, buat material untuk objek 3D Anda, dengan menggabungkan tekstur dan properti kustom yang dibuat sebelumnya.
```csharp
// Buat materi dengan properti khusus
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Langkah 4: Membuat Objek 3D
Sekarang, mari hidupkan pemandangan Anda dengan menambahkan objek 3D. Dalam contoh ini, kita akan menggunakan torus dan menerapkan material yang baru saja Anda buat.
```csharp
// Buat torus dengan menerapkan material yang dibuat sebelumnya
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Langkah 5: Menyimpan Adegan
Terakhir, simpan karya Anda ke sebuah file. Dalam contoh ini, kami akan menyimpannya dalam format FBX.
```csharp
// Simpan adegan ke file
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Selamat! Anda telah berhasil membuat adegan 3D dengan tekstur tertanam menggunakan Aspose.3D untuk .NET.
## Kode Sumber CreateTextureContent
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Kesimpulan
Dalam tutorial ini, kita menjelajahi dasar-dasar pembuatan adegan 3D yang menakjubkan secara visual dengan tekstur tersemat menggunakan Aspose.3D untuk .NET. Berbekal pengetahuan ini, Anda dapat mengeluarkan kreativitas Anda dan membangun aplikasi 3D yang menawan.

## Pertanyaan yang Sering Diajukan

### T: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?
J: Aspose.3D terutama dirancang untuk .NET, namun ada perpustakaan serupa yang tersedia untuk bahasa lain.
### T: Bagaimana cara menerapkan animasi ke adegan 3D saya?
J: Aspose.3D menyediakan kemampuan animasi; lihat dokumentasi untuk instruksi rinci.
### T: Apakah ada versi uji coba yang tersedia untuk Aspose.3D untuk .NET?
 A: Ya, Anda dapat mendownload versi trialnya[Di Sini](https://releases.aspose.com/).
### T: Di mana saya bisa mendapatkan dukungan dan sumber daya tambahan?
 J: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.
### T: Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?
 A: Ya, Anda dapat membeli lisensinya[Di Sini](https://purchase.aspose.com/buy).