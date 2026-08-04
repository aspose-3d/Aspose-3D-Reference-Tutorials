---
date: 2026-04-08
description: Pelajari cara membuat silinder dengan offset bagian atas di Aspose.3D
  untuk Java, tambahkan node anak Java, atur offset bagian atas, hasilkan model 3D,
  dan ekspor OBJ menggunakan lisensi sementara Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Lisensi Sementara Aspose – Buat Silinder dengan Bagian Atas Teroffset (Java)
second_title: Aspose.3D Java API
title: Lisensi Sementara Aspose – Membuat Silinder dengan Bagian Atas Teroffset (Java)
url: /id/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Buat Silinder dengan Offset Atas (Java)

## Pendahuluan

Jika Anda ingin **create cylinder** objek dengan offset atas khusus dalam adegan 3D berbasis Java, Aspose.3D membuat prosesnya sederhana. Dalam tutorial ini kami akan membahas setiap langkah—dari menyiapkan adegan hingga mengekspor model akhir sebagai file OBJ—sehingga Anda dapat mengintegrasikan silinder dengan offset‑atas ke dalam aplikasi Anda dengan percaya diri. Pada akhir panduan Anda juga akan memahami bagaimana **aspose temporary license** memungkinkan Anda mengevaluasi fitur-fitur ini tanpa harus membeli penuh.

## Jawaban Cepat
- **Library apa yang digunakan?** Aspose.3D for Java  
- **Bisakah saya mengoffset bagian atas silinder?** Yes, using `setOffsetTop`  
- **Bagaimana cara menambahkan child node di Java?** Call `createChildNode` on the root node  
- **Format apa yang dapat saya ekspor?** Wavefront OBJ (`java export obj`)  
- **Apakah saya memerlukan lisensi untuk pengujian?** An **aspose temporary license** is available for evaluation  

## Apa itu Aspose Temporary License?

Sebuah **aspose temporary license** adalah kunci evaluasi gratis jangka pendek yang membuka seluruh set fitur Aspose.3D untuk Java selama pengembangan dan pengujian. Kunci ini menghapus watermark evaluasi dan memungkinkan Anda menghasilkan file model 3D, seperti OBJ, STL, atau FBX, persis seperti lisensi berbayar.

## Mengapa Menggunakan Aspose.3D untuk Java?

- **High‑level API:** Tidak perlu mengelola data mesh tingkat rendah.  
- **Cross‑platform:** Berfungsi pada lingkungan apa pun yang kompatibel dengan JVM.  
- **Built‑in exporters:** Menyimpan langsung ke OBJ, STL, FBX, dan lainnya.  
- **Extensible:** Dengan mudah menambahkan child node, menerapkan transformasi, dan mengintegrasikan dengan pustaka Java lainnya.  

## Prasyarat

- **Java Development Kit (JDK)** – versi yang kompatibel terpasang.  
- **Aspose.3D for Java library** – unduh JAR terbaru dari situs resmi [here](https://releases.aspose.com/3d/java/).  
- Sebuah IDE pilihan Anda (Eclipse, IntelliJ IDEA, NetBeans, dll.).  

## Impor Paket

Pertama, impor kelas yang akan kita gunakan. Letakkan pernyataan ini di bagian atas file Java Anda:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Panduan Langkah‑per‑Langkah

### Langkah 1: Buat Adegan 3D Java

Sebuah **java 3d scene** berfungsi sebagai wadah untuk semua objek 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Langkah 2: Inisialisasi Silinder dengan Offset Atas

Di sini kami menjawab **how to create cylinder** dengan offset khusus. Konstruktor mendefinisikan radius, tinggi, slices, stacks, dan apakah silinder ditutup. Setelah itu, kami menggeser bagian atas menggunakan `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Langkah 3: Tambahkan Child Node Java – Lampirkan Silinder Pertama

Kami membuat child node di bawah root node adegan dan memindahkan silinder ke lokasi yang diinginkan.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Langkah 4: Inisialisasi Silinder Kedua (Tanpa Offset)

Sebagai perbandingan, kami menambahkan silinder biasa tanpa offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Langkah 5: Tambahkan Child Node Java – Lampirkan Silinder Kedua

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Langkah 6: Java Export OBJ – Simpan Adegan sebagai OBJ

Akhirnya, kami **java export obj** seluruh adegan (kedua silinder) sebagai file Wavefront OBJ, yang didukung secara luas oleh alat 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Saat Anda menjalankan program, Anda akan menemukan `CustomizedOffsetTopCylinder.obj` di direktori yang ditentukan, siap dibuka di Blender, Maya, atau penampil lain yang kompatibel dengan OBJ.

## Cara Menghasilkan Model 3D dan Mengekspor OBJ di Java

Kombinasi `Scene.save(..., FileFormat.WAVEFRONTOBJ)` dan **aspose temporary license** memungkinkan Anda **generate 3d model** file dengan cepat, tanpa memerlukan konverter eksternal. Ini sangat berguna selama prototyping atau saat berbagi aset dengan desainer.

## Kasus Penggunaan di Dunia Nyata

- **Architectural visualisation:** Silinder dengan offset‑atas memodelkan kolom yang menyempit menuju langit-langit.  
- **Mechanical parts:** Buat piston atau rumah gear dimana permukaan atas sengaja digeser.  
- **Game assets:** Hasilkan variasi bentuk pilar secara dinamis, mengurangi kebutuhan mesh buatan tangan.  

## Masalah Umum dan Solusinya

| Masalah | Alasan | Solusi |
|-------|--------|-----|
| **File OBJ kosong** | Adegan tidak disimpan dengan benar atau path salah. | Pastikan direktori output ada dan Anda memiliki izin menulis. |
| **Offset tidak diterapkan** | Menggunakan versi Aspose.3D yang lebih lama. | Perbarui ke pustaka terbaru yang mendukung `setOffsetTop`. |
| **Child node tidak terlihat** | Transformasi tidak diterapkan. | Pastikan Anda memanggil `getTransform().setTranslation` setelah membuat child node. |

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan berbagai IDE Java?**  
A: Ya, ia bekerja mulus dengan Eclipse, IntelliJ IDEA, NetBeans, dan IDE lainnya.

**Q: Bisakah saya menerapkan tekstur pada objek 3D yang dibuat?**  
A: Tentu! Gunakan kelas `Material` untuk menetapkan tekstur dan properti permukaan.

**Q: Apakah ada opsi lisensi untuk Aspose.3D?**  
A: Berbagai model lisensi tersedia; Anda dapat menjelajahinya [here](https://purchase.aspose.com/buy).

**Q: Bagaimana saya dapat mendapatkan bantuan atau berbagi pengalaman?**  
A: Bergabunglah dengan forum komunitas Aspose.3D [here](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

**Q: Apakah lisensi sementara tersedia untuk pengujian?**  
A: Ya, **aspose temporary license** dapat diperoleh untuk evaluasi [here](https://purchase.aspose.com/temporary-license/).

---

**Terakhir Diperbarui:** 2026-04-08  
**Diuji Dengan:** Aspose.3D for Java 24.12 (latest)  
**Penulis:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}