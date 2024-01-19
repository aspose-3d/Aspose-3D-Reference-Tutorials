---
title: Tambahkan Properti Animasi ke Adegan 3D di Java | Tutorial Aspose.3D
linktitle: Tambahkan Properti Animasi ke Adegan 3D di Java | Tutorial Aspose.3D
second_title: Asumsikan.3D Java API
description: Tingkatkan proyek 3D berbasis Java Anda dengan Aspose.3D. Ikuti tutorial kami untuk menambahkan properti animasi dengan lancar.
type: docs
weight: 10
url: /id/java/animations/add-animation-properties-to-scenes/
---
## Perkenalan

Selamat datang di tutorial langkah demi langkah tentang menambahkan properti animasi ke adegan 3D di Java menggunakan Aspose.3D. Jika Anda ingin menyempurnakan proyek 3D Anda dengan animasi dinamis, Anda berada di tempat yang tepat. Dalam panduan ini, kami akan memandu Anda melalui prosesnya, menguraikan setiap langkah untuk pengalaman yang lancar.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

- Pengetahuan dasar tentang pemrograman Java.
-  Pustaka Aspose.3D diinstal. Jika tidak, unduh dari[halaman rilis](https://releases.aspose.com/3d/java/).

## Paket Impor

Dalam proyek Java Anda, pastikan Anda mengimpor paket yang diperlukan untuk memanfaatkan fungsionalitas Aspose.3D:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

Sekarang, mari beralih ke panduan langkah demi langkah.

## Langkah 1: Inisialisasi Adegan

```java
// Inisialisasi objek adegan
Scene scene = new Scene();
```

## Langkah 2: Buat Mesh menggunakan Polygon Builder

```java
// Panggil kelas Common membuat mesh menggunakan metode pembuat poligon untuk menyetel instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Langkah 3: Buat Node Kubus dengan Terjemahan

```java
// Setiap node kubus memiliki terjemahannya sendiri
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Langkah 4: Temukan Properti Terjemahan

```java
// Temukan properti terjemahan pada objek transformasi node
Property translation = cube1.getTransform().findProperty("Translation");
```

## Langkah 5: Buat Titik Ikatan

```java
// Buat titik pengikatan berdasarkan properti terjemahan
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Langkah 6: Buat Kurva Animasi

```java
// Buat kurva animasi pada komponen X skala
KeyframeSequence kfs = new KeyframeSequence();

// Tambahkan bingkai utama untuk komponen X
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Ikat urutan keyframe ke komponen X
bindPoint.bindKeyframeSequence("X", kfs);
```

## Langkah 7: Ulangi untuk Komponen Z

```java
// Ulangi proses untuk komponen Z
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

## Langkah 8: Simpan Adegan 3D

```java
// Tentukan direktori untuk menyimpan adegan 3D
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

//Simpan adegan 3D dalam format file yang didukung
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

## Kesimpulan

Selamat! Anda telah berhasil menambahkan properti animasi ke adegan 3D menggunakan Aspose.3D di Java. Bereksperimenlah dengan parameter berbeda untuk mendapatkan animasi yang diinginkan untuk proyek Anda.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?

 A1: Ya, Anda bisa. Mengunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q2: Apakah tersedia uji coba gratis?

 A2: Tentu saja! Ambil milikmu[uji coba gratis](https://releases.aspose.com/) sebelum membuat keputusan pembelian.

### Q3: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A3: Bergabunglah dengan komunitas di[Forum Asumsikan.3D](https://forum.aspose.com/c/3d/18) untuk bantuan.

### Q4: Bagaimana cara mendapatkan lisensi sementara?

 A4: Dapatkan a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk periode evaluasi Anda.

### Q5: Apakah ada tutorial lain yang tersedia?

 A5: Jelajahi secara komprehensif[dokumentasi](https://reference.aspose.com/3d/java/) untuk tutorial tambahan.