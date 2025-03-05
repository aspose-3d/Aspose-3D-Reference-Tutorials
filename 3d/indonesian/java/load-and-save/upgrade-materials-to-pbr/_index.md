---
title: Tingkatkan Materi 3D ke PBR untuk Peningkatan Realisme di Java dengan Aspose.3D
linktitle: Tingkatkan Materi 3D ke PBR untuk Peningkatan Realisme di Java dengan Aspose.3D
second_title: Asumsikan.3D Java API
description: Tingkatkan materi 3D ke PBR dengan mudah di Java dengan Aspose.3D. Raih realisme yang ditingkatkan untuk visual yang menawan.
type: docs
weight: 13
url: /id/java/load-and-save/upgrade-materials-to-pbr/
---
## Perkenalan

Meningkatkan materi 3D Anda ke PBR adalah langkah transformatif menuju pencapaian visual yang nyata dalam aplikasi Java Anda. Aspose.3D menyederhanakan proses ini, memungkinkan Anda bertransisi dengan mulus dari material tradisional ke material PBR. Dalam tutorial ini, kita akan menjelajahi prasyarat yang diperlukan, mengimpor paket, dan memecah setiap contoh menjadi langkah-langkah mendetail.

## Prasyarat

Sebelum masuk ke tutorial, pastikan Anda memiliki prasyarat berikut:

1.  Aspose.3D untuk Java: Unduh dan instal perpustakaan Aspose.3D dari[halaman rilis](https://releases.aspose.com/3d/java/).

2. Lingkungan Pengembangan Java: Pastikan Anda telah menyiapkan lingkungan pengembangan Java di mesin Anda.

3. Direktori Dokumen: Buat direktori khusus untuk dokumen 3D Anda.

## Paket Impor

Untuk memulai proses pemutakhiran, impor paket yang diperlukan ke proyek Java Anda. Gunakan cuplikan kode berikut sebagai panduan:

```java
import com.aspose.threed.*;
```

Pastikan Anda menyertakan semua paket Aspose.3D yang diperlukan untuk memanfaatkan fungsinya dengan lancar.

## Langkah 1: Inisialisasi Adegan 3D Baru

Mulailah dengan menginisialisasi adegan 3D baru menggunakan kode berikut:

```java
// ExStart: Inisialisasi Adegan
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

## Langkah 2: Buat Kotak dengan PhongMaterial

Buat kotak 3D dan tetapkan PhongMaterial ke dalamnya:

```java
// ExStart:BuatKotakDenganBahan
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:BuatKotakDenganBahan
```

## Langkah 3: Simpan dalam Format GLTF 2.0

Simpan adegan dalam format GLTF 2.0, ubah PhongMaterial menjadi PBRMaterial selama proses:

```java
// ExStart:SimpanDalamGLTF
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
// ExEnd:SimpanDalamGLTF
```

Ikuti langkah-langkah ini dengan cermat untuk meningkatkan materi 3D Anda ke PBR dengan lancar, sehingga meningkatkan realisme dalam aplikasi Java.

## Kesimpulan

Kesimpulannya, Aspose.3D untuk Java memberdayakan Anda untuk meningkatkan daya tarik visual grafik 3D Anda dengan meningkatkan materi ke PBR. Manfaatkan teknologi ini untuk mencapai peningkatan realisme dan memikat audiens Anda dengan aplikasi Java yang menakjubkan secara visual.

## FAQ

### Q1: Apakah Aspose.3D kompatibel dengan lingkungan pengembangan Java selain Eclipse?

A1: Ya, Aspose.3D kompatibel dengan berbagai lingkungan pengembangan Java.

### Q2: Bisakah saya menggunakan Aspose.3D untuk proyek komersial?

 A2: Ya, Anda dapat menggunakan Aspose.3D untuk proyek pribadi dan komersial. Mengunjungi[halaman pembelian](https://purchase.aspose.com/buy) untuk rincian perizinan.

### Q3: Apakah tersedia uji coba gratis?

A3: Ya, Anda dapat mengakses uji coba gratis[Di Sini](https://releases.aspose.com/).

### Q4: Di mana saya dapat menemukan dukungan untuk Aspose.3D?

 A4: Jelajahi[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) untuk dukungan masyarakat.

### Q5: Bagaimana cara mendapatkan lisensi sementara untuk Aspose.3D?

 A5: Kunjungi[Link ini](https://purchase.aspose.com/temporary-license/) untuk informasi lisensi sementara.