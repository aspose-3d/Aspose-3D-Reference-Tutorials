---
title: Terapkan Material PBR ke Objek 3D di Java dengan Aspose.3D
linktitle: Terapkan Material PBR ke Objek 3D di Java dengan Aspose.3D
second_title: Asumsikan.3D Java API
description: Belajar menerapkan materi PBR realistis ke objek 3D di Java menggunakan Aspose.3D. Tingkatkan kualitas visual dengan Rendering Berbasis Fisik.
type: docs
weight: 10
url: /id/java/geometry/apply-pbr-materials-to-objects/
---
## Perkenalan

Selamat datang di panduan langkah demi langkah dalam menerapkan materi Rendering Berbasis Fisik (PBR) ke objek 3D di Java menggunakan Aspose.3D. Aspose.3D adalah perpustakaan Java yang kuat yang menyediakan fungsionalitas komprehensif untuk bekerja dengan model dan pemandangan 3D. Dalam tutorial ini, kita akan fokus pada penerapan material PBR, yang mensimulasikan pencahayaan dunia nyata dan properti permukaan, sehingga meningkatkan realisme objek 3D Anda.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

1. Lingkungan Pengembangan Java: Pastikan Anda telah menginstal Java di sistem Anda.

2.  Perpustakaan Aspose.3D: Unduh dan instal perpustakaan Aspose.3D dari[tautan unduhan](https://releases.aspose.com/3d/java/).

3.  Dokumentasi: Lihat[dokumentasi](https://reference.aspose.com/3d/java/) agar Aspose.3D membiasakan diri Anda dengan fitur-fitur perpustakaan.

4.  Lisensi Sementara (Opsional): Jika Anda tidak memiliki lisensi, Anda dapat memperoleh a[izin sementara](https://purchase.aspose.com/temporary-license/) untuk pengujian.

## Paket Impor

Dalam proyek Java Anda, sertakan paket yang diperlukan untuk menggunakan Aspose.3D. Tambahkan pernyataan import berikut ke kode Anda:

```java
import com.aspose.threed.*;
```

## Langkah 1: Inisialisasi Adegan

Mulailah dengan membuat adegan 3D menggunakan Aspose.3D. Adegan berfungsi sebagai kanvas untuk objek 3D Anda.

```java
// ExStart: Inisialisasi Adegan
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

## Langkah 2: Inisialisasi Materi PBR

Buat material PBR dan sesuaikan propertinya seperti faktor logam dan kekasaran.

```java
// ExStart: Inisialisasi PBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd: Inisialisasi PBRMaterial
```

## Langkah 3: Buat Objek 3D

Hasilkan objek 3D (misalnya kotak) yang akan diterapkan material PBR.

```java
// ExStart:Buat3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Buat3DObject
```

## Langkah 4: Simpan Adegan 3D

Simpan adegan 3D, termasuk materi PBR yang diterapkan, ke dalam format file tertentu, seperti STL.

```java
// ExStart:Simpan3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Simpan3DScene
```

Ulangi langkah-langkah ini untuk pemandangan yang lebih kompleks atau objek berbeda.

## Kesimpulan

Selamat! Anda telah berhasil menerapkan materi PBR ke objek 3D di Java menggunakan Aspose.3D. Hal ini meningkatkan daya tarik visual model 3D Anda, menjadikannya lebih realistis dan menakjubkan secara visual.

## FAQ

### Q1: Dapatkah saya menggunakan Aspose.3D untuk proyek komersial?

 A1: Ya, Anda bisa. Mengunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q2: Bagaimana cara mendapatkan dukungan untuk Aspose.3D?

 A2: Bergabunglah dengan[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan dan bantuan masyarakat.

### Q3: Apakah tersedia uji coba gratis?

 A3: Ya, Anda dapat menjelajahi a[uji coba gratis](https://releases.aspose.com/) sebelum melakukan pembelian.

### Q4: Di mana saya dapat menemukan dokumentasi terperinci untuk Aspose.3D?

 A4: Lihat[dokumentasi](https://reference.aspose.com/3d/java/) untuk panduan komprehensif.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk pengujian?

 A5: Kunjungi[Link ini](https://purchase.aspose.com/temporary-license/) untuk mendapatkan izin sementara.