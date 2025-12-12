---
date: 2025-12-12
description: Pelajari cara mengatur warna material sambil berbagi data geometri mesh
  dan menyimpan adegan sebagai FBX di Java 3D menggunakan Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Atur Warna Material dan Bagikan Data Geometri Mesh di Java 3D dengan Aspose.3D
url: /id/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Atur Warna Material dan Bagikan Data Geometri Mesh di Java 3D dengan Aspose.3D

## Introduction

Memulai perjalanan ke dunia Java 3D dengan Aspose.3D membuka banyak kemungkinan untuk membuat visualisasi menakjubkan dan pengalaman imersif. Pada tutorial ini, kami akan memandu Anda **cara berbagi data geometri mesh** di Java 3D menggunakan Aspose.3D, dan kami akan menunjukkan secara tepat **cara mengatur warna material** untuk setiap instance mesh. Ikuti setiap langkah dengan cermat, dan pada akhir tutorial, Anda akan dapat menukar data mesh antar beberapa node sambil mengontrol warna dan mengekspor ke FBX.

## Quick Answers
- **What is the main goal?** Atur warna material untuk setiap node dan bagikan data geometri mesh.  
- **Which library is required?** Aspose.3D for Java.  
- **How do I export the result?** Simpan adegan sebagai file FBX (FBX7400ASCII).  
- **Do I need a license?** Lisensi sementara atau penuh diperlukan untuk penggunaan produksi.  
- **What Java version works?** Lingkungan Java 8+ apa pun.

## Prerequisites

Sebelum kita masuk ke tutorial, pastikan Anda telah menyiapkan hal‑hal berikut:

- Lingkungan Pengembangan Java: Pastikan Anda memiliki lingkungan pengembangan Java yang terpasang di sistem Anda.  
- Library Aspose.3D: Unduh dan instal library Aspose.3D. Anda dapat menemukan library tersebut [di sini](https://releases.aspose.com/3d/java/).

## Import Packages

Mulailah dengan mengimpor paket‑paket yang diperlukan ke dalam proyek Java Anda. Langkah ini penting untuk mengakses fungsionalitas yang disediakan oleh library Aspose.3D.

```java
import com.aspose.threed.*;
```

## Step 1: Initialize Scene Object (initialize scene java)

Mari kita mulai proses dengan menginisialisasi objek scene. Objek ini akan menjadi kanvas tempat keajaiban 3D kita akan terwujud.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Step 2: Define Color Vectors

Pada langkah ini, kita mendefinisikan sebuah array vektor warna yang akan diterapkan pada elemen‑elemen berbeda dalam adegan 3D kita.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Step 3: Create 3D Mesh Java Using Polygon Builder (create 3d mesh java)

Gunakan kelas Common untuk membuat mesh menggunakan metode polygon builder. Mesh ini akan menjadi dasar bagi elemen‑elemen 3D kita.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## How to set material color for each node?

Iterasi melalui vektor warna, buat node kubus, dan atur atribut seperti material, **set material color**, serta translasi. Inilah inti pengendalian tampilan visual setiap instance mesh.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)

Tentukan direktori dan nama file untuk menyimpan adegan 3D dalam format file yang didukung, dalam hal ini FBX7400ASCII. Langkah ini juga memperlihatkan **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Conclusion

Selamat! Anda telah berhasil **mengatur warna material**, berbagi data geometri mesh antar beberapa node, dan mengekspor hasilnya sebagai file FBX menggunakan Aspose.3D untuk Java. Ini membuka peluang tak terbatas untuk membuat aplikasi 3D yang visualnya memukau dan interaktif.

## FAQ's

### Q1: Can I use Aspose.3D with other Java frameworks?

A1: Ya, Aspose.3D dirancang untuk bekerja mulus dengan berbagai framework Java.

### Q2: Are there any licensing options available for Aspose.3D?

A2: Ya, Anda dapat menjelajahi opsi lisensi [di sini](https://purchase.aspose.com/buy).

### Q3: How can I get support for Aspose.3D?

A3: Kunjungi forum Aspose.3D [di sini](https://forum.aspose.com/c/3d/18) untuk dukungan dan diskusi.

### Q4: Is there a free trial available?

A4: Ya, Anda dapat mendapatkan trial gratis [di sini](https://releases.aspose.com/).

### Q5: How do I obtain a temporary license for Aspose.3D?

A5: Anda dapat memperoleh lisensi sementara [di sini](https://purchase.aspose.com/temporary-license/).

## Additional Frequently Asked Questions

**Q: Can I export the scene to other formats besides FBX?**  
A: Ya, Aspose.3D mendukung OBJ, STL, 3MF, dan lainnya. Cukup ubah enum `FileFormat` pada pemanggilan `save`.

**Q: What if I need to change the material after the scene is created?**  
A: Ambil node tersebut, modifikasi `LambertMaterial`‑nya (misalnya, `setDiffuseColor`), dan simpan kembali adegan.

**Q: Does the library handle large meshes efficiently?**  
A: Aspose.3D menggunakan struktur data yang dioptimalkan; namun, untuk mesh yang sangat besar pertimbangkan streaming atau membagi adegan.

**Q: Is there a way to animate the color change?**  
A: Ya, Anda dapat menganimasikan properti material menggunakan API `AnimationController`.

---

**Last Updated:** 2025-12-12  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}