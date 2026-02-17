---
date: 2026-02-17
description: Pelajari cara mengonversi mesh ke FBX sambil mengatur warna material
  dan berbagi data geometri mesh di Java 3D menggunakan Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Konversi Mesh ke FBX dan Atur Warna Material di Java 3D
url: /id/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Konversi Mesh ke FBX dan Atur Warna Material di Java 3D

## Introduction

Jika Anda membangun aplikasi 3D berbasis Java, Anda sering perlu menggunakan kembali geometri yang sama pada beberapa objek sambil memberikan setiap instance tampilan yang unik. Dalam tutorial ini Anda akan belajar **cara mengonversi mesh ke FBX**, berbagi geometri mesh yang mendasarinya di antara beberapa node, dan **mengatur warna material yang berbeda untuk setiap node**. Pada akhir tutorial Anda akan memiliki scene FBX siap‑ekspor yang dapat Anda masukkan ke dalam mesin atau penampil apa pun.

## Quick Answers
- **Apa tujuan utama?** Mengonversi mesh ke FBX, berbagi geometri mesh, dan mengatur warna material yang berbeda untuk setiap node.  
- **Perpustakaan apa yang diperlukan?** Aspose.3D for Java.  
- **Bagaimana cara mengekspor hasilnya?** Simpan scene sebagai file FBX menggunakan `FileFormat.FBX7400ASCII`.  
- **Apakah saya memerlukan lisensi?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.  
- **Versi Java apa yang cocok?** Lingkungan Java 8+ apa pun.

## What is **convert mesh to FBX**?

`convert mesh to fbx` adalah proses mengambil objek mesh yang dibuat atau dimanipulasi dalam memori dan menuliskannya ke format file FBX, yang didukung secara luas oleh alat 3D seperti Maya, Blender, dan Unity. Aspose.3D menangani pekerjaan berat, sehingga Anda hanya perlu memanggil `scene.save(...)` dengan `FileFormat` yang sesuai.

## Why share mesh geometry data?

Berbagi geometri mengurangi konsumsi memori dan mempercepat rendering karena buffer vertex yang mendasari disimpan hanya sekali. Teknik ini sempurna untuk scene dengan banyak objek duplikat—misalnya hutan, kerumunan, atau arsitektur modular—di mana setiap instance hanya berbeda pada transformasi atau material.

## Prerequisites

Sebelum kita memulai tutorial, pastikan Anda memiliki prasyarat berikut:

- **Lingkungan Pengembangan Java** – IDE apa pun atau pengaturan command‑line dengan Java 8 atau yang lebih baru.  
- **Perpustakaan Aspose.3D** – unduh JAR terbaru dari situs resmi: [here](https://releases.aspose.com/3d/java/).

## Import Packages

Mulailah dengan mengimpor paket yang diperlukan ke dalam proyek Java Anda. Langkah ini penting untuk mengakses fungsionalitas yang disediakan oleh perpustakaan Aspose.3D.

```java
import com.aspose.threed.*;
```

## Step 1: Initialize Scene Object (initialize scene java)

Mari kita memulai proses dengan menginisialisasi objek scene. Ini akan berfungsi sebagai kanvas tempat keajaiban 3D kami akan terungkap.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Step 2: Define Color Vectors

Pada langkah ini, kami mendefinisikan sebuah array vektor warna yang akan diterapkan pada elemen berbeda dalam scene 3D kami.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Step 3: Create 3D Mesh Java Using Polygon Builder (create 3d mesh java)

Manfaatkan kelas Common untuk membuat mesh menggunakan metode polygon builder. Mesh ini akan menjadi dasar bagi elemen 3D kami.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## How to set material color for each node?

Iterasi melalui vektor warna, buat node kubus, dan atur atribut seperti material, **set material color**, dan translasi. Ini adalah inti dari mengontrol tampilan visual setiap instance mesh.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)

Tentukan direktori dan nama file untuk menyimpan scene 3D dalam format file yang didukung, dalam kasus ini, FBX7400ASCII. Langkah ini juga memperlihatkan **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Common Pitfalls & Tips

- **Masalah Path** – Pastikan jalur direktori diakhiri dengan pemisah file (`/` atau `\\`) sebelum menambahkan nama file.  
- **Inisialisasi Lisensi** – Jika Anda lupa mengatur lisensi Aspose.3D sebelum memanggil `scene.save`, perpustakaan akan berjalan dalam mode percobaan dan mungkin menyisipkan watermark.  
- **Penimpaan Material** – Menggunakan kembali instance `LambertMaterial` yang sama untuk beberapa node akan menyebabkan semua node berbagi warna yang sama. Selalu buat material baru per iterasi, seperti yang ditunjukkan di atas.  
- **Mesh Besar** – Untuk mesh dengan jutaan vertex, pertimbangkan menggunakan `MeshBuilder` dengan polygon terindeks untuk menjaga ukuran file FBX tetap dapat dikelola.

## Frequently Asked Questions

**T: Bisakah saya mengekspor scene ke format lain selain FBX?**  
J: Ya, Aspose.3D mendukung OBJ, STL, 3MF, GLTF, dan lainnya. Cukup ganti enum `FileFormat` dalam pemanggilan `save`.

**T: Bagaimana jika saya perlu mengubah material setelah scene dibuat?**  
J: Dapatkan node tersebut, ubah `LambertMaterial`-nya (misalnya, `setDiffuseColor`), dan simpan kembali scene.

**T: Apakah perpustakaan menangani mesh besar secara efisien?**  
J: Aspose.3D menggunakan struktur data yang dioptimalkan; namun, untuk mesh yang sangat besar pertimbangkan streaming atau memecah scene.

**T: Apakah ada cara untuk menganimasikan perubahan warna?**  
J: Ya, Anda dapat menganimasikan properti material menggunakan API `AnimationController`.

## Additional Frequently Asked Questions

**Q1: Bisakah saya menggunakan Aspose.3D dengan kerangka kerja Java lainnya?**  
A1: Ya, Aspose.3D dirancang untuk bekerja mulus dengan berbagai kerangka kerja Java.

**Q2: Apakah ada opsi lisensi yang tersedia untuk Aspose.3D?**  
A2: Ya, Anda dapat menjelajahi opsi lisensi [here](https://purchase.aspose.com/buy).

**Q3: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?**  
A3: Kunjungi [forum](https://forum.aspose.com/c/3d/18) Aspose.3D untuk dukungan dan diskusi.

**Q4: Apakah ada percobaan gratis yang tersedia?**  
A4: Ya, Anda dapat mendapatkan percobaan gratis [here](https://releases.aspose.com/).

**Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A5: Anda dapat memperoleh lisensi sementara [here](https://purchase.aspose.com/temporary-license/).

## Conclusion

Selamat! Anda telah berhasil **mengonversi mesh ke FBX**, berbagi data geometri mesh antara beberapa node, dan mengatur warna material individual menggunakan Aspose.3D untuk Java. Alur kerja ini memberi Anda arsitektur mesh ringan dan dapat digunakan kembali yang dapat diekspor ke pipeline apa pun yang kompatibel dengan FBX.

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}