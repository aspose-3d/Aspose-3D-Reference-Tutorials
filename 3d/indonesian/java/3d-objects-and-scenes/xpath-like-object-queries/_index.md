---
date: 2026-10-03
description: Pelajari cara **memilih objek berdasarkan nama** menggunakan kueri mirip
  XPath di Aspose.3D untuk Java dan membangun adegan 3D secara programatis.
keywords:
- select objects by name
- how to query scene
- Aspose.3D Java
lastmod: 2026-10-03
linktitle: Pilih objek berdasarkan nama di adegan Java 3D – kueri mirip XPath dengan
  Aspose.3D
og_description: Pilih objek berdasarkan nama di adegan Java 3D menggunakan kueri mirip
  XPath Aspose.3D. Panduan ini menunjukkan cara menanyakan grafik adegan secara efisien
  dan mengambil kamera, lampu, atau entitas apa pun berdasarkan nama.
og_image_alt: 'Developer guide: select objects by name in Java 3D scene using Aspose.3D'
og_title: Pilih objek berdasarkan nama di adegan Java 3D – panduan Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  headline: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  type: TechArticle
- description: Learn how to **select objects by name** using XPath‑like queries in
    Aspose.3D for Java and build a 3D scene programmatically.
  name: Select objects by name in Java 3D scene – XPath‑like queries with Aspose.3D
  steps:
  - name: create a scene for testing
    text: We start with an empty scene that will host our hierarchy. `
  - name: build a hierarchy of nodes
    text: Next, we add a few child nodes under the root node. Some nodes contain a
      **Camera** or a **Light** entity, which we'll later query. `
  - name: query objects by traversing the scene graph
    text: Now the fun part—iterating through the scene to **select objects by name**
      or type using the `NodeVisitor` pattern. `NodeVisitor` is a built‑in Aspose.3D
      class that walks the scene graph node‑by‑node, calling your callback for each
      visited node. It lets you inspect each node’s `Entity` and `Name` wi
  type: HowTo
- questions:
  - answer: The documentation is available **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.
    question: Where can I find the Aspose.3D for Java documentation?
  - answer: You can download it **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.
    question: How can I download Aspose.3D for Java?
  - answer: Yes, you can get a free trial **[Aspose free trial page](https://releases.aspose.com/)**.
    question: Is there a free trial available?
  - answer: Visit the support forum **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Obtain a temporary license **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Need a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- select objects by name
- Aspose.3D
- Java 3D scene
- XPath queries
- 3D programming
title: Pilih objek berdasarkan nama di adegan Java 3D – kueri mirip XPath dengan Aspose.3D
url: /id/java/3d-objects-and-scenes/xpath-like-object-queries/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Pilih objek berdasarkan nama dalam adegan Java 3D – kueri mirip XPath dengan Aspose.3D

## Introduction  

Jika Anda perlu **membuat aplikasi 3d scene java** yang memanipulasi hierarki objek yang kompleks, Aspose.3D untuk Java memberi Anda cara bersih ala XPath untuk menemukan tepat apa yang Anda butuhkan. Dalam tutorial ini kami akan membahas cara membangun adegan sederhana, menambahkan hierarki node, dan kemudian menggunakan kueri mirip XPath untuk **memilih objek berdasarkan nama** (misalnya, kamera atau lampu) tidak peduli di mana mereka berada dalam pohon. Pada akhir Anda akan nyaman melakukan kueri, penyaringan, dan mengambil entitas 3‑D dengan hanya satu ekspresi.

## Quick answers
- **Apa yang dapat saya kueri?** Node atau entitas apa pun (Camera, Light, Mesh, dll.) dalam sebuah Scene.  
- **Bagaimana cara memilih objek berdasarkan tipe?** Gunakan ekspresi mirip XPath seperti `//*[(@Type='Camera')]`.  
- **Apakah saya memerlukan lisensi untuk pengembangan?** Versi percobaan gratis cukup untuk pengujian; lisensi diperlukan untuk produksi.  
- **Versi Java mana yang didukung?** Java 8 atau lebih baru.  
- **Di mana saya dapat mengunduh Aspose.3D?** Dari halaman unduhan resmi yang ditautkan dalam prasyarat.  

## What is an XPath‑like query in Aspose.3D?  

Kueri mirip XPath dalam Aspose.3D adalah ekspresi singkat yang menyaring instance **A3DObject** (node, kamera, lampu, mesh, dll.) langsung pada grafik adegan. **A3DObject mewakili setiap objek dalam grafik adegan, seperti node, kamera, lampu, atau mesh.** Ini berfungsi seperti XML XPath tetapi menargetkan model objek 3‑D, memungkinkan Anda menemukan “semua kamera” atau “objek yang namanya ‘light’” tanpa menulis kode penelusuran manual.

## Why this matters  

Saat Anda bekerja dengan konten 3‑D, menelusuri grafik adegan secara manual dengan cepat menjadi rawan kesalahan dan sulit dipelihara. Kueri mirip XPath memberi Anda cara deklaratif dan mudah dibaca untuk menemukan tepat objek yang Anda butuhkan, yang mempercepat pengembangan dan mengurangi bug—terutama dalam adegan besar dengan puluhan atau ratusan node. Aspose.3D mendukung **lebih dari 50 format input dan output** dan dapat memproses adegan berukuran ratusan halaman tanpa memuat seluruh file ke memori, memberikan Anda fleksibilitas dan kinerja.

## How to select objects by name using XPath‑like queries  

Muat objek berdasarkan nama dengan satu ekspresi yang mencocokkan atribut `@Name`. Berikut tiga pola umum:

1. **Pilih semua kamera** – `//*[(@Type='Camera')]`  
2. **Pilih node dengan nama “light”** – `//*[(@Name='light')]`  
3. **Gabungkan tipe dan nama** – `//*[(@Type='Camera') or (@Name='light')]`

These expressions return the underlying entities, so you can work with them directly in Java.

## Prerequisites  

Before we start, make sure you have:

- Java Development Kit (JDK) terpasang di mesin Anda.  
- Pustaka Aspose.3D untuk Java sudah diunduh dan disiapkan. Anda dapat menemukan tautan unduhan **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Pengetahuan dasar tentang pemrograman Java.  

## Import packages  

First, import the Aspose.3D classes you’ll need. This step makes the library available to your project.

```java
import com.aspose.threed.*;
import com.aspose.threed.scene.*;
import java.util.ArrayList;
import java.util.List;
```

## Step‑by‑step guide  

### Step 1: create a scene for testing  

Buat adegan untuk pengujian  

We start with an empty scene that will host our hierarchy.

````java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
````

### Step 2: build a hierarchy of nodes  

Bangun hierarki node  

Next, we add a few child nodes under the root node. Some nodes contain a **Camera** or a **Light** entity, which we'll later query.

````java
// ExStart:CreateHierarchy
Node a = scene.getRootNode().createChildNode("a");
a.createChildNode("a1");
a.createChildNode("a2");
scene.getRootNode().createChildNode("b");
Node c = scene.getRootNode().createChildNode("c");
c.createChildNode("c1").addEntity(new Camera("cam"));
c.createChildNode("c2").addEntity(new Light("light"));
// ExEnd:CreateHierarchy
````

### Step 3: query objects by traversing the scene graph  

Kueri objek dengan menelusuri grafik adegan  

Now the fun part—iterating through the scene to **select objects by name** or type using the `NodeVisitor` pattern.

`NodeVisitor` is a built‑in Aspose.3D class that walks the scene graph node‑by‑node, calling your callback for each visited node. It lets you inspect each node’s `Entity` and `Name` without writing recursive loops.

```
\u0060\u0060\u0060\u0060java
// The scene from Step 1

// Create a list to store the found objects
List<Object> objects = new ArrayList<>();

// Use a NodeVisitor to traverse the scene graph
scene.getRootNode().accept(new NodeVisitor() {
    @Override
    public boolean call(Node node) {
        Entity entity = node.getEntity();
        // Check if the node has a Camera or if the node's name is 'light'
        if (entity instanceof Camera || "light".equals(node.getName())) {
            objects.add(entity);
        }
        return true;
    }
});

// Print the found objects
for (Object obj : objects) {
    System.out.println("Found: " + obj);
}
// ExEnd:XPathLikeObjectQueries
\u0060\u0060\u0060
```

**Penjelasan ekspresi kunci**

- `//*[(@Type = 'Camera') or (@Name = 'light')]` – Menemukan setiap objek dalam adegan yang atribut **type**‑nya sama dengan `Camera` **atau** atribut **name**‑nya sama dengan `light`. Ini adalah contoh klasik **memilih objek berdasarkan nama** (dan tipe).  
- `/c/*/<Camera>` – Mulai dari akar, pergi ke node `c`, kemudian ke anak apa saja (`*`), dan akhirnya memilih entitas `<Camera>`.  
- `a1` – Singkatan yang mencari seluruh pohon untuk node bernama `a1`.  
- `/` – Mengembalikan node akar itu sendiri.  

## Kesalahan umum & tips  

- **Sensitivitas huruf:** Nama atribut (`@Type`, `@Name`) bersifat case‑sensitive.  
- **Entitas vs. node:** Gunakan sintaks `<Camera>` hanya ketika Anda memerlukan entitas dasar, bukan sekadar node.  
- **Kinerja:** Untuk adegan yang sangat besar, persempit jalur pencarian (misalnya, mulai dari subtree tertentu) untuk meningkatkan kecepatan.  

## Common issues and solutions  

| Masalah | Alasan | Solusi |
|-------|--------|----------|
| Tidak ada hasil yang dikembalikan | Kesalahan ketik string kueri atau kasus atribut yang salah | Verifikasi ejaan dan kasus `@Name`; gunakan nama node yang tepat |
| Node yang tidak diharapkan termasuk | Menggunakan `//*` mencari seluruh pohon | Batasi jalur, misalnya `/c/*` untuk membatasi ruang lingkup |
| Kinerja lambat pada adegan besar | Kueri dijalankan pada seluruh grafik | Mulai kueri dari sub‑node yang diketahui alih-alih akar |

## Frequently asked questions  

**Q: Di mana saya dapat menemukan dokumentasi Aspose.3D untuk Java?**  
A: Dokumentasi tersedia **[Aspose.3D Java API reference](https://reference.aspose.com/3d/java/)**.

**Q: Bagaimana cara mengunduh Aspose.3D untuk Java?**  
A: Anda dapat mengunduhnya **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.

**Q: Apakah ada versi percobaan gratis?**  
A: Ya, Anda dapat memperoleh versi percobaan gratis **[Aspose free trial page](https://releases.aspose.com/)**.

**Q: Di mana saya dapat mendapatkan dukungan untuk Aspose.3D untuk Java?**  
A: Kunjungi forum dukungan **[Aspose 3D support forum](https://forum.aspose.com/c/3d/18)**.

**Q: Membutuhkan lisensi sementara?**  
A: Dapatkan lisensi sementara **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

**Q: Bisakah saya mengkueri properti yang didefinisikan pengguna?**  
A: Ya, Anda dapat memperluas ekspresi XPath dengan atribut `@` tambahan yang Anda tambahkan ke node.

**Q: Apakah mesin kueri bekerja dengan adegan beranimasi?**  
A: Tentu – kueri beroperasi pada hierarki statis; animasi terlampir pada node yang sama sehingga termasuk dalam hasil.

## Conclusion  

Anda kini tahu cara **memilih objek berdasarkan nama** dalam adegan Java 3D menggunakan kueri mirip XPath. Pendekatan ini dapat diskalakan dari demo sederhana hingga aplikasi 3‑D tingkat produksi, memberi Anda kontrol detail atas penelusuran adegan tanpa kode yang bertele‑tele.

**Terakhir Diperbarui:** 2026-10-03  
**Diuji Dengan:** Aspose.3D for Java 24.11  
**Penulis:** Aspose  








```java
import com.aspose.threed.*;

import java.util.ArrayList;
import java.util.List;
```

## Tutorial Terkait

- [Cara Menggunakan XPath untuk Mengubah Radius Bola di Java dengan Aspose.3D](/3d/java/3d-objects-and-scenes/)
- [Baca Adegan 3D di Java dengan Aspose.3D](/3d/java/load-and-save/read-existing-3d-scenes/)
- [Terapkan Transformasi Geometris pada Node Menggunakan Aspose.3D Java API](/3d/java/geometry/expose-geometric-transformations/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}