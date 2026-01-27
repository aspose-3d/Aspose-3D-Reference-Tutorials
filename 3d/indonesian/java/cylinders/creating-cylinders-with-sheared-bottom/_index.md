---
date: 2026-01-27
description: Pelajari pemodelan 3D Java dengan membuat silinder yang memiliki dasar
  miring menggunakan Aspose.3D untuk Java. Tutorial 3D pemula ini menunjukkan cara
  menginstal Aspose 3D, menerapkan transformasi shear, dan mengekspor file OBJ Java.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Pemodelan 3D Java – Silinder Dasar yang Dimiringkan dengan Aspose.3D
url: /id/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Pemodelan 3D Java – Silinder Dasar yang Di-shear dengan Aspose.3D

## Pendahuluan

Selamat datang di tutorial **java 3d modeling** ini! Dalam panduan langkah‑demi‑langkah ini kami akan menunjukkan cara membuat silinder dengan bagian bawah yang di-shear, menggunakan pustaka Aspose.3D untuk Java. Baik Anda mengikuti **beginner 3d tutorial** atau ingin menambahkan transformasi shear khusus pada model yang ada, Anda akan melihat secara tepat cara menyiapkan scene, menerapkan shear, dan akhirnya **export OBJ file java** untuk digunakan di alat lain.

## Jawaban Cepat
- **Library apa yang digunakan?** Aspose.3D for Java  
- **Bisakah saya menginstal Aspose 3D via Maven?** Ya – tambahkan dependensi Aspose.3D ke `pom.xml` Anda  
- **Apakah lisensi diperlukan untuk pengembangan?** Lisensi sementara cukup untuk pengujian; lisensi penuh diperlukan untuk produksi  
- **Format file apa yang ditunjukkan?** Wavefront OBJ (`.obj`)  
- **Berapa lama contoh ini dijalankan?** Kurang dari satu detik pada workstation tipikal  

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki hal berikut:

- Java Development Kit (JDK) terinstal di sistem Anda.  
- **Instal Aspose 3D** – unduh pustaka dari situs resmi [di sini](https://releases.aspose.com/3d/java/).  
- IDE atau alat build (Maven/Gradle) untuk mengelola dependensi Aspose.3D.  

## Impor Paket

Pertama, impor kelas-kelas yang diperlukan untuk scene, geometri, dan penanganan file.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Buat Scene

Scene adalah wadah untuk semua objek 3‑D. Kita akan memulai dengan membuat scene kosong.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Langkah 2: Buat Cylinder 1 – Cara Meng-shear Cylinder

Sekarang kita akan membangun silinder pertama dan **menerapkan transformasi shear** pada bagian bawahnya. Ini menunjukkan **cara meng-shear cylinder** secara langsung melalui API.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Langkah 3: Buat Cylinder 2 – Silinder Standar (Tanpa Shear)

Sebagai perbandingan, kita akan menambahkan silinder kedua yang **tidak** memiliki bagian bawah yang di-shear.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Langkah 4: Simpan Scene – Export OBJ File Java

Akhirnya, kita mengekspor scene ke file Wavefront OBJ, memperlihatkan penggunaan **export obj file java**.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Mengapa Ini Penting untuk Pemodelan 3D Java

Menambahkan shear pada primitif memungkinkan Anda membuat bentuk yang lebih organik tanpa harus menggunakan alat pemodelan eksternal. Teknik ini berguna untuk:

- Visualisasi arsitektur yang memerlukan dasar miring.  
- Aset game yang memerlukan jejak khusus sambil menjaga geometri tetap ringan.  
- Prototipe cepat di mana Anda ingin menyesuaikan dimensi secara programatis.

## Masalah Umum & Solusi

| Issue | Solution |
|-------|----------|
| **Shear terlihat terlalu ekstrem** | Sesuaikan nilai `Vector2`; nilai tersebut mewakili faktor shear (rentang 0‑1). |
| **File OBJ tidak dapat dibuka di penampil** | Pastikan direktori target ada dan Anda memiliki izin menulis. |
| **Pengecualian lisensi saat runtime** | Terapkan lisensi sementara atau permanen sebelum membuat scene (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D untuk Java dengan pustaka Java 3D lainnya?**  
A: Aspose.3D dirancang untuk bekerja secara mandiri. Meskipun Anda dapat mengintegrasikannya dengan pustaka lain, ia sudah menyediakan API lengkap untuk sebagian besar tugas 3‑D.

**Q: Apakah Aspose.3D cocok untuk pemula dalam pemodelan 3D?**  
A: Tentu saja. API-nya sederhana, dan **beginner 3d tutorial** ini menunjukkan konsep inti dengan kode minimal.

**Q: Di mana saya dapat menemukan dukungan tambahan untuk Aspose.3D untuk Java?**  
A: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan komunitas dan jawaban resmi.

**Q: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A: Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

**Q: Di mana saya dapat membeli lisensi penuh Aspose.3D untuk Java?**  
A: Opsi pembelian tersedia [di sini](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2026-01-27  
**Diuji Dengan:** Aspose.3D 24.11 for Java  
**Penulis:** Aspose