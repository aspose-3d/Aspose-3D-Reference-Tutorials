---
date: 2025-12-08
description: Pelajari cara membuat adegan 3D di Java, menerapkan material PBR realistis
  menggunakan Aspose.3D, dan menyimpan model 3D STL untuk merender objek 3D di Java.
language: id
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'Buat Adegan 3D Java: Terapkan Material PBR dengan Aspose.3D'
url: /java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat 3D Scene Java – Terapkan Material PBR dengan Aspose.3D

## Pendahuluan

Dalam tutorial praktis ini Anda akan belajar **cara membuat 3D scene di Java** dan memperkaya dengan material Physically Based Rendering (PBR) menggunakan pustaka Aspose.3D. Pada akhir panduan Anda akan dapat merender permukaan realistis dan **menyimpan model 3D STL** untuk penggunaan lebih lanjut dalam pipeline 3D apa pun.

## Jawaban Cepat
- **Apa arti “create 3d scene java”?** Ini adalah proses membangun objek Scene yang menyimpan geometri, cahaya, dan kamera dalam aplikasi Java.  
- **Library mana yang menangani material PBR?** Aspose.3D menyediakan kelas `PbrMaterial` yang siap pakai.  
- **Bisakah saya mengekspor hasilnya sebagai STL?** Ya – metode `Scene.save` mendukung STL (ASCII dan binary).  
- **Apakah saya memerlukan lisensi untuk produksi?** Lisensi Aspose.3D permanen diperlukan untuk penggunaan komersial; lisensi sementara dapat digunakan untuk pengujian.  
- **Versi Java apa yang dibutuhkan?** Runtime Java 8+ apa pun didukung.

## Apa itu 3D scene di Java?

*scene* adalah kontainer yang menyimpan semua objek (node), geometri, material, cahaya, dan kamera mereka. Anggaplah sebagai panggung virtual tempat Anda menempatkan model 3D Anda. Kelas `Scene` Aspose.3D memberikan cara yang bersih dan berorientasi objek untuk membangun panggung ini secara programatik.

## Mengapa menggunakan material PBR untuk merender objek 3D di Java?

PBR (Physically Based Rendering) meniru interaksi cahaya dunia nyata dengan menggunakan parameter seperti faktor metallic dan roughness. Hasilnya adalah tampilan yang lebih meyakinkan di berbagai kondisi pencahayaan, yang sangat berharga untuk visualisasi produk, game, atau pengalaman AR/VR.

## Prasyarat

1. **Lingkungan Pengembangan Java** – JDK 8 atau yang lebih baru terpasang.  
2. **Pustaka Aspose.3D** – Unduh JAR terbaru dari [tautan unduhan](https://releases.aspose.com/3d/java/).  
3. **Dokumentasi** – Kenali API melalui [dokumentasi resmi](https://reference.aspose.com/3d/java/).  
4. **Lisensi Sementara (Opsional)** – Jika Anda tidak memiliki lisensi permanen, dapatkan [lisensi sementara](https://purchase.aspose.com/temporary-license/) untuk pengujian.

## Impor Paket

Add the Aspose.3D namespace to your Java source file:

```java
import com.aspose.threed.*;
```

## Langkah 1: Inisialisasi Scene

Create the scene that will act as the canvas for your geometry and materials.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Tip Pro:** Pastikan `MyDir` mengarah ke folder yang dapat ditulisi; jika tidak, panggilan `save` akan gagal.

## Langkah 2: Inisialisasi Material PBR

Configure a PBR material with metallic and roughness values that give a near‑metallic look.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Mengapa nilai ini?** Faktor metallic tinggi (≈ 0.9) membuat permukaan berperilaku seperti logam, sementara roughness tinggi (≈ 0.9) menambahkan difusi halus, mencegah hasil akhir yang seperti cermin sempurna.

## Langkah 3: Buat Objek 3D dan Terapkan Material

Here we generate a simple box geometry, attach it to the scene’s root node, and assign the PBR material we just created.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Kesalahan umum:** Lupa menetapkan material pada node akan membuat objek menggunakan tampilan default (non‑PBR).

## Langkah 4: Simpan 3D Scene (Ekspor STL)

Export the entire scene—including the PBR‑enhanced box—to an STL file. STL is a widely‑supported format for 3‑D printing and quick visual checks.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

Anda juga dapat memilih `FileFormat.STLBINARY` jika diperlukan ukuran file yang lebih kecil.

## Masalah Umum dan Solusinya

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| **File tidak tersimpan** | `MyDir` mengarah ke folder yang tidak ada atau tidak memiliki izin menulis | Pastikan direktori ada dan proses Java Anda memiliki akses menulis |
| **Material terlihat datar** | Nilai Metallic/Roughness diatur ke 0 | Tingkatkan `setMetallicFactor` dan/atau `setRoughnessFactor` |
| **File STL tidak dapat dibuka** | Flag format file salah (ASCII vs Binary) untuk penampil | Gunakan enum `FileFormat` yang sesuai untuk penampil target Anda |

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?**  
A: Ya. Beli lisensi komersial di [halaman pembelian](https://purchase.aspose.com/buy).

**Q: Bagaimana cara mendapatkan dukungan untuk Aspose.3D?**  
A: Bergabunglah dengan komunitas di [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan gratis, atau buka tiket dukungan dengan lisensi yang valid.

**Q: Apakah tersedia trial gratis?**  
A: Tentu saja. Unduh versi trial dari [halaman trial gratis](https://releases.aspose.com/).

**Q: Di mana saya dapat menemukan dokumentasi detail untuk Aspose.3D?**  
A: Semua referensi API tersedia di [dokumentasi resmi](https://reference.aspose.com/3d/java/).

**Q: Bagaimana cara mendapatkan lisensi sementara untuk pengujian?**  
A: Minta satu melalui [tautan lisensi sementara](https://purchase.aspose.com/temporary-license/).

## Kesimpulan

Anda kini **telah membuat 3D scene di Java**, menerapkan material PBR yang realistis, dan mengekspor hasilnya sebagai file STL menggunakan Aspose.3D. Alur kerja ini memberi Anda dasar yang kuat untuk membangun visualisasi yang lebih kaya, menyiapkan aset untuk pencetakan 3‑D, atau memasukkan model ke dalam mesin game.

---

**Terakhir Diperbarui:** 2025-12-08  
**Diuji Dengan:** Aspose.3D 24.12 (terbaru)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}