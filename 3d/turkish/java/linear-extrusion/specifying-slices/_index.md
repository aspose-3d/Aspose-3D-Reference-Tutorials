---
date: 2026-05-24
description: Aspose.3D for Java kullanarak dilimler ile 3d ekstrüzyon oluşturmayı
  öğrenin. Bu adım adım kılavuz, lineer ekstrüzyonu, yuvarlama yarıçapını ayarlamayı
  ve OBJ dışa aktarmayı kapsar.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Dilimler ile 3D Ekstrüzyon Oluşturma – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Dilimler ile 3D Ekstrüzyon Oluşturma – Aspose.3D for Java
url: /tr/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Dilimlerle Ekstrüzyon Oluşturma – Aspose.3D for Java

## Giriş

If you need to **create 3d extrusion** objects that look smooth and precise, controlling the number of slices is the key. In this tutorial we’ll walk through how to specify slices while performing a linear extrusion with Aspose.3D for Java. You’ll see why slice count matters, how to set a rounding radius, and how to export the result as an OBJ file that can be used in any 3‑D pipeline.

## Hızlı Yanıtlar
- **“slices” neyi kontrol eder?** The number of intermediate cross‑sections used to approximate the extrusion surface.  
- **Hangi yöntem dilim sayısını ayarlar?** `LinearExtrusion.setSlices(int)`  
- **Profilin yuvarlama yarıçapını değiştirebilir miyim?** Yes, via `RectangleShape.setRoundingRadius(double)`  
- **Bu örnekte hangi dosya formatı kullanılıyor?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** A free trial works for evaluation; a commercial license is required for production.

`LinearExtrusion.setSlices(int)` sets how many intermediate slices the extrusion will generate.  
`RectangleShape.setRoundingRadius(double)` defines the corner radius of a rectangular profile.

## Dilimlerle Java’da 3D ekstrüzyon nasıl oluşturulur?

Load your 2‑D profile, choose a slice count, set the rounding radius, and call `save` – the entire workflow fits in a handful of lines. Aspose.3D for Java handles the geometry creation, slice interpolation, and OBJ export automatically, so you can focus on visual quality rather than low‑level mesh calculations.

## Dilimlerle lineer ekstrüzyon nedir?

A linear extrusion with slices turns a flat 2‑D shape into a 3‑D solid by sweeping it along a straight line while generating a configurable number of intermediate cross‑sections. The slice count directly influences how smoothly curved edges, such as rounded corners, are rendered.

## 3D ekstrüzyon oluşturmak için Aspose.3D for Java neden kullanılmalı?

Aspose.3D provides **full programmatic control** over every extrusion parameter, supports **50+ input and output formats** (including OBJ, FBX, STL, and GLTF), and can process **multi‑hundred‑page models** without loading the entire file into memory. It runs on any Java‑enabled platform, requires no native DLLs, and guarantees deterministic results across Windows, Linux, and macOS.

## Önkoşullar

1. **Java Development Kit** – JDK 8 or higher installed.  
2. **Aspose.3D for Java** – Download the library from the official site [here](https://releases.aspose.com/3d/java/).  
3. An IDE or text editor of your choice.

## Paketleri İçe Aktar

Add the Aspose.3D namespace to your project so you can access the 3‑D modeling classes.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Adım Adım Kılavuz

### Adım 1: Sahneyi kurun ve profili tanımlayın

`RectangleShape` is a class that defines a 2‑D rectangle profile.  
First we create a `RectangleShape` and give it a **rounding radius** so the corners are smooth.  
`Scene` is the root container for all nodes and geometry.  
Then we initialise a new `Scene` that will hold all geometry.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Adım 2: Her ekstrüzyon için alt düğüm nesneleri oluşturun

`Node` represents an element in the scene graph that can hold geometry and transformations.  
Every piece of geometry lives under a `Node`. Here we generate two sibling nodes – one for a low‑slice extrusion and another for a high‑slice extrusion – and move the left node a little to the side so the results are easy to compare.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Adım 3: Lineer ekstrüzyonu gerçekleştir ve dilimleri ayarla

`LinearExtrusion` is the class that creates a solid by sweeping a profile linearly.  
`LinearExtrusion` is Aspose.3D's class that generates a solid by extruding a 2‑D profile along a straight line. Using an **anonymous inner class** we call `setSlices` to control the smoothness. The left node gets only 2 slices (coarse), while the right node gets 10 slices (smooth).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Adım 4: OBJ Dışa Aktar – sahneyi kaydet

Finally we write the scene to a Wavefront OBJ file, a format widely supported by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability of Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Ekstrüzyon düz görünüyor** | Dilim sayısı 1 veya 0 olarak ayarlandı | Ensure `setSlices` is called with a value ≥ 2. |
| **Yuvarlatılmış köşeler pürüzlü görünüyor** | Yuvarlama yarıçapı, dilim sayısına göre çok küçük | Increase either the radius or the slice count for smoother curves. |
| **Kaydetme sırasında dosya bulunamadı** | `MyDir` mevcut olmayan bir klasöre işaret ediyor | Create the directory beforehand or use an absolute path. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java’yı nasıl indirebilirim?**  
C: You can download the library [here](https://releases.aspose.com/3d/java/).

**S: Aspose.3D belgelerini nerede bulabilirim?**  
C: Refer to the documentation [here](https://reference.aspose.com/3d/java/).

**S: Ücretsiz deneme mevcut mu?**  
C: Yes, you can explore a free trial [here](https://releases.aspose.com/).

**S: Aspose.3D için destek nasıl alabilirim?**  
C: Visit the support forum [here](https://forum.aspose.com/c/3d/18).

**S: Geçici bir lisans satın alabilir miyim?**  
C: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).

**Son Güncelleme:** 2026-05-24  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Yazar:** Aspose

## İlgili Eğitimler

- [Aspose.3D ile Java’da 3D Ekstrüzyon Oluşturma](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Aspose.3D for Java ile Lineer Ekstrüzyonda Yön Nasıl Ayarlanır](/3d/java/linear-extrusion/setting-direction/)
- [Aspose.3D for Java – Lineer Ekstrüzyonda Burulma ile 3D Sahne Oluşturma](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}