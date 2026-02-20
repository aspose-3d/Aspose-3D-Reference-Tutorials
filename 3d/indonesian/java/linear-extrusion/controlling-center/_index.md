---
date: 2026-02-20
description: Pelajari tutorial grafis 3D Java tentang mengontrol pusat dalam ekstrusi
  linier dengan Aspose.3D, termasuk cara mengatur radius pembulatan dan menyimpan
  file OBJ Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tutorial Grafik 3D Java – Pusat pada Ekstrusi Linear
url: /id/java/linear-extrusion/controlling-center/
weight: 11
---

 produce final output.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tutorial Grafik 3D Java – Pusat pada Ekstrusi Linear

## Pendahuluan

Jika Anda membangun visualisasi 3D dalam Java, menguasai teknik ekstrusi sangat penting. **java 3d graphics tutorial** ini memandu Anda mengontrol pusat ekstrusi linear menggunakan Aspose.3D for Java, sehingga Anda dapat membuat model yang tepat dan simetris tanpa perhitungan tambahan. Pada akhir panduan ini Anda akan memahami mengapa properti `center` penting, cara **set rounding radius**, dan cara **save OBJ file java**‑compatible output.

## Jawaban Cepat
- **Apa fungsi properti center?** Menentukan apakah ekstrusi simetris di sekitar asal profil.  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Lisensi sementara dapat digunakan untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Format file apa yang digunakan untuk hasil?** Scene disimpan sebagai file Wavefront OBJ.  
- **Bisakah saya mengubah jumlah irisan?** Ya, gunakan `setSlices(int)` pada objek `LinearExtrusion`.  
- **Apakah Aspose.3D kompatibel dengan Java 8+?** Tentu – mendukung semua versi Java modern.

## Apa itu tutorial grafik 3D Java?

**java 3d graphics tutorial** menjelaskan langkah‑per‑langkah cara menggunakan pustaka Java untuk membuat, memanipulasi, dan merender objek tiga‑dimensi. Dalam kasus ini, kami fokus pada API ekstrusi Aspose.3D, yang mengubah profil 2‑D menjadi mesh 3‑D lengkap.

## Mengapa menggunakan Aspose.3D untuk Java?

- **API tingkat tinggi** – Tidak perlu menulis perhitungan mesh tingkat rendah.  
- **Dukungan lintas format** – Ekspor ke OBJ, FBX, STL, dan lainnya.  
- **Dioptimalkan untuk kinerja** – Menangani scene besar secara efisien.  
- **Dokumentasi lengkap** – Menyertakan contoh seperti di bawah.

## Prasyarat

Sebelum kita mulai, pastikan Anda memiliki:

1. **Lingkungan Pengembangan Java** – JDK 8 atau yang lebih baru terpasang.  
2. **Aspose.3D untuk Java** – Unduh pustaka dan dokumentasi [di sini](https://reference.aspose.com/3d/java/).  
3. **Direktori Dokumen** – Buat folder di mesin Anda untuk menyimpan file yang dihasilkan; kami akan menyebutnya **“Your Document Directory.”**

## Impor Paket

Di IDE Java Anda, impor kelas Aspose.3D yang diperlukan. Ini memberi kompiler akses ke fitur ekstrusi dan pembuatan scene.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Siapkan Profil Dasar

Pertama, buat bentuk 2‑D yang akan diekstrusi. Di sini kami menggunakan persegi panjang dan **set rounding radius** ke 0.3, yang melunakkan sudut.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Langkah 2: Buat Scene 3D

Objek `Scene` berfungsi sebagai wadah untuk semua node 3‑D, cahaya, dan kamera.

```java
Scene scene = new Scene();
```

### Langkah 3: Tambahkan Node Kiri dan Kanan

Kami akan menempatkan dua node terpisah berdampingan sehingga Anda dapat membandingkan ekstrusi dengan dan tanpa pemusatan.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Langkah 4: Ekstrusi Linear – Tanpa Pusat (Node Kiri)

Buat ekstrusi pada node kiri, nonaktifkan pemusatan, dan batasi mesh menjadi tiga irisan untuk pratinjau low‑poly.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Langkah 5: Tambahkan Plane Dasar untuk Referensi (Node Kiri)

Kotak tipis berfungsi sebagai lantai visual, membantu Anda melihat orientasi ekstrusi.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Langkah 6: Ekstrusi Linear – Berpusat (Node Kanan)

Sekarang ulangi ekstrusi, kali ini mengaktifkan `center`. Geometri akan simetris di sekitar asal profil.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Langkah 7: Tambahkan Plane Dasar untuk Referensi (Node Kanan)

Plane dasar yang sama untuk sisi kanan, membuat perbandingan menjadi jelas.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Langkah 8: Simpan Scene 3D

Akhirnya, ekspor seluruh scene ke file Wavefront OBJ – format yang siap pakai di sebagian besar editor 3‑D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Mengapa Terjadi | Solusi |
|-------|----------------|-----|
| **Ekstrusi terlihat bergeser** | `setCenter(false)` membuat profil terikat pada sudutnya. | Gunakan `setCenter(true)` untuk hasil simetris. |
| **File OBJ kosong** | Path direktori output tidak benar atau tidak memiliki izin menulis. | Pastikan `MyDir` mengarah ke folder yang ada dan aplikasi memiliki akses menulis. |
| **Sudut melengkung terlihat tajam** | Radius pembulatan terlalu kecil dibandingkan ukuran persegi panjang. | Tingkatkan nilai radius (mis., `setRoundingRadius(0.5)`). |

## Pertanyaan yang Sering Diajukan

### Q1: Can I use Aspose.3D for Java in commercial projects?

A1: Ya, Aspose.3D untuk Java tersedia untuk penggunaan komersial. Untuk detail lisensi, kunjungi [di sini](https://purchase.aspose.com/buy).

### Q2: Is there a free trial available?

A2: Ya, Anda dapat mencoba versi percobaan gratis Aspose.3D untuk Java [di sini](https://releases.aspose.com/).

### Q3: Where can I find support for Aspose.3D for Java?

A3: Forum komunitas Aspose.3D adalah tempat yang bagus untuk mencari dukungan dan berbagi pengalaman. Kunjungi forum [di sini](https://forum.aspose.com/c/3d/18).

### Q4: Do I need a temporary license for testing?

A4: Ya, jika Anda memerlukan lisensi sementara untuk tujuan pengujian, Anda dapat mendapatkannya [di sini](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I find the documentation?

A5: Dokumentasi untuk Aspose.3D untuk Java tersedia [di sini](https://reference.aspose.com/3d/java/).

## Kesimpulan

Dengan menyelesaikan **java 3d graphics tutorial** ini, Anda kini tahu cara mengontrol pusat ekstrusi linear, menyesuaikan radius pembulatan, dan **save OBJ file java** output menggunakan Aspose.3D. Teknik ini memberi Anda kontrol detail atas simetri mesh, yang penting untuk aset game, prototipe CAD, dan visualisasi ilmiah. Jangan ragu untuk bereksperimen dengan profil berbeda, jumlah irisan, dan format ekspor untuk memperluas kotak peralatan 3‑D Anda.

---

**Last Updated:** 2026-02-20  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}