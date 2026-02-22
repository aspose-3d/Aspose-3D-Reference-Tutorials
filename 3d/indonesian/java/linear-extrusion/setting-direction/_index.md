---
date: 2026-02-22
description: Pelajari cara mengatur arah pada ekstrusi linier dan mengekspor model
  3D OBJ menggunakan Aspose.3D untuk Java. Ikuti panduan langkah demi langkah kami.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara Mengatur Arah pada Ekstrusi Linear dengan Aspose.3D untuk Java
url: /id/java/linear-extrusion/setting-direction/
weight: 12
---

.

Let's produce final content.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengatur Arah pada Linear Extrusion dengan Aspose.3D untuk Java

## Pendahuluan

Dalam tutorial komprehensif ini Anda akan menemukan **cara mengatur arah** saat melakukan linear extrusion dengan Aspose.3D untuk Java. Baik Anda sedang membangun alat mirip CAD atau menghasilkan geometri untuk mesin game, mengontrol arah ekstrusi memungkinkan Anda membuat bentuk yang tepat sesuai kebutuhan. Kami akan membimbing Anda melalui setiap langkah, mulai dari menginisialisasi profil hingga menyimpan hasil sebagai file OBJ, sehingga Anda juga dapat **mengekspor 3d model obj** langsung dari Java.

## Jawaban Cepat
- **Apa kelas utama untuk linear extrusion?** `LinearExtrusion`
- **Metode mana yang menentukan arah ekstrusi?** `setDirection(Vector3 direction)`
- **Apakah saya dapat mengekspor hasil sebagai OBJ?** Ya, dengan menggunakan `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis tersedia; lisensi diperlukan untuk produksi.
- **IDE Java apa yang paling cocok?** IntelliJ IDEA atau Eclipse keduanya didukung penuh.

## Apa itu Linear Extrusion?

Linear extrusion mengambil profil 2‑D (seperti persegi panjang atau lingkaran) dan memperluasnya sepanjang garis lurus untuk membuat padatan 3‑D. Secara default ekstrusi mengikuti sumbu Z positif, tetapi Aspose.3D memungkinkan Anda mengubah jalur tersebut dengan properti `setDirection`.

## Mengapa Mengatur Arah pada Linear Extrusion?

Mengatur arah khusus berguna ketika:
- Menyelaraskan geometri dengan objek yang sudah ada dalam scene.
- Membuat bagian miring atau berangsur tanpa langkah transformasi tambahan.
- Mengekspor model yang harus cocok dengan sistem koordinat tertentu (mis., untuk pencetakan 3‑D atau mesin game).

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

- Pengetahuan dasar tentang Java.
- Library Aspose.3D terpasang. Anda dapat mengunduhnya dari [here](https://releases.aspose.com/3d/java/).
- IDE seperti Eclipse atau IntelliJ IDEA.

## Impor Paket

Pertama, impor namespace yang menyediakan kelas 3‑D inti dan tipe utilitas.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Inisialisasi Profil Dasar

Buat bentuk yang akan diekstrusi. Pada contoh ini kami menggunakan `RectangleShape` dengan radius pembulatan kecil untuk memberi tepi tampilan halus.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 2: Buat Scene

Objek `Scene` berfungsi sebagai wadah untuk semua node 3‑D, lampu, kamera, dan material.

```java
Scene scene = new Scene();
```

## Langkah 3: Buat Node

Tambahkan dua node anak ke root scene—satu untuk ekstrusi kiri dan satu untuk ekstrusi kanan. Node kanan dipindahkan sehingga kedua objek tidak saling tumpang tindih.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Lakukan Linear Extrusion pada Node Kiri

Ekstrusi profil pada node kiri menggunakan arah sumbu Z default. Kami juga menambahkan putaran penuh 360° dan meningkatkan jumlah slice untuk mesh yang lebih halus.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Langkah 5: Lakukan Linear Extrusion pada Node Kanan dengan Arah

Di sinilah kami **mengatur arah**. Dengan memberikan `Vector3` khusus ke `setDirection`, ekstrusi mengikuti vektor (0.3, 0.2, 1), menghasilkan bentuk miring.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Langkah 6: Simpan Scene 3D

Akhirnya, ekspor scene ke format Wavefront OBJ. Langkah ini menunjukkan cara **menyimpan file obj java** dan memudahkan melihat hasil di penampil 3‑D apa pun.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| File OBJ muncul kosong | Profil tidak ditambahkan ke node | Pastikan `createChildNode` dipanggil pada node yang valid |
| Arah tampak tidak berubah | `setDirection` dipanggil setelah ekstrusi sudah dibuat | Atur arah di dalam inisialisasi `LinearExtrusion` seperti yang ditunjukkan |
| Mesh beresolusi rendah | Nilai `setSlices` terlalu rendah | Tingkatkan jumlah slice (mis., 100 atau lebih) |

## Kesimpulan

Anda kini tahu **cara mengatur arah** dalam linear extrusion, cara menyesuaikan pengaturan twist dan slice, serta **mengekspor 3d model obj** menggunakan Aspose.3D untuk Java. Teknik ini memberi Anda kontrol detail atas pembuatan geometri dan memudahkan integrasi aset 3‑D ke dalam pipeline yang lebih besar.

## FAQ

### Q1: Bisakah saya menggunakan Aspose.3D dengan bahasa pemrograman lain?

A1: Aspose.3D mendukung berbagai bahasa pemrograman, termasuk .NET dan Java.

### Q2: Apakah ada percobaan gratis untuk Aspose.3D?

A2: Ya, Anda dapat menjelajahi fitur Aspose.3D dengan percobaan gratis [here](https://releases.aspose.com/).

### Q3: Di mana saya dapat menemukan dokumentasi detail untuk Aspose.3D untuk Java?

A3: Dokumentasi lengkap tersedia [here](https://reference.aspose.com/3d/java/).

### Q4: Bagaimana saya dapat mendapatkan dukungan untuk Aspose.3D?

A4: Kunjungi [Aspose.3D forum](https://forum.aspose.com/c/3d/18) untuk bantuan atau pertanyaan.

### Q5: Apakah lisensi sementara tersedia untuk Aspose.3D?

A5: Ya, Anda dapat memperoleh lisensi sementara [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2026-02-22  
**Diuji Dengan:** Aspose.3D for Java (latest release)  
**Penulis:** Aspose