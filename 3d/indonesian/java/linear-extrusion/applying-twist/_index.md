---
date: 2025-12-17
description: Pelajari cara membuat model 3D berputar menggunakan Aspose.3D untuk Java
  dengan ekstrusi linier berputar dan mengekspor file OBJ Java. Ikuti panduan langkah
  demi langkah kami.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Buat Model 3D Berputar – Menerapkan Putaran pada Ekstrusi Linear dengan Aspose.3D
  untuk Java
url: /id/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Menerapkan Twist pada Linear Extrusion dengan Aspose.3D untuk Java

## Pendahuluan

Selamat datang di tutorial langkah‑demi‑langkah ini tentang **cara membuat model 3D berputar** dengan menerapkan twist selama linear extrusion menggunakan Aspose.3D untuk Java. Baik Anda membuat visualisasi arsitektur, aset game, atau prototipe rekayasa, menambahkan twist dapat memberikan geometri Anda tampilan dinamis yang berspiral dengan hanya beberapa baris kode.

## Jawaban Cepat
- **Apa arti “twist” dalam extrusion?** Itu memutar profil di sekitar sumbu extrusion saat bentuk diperluas.  
- **Kelas API mana yang menangani twist?** `LinearExtrusion` menyediakan metode `setTwist`.  
- **Apakah saya memerlukan lisensi untuk menjalankan contoh?** Versi percobaan gratis dapat digunakan untuk evaluasi; lisensi komersial diperlukan untuk produksi.  
- **Bisakah saya mengekspor hasil sebagai OBJ?** Ya, gunakan `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Versi Java apa yang diperlukan?** Java 8 atau yang lebih baru didukung sepenuhnya.

## Prasyarat

Sebelum memulai tutorial, pastikan Anda memiliki prasyarat berikut:

- Lingkungan Pengembangan Java: Pastikan Java terpasang di sistem Anda.  
- Perpustakaan Aspose.3D: Unduh dan instal perpustakaan Aspose.3D untuk Java dari [tautan unduhan](https://releases.aspose.com/3d/java/).  
- Dokumentasi: Lihat [dokumentasi Aspose.3D](https://reference.aspose.com/3d/java/) untuk panduan lengkap.

## Impor Paket

Sebelum memulai proses penulisan kode, impor paket yang diperlukan ke dalam proyek Java Anda. Berikut contoh cara melakukannya:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Atur Direktori Dokumen

Pertama, tentukan lokasi penyimpanan file 3D yang dihasilkan.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Inisialisasi Profil Dasar

Selanjutnya, buat bentuk yang akan diekstrusi. Pada contoh ini kami menggunakan persegi panjang dengan radius pembulatan kecil.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Buat Scene

Objek `Scene` berfungsi sebagai wadah untuk semua node 3D.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Buat Node

Tambahkan dua node anak ke scene – satu akan tetap lurus, yang lainnya akan menerima twist.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Twist pada Linear Extrusion

Sekarang kita melakukan **twist linear extrusion** pada kedua node. Node kiri mendapatkan twist 0° (lurus), sedangkan node kanan mendapatkan twist 90°, menghasilkan bentuk berspiral. Kami juga mengatur jumlah irisan (slices) untuk memastikan geometri yang halus.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Ekspor File OBJ Java

Akhirnya, simpan scene dalam format OBJ yang banyak didukung. Ini menunjukkan kemampuan **ekspor file OBJ Java** dari Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Mengapa Ini Penting

Membuat model 3D bertwist memberikan efek visual yang kuat tanpa memerlukan alat pemodelan eksternal. Ini sangat berguna untuk:

- **Komponen mekanik** yang memerlukan fitur heliks (mis., pegas, sekrup).  
- **Desain artistik** di mana spiral halus menambah daya tarik visual.  
- **Aset game** yang mendapat manfaat dari geometri low‑poly yang dihasilkan secara prosedural.

## Masalah Umum & Tips

| Masalah | Solusi |
|-------|----------|
| Twist muncul datar atau tidak muncul | Pastikan `setSlices` cukup tinggi (mis., 100) untuk rotasi yang halus. |
| File OBJ tidak dapat dibuka di penampil | Verifikasi bahwa jalur output (`MyDir`) benar dan file memiliki izin menulis. |
| Skala tidak terduga | Periksa sistem satuan profil sumber Anda; Aspose.3D secara default menggunakan meter. |

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D untuk Java untuk bekerja dengan format file 3D lainnya?**  
A: Ya, Aspose.3D mendukung berbagai format seperti FBX, STL, 3MF, dan lainnya.

**Q: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?**  
A: Kunjungi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk bantuan komunitas dan dukungan resmi.

**Q: Apakah tersedia versi percobaan gratis?**  
A: Ya, Anda dapat mengunduh versi percobaan dari [sini](https://releases.aspose.com/).

**Q: Bagaimana cara mendapatkan lisensi sementara untuk pengujian?**  
A: Dapatkan lisensi sementara dari [halaman lisensi sementara](https://purchase.aspose.com/temporary-license/).

**Q: Di mana saya dapat membeli lisensi penuh?**  
A: Beli Aspose.3D untuk Java dari [halaman pembelian](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Terakhir Diperbarui:** 2025-12-17  
**Diuji Dengan:** Aspose.3D 24.11 untuk Java  
**Penulis:** Aspose  

---