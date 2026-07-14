---
date: 2026-05-24
description: Pelajari cara mengekstrusi bentuk menggunakan Aspose.3D untuk Java. Tutorial
  pemodelan 3D java ini mencakup ekstrusi linear, kontrol pusat, arah, irisan, putaran,
  dan lainnya!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Membuat Model 3D dengan Ekstrusi Linear di Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Cara Mengekstrusi Bentuk - Membuat Model 3D dengan Ekstrusi Linear di Java
url: /id/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cara Mengekstrusi Bentuk – Membuat Model 3D dengan Ekstrusi Linear di Java

Jika Anda pernah bertanya-tanya **cara mengekstrusi bentuk** dalam aplikasi Java, Anda berada di tempat yang tepat. Dalam tutorial ini kami akan menjelajahi fitur ekstrusi linear Aspose.3D untuk Java, menunjukkan cara mengubah profil 2‑D sederhana menjadi model 3‑D yang lengkap. Baik Anda membangun penampil bergaya CAD, pipeline aset game, atau hanya bereksperimen dengan geometri, menguasai ekstrusi linear akan memberi Anda kepercayaan untuk membuat bentuk kompleks dengan hanya beberapa baris kode.

## Jawaban Cepat
- **Apa itu ekstrusi linear?** Mengubah sketsa 2‑D menjadi padatan 3‑D dengan memperluasnya sepanjang suatu arah.  
- **Perpustakaan mana yang membantu Anda?** Aspose.3D untuk Java menyediakan API yang fluens untuk tugas ekstrusi.  
- **Apakah saya memerlukan lisensi?** Versi percobaan gratis cukup untuk belajar; lisensi komersial diperlukan untuk produksi.  
- **Versi Java apa yang diperlukan?** Java 8 atau lebih tinggi.  
- **Bisakah saya menerapkan putaran atau offset?** Ya – API mendukung sudut putar (twist angle) dan offset putar (twist offset) secara langsung.  

## Apa itu “cara mengekstrusi bentuk” dalam Java?
Operasi `Extrusion` adalah fitur inti Aspose.3D yang mengubah kontur datar menjadi mesh volumetrik. Dalam istilah sederhana, Anda menyediakan profil 2‑D (misalnya, persegi panjang atau poligon khusus), memberi tahu mesin seberapa jauh menariknya, dan perpustakaan membangun geometri 3‑D untuk Anda.

## Mengapa menggunakan Aspose.3D untuk Java?
Aspose.3D mendukung **lebih dari 50 format input dan output** – termasuk OBJ, STL, FBX, dan GLTF – dan dapat menghasilkan mesh dengan hingga **10 000 vertex per ekstrusi** tanpa memuat seluruh adegan ke memori. Mesin lintas‑platformnya berjalan di Windows, Linux, dan macOS, memberikan hasil yang konsisten baik Anda berada di workstation desktop atau server CI tanpa tampilan.

## Prasyarat
- Java 8 atau yang lebih baru terpasang di mesin pengembangan Anda.  
- Maven atau Gradle untuk manajemen dependensi.  
- File lisensi Aspose.3D untuk Java (opsional untuk percobaan).  

## Bagaimana cara kerja ekstrusi linear?
Ekstrusi linear membuat padatan 3‑D dengan menyapu profil 2‑D sepanjang garis lurus. Mesin pertama-tama melakukan triangulasi pada profil, kemudian mereplikasi profil tersebut pada setiap irisan sepanjang sumbu ekstrusi, dan akhirnya menjahit irisan‑irisan tersebut menjadi mesh kedap air. Proses ini secara otomatis menghitung normal dan koordinat UV, sehingga Anda dapat merender hasilnya tanpa pemrosesan geometri tambahan.

## Apa saja parameter kunci untuk ekstrusi linear?
Ekstrusi linear dapat disesuaikan dengan beberapa parameter. **center** menentukan titik pivot profil sebelum ekstrusi. Vektor **direction** menetapkan sumbu ekstrusi, secara default mengarah ke sumbu Z positif. **Slices** mengontrol berapa banyak penampang antar‑tengah yang dihasilkan, memengaruhi kelancaran untuk bentuk yang dipelintir atau meruncing. **Twist angle** memutar profil secara progresif dari awal hingga akhir, sementara **twist offset** menambahkan perpindahan linear sepanjang sumbu, memungkinkan bentuk spiral.

- **Center** – Titik pivot di sekitar mana profil diposisikan sebelum ekstrusi.  
- **Direction** – Vektor yang menentukan sumbu ekstrusi; default adalah sumbu Z positif.  
- **Slices** – Jumlah penampang antar‑tengah; lebih banyak irisan menghasilkan transisi yang lebih halus untuk ekstrusi yang dipelintir atau meruncing.  
- **Twist Angle** – Rotasi total yang diterapkan pada profil dari awal hingga akhir, dinyatakan dalam derajat.  
- **Twist Offset** – Offset linear yang memindahkan profil sepanjang sumbu ekstrusi sambil memutar, memungkinkan bentuk spiral.

## Melakukan Ekstrusi Linear di Aspose.3D untuk Java

Muat profil Anda, konfigurasikan parameter, dan biarkan API menghasilkan mesh. Langkah‑langkah berikut menggambarkan alur kerja tipikal.

### Langkah 1: Definisikan profil 2‑D
Buat `Polygon` atau `Polyline` yang mewakili bentuk yang ingin Anda ekstrusi.  
*`Polygon` mewakili bentuk tertutup yang didefinisikan oleh vertex, sementara `Polyline` adalah rangkaian segmen garis terbuka.*  
Siap memulai? [Perform Linear Extrusion Now](./performing-linear-extrusion/)  
Untuk tutorial terperinci, lihat [Performing Linear Extrusion in Aspose.3D for Java](./performing-linear-extrusion/).

### Langkah 2: Konfigurasikan opsi ekstrusi
Atur center, direction, slices, twist, dan twist offset pada objek `Extrusion`.  
*Kelas `Extrusion` mengenkapsulasi semua parameter yang diperlukan untuk menghasilkan mesh 3‑D dari profil 2‑D.*  
Coba kontrol center: [Control Center in Linear Extrusion](./controlling-center/)  
Baca lebih lanjut tentang kontrol center: [Controlling Center in Linear Extrusion with Aspose.3D for Java](./controlling-center/)

### Langkah 3: Tambahkan ekstrusi ke scene
Buat instance `Scene`, lampirkan mesh ekstrusi, dan ekspor ke format yang Anda inginkan.  
*`Scene` adalah wadah yang menyimpan semua objek 3‑D dan menangani ekspor ke berbagai format file.*  
Siap mengatur arah? [Explore Now](./setting-direction/)  
Pelajari lebih lanjut tentang arah: [Setting Direction in Linear Extrusion with Aspose.3D for Java](./setting-direction/)

### Langkah 4: Ekspor atau render
Gunakan `Scene.save()` untuk menulis model ke OBJ, STL, atau format lain yang didukung.  
*`Scene.save()` menulis seluruh scene ke format file yang ditentukan, menerapkan post‑processing yang diperlukan.*  
Mulai menentukan slices: [Learn More](./specifying-slices/)  
Panduan lengkap: [Specifying Slices in Linear Extrusion with Aspose.3D for Java](./specifying-slices/)

## Bagaimana cara menerapkan twist pada ekstrusi?
Terapkan twist dengan mengatur properti `twistAngle` pada opsi ekstrusi. Mesin memutar setiap irisan secara proporsional, menciptakan efek heliks. Dengan menyesuaikan sudut, Anda dapat menghasilkan apa saja mulai dari torsi halus hingga spiral 360° penuh, berguna untuk elemen dekoratif atau pegas fungsional.  
Siap memutar? [Apply Twist Now](./applying-twist/)  
Contoh lengkap: [Applying Twist in Linear Extrusion with Aspose.3D for Java](./applying-twist/)

## Bagaimana cara menggunakan twist offset untuk bentuk spiral?
Twist offset memindahkan setiap irisan sepanjang sumbu ekstrusi sambil berputar, membentuk tangga spiral atau geometri sekrup. Menggabungkan twist angle dengan offset positif menghasilkan ramp heliks yang halus, sementara offset negatif dapat membuat spiral menurun. Teknik ini ideal untuk memodelkan ulir, pegas, atau pita artistik.  
Tingkatkan kemampuan Anda: [Learn Twist Offset](./using-twist-offset/)  
Panduan komprehensif: [Using Twist Offset in Linear Extrusion with Aspose.3D for Java](./using-twist-offset/)

## Kasus Penggunaan Umum untuk Ekstrusi Linear
- **Mechanical parts** – Dengan cepat menghasilkan baut, poros, dan braket dari sketsa sederhana.  
- **Architectural elements** – Mengekstrusi rencana lantai menjadi dinding atau kolom untuk prototipe BIM.  
- **Game assets** – Membuat properti low‑poly seperti pagar, pipa, atau rel dekoratif langsung dari seni 2‑D.  
- **Educational tools** – Memvisualisasikan permukaan matematis dengan mengekstrusi kurva parametrik.

## Memecahkan Masalah Umum
- **Missing faces** – Pastikan profil merupakan loop tertutup; kontur terbuka menghasilkan celah.  
- **Excessive memory usage** – Kurangi jumlah `slices` atau aktifkan `scene.setMemoryOptimization(true)`.  
- **Incorrect twist direction** – Sudut positif memutar searah jarum jam saat melihat sepanjang arah ekstrusi; gunakan nilai negatif untuk membalikkan.

## Pertanyaan yang Sering Diajukan

**Q: Bisakah saya menggunakan Aspose.3D untuk Java dalam proyek komersial?**  
A: Ya, lisensi Aspose yang valid diperlukan untuk penggunaan produksi, tetapi versi percobaan gratis tersedia untuk evaluasi.

**Q: Versi Java apa yang didukung?**  
A: Perpustakaan ini bekerja dengan runtime Java 8 dan yang lebih baru, termasuk Java 11, 17, dan 21.

**Q: Apakah saya perlu mengelola memori untuk ekstrusi besar?**  
A: Aspose.3D menangani pembuatan mesh secara efisien, tetapi Anda dapat memanggil `scene.dispose()` ketika selesai dengan scene besar untuk membebaskan sumber daya native.

**Q: Bisakah saya menggabungkan beberapa operasi ekstrusi dalam satu model?**  
A: Tentu – Anda dapat membuat beberapa objek ekstrusi, menempatkannya secara independen, dan menambahkannya ke scene yang sama.

**Q: Apakah ada contoh kode untuk menerapkan twist dan twist offset secara bersamaan?**  
A: Ya, tutorial “Applying Twist” dan “Using Twist Offset” menunjukkan cara mengatur kedua properti pada objek ekstrusi yang sama.

---

**Terakhir Diperbarui:** 2026-05-24  
**Diuji Dengan:** Aspose.3D for Java 24.11  
**Penulis:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Tutorial Terkait

- [Tutorial Grafik 3D Java – Center dalam Ekstrusi Linear](/3d/java/linear-extrusion/controlling-center/)
- [Cara Mengatur Arah dalam Ekstrusi Linear dengan Aspose.3D untuk Java](/3d/java/linear-extrusion/setting-direction/)
- [Buat Ekstrusi 3D dengan Slices – Aspose.3D untuk Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}