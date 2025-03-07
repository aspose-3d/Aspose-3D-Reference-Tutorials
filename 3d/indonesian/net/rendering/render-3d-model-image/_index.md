---
title: Merender Gambar Model 3D dari Kamera
linktitle: Merender Gambar Model 3D dari Kamera
second_title: Aspose.3D .NET API
description: Jelajahi dunia rendering 3D dengan Aspose.3D untuk .NET. Pelajari cara membuat visualisasi menawan dengan mudah menggunakan panduan langkah demi langkah kami.
weight: 11
url: /id/net/rendering/render-3d-model-image/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Merender Gambar Model 3D dari Kamera

## Perkenalan
Membuat visualisasi 3D yang menakjubkan adalah aspek menarik dalam pengembangan perangkat lunak, dan dengan Aspose.3D untuk .NET, Anda dapat menghidupkan model 3D Anda. Dalam tutorial ini, kami akan memandu Anda dalam merender gambar model 3D dari kamera menggunakan Aspose.3D, memberikan petunjuk langkah demi langkah dan wawasan berharga.
## Prasyarat
Sebelum kita mendalami proses rendering, pastikan Anda memiliki prasyarat berikut:
-  Aspose.3D untuk .NET Library: Unduh dan instal perpustakaan dari[tautan unduhan](https://releases.aspose.com/3d/net/).
- Model 3D: Siapkan file model 3D (misalnya Aspose3D.obj) yang ingin Anda render.
- Lingkungan Pengembangan .NET: Pastikan Anda memiliki lingkungan pengembangan .NET yang berfungsi dan siap.
## Impor Namespace
Dalam proyek .NET Anda, sertakan namespace yang diperlukan untuk Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## Langkah 1: Muat Adegan 3D
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## Langkah 2: Buat Kamera
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## Langkah 3: Tambahkan Lampu ke Pemandangan
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## Langkah 4: Tentukan Opsi Render Gambar
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## Langkah 5: Render Adegan
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## Kesimpulan
Selamat! Anda telah berhasil merender gambar model 3D dari kamera menggunakan Aspose.3D untuk .NET. Jangan ragu untuk bereksperimen dengan berbagai model, sudut kamera, dan pengaturan pencahayaan untuk menyempurnakan visualisasi 3D Anda.
## FAQ
### T: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan alat pemodelan 3D lainnya?
J: Aspose.3D mendukung berbagai format model 3D, sehingga kompatibel dengan banyak alat pemodelan populer.
### T: Bagaimana cara memecahkan masalah rendering?
 A: Periksa Aspose.3D[forum](https://forum.aspose.com/c/3d/18) untuk dukungan dan solusi terhadap masalah rendering umum.
### T: Apakah tersedia uji coba gratis?
A: Ya, Anda dapat menjelajahi fitur Aspose.3D dengan memperoleh a[uji coba gratis](https://releases.aspose.com/).
### T: Di mana saya dapat menemukan dokumentasi lengkap?
 J: Lihat[dokumentasi](https://reference.aspose.com/3d/net/) untuk panduan mendalam tentang Aspose.3D untuk .NET.
### T: Bagaimana cara membeli Aspose.3D untuk .NET?
 J: Kunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk mendapatkan lisensi yang paling sesuai dengan kebutuhan Anda.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
