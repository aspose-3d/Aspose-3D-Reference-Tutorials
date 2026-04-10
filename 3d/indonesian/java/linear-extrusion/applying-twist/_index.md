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

## Introduction

Dalam tutorial **java 3d** praktis ini Anda akan belajar cara **membuat adegan 3d** objek, menerapkan *twist pada ekstrusi linear*, dan akhirnya **mengekspor file obj java** menggunakan Aspose.3D untuk Java. Baik Anda membuat aset game, prototipe CAD, atau efek visual, menambahkan twist selama ekstrusi memberi model Anda tampilan dinamis berbentuk spiral yang sulit dicapai dengan ekstrusi biasa.

## Quick Answers
- **What does “twist” mean in extrusion?** Apa arti “twist” dalam ekstrusi? It rotates the profile gradually along the extrusion path.  
- **Which library provides the twist feature?** Perpustakaan mana yang menyediakan fitur twist? Aspose.3D for Java.  
- **Can I export the result as OBJ?** Bisakah saya mengekspor hasil sebagai OBJ? Yes – use `FileFormat.WAVEFRONTOBJ`.  
- **Do I need a license for this tutorial?** Apakah saya memerlukan lisensi untuk tutorial ini? A temporary or full license is required for production use.  
- **What Java version is required?** Versi Java apa yang diperlukan? Java 8 or higher.

## What is a “twist” in linear extrusion?

Twist adalah transformasi yang memutar setiap irisan bentuk yang diekstrusi dengan sudut tertentu. Dengan mengendalikan sudut tersebut, Anda dapat membuat spiral, sekrup, atau torsi halus yang menambah daya tarik visual pada ekstrusi yang biasanya datar.

## Why use Aspose.3D for Java?

- **Cross‑format support:** Dukungan lintas format: Impor dan ekspor puluhan format 3D, termasuk OBJ, FBX, dan STL.  
- **Pure Java API:** API Java murni: Tanpa ketergantungan native, memudahkan integrasi ke proyek Java apa pun.  
- **High‑performance geometry engine:** Mesin geometri berperforma tinggi: Menangani operasi kompleks seperti twisting tanpa mengorbankan kecepatan.

## Prerequisites

- **Java Development Kit (JDK) 8+** terpasang di mesin Anda.  
- **Aspose.3D for Java** – unduh dari [tautan unduhan](https://releases.aspose.com/3d/java/).  
- Familiarity with basic Java syntax and 3‑D concepts.  
- Access to the official [Aspose.3D documentation](https://reference.aspose.com/3d/java/) for reference.

## Import Packages

Pertama, masukkan kelas Aspose.3D yang diperlukan ke dalam proyek Anda.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set the Document Directory

Tentukan lokasi penyimpanan file OBJ yang dihasilkan. Ganti placeholder dengan jalur folder yang sebenarnya di sistem Anda.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Step 2: Initialize the Base Profile

Buat bentuk yang akan diekstrusi. Di sini kami menggunakan persegi panjang dengan radius pembulatan kecil untuk memberikan tepi yang lebih lembut.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Step 3: Create a Scene to Host Your Nodes

Objek `Scene` adalah wadah untuk semua entitas 3‑D (mesh, cahaya, kamera, dll).

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Step 4: Add Left and Right Nodes

Kami akan membuat dua node saudara: satu tanpa twist (untuk perbandingan) dan satu dengan twist 90‑derajat.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Step 5: Perform Linear Extrusion with Twist

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

## Step 6: Save the 3D Scene as OBJ

Akhirnya, tulis scene ke file OBJ sehingga Anda dapat melihatnya di penampil 3‑D standar apa pun.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Common Issues & Tips

- **File path errors:** Kesalahan jalur file: Pastikan `MyDir` diakhiri dengan pemisah jalur (`/` atau `\\`) yang sesuai untuk OS Anda.  
- **Twist angle too high:** Sudut twist terlalu tinggi: Sudut di atas 360° dapat menyebabkan geometri tumpang tindih; pertahankan dalam rentang 0‑360° untuk hasil yang dapat diprediksi.  
- **Performance:** Kinerja: Meningkatkan `setSlices` meningkatkan kelancaran tetapi dapat mempengaruhi memori; 100 slice merupakan keseimbangan yang baik untuk kebanyakan kasus.

## Frequently Asked Questions (Original)

### Q1: Can I use Aspose.3D for Java to work with other 3D file formats?

A1: Ya, Aspose.3D mendukung berbagai format file 3D, memungkinkan Anda mengimpor, mengekspor, dan memanipulasi berbagai jenis file.

### Q2: Where can I find support for Aspose.3D for Java?

A2: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas dan diskusi.

### Q3: Is there a free trial available for Aspose.3D for Java?

A3: Ya, Anda dapat mengakses versi percobaan gratis dari [sini](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D for Java?

A4: Dapatkan lisensi sementara dari [halaman lisensi sementara](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase Aspose.3D for Java?

A5: Beli Aspose.3D untuk Java dari [halaman pembelian](https://purchase.aspose.com/buy).

## Additional FAQ (AI‑Optimized)

**Q: Can I change the twist direction?**  
A: Ya – gunakan sudut negatif pada `setTwist()` untuk memutar ke arah berlawanan.

**Q: Is it possible to apply different twist values along the extrusion?**  
A: Aspose.3D saat ini menerapkan twist seragam; untuk twist variabel Anda harus menghasilkan beberapa segmen secara manual.

**Q: How do I view the exported OBJ file?**  
A: Penampil 3‑D standar apa pun (mis., Blender, MeshLab) dapat membuka file OBJ.

**Q: Does the library support texture mapping on twisted extrusions?**  
A: Ya – setelah ekstrusi Anda dapat menetapkan material atau koordinat UV ke mesh node.

## Conclusion

Anda kini telah **membuat adegan 3D**, menerapkan **twist pada ekstrusi linear**, dan mengekspor hasilnya sebagai file OBJ menggunakan Aspose.3D untuk Java. Bereksperimenlah dengan profil berbeda, sudut twist, dan jumlah slice untuk membuat geometri unik bagi game, simulasi, atau pencetakan 3‑D.

---

**Last Updated:** 2026-02-20  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}