---
title: Bangun Hierarki Node dalam Adegan 3D dengan Java dan Aspose.3D
linktitle: Bangun Hierarki Node dalam Adegan 3D dengan Java dan Aspose.3D
second_title: Asumsikan.3D Java API
description: Pelajari cara membuat adegan 3D dinamis di Java dengan Aspose.3D. Buat hierarki node dengan mudah dan tingkatkan permainan grafis 3D Anda.
weight: 16
url: /id/java/geometry/build-node-hierarchies/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Bangun Hierarki Node dalam Adegan 3D dengan Java dan Aspose.3D

## Perkenalan

Dalam dunia grafis 3D dan pemrograman Java yang dinamis, membuat dan mengelola hierarki node dalam adegan 3D adalah keterampilan yang sangat penting. Aspose.3D untuk Java memberdayakan pengembang untuk mencapai hal ini dengan lancar, menawarkan seperangkat alat canggih untuk membuat adegan 3D yang rumit dengan mudah. Dalam tutorial ini, kami akan memandu Anda melalui proses membangun hierarki node menggunakan Aspose.3D untuk Java, memastikan bahwa pemula pun dapat mengikutinya.

## Prasyarat

Sebelum mempelajari tutorialnya, pastikan Anda memiliki prasyarat berikut:

1. Lingkungan Pengembangan Java: Pastikan Anda telah menyiapkan lingkungan pengembangan Java di mesin Anda.
2.  Aspose.3D untuk Perpustakaan Java: Unduh dan instal perpustakaan Aspose.3D untuk Java dari[Unduh Halaman](https://releases.aspose.com/3d/java/).
3. Direktori Dokumen: Buat direktori untuk menyimpan file adegan 3D Anda.

## Paket Impor

Mulailah dengan mengimpor paket yang diperlukan untuk memanfaatkan fungsi Aspose.3D untuk Java. Tambahkan baris berikut ke kode Java Anda:

```java
import com.aspose.threed.*;

```

## Langkah 1: Inisialisasi Objek Pemandangan

```java
// Inisialisasi objek adegan
Scene scene = new Scene();
```

## Langkah 2: Buat Node dan Mesh Anak

```java
// Dapatkan objek simpul anak
Node top = scene.getRootNode().createChildNode();

// Buat simpul kubus pertama
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Gunakan metode pembuatan mesh Anda
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Buat simpul kubus kedua
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Langkah 3: Terapkan Rotasi ke Node Atas

```java
// Memutar node teratas, mempengaruhi semua node anak
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Langkah 4: Simpan Adegan 3D

```java
// Simpan adegan 3D dalam format file yang didukung (dalam hal ini FBX)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

Panduan langkah demi langkah ini memberikan dasar yang kuat untuk membangun hierarki node dalam adegan 3D menggunakan Aspose.3D untuk Java. Bereksperimenlah dengan berbagai parameter dan sesuaikan kode dengan kebutuhan spesifik Anda.

## Kesimpulan

Menguasai pembuatan hierarki simpul adalah tonggak penting dalam perjalanan Anda dengan Aspose.3D untuk Java. Tutorial ini telah membekali Anda dengan pengetahuan untuk menavigasi kompleksitas adegan 3D dengan mulus. Sekarang, keluarkan kreativitas Anda dan bangun lingkungan 3D yang menawan dengan percaya diri.

## FAQ

### Q1: Apakah Aspose.3D untuk Java cocok untuk pemula?

A1: Tentu saja! Aspose.3D untuk Java menyediakan antarmuka yang ramah pengguna, sehingga dapat diakses oleh pemula dan pengembang berpengalaman.

### Q2: Dapatkah saya menggunakan Aspose.3D untuk Java untuk proyek komersial?

 A2: Ya, Anda bisa. Mengunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q3: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D untuk Java?

 A3: Bergabunglah dengan[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk mendapatkan bantuan dari komunitas dan tim dukungan Aspose.

### Q4: Apakah tersedia uji coba gratis?

 A4: Tentu saja! Jelajahi fitur-fiturnya dengan[uji coba gratis](https://releases.aspose.com/) sebelum membuat komitmen.

### Q5: Di mana saya dapat menemukan dokumentasinya?

 A5: Lihat[dokumentasi](https://reference.aspose.com/3d/java/) untuk informasi rinci tentang Aspose.3D untuk Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
