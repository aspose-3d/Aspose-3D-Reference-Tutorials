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

## Perkenalan

Jika Anda membangun aplikasi 3D berbasis Java, Anda sering perlu menggunakan kembali geometri yang sama pada beberapa objek sambil memberikan setiap contoh tampilan yang unik. Dalam tutorial ini Anda akan belajar **cara mengonversi mesh ke FBX**, berbagi geometri mesh yang mendasarinya di antara beberapa node, dan **mengatur warna material yang berbeda untuk setiap node**. Pada akhir tutorial Anda akan memiliki scene FBX siap‑ekspor yang dapat Anda masukkan ke dalam mesin atau penaampil apa pun.

## Jawaban Cepat
- **Apa tujuan utama?** Mengonversi mesh ke FBX, berbagi geometri mesh, dan mengatur warna material yang berbeda untuk setiap node.
- **Perpustakaan apa yang diperlukan?** Aspose.3D untuk Java.
- **Bagaimana cara mengekspor hasilnya?** Simpan adegan sebagai file FBX menggunakan `FileFormat.FBX7400ASCII`.
- **Apakah saya memerlukan lisensi?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.
- **Versi Java apa yang cocok?** Lingkungan Java8+ apa pun.

## Apa itu **konversi mesh ke FBX**?

`convert mesh to fbx` adalah proses pengambilan objek mesh yang dibuat atau dimanipulasi dalam memori dan menuliskannya ke format file FBX, yang didukung secara luas oleh alat 3D seperti Maya, Blender, dan Unity. Aspose.3D menangani pekerjaan berat, sehingga Anda hanya perlu memanggil `scene.save(...)` dengan `FileFormat` yang sesuai.

## Mengapa berbagi data geometri mesh?

Berbagi geometri mengurangi konsumsi memori dan mempercepat rendering karena buffer vertex yang mendasarinya disimpan hanya sekali. Teknik ini sempurna untuk pemandangan dengan banyak duplikat objek—misalnya hutan, kepadatan, atau arsitektur modular—di mana setiap instance hanya berbeda pada transformasi atau material.

## Prasyarat

Sebelum kita memulai tutorial, pastikan Anda memiliki prasyarat berikut:

- **Lingkungan Pengembangan Java** – IDE apa pun atau pengaturan command‑line dengan Java8 atau yang lebih baru.
- **Perpustakaan Aspose.3D** – unduh JAR terbaru dari situs resmi: [here](https://releases.aspose.com/3d/java/).

## Impor Paket

Mulailah dengan mengimpor paket yang diperlukan ke dalam proyek Java Anda. Langkah ini penting untuk mengakses fungsionalitas yang disediakan oleh perpustakaan Aspose.3D.

```java
import com.aspose.threed.*;
```

## Langkah 1: Inisialisasi Objek Scene (inisialisasi scene java)

Mari kita memulai proses dengan menginisialisasi objek scene. Ini akan berfungsi sebagai kanvas tempat keajaiban 3D kami akan terungkap.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Langkah 2: Definisikan Vektor Warna

Pada langkah ini, kami mendefinisikan sebuah array vektor warna yang akan diterapkan pada elemen berbeda dalam scene 3D kami.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Langkah 3: Buat Mesh 3D Java Menggunakan Polygon Builder (buat mesh 3d java)

Manfaatkan kelas Common untuk membuat mesh menggunakan metode polygon builder. Mesh ini akan menjadi dasar bagi elemen 3D kami.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Bagaimana cara mengatur warna material untuk setiap node?

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

## Langkah 5: Simpan Scene 3D (simpan scene fbx, konversi mesh ke fbx)

Tentukan direktori dan nama file untuk menyimpan scene 3D dalam format file yang didukung, dalam kasus ini, FBX7400ASCII. Langkah ini juga memperlihatkan **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Kesalahan Umum & Tips

- **Masalah Path** – Pastikan jalur direktori diakhiri dengan pemisah file (`/` atau `\\`) sebelum menambahkan nama file.  
- **Inisialisasi Lisensi** – Jika Anda lupa mengatur lisensi Aspose.3D sebelum memanggil `scene.save`, perpustakaan akan berjalan dalam mode percobaan dan mungkin menyisipkan watermark.  
- **Penimpaan Material** – Menggunakan kembali instance `LambertMaterial` yang sama untuk beberapa node akan menyebabkan semua node berbagi warna yang sama. Selalu buat material baru per iterasi, seperti yang ditunjukkan di atas.  
- **Mesh Besar** – Untuk mesh dengan jutaan vertex, pertimbangkan menggunakan `MeshBuilder` dengan polygon terindeks untuk menjaga ukuran file FBX tetap dapat dikelola.

## Pertanyaan yang Sering Diajukan Tambahan

**T1: Dapatkah saya menggunakan Aspose.3D dengan framework Java lainnya?**
J1: Ya, Aspose.3D dirancang untuk bekerja dengan lancar dengan berbagai framework Java.

**T2: Apakah ada opsi lisensi yang tersedia untuk Aspose.3D?**
J2: Ya, Anda dapat menjelajahi opsi lisensi [di sini](https://purchase.aspose.com/buy).

**T3: Bagaimana saya bisa mendapatkan dukungan untuk Aspose.3D?**
J3: Kunjungi [forum](https://forum.aspose.com/c/3d/18) Aspose.3D untuk mendapatkan dukungan dan diskusi.

**T4: Apakah ada uji coba gratis yang tersedia?**
J4: Ya, Anda bisa mendapatkan uji coba gratis [di sini](https://releases.aspose.com/).

**T5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**
J5: Anda bisa mendapatkan lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

## Kesimpulan

Selamat! Anda telah berhasil **mengonversi mesh ke FBX**, membagikan data geometri mesh antar beberapa node, dan mengatur warna material individual menggunakan Aspose.3D untuk Java. Alur kerja ini memberi Anda arsitektur mesh yang ringan dan dapat digunakan kembali yang dapat diekspor ke pipeline yang kompatibel dengan FBX.

---

**Terakhir Diperbarui:** 2026-02-17
**Diuji Dengan:** Aspose.3D 24.11 untuk Java
**Penulis:** Aspose 

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}