---
title: Menangkap Area Pandang dalam Pemandangan 3D
linktitle: Menangkap Area Pandang dalam Pemandangan 3D
second_title: Aspose.3D .NET API
description: Pelajari cara menangkap area pandang 3D yang menakjubkan menggunakan Aspose.3D untuk .NET. Panduan langkah demi langkah untuk merender adegan dengan fleksibilitas.
weight: 11
url: /id/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menangkap Area Pandang dalam Pemandangan 3D

## Perkenalan

Dalam bidang grafik dan visualisasi 3D, menangkap area pandang adalah keterampilan penting yang meningkatkan kedalaman dan detail pemandangan Anda. Aspose.3D untuk .NET memberikan solusi tangguh untuk merender dan memanipulasi adegan 3D. Tutorial ini akan memandu Anda melalui proses menangkap area pandang dalam adegan 3D menggunakan Aspose.3D, memungkinkan Anda membuat visualisasi menakjubkan dengan mudah.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk Perpustakaan .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).

## Impor Namespace

Untuk memulai, impor namespace yang diperlukan ke proyek .NET Anda:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Langkah 1: Muat Adegan 3D yang Ada

Mulailah dengan memuat adegan 3D yang ada ke dalam proyek Anda. Cuplikan kode berikut menunjukkan hal ini:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Langkah 2: Buat Kamera

Selanjutnya, buat sebuah instance kamera dan atur posisi dan targetnya:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Langkah 3: Tambahkan Pencahayaan ke Pemandangan

Sempurnakan pemandangan Anda dengan menambahkan sumber cahaya. Cuplikan kode di bawah ini menunjukkan cara membuat titik cahaya:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Langkah 4: Konfigurasikan Renderer dan Target Render

Siapkan penyaji dan buat target render untuk menangkap adegan:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (lanjutan pada langkah selanjutnya)
    }
}
```

## Langkah 5: Tentukan Area Pandang dan Render

Tentukan area pandang dan render adegan untuk menghasilkan gambar keluaran:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Langkah 6: Ubah Area Pandang dan Render Lagi

Ubah area pandang dan render pemandangan sekali lagi, yang menunjukkan fleksibilitas Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Lanjutkan bereksperimen dengan konfigurasi berbeda untuk mencapai efek visual yang diinginkan.

## Kesimpulan

Dalam tutorial ini, kami menjelajahi proses menangkap area pandang dalam adegan 3D menggunakan Aspose.3D untuk .NET. Dengan memanfaatkan fitur-fitur canggihnya, Anda dapat meningkatkan proyek grafis 3D Anda ke tingkat yang lebih tinggi, memberikan pengalaman visual yang menawan.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memastikan kompatibilitas dengan berbagai alat desain.

### Q2: Dapatkah saya menggunakan Aspose.3D untuk pengembangan game?

A2: Meskipun Aspose.3D terutama dirancang untuk grafis dan visualisasi, fungsinya dapat melengkapi aspek-aspek tertentu dari pengembangan game.

### Q3: Di mana saya dapat menemukan contoh dan dokumentasi tambahan?

 A3: Jelajahi secara komprehensif[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/net/) untuk lebih banyak contoh dan informasi rinci.

### Q4: Apakah tersedia uji coba gratis?

 A4: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q5: Bagaimana saya bisa mencari bantuan atau berpartisipasi dalam komunitas?

 A5: Bergabunglah dengan komunitas Aspose.3D di[forum dukungan](https://forum.aspose.com/c/3d/18) untuk bantuan dan kerjasama.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
