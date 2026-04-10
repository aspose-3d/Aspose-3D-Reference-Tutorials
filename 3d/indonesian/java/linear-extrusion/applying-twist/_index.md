---
date: 2026-02-20
description: Pelajari cara membuat adegan 3D dan menerapkan putaran ekstrusi linear
  menggunakan Aspose.3D untuk Java. Ekspor file OBJ dengan panduan langkah demi langkah
  yang mudah.
linktitle: Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Buat Adegan 3D dengan Twist pada Ekstrusi Linear – Aspose.3D untuk Java
url: /id/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat Adegan 3D dengan Twist pada Ekstrusi Linear – Aspose.3D untuk Java

## Perkenalan

Dalam tutorial **java 3d** praktis ini Anda akan belajar cara **membuat adegan 3d** objek, menerapkan *twist pada ekstrusi linear*, dan terakhir **mengekspor file obj java** menggunakan Aspose.3D untuk Java. Baik Anda membuat aset game, prototipe CAD, atau efek visual, menambahkan twist selama ekstrusi memberi model Anda tampilan dinamis berbentuk spiral yang sulit dicapai dengan ekstrusi biasa.

## Jawaban Cepat
- **Apa yang dimaksud dengan “twist” dalam ekstrusi?** Apa arti “twist” dalam ekstrusi? Ini memutar profil secara bertahap sepanjang jalur ekstrusi.
- **Perpustakaan manakah yang menyediakan fitur twist?** Perpustakaan mana yang menyediakan fitur twist? Aspose.3D untuk Java.
- **Dapatkah saya mengekspor hasilnya sebagai OBJ?** Dapatkah saya mengekspor hasil sebagai OBJ? Ya – gunakan `FileFormat.WAVEFRONTOBJ`.
- **Apakah saya memerlukan lisensi untuk tutorial ini?** Apakah saya memerlukan lisensi untuk tutorial ini? Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.
- **Versi Java apa yang diperlukan?** Versi Java apa yang diperlukan? Java8 atau lebih tinggi.

## Apa yang dimaksud dengan “twist” dalam ekstrusi linier?

Twist adalah transformasi yang memutar setiap irisan bentuk yang diekstrusi dengan sudut tertentu. Dengan mengendalikan sudut tersebut, Anda dapat membuat spiral, sekrup, atau torsi halus yang menambah daya tarik visual pada ekstrusi yang biasanya datar.

## Mengapa menggunakan Aspose.3D untuk Java?

- **Dukungan lintas format:** Dukungan lintas format: Impor dan ekspor puluhan format 3D, termasuk OBJ, FBX, dan STL.
- **Pure Java API:** API Java murni: Tanpa ketergantungan native, memudahkan integrasi ke proyek Java apa pun.
- **Mesin geometri performa tinggi:** Mesin geometri berperforma tinggi: menggabungkan operasi kompleks seperti memutar tanpa mengorbankan kecepatan.

## Prasyarat

- **Java Development Kit (JDK) 8+** terpasang di mesin Anda.
- **Aspose.3D for Java** – unduh dari [tautan unduh](https://releases.aspose.com/3d/java/).
- Keakraban dengan sintaksis dasar Java dan konsep 3D.
- Akses ke [dokumentasi Aspose.3D] resmi (https://reference.aspose.com/3d/java/) untuk referensi.

## Impor Paket

Pertama, masukkan kelas Aspose.3D yang diperlukan ke dalam proyek Anda.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Tetapkan Direktori Dokumen

Tentukan lokasi penyimpanan file OBJ yang dihasilkan. Ganti placeholder dengan jalur folder yang sebenarnya di sistem Anda.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Langkah 2: Inisialisasi Profil Dasar

Buat bentuk yang akan diekstrusi. Di sini kami menggunakan persegi panjang dengan radius pembulatan kecil untuk memberikan tepi yang lebih lembut.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Langkah 3: Buat Scene untuk Menampung Node Anda

Objek `Scene` adalah wadah untuk semua entitas 3‑D (mesh, cahaya, kamera, dll).

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Langkah 4: Tambahkan Node Kiri dan Kanan

Kami akan membuat dua node saudara: satu tanpa twist (untuk perbandingan) dan satu dengan twist 90‑derajat.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Langkah 5: Lakukan Ekstrusi Linier dengan Putaran

Konstruktor `LinearExtrusion` menerima profil dan panjang ekstrusi.  
- `setTwist(0)` → tidak ada rotasi (ekstrusi lurus).  
- `setTwist(90)` → rotasi penuh 90‑derajat sepanjang panjang.  
Kedua node menggunakan 100 slice untuk geometri yang halus.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Langkah 6: Simpan Scene 3D sebagai OBJ

Akhirnya, tulis scene ke file OBJ sehingga Anda dapat melihatnya di penampil 3‑D standar apa pun.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Masalah & Tip Umum

- **Kesalahan jalur file:** Kesalahan jalur file: Pastikan `MyDir` diakhiri dengan batas jalur (`/` atau `\\`) yang sesuai dengan OS Anda.
- **Sudut puntir terlalu tinggi:** Sudut puntir terlalu tinggi: Sudut di atas 360° dapat menyebabkan geometri tumpang tindih; tahan dalam rentang 0‑360° untuk hasil yang dapat diprediksi.
- **Kinerja:** Kinerja: Meningkatkan `setSlices` meningkatkan kelancaran tetapi dapat mempengaruhi memori; 100 irisan merupakan keseimbangan yang baik untuk kebanyakan kasus.

## Pertanyaan yang Sering Diajukan (Asli)

### Q1: Dapatkah saya menggunakan Aspose.3D untuk Java untuk bekerja dengan format file 3D lainnya?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memungkinkan Anda mengimpor, mengekspor, dan memanipulasi berbagai jenis file.

### Q2: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?

A2: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas dan diskusi.

### Q3: Apakah tersedia uji coba gratis untuk Aspose.3D untuk Java?

A3: Ya, Anda dapat mengakses versi percobaan gratis dari [sini](https://releases.aspose.com/).

### Q4: Bagaimana cara mendapatkan lisensi sementara Aspose.3D untuk Java?

A4: Dapatkan lisensi sementara dari [halaman lisensi sementara](https://purchase.aspose.com/temporary-license/).

### Q5: Dimana saya bisa membeli Aspose.3D untuk Java?

A5: Beli Aspose.3D untuk Java dari [halaman pembelian](https://purchase.aspose.com/buy).

## FAQ Tambahan (Dioptimalkan AI)

**Q: Bisakah saya mengubah arah putaran?**
A: Ya – gunakan sudut negatif pada `setTwist()` untuk memutar ke arah berlawanan.

**T: Apakah mungkin untuk menerapkan nilai putaran yang berbeda di sepanjang ekstrusi?**
A: Aspose.3D saat ini menerapkan twist seragam; untuk memutar variabel Anda harus menghasilkan beberapa segmen secara manual.

**Q: Bagaimana cara melihat file OBJ yang diekspor?**
A: Penampil 3‑D standar apa pun (mis., Blender, MeshLab) dapat membuka file OBJ.

**T: Apakah perpustakaan mendukung pemetaan tekstur pada ekstrusi bengkok?**
A: Ya – setelah ekstrusi Anda dapat menetapkan material atau koordinat UV ke mesh node.

## Kesimpulan

Anda kini telah **membuat adegan 3D**, menerapkan **twist pada ekstrusi linear**, dan mengekspor hasilnya sebagai file OBJ menggunakan Aspose.3D untuk Java. Bereksperimenlah dengan profil berbeda, sudut twist, dan jumlah irisan untuk membuat geometri unik bagi game, simulasi, atau pencetakan 3‑D.

---

**Terakhir Diperbarui:** 20-02-2026
**Diuji Dengan:** Aspose.3D untuk Java 24.11
**Penulis:** Beranggapan  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}