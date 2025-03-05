---
title: Buat Adegan Kubus 3D di Java dengan Aspose.3D
linktitle: Buat Adegan Kubus 3D di Java dengan Aspose.3D
second_title: Asumsikan.3D Java API
description: Jelajahi keajaiban grafik adegan kubus 3D dengan Aspose.3D untuk Java. Ciptakan pemandangan menakjubkan dengan mudah.
type: docs
weight: 12
url: /id/java/geometry/create-3d-cube-scene/
---
## Perkenalan

Selamat datang di dunia grafis 3D yang menakjubkan di Java menggunakan Aspose.3D! Dalam tutorial ini, kami akan memandu Anda melalui proses pembuatan adegan kubus 3D yang menakjubkan menggunakan Aspose.3D untuk Java. Aspose.3D adalah perpustakaan Java yang kuat yang menyediakan fungsionalitas komprehensif untuk bekerja dengan model dan pemandangan 3D.

## Prasyarat

Sebelum kita mendalami pembuatan adegan kubus 3D, pastikan Anda memiliki prasyarat berikut:

1.  Java Development Kit (JDK): Pastikan Anda telah menginstal Java di sistem Anda. Anda dapat mengunduh versi terbaru dari[situs web Oracle](https://www.oracle.com/java/).

2.  Aspose.3D untuk Perpustakaan Java: Unduh dan instal perpustakaan Aspose.3D. Anda dapat menemukan tautan unduhan[Di Sini](https://releases.aspose.com/3d/java/).

## Paket Impor

Mulailah dengan mengimpor paket yang diperlukan ke proyek Java Anda:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

Sekarang, mari kita uraikan proses pembuatan adegan kubus 3D menjadi beberapa langkah.

## Langkah 1: Inisialisasi Adegan

```java
// Inisialisasi objek adegan
Scene scene = new Scene();
```

## Langkah 2: Inisialisasi Node dan Mesh

```java
// Inisialisasi objek kelas Node
Node cubeNode = new Node("box");

// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Arahkan simpul ke geometri Mesh
cubeNode.setEntity(mesh);
```

## Langkah 3: Tambahkan Node ke Adegan

```java
// Tambahkan Node ke sebuah adegan
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Langkah 4: Simpan Adegan 3D

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

// Simpan adegan 3D dalam format file yang didukung
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Langkah 5: Cetak Pesan Sukses

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## Kesimpulan

Selamat! Anda telah berhasil membuat adegan kubus 3D menggunakan Aspose.3D untuk Java. Tutorial ini memberikan dasar yang kuat untuk menjelajahi fitur-fitur lebih lanjut dan melepaskan kreativitas Anda dalam dunia grafis 3D.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?

 A1: Ya, Anda bisa. Periksalah[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q2: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?

 A2: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan masyarakat.

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, Anda bisa mendapatkan uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat menemukan dokumentasi untuk Aspose.3D?

 A4: Lihat[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/java/) untuk informasi rinci.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).