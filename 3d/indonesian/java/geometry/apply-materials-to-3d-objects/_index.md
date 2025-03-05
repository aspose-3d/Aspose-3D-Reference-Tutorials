---
title: Terapkan Material ke Objek 3D di Java dengan Aspose.3D
linktitle: Terapkan Material ke Objek 3D di Java dengan Aspose.3D
second_title: Asumsikan.3D Java API
description: Jelajahi dunia grafis 3D dengan Aspose.3D untuk Java. Pelajari cara menerapkan materi ke objek 3D dengan mulus. Tingkatkan proyek Anda dengan visual yang realistis.
type: docs
weight: 14
url: /id/java/geometry/apply-materials-to-3d-objects/
---
## Perkenalan

Dalam dunia grafis 3D yang dinamis, Aspose.3D untuk Java menonjol sebagai alat yang ampuh untuk menghidupkan proyek Anda. Menambahkan material ke objek 3D meningkatkan daya tarik visual, menjadikannya lebih realistis. Dalam tutorial ini, kami akan memandu Anda melalui proses penerapan material ke kubus 3D menggunakan Aspose.3D untuk Java.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

- Java Development Kit (JDK) diinstal pada sistem Anda.
- Aspose.3D untuk perpustakaan Java diunduh dan ditambahkan ke proyek Anda.
- Keakraban dengan konsep dasar pemrograman Java.

## Paket Impor

Untuk memulai, impor paket yang diperlukan ke proyek Java Anda. Tambahkan baris berikut di awal kode Anda:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Langkah 1: Inisialisasi Objek Pemandangan

```java
// Inisialisasi objek adegan
Scene scene = new Scene();
```

## Langkah 2: Inisialisasi Objek Node Kubus

```java
// Inisialisasi objek simpul kubus
Node cubeNode = new Node("cube");
```

## Langkah 3: Buat Mesh menggunakan Polygon Builder

```java
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Langkah 4: Arahkan Node ke Mesh

```java
// Arahkan simpul ke jaring
cubeNode.setEntity(mesh);
```

## Langkah 5: Tambahkan Kubus ke Adegan

```java
// Tambahkan kubus ke tempat kejadian
scene.getRootNode().addChildNode(cubeNode);
```

## Langkah 6: Inisialisasi Objek PhongMaterial

```java
// Inisialisasi objek PhongMaterial
PhongMaterial mat = new PhongMaterial();
```

## Langkah 7: Inisialisasi Objek Tekstur

```java
// Inisialisasi objek Tekstur
Texture diffuse = new Texture();
```

## Langkah 8: Tetapkan Jalur File Lokal untuk Tekstur

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
```

## Langkah 9: Tetapkan Jalur File Lokal untuk Tekstur Tersemat

```java
// Tetapkan jalur file lokal untuk tekstur yang disematkan
diffuse.setFileName(MyDir + "surface.dds");
```

## Langkah 10: Atur Tekstur Material

```java
// Atur Tekstur material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Langkah 11: Sematkan Data Konten Mentah ke FBX (Opsional)

```java
// Tetapkan nama file untuk tekstur yang disematkan
diffuse.setFileName("embedded-texture.png");
// Tetapkan konten biner
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Langkah 12: Tetapkan Warna Spekuler

```java
// Tetapkan warna khusus
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Langkah 13: Atur Kecerahan

```java
// Atur kecerahan
mat.setShininess(100);
```

## Langkah 14: Tetapkan Properti Material dari Objek Kubus

```java
// Tetapkan properti material dari objek kubus
cubeNode.setMaterial(mat);
```

## Langkah 15: Simpan Adegan 3D

```java
// Tetapkan nama file
MyDir = MyDir + "MaterialToCube.fbx";
// Simpan adegan 3D dalam format file yang didukung
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Kesimpulan

Selamat! Anda telah berhasil menerapkan material ke kubus 3D menggunakan Aspose.3D untuk Java. Teknik sederhana namun kuat ini dapat meningkatkan proyek 3D Anda ke tingkat yang lebih tinggi, memberikan pengalaman visual yang realistis dan menakjubkan.

## FAQ

### Q1: Dapatkah saya menerapkan beberapa materi ke satu objek 3D?

A1: Ya, Aspose.3D memungkinkan Anda menerapkan beberapa material ke berbagai bagian objek 3D untuk penyesuaian yang lebih baik.

### Q2: Format file apa yang didukung Aspose.3D untuk menyimpan adegan?

 A2: Aspose.3D mendukung berbagai format file, termasuk FBX, STL, dan 3DS. Mengacu kepada[dokumentasi](https://reference.aspose.com/3d/java/) untuk daftar lengkapnya.

### Q3: Apakah lisensi sementara tersedia untuk Aspose.3D untuk Java?

 A3: Ya, Anda bisa mendapatkan a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk tujuan evaluasi.

### Q4: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A4: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q5: Bisakah saya mengunduh perpustakaan Aspose.3D dari tautan tertentu?

 A5: Ya, gunakan[tautan unduhan](https://releases.aspose.com/3d/java/) untuk mengakses versi terbaru Aspose.3D untuk Java.