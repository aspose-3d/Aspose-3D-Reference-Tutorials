---
title: Optimalkan Penyimpanan File 3D di Java dengan Aspose.3D SaveOptions
linktitle: Optimalkan Penyimpanan File 3D di Java dengan Aspose.3D SaveOptions
second_title: Asumsikan.3D Java API
description: Pelajari cara mengoptimalkan penyimpanan file 3D di Java dengan Aspose.3D SaveOptions. Tingkatkan kinerja dan sesuaikan keluaran dengan mudah.
type: docs
weight: 16
url: /id/java/load-and-save/optimize-3d-file-saving/
---
## Perkenalan

Aspose.3D adalah perpustakaan Java kaya fitur yang memberdayakan pengembang untuk bekerja dengan model 3D secara lancar. Dalam hal menyimpan file 3D, kelas SaveOptions menawarkan sejumlah besar pengaturan untuk menyempurnakan output sesuai kebutuhan Anda. Dalam tutorial ini, kita akan menjelajahi berbagai opsi penyimpanan dan bagaimana opsi tersebut dapat dimanfaatkan untuk mengoptimalkan proses.

## Prasyarat

Sebelum kita mendalami tutorialnya, pastikan Anda memiliki prasyarat berikut:

-  Aspose.3D untuk Java: Pastikan Anda memiliki perpustakaan Aspose.3D yang terintegrasi ke dalam proyek Java Anda. Anda dapat mengunduhnya[Di Sini](https://releases.aspose.com/3d/java/).

- Lingkungan Pengembangan Java: Siapkan lingkungan pengembangan Java yang fungsional di mesin Anda.

- Direktori Dokumen: Buat direktori tempat Anda ingin menyimpan file 3D dan catat jalurnya untuk digunakan nanti.

## Paket Impor

 Di proyek Java Anda, impor paket yang diperlukan untuk bekerja dengan Aspose.3D. Ini termasuk`Scene` kelas dan berbagai kelas SaveOptions. Di bawah ini adalah contoh dasar:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Sekarang, mari kita bagi setiap contoh menjadi beberapa langkah untuk mendemonstrasikan penggunaan SaveOptions yang berbeda.

## Langkah 1: Cetak Cantik di GLTF SaveOption

 Itu`prettyPrintInGltfSaveOption` Metode ini memungkinkan Anda membuat file GLTF dengan konten JSON yang diindentasi agar mudah dibaca manusia.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Inisialisasi adegan 3D
    Scene scene = new Scene(new Sphere());
    
    // Inisialisasi GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Aktifkan pencetakan cantik agar lebih mudah dibaca
    opt.setPrettyPrint(true);
    
    // Simpan Adegan 3D
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Langkah 2: Opsi Simpan HTML5

 Itu`html5SaveOption` Metode ini mendemonstrasikan cara menyimpan adegan 3D sebagai file HTML5, termasuk opsi penyesuaian.

```java
public static void html5SaveOption() throws IOException {
    // Inisialisasi sebuah adegan
    Scene scene = new Scene();
    
    // Buat node anak dengan silinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Tetapkan properti untuk node anak
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Tambahkan cahaya pada pemandangan itu
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Inisialisasi HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Sesuaikan opsi (misalnya, matikan jaringan dan antarmuka pengguna)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Simpan adegan sebagai file HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Lanjutkan dengan pengelompokan serupa untuk metode SaveOptions lainnya seperti`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , Dan`drcSaveOptions`.

## Kesimpulan

Dengan mengikuti tutorial komprehensif ini, Anda telah mempelajari cara mengoptimalkan penyimpanan file 3D di Java menggunakan Aspose.3D SaveOptions. Baik Anda tertarik untuk mencetak file GLTF dengan indah atau menyesuaikan keluaran HTML5, Aspose.3D membekali Anda dengan alat untuk meningkatkan alur kerja grafis 3D Anda.

## FAQ

### Q1: Bagaimana cara menyematkan aset dalam file glTF?

 A1: Untuk menyematkan aset, gunakan`setEmbedAssets(true)` metode di`GltfSaveOptions` kelas.

###  Q2: Apa tujuan dari`setPositionBits` method in `DracoSaveOptions`?

 A2: Itu`setPositionBits` metode menetapkan bit kuantisasi untuk posisi dalam algoritma kompresi Draco.

### Q3: Dapatkah saya mengekspor data normal dalam file U3D?

 A3: Ya, Anda dapat mengekspor data normal dengan pengaturan`setExportNormals(true)` dalam`U3dSaveOptions` kelas.

### Q4: Bagaimana cara membuang file material yang disimpan dalam ekspor OBJ?

A4: Gunakan`setFileSystem(new DummyFileSystem())` metode di`ObjSaveOptions` kelas untuk membuang file materi.

### Q5: Apakah ada cara untuk menyimpan dependensi ke direktori lokal di file OBJ?

 A5: Ya, gunakan`setFileSystem(new LocalFileSystem(MyDir))` metode di`ObjSaveOptions` kelas untuk menyimpan dependensi secara lokal.