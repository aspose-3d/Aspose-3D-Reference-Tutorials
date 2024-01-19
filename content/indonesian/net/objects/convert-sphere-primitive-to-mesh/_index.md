---
title: Mengubah Sphere Primitif menjadi Mesh
linktitle: Mengubah Sphere Primitif menjadi Mesh
second_title: Aspose.3D .NET API
description: Jelajahi Aspose.3D untuk .NET dan konversi Sphere Mesh ke Triangle Mesh dengan mudah dengan tata letak memori khusus. Ikuti panduan langkah demi langkah kami untuk integrasi yang lancar.
type: docs
weight: 16
url: /id/net/objects/convert-sphere-primitive-to-mesh/
---
## Perkenalan
Apakah Anda ingin memanfaatkan kekuatan Aspose.3D untuk .NET untuk mengubah Sphere Mesh menjadi Triangle Mesh dengan tata letak memori khusus? Panduan langkah demi langkah ini akan memandu Anda melalui prosesnya, sehingga memudahkan bahkan bagi pemula untuk mengikutinya. Di akhir tutorial ini, Anda akan memiliki pemahaman yang kuat tentang cara mencapai hal ini menggunakan Aspose.3D untuk .NET.
## Prasyarat
Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:
- Pengetahuan dasar tentang pemrograman .NET.
-  Aspose.3D untuk perpustakaan .NET diinstal. Anda dapat mengunduhnya dari[Aspose.3D untuk halaman unduhan .NET](https://releases.aspose.com/3d/net/).
- Familiar dengan bahasa pemrograman C#.
## Impor Namespace
Dalam proyek C# Anda, pastikan untuk mengimpor namespace yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Langkah 1: Inisialisasi Objek Adegan
```csharp
// Inisialisasi objek adegan
Scene scene = new Scene();
```
## Langkah 2: Inisialisasi Objek Kelas Node
```csharp
// Inisialisasi objek kelas Node
Node cubeNode = new Node("sphere");
```
## Langkah 3: Ubah Sphere Mesh menjadi Typed TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Langkah 4: Dapatkan Data Vertex dalam Struktur yang Disesuaikan
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Langkah 5: Dapatkan Indeks 32-bit dan 16-bit
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Langkah 6: Tulis Data Vertex dan Indeks ke Memory Stream
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Langkah 7: Arahkan Node ke Geometri Mesh
```csharp
cubeNode.Entity = sphere;
```
## Langkah 8: Tambahkan Node ke Adegan
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Langkah 9: Simpan Adegan 3D
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Langkah 10: Tampilkan Hasil
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## Contoh Kode Sumber MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Kesimpulan
Selamat! Anda telah berhasil mengonversi Sphere Mesh menjadi Triangle Mesh dengan tata letak memori khusus menggunakan Aspose.3D untuk .NET. Pustaka canggih ini menyediakan cara mulus untuk memanipulasi objek 3D di aplikasi .NET Anda.
## FAQ
### T: Dapatkah saya menggunakan Aspose.3D untuk .NET dengan kerangka .NET lainnya?
J: Ya, Aspose.3D untuk .NET kompatibel dengan berbagai kerangka .NET.
### T: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D untuk .NET?
 J: Lihat[Aspose.3D untuk dokumentasi .NET](https://reference.aspose.com/3d/net/) untuk informasi mendalam.
### T: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk .NET?
 Sebuah kunjungan[Link ini](https://purchase.aspose.com/temporary-license/) untuk mendapatkan izin sementara.
### T: Apakah ada contoh proyek yang tersedia untuk Aspose.3D untuk .NET?
 J: Jelajahi dokumentasi Aspose.3D untuk .NET dan[Repositori GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) untuk proyek sampel.
### T: Apakah ada komunitas aktif untuk dukungan Aspose.3D untuk .NET?
 A: Ya, bergabunglah dengan[Aspose.3D untuk forum .NET](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dari masyarakat.