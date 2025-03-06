---
title: Menerapkan Efek Lensa Fisheye dengan Aspose.3D untuk .NET
linktitle: Menerapkan Efek Lensa Mata Ikan pada Pemandangan 3D
second_title: Aspose.3D .NET API
description: Sempurnakan adegan 3D Anda dengan Aspose.3D untuk .NET! Pelajari cara menerapkan efek lensa mata ikan yang menawan langkah demi langkah. Unduh sekarang!
weight: 12
url: /id/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menerapkan Efek Lensa Fisheye dengan Aspose.3D untuk .NET

## Perkenalan
Apakah Anda ingin meningkatkan daya tarik visual adegan 3D Anda? Selami dunia efek lensa fisheye yang menakjubkan dengan Aspose.3D untuk .NET. Tutorial ini akan memandu Anda langkah demi langkah tentang cara menerapkan efek lensa mata ikan pada pemandangan 3D Anda, sehingga memberikan perspektif yang unik dan menawan.
## Prasyarat
Sebelum kita mulai, pastikan Anda memiliki prasyarat berikut:
-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D untuk .NET. Jika belum, Anda dapat mendownloadnya[Di Sini](https://releases.aspose.com/3d/net/).
-  Contoh Adegan 3D: Kami akan bekerja dengan contoh file adegan 3D (VirtualCity.glb). Anda dapat menggunakan adegan Anda sendiri atau mengunduh sampel dari[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/net/).
## Impor Namespace
Dalam proyek .NET Anda, sertakan namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D. Tambahkan namespace berikut di awal kode Anda:
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
## Langkah 1: Muat Adegan 3D
Muat file adegan 3D ke dalam proyek Anda menggunakan kode berikut:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Langkah 2: Siapkan Kamera dan Lampu
Buat kamera dan lampu untuk menyempurnakan aspek visual pemandangan Anda. Sesuaikan parameter seperti NearPlane, FarPlane, dan RotationMode sesuai kebutuhan:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Langkah 3: Buat Renderer dan Target Render
Siapkan perender dan buat target render untuk peta kubus dan tekstur 2D:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Langkah 4: Terapkan Efek Lensa Fisheye
Jalankan pasca-pemrosesan efek lensa mata ikan pada peta kubus yang dirender:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Kesimpulan
Selamat! Anda telah berhasil menerapkan efek lensa mata ikan ke pemandangan 3D Anda menggunakan Aspose.3D untuk .NET. Bereksperimenlah dengan pemandangan dan parameter berbeda untuk melepaskan kreativitas Anda.
## Pertanyaan yang Sering Diajukan
### Bisakah saya menerapkan efek mata ikan pada pemandangan 3D apa pun?
Ya, Anda dapat menerapkan efek mata ikan ke pemandangan 3D mana pun. Pastikan adegan dimuat dan diterangi dengan benar untuk hasil optimal.
### Apa pentingnya mengatur bidang pandang (fov) menjadi 360 derajat?
Bidang pandang 360 derajat memastikan proyeksi bola yang lengkap, menciptakan efek mata ikan yang menakjubkan.
### Bagaimana cara menyesuaikan pencahayaan dalam adegan 3D saya?
Anda dapat menyesuaikan properti lampu, seperti posisi, jenis, dan warna, untuk mendapatkan efek pencahayaan yang diinginkan.
### Apakah ada batasan ukuran adegan 3D yang dapat diproses?
Ukuran adegan 3D terutama dibatasi oleh sumber daya sistem. Pastikan perangkat keras Anda dapat menangani ukuran pemandangan Anda.
### Bisakah saya menggunakan format keluaran lain selain PNG untuk hasil efek mata ikan?
Ya, Anda dapat memodifikasi kode untuk menyimpan keluaran dalam format gambar berbeda berdasarkan kebutuhan Anda.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
