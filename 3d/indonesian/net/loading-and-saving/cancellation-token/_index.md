---
title: Menggunakan CancellationToken
linktitle: Menggunakan CancellationToken
second_title: Aspose.3D .NET API
description: Jelajahi dunia pemodelan 3D yang mulus dengan Aspose.3D untuk .NET. Pelajari cara memuat dan menyimpan dokumen 3D secara efisien menggunakan CancellationToken.
weight: 10
url: /id/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menggunakan CancellationToken

## Perkenalan

Selamat datang di panduan komprehensif kami tentang penggunaan Aspose.3D untuk .NET guna menyempurnakan proyek pemodelan dan rendering 3D Anda. Aspose.3D adalah perpustakaan canggih yang memberdayakan pengembang .NET untuk bekerja dengan file 3D secara lancar. Dalam tutorial ini, kita akan mempelajari aspek pemuatan dan penyimpanan, khususnya berfokus pada penggunaan CancellationToken untuk pengelolaan tugas asinkron yang efisien.

## Prasyarat

Sebelum kita memulai perjalanan ini, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk .NET: Unduh dan instal perpustakaan dari[Di Sini](https://releases.aspose.com/3d/net/).
- Lingkungan .NET: Pastikan Anda telah menyiapkan lingkungan pengembangan .NET yang kompatibel.
- Pemahaman Dasar C#: Disarankan untuk menguasai bahasa pemrograman C#.

## Impor Namespace

Untuk memulai, pastikan Anda menyertakan namespace yang diperlukan dalam proyek Anda. Namespace ini akan memberikan akses ke fungsionalitas yang diperlukan untuk manipulasi file 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Memuat dan Menyimpan - Menggunakan CancellationToken

### Langkah 1: Buat CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Di sini, kami membuat instance CancellationTokenSource, komponen penting untuk mengelola pembatalan dalam operasi asinkron.

### Langkah 2: Inisialisasi Pemandangan 3D

```csharp
Scene scene = new Scene();
```

Buat sebuah instance dari kelas Scene. Ini akan menjadi kanvas untuk aktivitas pemodelan 3D Anda.

### Langkah 3: Tetapkan Batas Waktu CancellationToken

```csharp
cts.CancelAfter(1000);
```

 Atur batas waktu pembatalan menggunakan`CancelAfter` metode. Dalam contoh ini, batas waktu diatur ke 1000 milidetik (1 detik).

### Langkah 4: Buka Dokumen 3D

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Cobalah untuk membuka dokumen 3D dalam jangka waktu yang ditentukan. Itu`cts.Token` parameter memastikan bahwa operasi dapat dibatalkan jika melebihi batas waktu yang ditetapkan.

### Langkah 5: Tangani Pengecualian Impor

Jika terjadi ImportException, tangani dengan baik dengan memeriksa apakah hal tersebut disebabkan oleh OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Kesimpulan

Selamat! Anda telah berhasil menavigasi proses penggunaan Aspose.3D untuk .NET dengan CancellationToken untuk mengelola pemuatan dokumen 3D. Teknik ini memastikan operasi impor yang efisien dan tepat waktu, sehingga meningkatkan kinerja aplikasi 3D Anda secara keseluruhan.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan semua format file 3D?

 A1: Aspose.3D mendukung berbagai format file 3D, termasuk FBX, STL, OBJ, dan banyak lagi. Mengacu kepada[dokumentasi](https://reference.aspose.com/3d/net/) untuk daftar lengkapnya.

### Q2: Bagaimana saya bisa mendapatkan lisensi sementara untuk Aspose.3D?

 A2: Dapatkan lisensi sementara dengan mengunjungi[Link ini](https://purchase.aspose.com/temporary-license/).

### Q3: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A3: Bergabunglah dengan diskusi komunitas di[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Dapatkah saya mencoba Aspose.3D secara gratis sebelum membeli?

 A4: Ya, jelajahi fitur-fiturnya dengan uji coba gratis yang tersedia[Di Sini](https://releases.aspose.com/).

### Q5: Apa versi terbaru Aspose.3D untuk .NET?

 A5: Tetap up-to-date dengan memeriksa[Unduh Halaman](https://releases.aspose.com/3d/net/) untuk rilis terbaru.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
