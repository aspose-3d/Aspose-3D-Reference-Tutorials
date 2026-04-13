---
date: 2026-02-22
description: Pelajari cara membuat ekstrusi 3D dengan irisan menggunakan Aspose.3D
  untuk Java. Panduan langkah demi langkah ini mencakup ekstrusi linier, mengatur
  radius pembulatan, dan mengekspor OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Buat Ekstrusi 3D dengan Irisan – Aspose.3D untuk Java
url: /id/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Buat Ekstrusi 3D dengan Irisan – Aspose.3D untuk Java

## Pendahuluan

Jika Anda perlu **membuat ekstrusi 3d** objek yang tampak halus dan presisi, mengontrol jumlah irisan adalah kuncinya. Dalam tutorial ini kami akan menjelaskan cara menentukan irisan saat melakukan ekstrusi linier dengan Aspose.3D untuk Java. Anda akan melihat mengapa jumlah irisan penting, cara mengatur radius pembulatan, dan cara mengekspor hasilnya sebagai file OBJ yang dapat digunakan dalam pipeline 3D apa pun.

## Jawaban Cepat
- **Apa yang dikontrol oleh “slices”?** Jumlah penampang menengah yang digunakan untuk memperkirakan permukaan ekstrusi.  
- **Metode mana yang mengatur jumlah irisan?** `LinearExtrusion.setSlices(int)`  
- **Bisakah saya mengubah radius pembulatan profil?** Ya, melalui `RectangleShape.setRoundingRadius(double)`  
- **Format file apa yang digunakan dalam contoh ini?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Versi percobaan gratis cukup untuk evaluasi; lisensi komersial diperlukan untuk produksi.

## Apa itu ekstrusi linier dengan irisan?

Ekstrusi linier mengambil profil 2‑D (seperti persegi panjang) dan memanjang‑nya sepanjang garis lurus untuk membentuk padatan 3‑D. Dengan menentukan **irisan**, Anda memberi tahu Aspose.3D berapa banyak langkah menengah yang harus dihasilkan, yang secara langsung memengaruhi kelancaran tepi melengkung seperti persegi panjang dengan sudut bulat.

## Mengapa menggunakan Aspose.3D untuk Java untuk membuat ekstrusi 3d?

* **Kontrol penuh** – Anda dapat menyesuaikan jumlah irisan, radius pembulatan, dan format ekspor secara programatik.  
* **Lintas platform** – Berfungsi di lingkungan Java apa pun tanpa ketergantungan native.  
* **Fleksibilitas ekspor** – Langsung menyimpan ke OBJ, FBX, STL, dan banyak format lainnya.

## Prasyarat

1. **Java Development Kit** – JDK 8 atau lebih tinggi terpasang.  
2. **Aspose.3D untuk Java** – Unduh perpustakaan dari situs resmi [di sini](https://releases.aspose.com/3d/java/).  
3. IDE atau editor teks pilihan Anda.

## Impor Paket

Tambahkan namespace Aspose.3D ke proyek Anda sehingga dapat mengakses kelas pemodelan 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan scene dan definisikan profil

Pertama kami membuat `RectangleShape` dan memberikan **radius pembulatan** agar sudutnya halus. Kemudian kami menginisialisasi `Scene` baru yang akan menampung semua geometri.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Langkah 2: **Buat objek child node** untuk setiap ekstrusi

Setiap potongan geometri berada di bawah sebuah `Node`. Di sini kami menghasilkan dua node saudara – satu untuk ekstrusi irisan rendah dan satu lagi untuk ekstrusi irisan tinggi – serta memindahkan node kiri sedikit ke samping agar hasilnya mudah dibandingkan.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 3: Lakukan ekstrusi linier dan **atur irisan**

Sekarang kami benar‑benar **membuat objek ekstrusi 3d**. Konstruktor `LinearExtrusion` menerima profil dan kedalaman ekstrusi. Menggunakan **kelas anonim dalam** kami memanggil `setSlices` untuk mengontrol kelancaran. Node kiri hanya mendapat 2 irisan (kasar), sementara node kanan mendapat 10 irisan (halus).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Langkah 4: **Ekspor OBJ** – simpan scene

Akhirnya kami menulis scene ke file Wavefront OBJ, format yang banyak didukung oleh editor 3‑D dan mesin game. Ini menunjukkan kemampuan **export obj java** dari Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|---------|----------------|--------|
| **Ekstrusi tampak datar** | Jumlah irisan diatur ke 1 atau 0 | Pastikan `setSlices` dipanggil dengan nilai ≥ 2. |
| **Sudut bulat terlihat bergerigi** | Radius pembulatan terlalu kecil relatif terhadap jumlah irisan | Tingkatkan radius atau jumlah irisan untuk kurva yang lebih halus. |
| **File tidak ditemukan saat menyimpan** | `MyDir` mengarah ke folder yang tidak ada | Buat direktori terlebih dahulu atau gunakan path absolut. |

## Pertanyaan yang Sering Diajukan

**Q: Bagaimana saya dapat mengunduh Aspose.3D untuk Java?**  
A: Anda dapat mengunduh perpustakaan [di sini](https://releases.aspose.com/3d/java/).

**Q: Di mana saya dapat menemukan dokumentasi untuk Aspose.3D?**  
A: Lihat dokumentasi [di sini](https://reference.aspose.com/3d/java/).

**Q: Apakah tersedia versi percobaan gratis?**  
A: Ya, Anda dapat menjelajahi versi percobaan gratis [di sini](https://releases.aspose.com/).

**Q: Bagaimana cara mendapatkan dukungan untuk Aspose.3D?**  
A: Kunjungi forum dukungan [di sini](https://forum.aspose.com/c/3d/18).

**Q: Bisakah saya membeli lisensi sementara?**  
A: Ya, lisensi sementara dapat diperoleh [di sini](https://purchase.aspose.com/temporary-license/).

---

**Terakhir Diperbarui:** 2026-02-22  
**Diuji dengan:** Aspose.3D untuk Java 24.11 (terbaru pada saat penulisan)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}