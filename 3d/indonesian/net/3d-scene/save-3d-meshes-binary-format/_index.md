---
title: Menyimpan Jerat 3D dalam Format Biner Khusus
linktitle: Menyimpan Jerat 3D dalam Format Biner Khusus
second_title: Aspose.3D .NET API
description: Jelajahi dunia 3D dengan Aspose.3D untuk .NET. Pelajari cara menyimpan jerat dalam format biner khusus.
weight: 13
url: /id/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menyimpan Jerat 3D dalam Format Biner Khusus

## Perkenalan

Selamat datang di dunia Aspose.3D untuk .NET, perpustakaan canggih yang memberdayakan pengembang untuk bekerja dengan file 3D dengan mudah. Dalam tutorial ini, kita akan mempelajari proses menyimpan jerat 3D dalam format biner khusus menggunakan Aspose.3D untuk .NET. Panduan ini mengasumsikan Anda memiliki pemahaman dasar tentang C# dan familiar dengan perpustakaan Aspose.3D.

## Prasyarat

Sebelum kita masuk ke tutorial, pastikan Anda memiliki yang berikut ini:

-  Aspose.3D untuk .NET: Pastikan Anda telah menginstal perpustakaan Aspose.3D. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/net/).

- Lingkungan Pengembangan: Siapkan lingkungan pengembangan C# pilihan Anda, seperti Visual Studio.

- Masukkan File 3D: Miliki file 3D (misalnya, test.fbx) yang ingin Anda ubah menjadi format biner khusus.

## Impor Namespace

Dalam kode C# Anda, sertakan namespace yang diperlukan untuk mengakses fungsionalitas Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Langkah 1: Muat File 3D

Muat file 3D Anda menggunakan Aspose.3D. Dalam contoh ini, kita memuat file bernama "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Langkah 2: Tentukan Format Biner Khusus

Tentukan struktur format biner khusus tempat Anda ingin menyimpan jerat 3D. Contoh ini menggunakan struktur dengan MeshBlock, Vertex, dan Triangle sebagai komponennya.

```csharp
// Tata letak memori sebuah simpul adalah
// posisi float[3];
// mengapung[3] biasa;
// mengapung[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Langkah 3: Buka File untuk Menulis

Buka file biner untuk menulis, tempat jerat 3D yang dikonversi akan disimpan:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Langkah 4: Iterasi melalui Node dan Entitas

Kunjungi setiap node dalam adegan 3D dan konversikan entitas mesh ke format biner khusus. Abaikan lampu, kamera, dan entitas non-mesh lainnya:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (lanjutkan pemrosesan)
    }
    return true;
});
```

## Langkah 5: Konversi dan Tulis Titik Kontrol dan Segitiga

Untuk setiap entitas mesh, konversikan titik kontrol ke ruang dunia dan tuliskan ke file biner bersama dengan indeks segitiga:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Tata letak memori mesh adalah:
// float[16] transform_matrix;
// int jumlah_simpul;
// int indeks_hitungan;
// simpul[vertices_count] simpul;
// indeks ushort[indices_count];


//tulis transformasi
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//tulis jumlah simpul/indeks
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//menulis simpul dan indeks
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Kesimpulan

Dalam tutorial ini, kami membahas proses menyimpan jerat 3D dalam format biner khusus menggunakan Aspose.3D untuk .NET. Pustaka canggih ini menyediakan alat yang dibutuhkan pengembang untuk memanipulasi file 3D dengan lancar. Bereksperimenlah dengan berbagai format dan pengaturan untuk membuka potensi penuh Aspose.3D dalam proyek Anda.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk .NET dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung bahasa .NET, namun Anda dapat menjelajahi opsi kompatibilitas untuk bahasa lain.

### Q2: Di mana saya dapat menemukan contoh dan sumber tambahan?

 A2: Itu[Forum Aspose.3D](https://forum.aspose.com/c/3d/18)adalah tempat yang bagus untuk mendapatkan dukungan, contoh, dan terlibat dengan komunitas.

### Q3: Apakah ada versi uji coba yang tersedia untuk Aspose.3D?

 A3: Ya, Anda bisa mendapatkan uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A4: Kunjungi[Link ini](https://purchase.aspose.com/temporary-license/) untuk mendapatkan lisensi sementara untuk tujuan pengujian.

### Q5: Dapatkah saya membeli Aspose.3D untuk .NET?

 A5: Ya, Anda dapat membeli Aspose.3D dari[halaman pembelian](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
