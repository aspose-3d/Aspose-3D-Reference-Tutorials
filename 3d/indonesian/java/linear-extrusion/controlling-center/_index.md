---
date: 2025-12-18
description: Pelajari cara menambahkan bidang dasar dan mengatur properti center pada
  ekstrusi linear menggunakan Aspose.3D untuk Java, dengan contoh kode langkah demi
  langkah.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cara Menambahkan Bidang Tanah dan Pusat Kontrol pada Ekstrusi Linear dengan
  Aspose.3D untuk Java
url: /id/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Mengontrol Pusat pada Ekstrusi Linear dengan Aspose.3D untuk Java

## Pendahuluan

Saat Anda membangun adegan 3D di Java, kemampuan untuk **menambahkan ground plane** sambil secara tepat **mengatur properti center** pada ekstrusi linear dapat membuat perbedaan antara prototipe datar dan visual yang halus. Pada tutorial ini kami akan membimbing Anda melalui proses lengkap mengontrol pusat ekstrusi dan menambahkan ground plane menggunakan Aspose.3D untuk Java. Anda akan melihat mengapa hal ini penting, cara menyiapkannya, dan mendapatkan contoh kode siap‑jalankan yang dapat Anda sesuaikan dengan proyek Anda sendiri.

## Jawaban Cepat
- **Apa yang dilakukan “add ground plane”?** Ini membuat geometri referensi tipis yang membantu Anda melihat posisi ekstrusi relatif terhadap sumbu dunia.  
- **Bagaimana cara mengatur pusat pada ekstrusi linear?** Gunakan metode `setCenter(boolean)` pada objek `LinearExtrusion`.  
- **Apakah saya memerlukan lisensi untuk menjalankan contoh?** Lisensi sementara cukup untuk pengujian; lisensi penuh diperlukan untuk produksi.  
- **Format file apa yang digunakan untuk menyimpan?** Contoh menyimpan ke Wavefront OBJ (`.obj`).  
- **Versi Java apa yang diperlukan?** Java 8 atau yang lebih baru sudah cukup.

## Apa itu “add ground plane” dalam sebuah adegan 3D?

Menambahkan ground plane berarti menyisipkan geometri persegi panjang tipis (sering kali berupa kotak dengan ketebalan minimal) yang terletak pada bidang X‑Z. Ini berfungsi sebagai lantai visual, memudahkan penilaian tinggi dan penyelarasan objek lain, terutama ketika Anda bereksperimen dengan pusat ekstrusi.

## Mengapa mengatur properti center pada ekstrusi linear?

Secara default, ekstrusi linear dimulai dari asal profil. Mengatur properti center (`setCenter(true)`) memindahkan profil sehingga ekstrusi terpusat di sekitar asal, yang berguna untuk desain simetris atau ketika Anda memerlukan penyelarasan konsisten di antara beberapa objek.

## Prasyarat

Sebelum memulai tutorial ini, pastikan Anda telah menyiapkan prasyarat berikut:

1. **Lingkungan Pengembangan Java** – Pastikan Anda memiliki lingkungan pengembangan Java yang terpasang di mesin Anda.  
2. **Aspose.3D untuk Java** – Unduh dan instal pustaka Aspose.3D. Anda dapat menemukan pustaka dan dokumentasinya [di sini](https://reference.aspose.com/3d/java/).  
3. **Direktori Dokumen** – Buat sebuah direktori untuk menyimpan dokumen Java Anda. Kita sebut “Your Document Directory”.

## Impor Paket

Di lingkungan pengembangan Java Anda, impor paket‑paket yang diperlukan untuk Aspose.3D. Ini memastikan kode Anda memiliki akses ke fungsionalitas yang disediakan oleh pustaka.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Langkah 1: Siapkan Profil Dasar

Inisialisasi profil dasar yang akan diekstrusi. Dalam contoh ini, kita akan menggunakan bentuk persegi panjang dengan jari‑jari pembulatan 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Langkah 2: Buat Adegan 3D

Bangun fondasi dunia 3D Anda dengan membuat sebuah adegan.

```java
Scene scene = new Scene();
```

## Langkah 3: Buat Node Kiri dan Kanan

Tetapkan node kiri dan kanan dalam adegan Anda. Node‑node ini berfungsi sebagai kanvas untuk objek 3D Anda.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Langkah 4: Ekstrusi Linear dengan Properti Center (Node Kiri)

Lakukan ekstrusi linear pada node kiri **tanpa penengahan** dan atur jumlah irisan menjadi 3. Perhatikan pemanggilan `setCenter(false)` – di sinilah kita **mengatur properti center** menjadi *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Langkah 5: Tambahkan Ground Plane untuk Referensi (Node Kiri)

Tingkatkan representasi visual dengan **menambahkan ground plane** ke node kiri. Kotak tipis berfungsi sebagai lantai sehingga Anda dapat melihat tinggi ekstrusi dengan jelas.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Langkah 6: Ekstrusi Linear dengan Properti Center (Node Kanan)

Sekarang lakukan ekstrusi linear pada node kanan, kali ini **menengahkan ekstrusi**. Pemanggilan `setCenter(true)` menunjukkan cara **mengatur properti center** menjadi *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Langkah 7: Tambahkan Ground Plane untuk Referensi (Node Kanan)

Seperti pada sisi kiri, tambahkan ground plane ke node kanan untuk baseline visual yang konsisten.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Langkah 8: Simpan Adegan 3D

Simpan adegan 3D Anda dalam format Wavefront OBJ sehingga dapat dilihat di penampil 3D standar mana pun.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Masalah Umum dan Solusinya

| Masalah | Penyebab | Solusi |
|-------|----------------|-----|
| Ground plane tidak terlihat | Ketebalan kotak terlalu kecil untuk skala penampil. | Tingkatkan ketebalan (parameter pertama dari `Box`) atau perkecil tampilan di penampil. |
| Ekstrusi tampak bergeser | Nilai `setCenter` tidak diatur sesuai yang diinginkan. | Periksa kembali nilai boolean yang diberikan ke `setCenter`. |
| File tidak tersimpan | Jalur direktori salah atau izin menulis tidak ada. | Pastikan `MyDir` mengarah ke folder yang ada dengan hak akses menulis. |

## Pertanyaan yang Sering Diajukan

**T1: Apakah saya dapat menggunakan Aspose.3D untuk Java dalam proyek komersial?**  
J1: Ya, Aspose.3D untuk Java tersedia untuk penggunaan komersial. Untuk detail lisensi, kunjungi [di sini](https://purchase.aspose.com/buy).

**T2: Apakah ada versi percobaan gratis?**  
J2: Ya, Anda dapat mencoba versi percobaan gratis Aspose.3D untuk Java [di sini](https://releases.aspose.com/).

**T3: Di mana saya dapat menemukan dukungan untuk Aspose.3D untuk Java?**  
J3: Forum komunitas Aspose.3D adalah tempat yang bagus untuk mencari dukungan dan berbagi pengalaman. Kunjungi forum [di sini](https://forum.aspose.com/c/3d/18).

**T4: Apakah saya memerlukan lisensi sementara untuk pengujian?**  
J4: Ya, jika Anda memerlukan lisensi sementara untuk tujuan pengujian, Anda dapat memperolehnya [di sini](https://purchase.aspose.com/temporary-license/).

**T5: Di mana saya dapat menemukan dokumentasinya?**  
J5: Dokumentasi Aspose.3D untuk Java tersedia [di sini](https://reference.aspose.com/3d/java/).

## Kesimpulan

Mengontrol pusat pada ekstrusi linear **dan** mempelajari cara **menambahkan ground plane** dengan Aspose.3D untuk Java membuka peluang menarik dalam pengembangan grafis 3D. Dengan mengikuti langkah‑langkah di atas, Anda kini memiliki pola yang dapat digunakan kembali untuk membuat ekstrusi terpusat, bidang referensi visual, dan mengekspor hasil ke OBJ. Jangan ragu untuk bereksperimen dengan profil berbeda, jumlah irisan, dan transformasi agar sesuai dengan kebutuhan proyek Anda.

---

**Terakhir Diperbarui:** 2025-12-18  
**Diuji Dengan:** Aspose.3D 24.11 untuk Java (versi terbaru saat penulisan)  
**Penulis:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}