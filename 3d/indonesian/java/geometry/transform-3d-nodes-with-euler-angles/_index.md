---
title: Transformasi Node 3D dengan Sudut Euler di Java menggunakan Aspose.3D
linktitle: Transformasi Node 3D dengan Sudut Euler di Java menggunakan Aspose.3D
second_title: Asumsikan.3D Java API
description: Jelajahi dunia transformasi 3D di Java dengan Aspose.3D. Ikuti panduan langkah demi langkah kami untuk menambahkan sudut Euler dinamis ke node 3D Anda.
weight: 19
url: /id/java/geometry/transform-3d-nodes-with-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformasi Node 3D dengan Sudut Euler di Java menggunakan Aspose.3D

## Perkenalan

Selamat datang di tutorial langkah demi langkah tentang mengubah node 3D dengan sudut Euler di Java menggunakan Aspose.3D. Dalam panduan ini, kita akan mempelajari proses menambahkan transformasi ke node 3D, menggunakan sudut Euler untuk mencapai posisi dan orientasi dinamis.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan dasar tentang pemrograman Java.
- Java Development Kit (JDK) diinstal pada mesin Anda.
-  Pustaka Aspose.3D, yang dapat Anda peroleh[Dokumentasi Java Aspose.3D](https://reference.aspose.com/3d/java/).

## Paket Impor

 Mulailah dengan mengimpor paket yang diperlukan ke proyek Java Anda. Pastikan perpustakaan Aspose.3D ditambahkan dengan benar ke classpath Anda. Jika Anda belum mendownloadnya, Anda dapat menemukan link downloadnya[Di Sini](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Langkah 1. Inisialisasi Scene dan Node

```java
// ExStart:TambahkanTransformasiKeNodeByEulerAngles
// Inisialisasi objek adegan
Scene scene = new Scene();

// Inisialisasi objek kelas Node
Node cubeNode = new Node("cube");
```

## Langkah 2. Buat Mesh dan Atur Geometri

```java
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Arahkan simpul ke geometri Mesh
cubeNode.setEntity(mesh);
```

## Langkah 3. Tetapkan Sudut Euler dan Terjemahannya

```java
// Sudut Euler
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Atur terjemahan
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Langkah 4. Tambahkan Node ke Adegan

```java
// Tambahkan kubus ke tempat kejadian
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Langkah 5. Simpan Adegan 3D

```java
// Jalur ke direktori dokumen.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Simpan adegan 3D dalam format file yang didukung
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:TambahkanTransformasiKeNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Pastikan untuk mengganti "Direktori Dokumen Anda" dengan jalur yang sesuai di mesin Anda.

## Kesimpulan

Selamat! Anda telah berhasil mengubah node 3D menggunakan sudut Euler di Java dengan Aspose.3D. Bereksperimenlah dengan berbagai sudut dan terjemahan untuk menciptakan pemandangan 3D yang dinamis dan menarik.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java dalam proyek komersial?

 A1: Ya, Anda bisa. Mengunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A2: Itu[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) adalah tempat untuk mencari bantuan dan berhubungan dengan komunitas.

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, Anda dapat menjelajahinya[uji coba gratis](https://releases.aspose.com/) untuk merasakan kemampuan Aspose.3D.

### Q4: Bagaimana cara mendapatkan lisensi sementara?

 A4: Anda bisa mendapatkan lisensi sementara[Di Sini](https://purchase.aspose.com/temporary-license/).

### Q5: Di mana saya dapat menemukan dokumentasinya?

 A5: Itu[dokumentasi](https://reference.aspose.com/3d/java/) memberikan panduan komprehensif tentang penggunaan Aspose.3D untuk Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
