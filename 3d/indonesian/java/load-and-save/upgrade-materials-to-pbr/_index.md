---
date: 2025-12-22
description: Pelajari cara mengekspor adegan ke glTF dalam Java menggunakan Aspose.3D
  sambil meningkatkan material 3D ke PBR untuk realisme yang lebih tinggi.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Ekspor Adegan ke glTF di Java dengan Aspose.3D
url: /id/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ekspor Adegan ke glTF dalam Java dengan Aspose.3D – Tingkatkan Material ke PBR

## Pendahuluan

Pada tutorial ini Anda akan belajar cara **mengekspor adegan ke glTF** dalam Java dengan Aspose.3D sambil meningkatkan material 3D Anda ke Physically‑Based Rendering (PBR). Meningkatkan ke PBR memberikan model Anda tampilan yang jauh lebih realistis, dan mengekspor ke format glTF 2.0 yang banyak didukung memungkinkan Anda berbagi aset berkualitas tinggi tersebut di berbagai engine, browser, dan platform AR/VR. Kami akan membahas prasyarat, mengimpor paket yang diperlukan, dan memecah setiap contoh langkah demi langkah sehingga Anda dapat menerapkan teknik ini dalam proyek Anda sendiri.

## Jawaban Cepat
- **Apa arti “export scene to glTF”?** Itu mengonversi adegan Aspose.3D menjadi format file glTF 2.0, mempertahankan geometri, material, dan hierarki.  
- **Mengapa harus meningkatkan material ke PBR terlebih dahulu?** Material PBR langsung dipetakan ke alur kerja metallic‑roughness glTF, memberikan pencahayaan realistis tanpa langkah konversi tambahan.  
- **Apakah saya memerlukan lisensi untuk menjalankan kode?** Versi percobaan gratis dapat digunakan untuk pengembangan; lisensi komersial diperlukan untuk produksi.  
- **IDE Java mana yang didukung?** Semua IDE yang dapat mengompilasi Java (Eclipse, IntelliJ IDEA, VS Code, dll.).  
- **Apakah saya dapat mengekspor adegan besar?** Ya, Aspose.3D mengalirkan data secara efisien; pastikan cukup memori heap untuk model yang sangat besar.

## Apa itu “export scene to glTF”?

Mengekspor adegan ke glTF berarti menyerialisasi seluruh adegan 3D—termasuk mesh, node, kamera, cahaya, dan material—ke dalam GL Transmission Format (glTF). glTF adalah format standar terbuka yang dioptimalkan untuk rendering waktu nyata, menjadikannya ideal untuk penggunaan di web, seluler, dan mesin game.

## Mengapa meningkatkan material ke PBR sebelum mengekspor?

Material PBR (Physically‑Based Rendering) menjelaskan bagaimana cahaya berinteraksi dengan permukaan menggunakan parameter seperti albedo, metallic, dan roughness. glTF 2.0 secara native mendukung PBR, sehingga mengonversi material Phong atau kustom ke PBR memastikan warna, refleksi, dan shading terlihat benar ketika model dimuat di viewer yang kompatibel dengan glTF.

## Prasyarat

1. **Aspose.3D for Java** – unduh dari [halaman rilis](https://releases.aspose.com/3d/java/).  
2. **Lingkungan Pengembangan Java** – JDK 8 atau lebih tinggi dan IDE pilihan Anda.  
3. **Direktori Dokumen** – sebuah folder di mesin Anda tempat Anda akan membaca/menulis file 3D.

## Impor Paket

Tambahkan namespace inti Aspose.3D ke proyek Anda:

```java
import com.aspose.threed.*;
```

Impor tunggal ini memberi Anda akses ke `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions`, dan API konversi material.

## Langkah 1: Inisialisasi Adegan 3D Baru

Buat adegan baru yang akan menampung geometri dan material Anda:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Tips Pro:** Pertahankan `MyDir` sebagai path absolut selama pengembangan untuk menghindari kesalahan file‑tidak‑ditemukan.

## Langkah 2: Buat Kotak dengan PhongMaterial

Kita akan memulai dengan kotak sederhana yang menggunakan material Phong klasik. Ini nantinya akan dikonversi menjadi material PBR saat ekspor:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Mengapa Phong?** PhongMaterial mudah disiapkan dan menunjukkan cara kerja logika konversi.

## Langkah 3: Simpan dalam Format GLTF 2.0 (Export Scene to glTF)

Konfigurasikan opsi penyimpanan GLTF untuk secara otomatis mengonversi setiap `PhongMaterial` menjadi `PbrMaterial`. Ini adalah inti dari **export scene to glTF**:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

Saat kode ini dijalankan, adegan ditulis ke `Non_PBRtoPBRMaterial_Out.gltf`. `MaterialConverter` khusus memastikan bahwa material Phong diubah menjadi material PBR, sehingga file glTF yang dihasilkan menampilkan shading realistis di viewer glTF mana pun.

## Masalah Umum & Solusi

| Masalah | Solusi |
|-------|----------|
| **FileNotFoundException** saat menyimpan | Pastikan `MyDir` mengarah ke folder yang ada dan aplikasi memiliki izin menulis. |
| **ClassCastException** dalam konverter | Pastikan material yang diberikan ke konverter memang `PhongMaterial`. Tambahkan pemeriksaan `instanceof` jika Anda mencampur tipe material. |
| **Missing textures** setelah ekspor | glTF mengharapkan tekstur disediakan secara terpisah; tambahkan penanganan tekstur ke konverter jika diperlukan. |

## Pertanyaan yang Sering Diajukan

**Q: Apakah Aspose.3D kompatibel dengan lingkungan pengembangan Java selain Eclipse?**  
A: Ya, Aspose.3D bekerja dengan semua IDE Java, termasuk IntelliJ IDEA, NetBeans, dan VS Code.

**Q: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?**  
A: Ya, Anda dapat menggunakan Aspose.3D untuk proyek pribadi maupun komersial. Kunjungi [halaman pembelian](https://purchase.aspose.com/buy) untuk detail lisensi.

**Q: Apakah tersedia versi percobaan gratis?**  
A: Ya, Anda dapat mengakses versi percobaan gratis [di sini](https://releases.aspose.com/).

**Q: Di mana saya dapat menemukan dukungan untuk Aspose.3D?**  
A: Jelajahi [forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan komunitas.

**Q: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?**  
A: Kunjungi [tautan ini](https://purchase.aspose.com/temporary-license/) untuk informasi lisensi sementara.

## Kesimpulan

Dengan mengikuti langkah-langkah di atas, Anda kini tahu cara **mengekspor adegan ke glTF** dalam Java menggunakan Aspose.3D sambil secara otomatis meningkatkan material Phong ke PBR. Alur kerja ini memungkinkan Anda membuat aset berkualitas tinggi dan berbasis fisika yang siap untuk pipeline rendering modern, viewer web, dan pengalaman AR/VR. Bereksperimenlah dengan geometri, tekstur, dan pencahayaan yang lebih kompleks untuk memanfaatkan sepenuhnya kekuatan PBR dan glTF.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-22  
**Tested With:** Aspose.3D 24.12 untuk Java  
**Author:** Aspose