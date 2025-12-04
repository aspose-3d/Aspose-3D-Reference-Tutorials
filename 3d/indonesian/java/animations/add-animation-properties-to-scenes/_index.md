---
date: 2025-12-04
description: Pelajari **cara menganimasi 3D** dalam Java menggunakan Aspose.3D. Panduan
  langkah‑demi‑langkah ini menunjukkan cara menambahkan properti animasi, membuat
  keyframe, dan mengekspor hasilnya.
language: id
linktitle: How to Animate 3D Scenes in Java – Add Animation Properties with Aspose.3D
  Tutorial
second_title: Aspose.3D Java API
title: Cara Menganimasikan Adegan 3D dalam Java – Tambahkan Properti Animasi dengan
  Tutorial Aspose.3D
url: /java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Menggerakkan Adegan 3D di Java – Menambahkan Properti Animasi dengan Aspose.3D

## Pendahuluan

Jika Anda mencari panduan praktis yang jelas tentang **cara menggerakkan objek 3D** dalam aplikasi Java, Anda berada di tempat yang tepat. Pada tutorial ini kami akan membahas setiap langkah yang diperlukan untuk menambahkan properti animasi ke sebuah adegan 3D menggunakan pustaka Aspose.3D— mulai dari membuat adegan dan mesh hingga mendefinisikan keyframe dan akhirnya mengekspor file yang telah dianimasikan. Pada akhir tutorial Anda akan memiliki file FBX yang dapat dimuat ke dalam penampil 3D modern atau mesin game apa pun.

## Jawaban Cepat
- **Pustaka apa yang digunakan?** Aspose.3D untuk Java  
- **Apakah dapat mengekspor ke FBX?** Ya, tutorial ini menyimpan adegan sebagai FBX7500ASCII.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis cukup untuk pengujian; lisensi komersial diperlukan untuk produksi.  
- **Versi Java apa yang dibutuhkan?** Java 8 atau lebih tinggi.  
- **Apakah animasinya linear atau spline?** Kedua‑nya—keyframe dapat menggunakan interpolasi BEZIER atau LINEAR.

## Apa itu “cara menggerakkan 3d” di Java?

Menggerakkan objek 3D berarti mengubah properti transformasinya (posisi, rotasi, skala) seiring waktu. Aspose.3D menyediakan API tingkat tinggi yang memungkinkan Anda membuat **bind point**, melampirkan **urutan keyframe**, dan mengontrol interpolasi, semuanya tanpa menulis mesin animasi khusus.

## Mengapa menggunakan Aspose.3D untuk animasi?

- **Dukungan lintas format** – Ekspor ke FBX, OBJ, 3MF, dan lainnya.  
- **Tanpa dependensi native** – Murni Java, ideal untuk pipeline sisi‑server.  
- **Opsi interpolasi kaya** – Kurva BEZIER, LINEAR, dan STEP.  
- **Graf adegan lengkap** – Node, mesh, material, dan animasi semuanya dapat diakses melalui satu API.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pengetahuan dasar pemrograman Java.  
- Aspose.3D untuk Java terpasang (unduh dari [halaman rilis](https://releases.aspose.com/3d/java/)).  
- IDE Java atau alat build (Maven/Gradle) siap untuk mengkompilasi contoh.

## Mengimpor Paket

Di proyek Java Anda, impor kelas inti Aspose.3D dan kelas pembantu `Common` yang digunakan untuk membangun mesh sederhana:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

Setelah namespace siap, mari mulai membangun adegan.

## Langkah 1: Inisialisasi Adegan

```java
// Initialize scene object
Scene scene = new Scene();
```

`Scene` adalah kontainer untuk semua node, mesh, cahaya, dan data animasi.

## Langkah 2: Buat Mesh menggunakan Polygon Builder

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

Pembantu ini membuat mesh kubus dasar yang akan kita animasikan nanti.

## Langkah 3: Buat Node Kubus dengan Translasi

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

Setiap node dapat memiliki transformasinya sendiri (translasi, rotasi, skala). Di sini kami menambahkan node anak bernama **cube1**.

## Langkah 4: Temukan Properti Translasi

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

Properti `Translation` adalah yang akan kami animasikan—memindahkan kubus sepanjang sumbu X, Y, atau Z.

## Langkah 5: Buat Bind Point

```java
// Create a bind point based on the translation property
BindPoint bindPoint = new BindPoint(scene, translation);
```

Sebuah **bind point** menghubungkan properti (seperti translasi) ke kurva animasi.

## Langkah 6: Buat Kurva Animasi untuk Sumbu X

```java
// Create the animation curve on the X component of the scale
KeyframeSequence kfs = new KeyframeSequence();

// Add keyframes for X component
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X component
bindPoint.bindKeyframeSequence("X", kfs);
```

Kurva ini mendefinisikan tiga keyframe: pada waktu 0, 3, dan 5 detik. Dua pertama menggunakan **BEZIER** untuk gerakan halus, sementara yang terakhir menggunakan **LINEAR**.

## Langkah 7: Ulangi untuk Komponen Z

```java
// Repeat the process for the Z component
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

Menganimasikan sumbu Z memberi kubus jalur yang lebih dinamis melalui ruang 3‑D.

## Langkah 8: Simpan Adegan 3D

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

Adegan disimpan sebagai file FBX, yang dapat Anda buka di alat seperti Blender, Unity, atau Autodesk Maya untuk melihat pratinjau animasi.

## Masalah Umum dan Solusinya

| Gejala | Penyebab Kemungkinan | Solusi |
|--------|----------------------|--------|
| Tidak ada gerakan yang terlihat | Keyframe ditambahkan ke komponen yang salah (misalnya “Y” alih‑alih “X”) | Verifikasi nama komponen dalam `bindKeyframeSequence`. |
| Animasi melompat | Interpolasi BEZIER dan LINEAR dicampur secara tidak tepat | Jaga konsistensi interpolasi untuk gerakan lebih halus, atau sesuaikan tangent secara manual. |
| File tidak tersimpan | Path direktori tidak valid | Pastikan `MyDir` mengarah ke folder yang ada dan dapat ditulisi serta berakhiran `.fbx`. |

## Pertanyaan yang Sering Diajukan

**T: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?**  
J: Ya. Beli lisensi komersial di [halaman pembelian Aspose](https://purchase.aspose.com/buy).

**T: Apakah tersedia versi percobaan gratis?**  
J: Tentu saja. Unduh percobaan dari [halaman rilis Aspose](https://releases.aspose.com/).

**T: Di mana saya dapat menemukan dukungan untuk Aspose.3D?**  
J: Bergabunglah dengan komunitas di [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan dari staf maupun pengguna lain.

**T: Bagaimana cara mendapatkan lisensi sementara untuk evaluasi?**  
J: Minta [lisensi sementara](https://purchase.aspose.com/temporary-license/) untuk menghindari pembatasan runtime selama pengujian.

**T: Apakah ada tutorial lain yang tersedia?**  
J: Ya—jelajahi dokumentasi lengkap [Aspose.3D](https://reference.aspose.com/3d/java/) untuk contoh tambahan dan topik lanjutan.

## Kesimpulan

Anda kini mengetahui **cara menggerakkan objek 3D** di Java menggunakan Aspose.3D: membuat adegan, mengikat properti translasi, mendefinisikan urutan keyframe, dan mengekspor file FBX yang telah dianimasikan. Silakan bereksperimen dengan rotasi, skala, atau beberapa node untuk membangun animasi yang lebih kaya bagi game, simulasi, atau visualisasi.

---

**Terakhir Diperbarui:** 2025-12-04  
**Diuji Dengan:** Aspose.3D untuk Java 24.12 (terbaru)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}