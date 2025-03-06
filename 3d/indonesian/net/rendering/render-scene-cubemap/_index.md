---
title: Merender Adegan menjadi Peta Kubus dengan Enam Wajah
linktitle: Merender Adegan menjadi Peta Kubus dengan Enam Wajah
second_title: Aspose.3D .NET API
description: Buat peta kubus yang menakjubkan dengan Aspose.3D untuk .NET. Ikuti panduan langkah demi langkah kami untuk merender adegan 3D menjadi peta kubus bermuka enam yang menawan.
weight: 14
url: /id/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Merender Adegan menjadi Peta Kubus dengan Enam Wajah

## Perkenalan
Selamat datang di panduan langkah demi langkah dalam merender adegan menjadi peta kubus dengan enam wajah menggunakan Aspose.3D untuk .NET. Dalam tutorial ini, kami akan memandu Anda melalui proses pembuatan peta kubus yang menakjubkan dengan merender adegan 3D. Aspose.3D adalah .NET API canggih yang menyederhanakan manipulasi grafik 3D, dan dengan panduan ini, Anda akan memanfaatkan kemampuannya untuk membuat peta kubus yang menawan.
## Prasyarat
Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:
- Pengetahuan tentang pengembangan C# dan .NET.
-  Aspose.3D untuk .NET diinstal. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/net/).
- File adegan 3D dalam format GLB (misalnya, "VirtualCity.glb") untuk rendering.
## Impor Namespace
Mulailah dengan mengimpor namespace yang diperlukan untuk Aspose.3D dalam kode C# Anda:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Langkah 1: Muat Adegan
Muat file adegan 3D menggunakan kode berikut:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Langkah 2: Buat Kamera dan Lampu
Buat kamera dan dua lampu untuk menerangi pemandangan:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Langkah 3: Buat Renderer dan Target Render
Buat penyaji dan target render peta kubus dengan tekstur kedalaman:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Langkah 4: Simpan Wajah Cubemap
Simpan setiap sisi peta kubus ke disk dengan nama file tertentu:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Kesimpulan
Selamat! Anda telah berhasil merender adegan 3D ke dalam peta kubus menggunakan Aspose.3D untuk .NET. Jelajahi opsi penyesuaian lebih lanjut dan tingkatkan proyek grafis 3D Anda dengan API canggih ini.
## Pertanyaan yang Sering Diajukan
### T: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan format file 3D lainnya?
Ya, Aspose.3D mendukung berbagai format file 3D, memberikan fleksibilitas dalam proyek Anda.
### T: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?
 Mengunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.
### T: Apakah tersedia uji coba gratis?
 Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).
### T: Dapatkah saya merender adegan dengan animasi menggunakan Aspose.3D?
Sangat! Aspose.3D mendukung rendering adegan 3D animasi.
### T: Di mana saya dapat menemukan dokumentasi detailnya?
 Mengacu kepada[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/net/) untuk informasi mendalam.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
