---
title: Transformasi Node 3D dengan Matriks Transformasi menggunakan Aspose.3D
linktitle: Transformasi Node 3D dengan Matriks Transformasi di Java menggunakan Aspose.3D
second_title: Asumsikan.3D Java API
description: Jelajahi dunia grafis 3D di Java dengan Aspose.3D. Pelajari cara mengubah node dengan mudah menggunakan matriks transformasi.
weight: 21
url: /id/java/geometry/transform-3d-nodes-with-matrices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformasi Node 3D dengan Matriks Transformasi menggunakan Aspose.3D

## Perkenalan

Selamat datang di panduan langkah demi langkah tentang transformasi node 3D dengan matriks transformasi di Java menggunakan Aspose.3D. Jika Anda seorang pengembang Java yang ingin meningkatkan keterampilan grafis dan pemodelan 3D, Anda berada di tempat yang tepat. Dalam tutorial ini, kita akan mendalami proses penerapan transformasi ke node 3D dalam kerangka Aspose.3D.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan dasar tentang pemrograman Java.
-  Pustaka Aspose.3D diinstal. Anda dapat mengunduhnya dari[Di Sini](https://releases.aspose.com/3d/java/).
- Lingkungan Pengembangan Terpadu (IDE) yang berfungsi untuk pengembangan Java.

## Paket Impor

Di proyek Java Anda, impor paket yang diperlukan dari Aspose.3D. Pastikan proyek Anda dikonfigurasi dengan benar untuk menggunakan perpustakaan Aspose.3D. Berikut ini contoh pernyataan impor:

```java
import com.aspose.threed.*;

```

## Mengubah Node 3D

### Langkah 1: Inisialisasi Objek Pemandangan

Mulailah dengan menginisialisasi objek pemandangan, yang berfungsi sebagai wadah elemen 3D.

```java
Scene scene = new Scene();
```

### Langkah 2: Inisialisasi Objek Kelas Node

Buat objek kelas Node, seperti kubus, yang akan mengalami transformasi.

```java
Node cubeNode = new Node("cube");
```

### Langkah 3: Buat Mesh Menggunakan Polygon Builder

Manfaatkan kelas Common untuk membuat mesh menggunakan metode pembuat poligon. Ini menetapkan instance mesh untuk kubus.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Langkah 4: Arahkan Node ke Geometri Mesh

Tetapkan mesh yang dibuat ke node kubus.

```java
cubeNode.setEntity(mesh);
```

### Langkah 5: Tetapkan Matriks Terjemahan Kustom

Terapkan matriks terjemahan khusus ke simpul kubus. Contoh ini menetapkan matriks transformasi untuk terjemahan.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Langkah 6: Tambahkan Kubus ke Adegan

Sertakan simpul kubus di simpul akar adegan.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Langkah 7: Simpan Adegan 3D

Tentukan direktori dan nama file untuk menyimpan adegan 3D dalam format file yang didukung, seperti FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengubah node 3D menggunakan Aspose.3D di Java. Bereksperimenlah dengan matriks yang berbeda dan jelajahi kemungkinan grafis 3D yang tak terbatas.

## FAQ

### Q1: Bisakah saya menerapkan beberapa transformasi ke satu node 3D?

A1: Ya, Anda dapat menggabungkan beberapa matriks transformasi untuk transformasi kompleks.

### Q2: Bagaimana cara memutar objek 3D di Aspose.3D?

A2: Gunakan matriks rotasi yang sesuai dalam matriks transformasi untuk rotasi yang diinginkan.

### Q3: Apakah ada batasan ukuran adegan 3D yang dapat saya buat?

A3: Ukuran adegan 3D Anda mungkin dibatasi oleh sumber daya sistem, namun Aspose.3D dirancang untuk efisiensi.

### Q4: Di mana saya dapat menemukan contoh dan dokumentasi tambahan?

 A4: Kunjungi[Dokumentasi Aspose.3D](https://reference.aspose.com/3d/java/) untuk lebih banyak contoh dan detail.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
