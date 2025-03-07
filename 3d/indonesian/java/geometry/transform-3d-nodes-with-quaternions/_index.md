---
title: Transformasi Node 3D dengan Quaternion di Java menggunakan Aspose.3D
linktitle: Transformasi Node 3D dengan Quaternion di Java menggunakan Aspose.3D
second_title: Asumsikan.3D Java API
description: Sempurnakan aplikasi Java Anda dengan Aspose.3D untuk transformasi 3D yang hebat. Pelajari cara mengubah node menggunakan angka empat dalam panduan langkah demi langkah ini.
weight: 20
url: /id/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformasi Node 3D dengan Quaternion di Java menggunakan Aspose.3D

## Perkenalan

Selamat datang di panduan langkah demi langkah tentang mengubah node 3D dengan angka empat di Java menggunakan Aspose.3D. Jika Anda ingin menyempurnakan aplikasi Java Anda dengan transformasi 3D yang hebat, tutorial ini cocok untuk Anda. Aspose.3D untuk Java menyediakan serangkaian fitur canggih untuk bekerja dengan grafik 3D, dan dalam tutorial ini, kami akan fokus pada transformasi node 3D menggunakan angka empat.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan dasar tentang pemrograman Java.
- Aspose.3D untuk Java diinstal. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/java/).
- Direktori dokumen disiapkan untuk menyimpan adegan 3D Anda.

## Paket Impor

Di bagian ini, kita akan mengimpor paket yang diperlukan untuk memulai transformasi 3D menggunakan Aspose.3D.

```java
import com.aspose.threed.*;
```

## Langkah 1: Inisialisasi Objek Pemandangan

Untuk memulai, buatlah objek pemandangan yang akan berfungsi sebagai wadah untuk elemen 3D Anda.

```java
Scene scene = new Scene();
```

## Langkah 2: Inisialisasi Objek Kelas Node

Sekarang, buat objek kelas simpul, dalam hal ini, mewakili sebuah kubus.

```java
Node cubeNode = new Node("cube");
```

## Langkah 3: Buat Mesh menggunakan Polygon Builder

Manfaatkan kelas umum untuk membuat mesh menggunakan metode pembuat poligon.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Langkah 4: Atur Geometri Mesh

Tetapkan mesh yang dibuat ke node kubus.

```java
cubeNode.setEntity(mesh);
```

## Langkah 5: Atur Rotasi dengan Quaternion

Terapkan rotasi ke simpul kubus menggunakan angka empat.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Langkah 6: Atur Terjemahan

Tentukan terjemahan untuk node kubus.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Langkah 7: Tambahkan Kubus ke Adegan

Sertakan simpul kubus dalam adegan.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Langkah 8: Simpan Adegan 3D

Simpan adegan 3D dalam format file yang didukung, misalnya FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Kesimpulan

Selamat! Anda telah berhasil mempelajari cara mengubah node 3D menggunakan angka empat di Java dengan Aspose.3D. Bereksperimenlah dengan berbagai transformasi untuk menghidupkan aplikasi 3D Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java secara gratis?

A1: Aspose.3D untuk Java menawarkan uji coba gratis. Kamu bisa menemukannya[Di Sini](https://releases.aspose.com/).

### Q2: Di mana saya dapat menemukan dokumentasi Aspose.3D untuk Java?

 A2: Dokumentasi tersedia[Di Sini](https://reference.aspose.com/3d/java/).

### Q3: Bagaimana cara mendapatkan dukungan untuk Aspose.3D untuk Java?

 A3: Kunjungi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan.

### Q4: Apakah lisensi sementara tersedia?

 A4: Ya, Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya bisa membeli Aspose.3D untuk Java?

 A5: Anda bisa membelinya[Di Sini](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
