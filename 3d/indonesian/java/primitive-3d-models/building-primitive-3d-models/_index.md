---
title: Membangun Model 3D Primitif dengan Aspose.3D untuk Java
linktitle: Membangun Model 3D Primitif dengan Aspose.3D untuk Java
second_title: Asumsikan.3D Java API
description: Temukan seni pemodelan 3D dengan Aspose.3D untuk Java. Belajar membuat model 3D primitif dengan mudah dan bebaskan kreativitas Anda.
weight: 10
url: /id/java/primitive-3d-models/building-primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Membangun Model 3D Primitif dengan Aspose.3D untuk Java

## Perkenalan

Membuat model 3D secara terprogram bisa menjadi tugas yang menakutkan, namun dengan Aspose.3D untuk Java, prosesnya menjadi proses yang menyenangkan dan mudah. Tutorial ini bertujuan untuk membantu Anda memulai membuat model 3D primitif, dengan fokus pada kesederhanaan dan efektivitas.

## Prasyarat

Sebelum terjun ke dunia pemodelan 3D dengan Aspose.3D untuk Java, pastikan Anda memiliki prasyarat berikut:

1. Java Development Kit (JDK): Pastikan Anda telah menginstal JDK di mesin Anda.
2.  Aspose.3D untuk Perpustakaan Java: Unduh dan instal perpustakaan Aspose.3D untuk Java dari[Unduh Halaman](https://releases.aspose.com/3d/java/).

## Paket Impor

Mulailah dengan mengimpor paket yang diperlukan ke proyek Java Anda. Langkah ini penting untuk mengakses fungsionalitas yang disediakan oleh Aspose.3D untuk Java.

```java

import com.aspose.threed.*;
```

Sekarang setelah semuanya siap, mari beralih ke inti tutorial ini – membuat model 3D primitif.

## Membuat Adegan

### Langkah 1: Inisialisasi Objek Adegan

```java
// Jalur ke direktori dokumen.
String myDir = "Your Document Directory";

//Inisialisasi objek Scene
Scene scene = new Scene();
```

### Langkah 2: Buat Model Kotak

```java
// Buat model Kotak
scene.getRootNode().createChildNode("box", new Box());
```

### Langkah 3: Buat Model Silinder

```java
// Buat model Silinder
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Langkah 4: Simpan Gambar dalam Format FBX

```java
// Simpan gambar dalam format FBX
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Kesimpulan

Selamat! Anda telah berhasil membuat adegan dari model 3D primitif menggunakan Aspose.3D untuk Java. File tersebut sekarang disimpan di direktori yang ditentukan.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D untuk Java dengan bahasa pemrograman lain?

A1: Aspose.3D terutama mendukung Java, namun ada versi yang tersedia untuk bahasa lain seperti .NET.

### Q2: Apakah Aspose.3D cocok untuk tugas pemodelan 3D yang kompleks?

A2: Tentu saja! Aspose.3D menyediakan serangkaian fitur yang komprehensif, sehingga cocok untuk tugas pemodelan 3D yang sederhana dan kompleks.

### Q3: Di mana saya bisa mendapatkan bantuan dan dukungan tambahan?

 A3: Kunjungi[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi komunitas.

### Q4: Dapatkah saya mencoba Aspose.3D sebelum membeli?

 A4: Ya, Anda dapat menjelajahi a[uji coba gratis](https://releases.aspose.com/) sebelum membuat keputusan pembelian.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Anda dapat memperoleh a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk Aspose.3D melalui situs web.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
