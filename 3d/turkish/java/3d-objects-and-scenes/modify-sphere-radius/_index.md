---
date: 2026-10-03
description: Aspose.3D'yi kullanarak Java'da küre oluşturmayı ve OBJ dosyasını dışa
  aktarmayı öğrenin; 3D modelleri dönüştürmek için önde gelen Java 3D kütüphanesidir.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Java''da küre oluşturma: Aspose.3D ile 3D''yi OBJ''ye dönüştürün'
og_description: Aspose.3D'yi kullanarak Java'da küre oluşturmayı ve OBJ dosyasını
  dışa aktarmayı öğrenin. Bu adım adım kılavuz, bir küre eklemeyi, yarıçapını değiştirmeyi
  ve OBJ olarak kaydetmeyi gösterir.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Java'da küre oluşturma – Aspose.3D ile OBJ dışa aktarımı
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Java''da küre oluşturma: Aspose.3D ile 3D''yi OBJ''ye dönüştürün'
url: /tr/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Küre oluşturma java ve OBJ'ye dışa aktarma

## Giriş

Bu öğreticide **create sphere java**, yarıçapını ayarlamayı ve ardından Aspose.3D Java kütüphanesini kullanarak **save 3d as obj** yapmayı öğreneceksiniz. Kodun her satırını adım adım inceleyecek, her adımın neden önemli olduğunu açıklayacak ve bu iş akışını oyunlara, CAD araçlarına veya bilimsel görselleştirmelere güvenle entegre edebilmeniz için pratik ipuçları vereceğiz.

## Hızlı Yanıtlar
- **What is the main goal of this tutorial?** Bu öğreticinin ana hedefi, **create sphere java**, boyutunu değiştirmeyi ve modeli Java kullanarak OBJ olarak dışa aktarmayı göstermek.
- **Which library provides the 3D functionality?** Aspose.3D, tam özellikli **java 3d library tutorial**.
- **How do I change the sphere size?** `Sphere` örneği üzerinde `sphere.setRadius(double)` metodunu çağırın.
- **Can I write the OBJ file directly from Java?** Evet—`scene.save("file.obj", FileFormat.WAVEFRONTOBJ)` kullanın.
- **Do I need a license for production?** Geliştirme için ücretsiz deneme yeterlidir; ticari kullanım için kalıcı bir lisans gereklidir.

## Aspose.3D for Java nedir?

Aspose.3D for Java, geliştiricilerin dış bağımlılıklar olmadan 3D dosyaları oluşturmasını, düzenlemesini ve dönüştürmesini sağlayan kapsamlı bir **java 3d library**'dir. **50'den fazla giriş ve çıkış formatını** destekler—OBJ, FBX, STL ve GLTF dahil—ve herhangi bir 3‑D işlem hattına sorunsuz entegrasyon sağlar.

## Neden 3D'yi OBJ'ye dönüştürmeliyiz?

OBJ'ye dönüştürmek, evrensel olarak desteklenen, düz metin tabanlı bir geometri temsili sağlar; bu dosya herhangi bir 3D araç tarafından okunabilir, bu da hızlı prototipleme, platformlar arası varlık değişimi ve vertex verisinin kolay hata ayıklaması için idealdir. OBJ dosyaları hafif ve insan tarafından okunabilir olduğundan, gerektiğinde basit bir metin düzenleyiciyle inceleyebilir veya değiştirebilirsiniz.

## Önkoşullar

- Temel Java programlama bilgisi.  
- Aspose.3D kütüphanesi yüklü – bunu [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresinden indirin.  
- Geliştirme makinenizde JDK 8 veya daha yeni bir sürüm yüklü.

## Paketleri içe aktar

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## sphere radius java nasıl değiştirilir?

`Sphere`, Aspose.3D içinde bir küreyi temsil eden geometrik bir ilkel (primitive) nesnedir.  
`Sphere` nesnesini yükleyin, istediğiniz değeri `setRadius` ile çağırın ve ardından sahneyi OBJ olarak kaydedin—bu tüm iş akışı beş kısa adımda gerçekleştirilebilir. Yaklaşım, herhangi bir sayısal yarıçap için çalışır ve dışa aktarılan OBJ'nin belirttiğiniz tam boyutu yansıtmasını sağlar.

### Adım 1: Bir sahne başlatın

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** `Scene` sınıfı, bir 3D modelinin geometri, ışık ve kameralarını tutan Aspose.3D'nin üst‑seviye konteyneridir. Bir `Scene` oluşturmak, nesneleri ekleyip manipüle edebileceğiniz bir çalışma alanı sağlar.

Bir `Scene` oluşturmak, tüm geometri, ışık ve kameralar için bir konteyner sağlar. Daha sonra **add sphere to scene** burada eklenecek.

### Adım 2: Bir küre başlatın

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** `Sphere` sınıfı, yapılandırılabilir bir yarıçap, merkez ve malzemeye sahip geometrik bir küre ilkelini temsil eder. Varsayılan olarak 1.0 yarıçapla başlar.

Bir `Sphere` nesnesi varsayılan olarak 1.0 yarıçapla başlar. Dışa aktarmak istediğiniz şekil için boş bir tuval gibi düşünün.

### Adım 3: İstenen yarıçapı ayarlayın

**Definition anchor:** `setRadius(double)` metodu, sahnede kullanılan aynı birimlerde kürenin yarıçapını ayarlar.  

```java
// set radius
sphere.setRadius(10);
```

Burada **write obj file java**‑stilinde kod yazarak tam yarıçapı ayarlıyoruz. `10` değerini, tasarım gereksinimlerinize uyan herhangi bir `double` değerle değiştirin.

### Adım 4: Küreyi sahneye ekleyin

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Bu satır, kök düğüm altında bir alt düğüm oluşturarak **adds sphere to scene** gerçekleştirir. Geometrinin sahne grafiğinin bir parçası haline geldiği an budur.

### Adım 5: Modeli OBJ olarak dışa aktar

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

`save(String, FileFormat)` metodu, seçilen format (örneğin OBJ) kullanarak tüm sahneyi belirtilen dosyaya yazar. `scene.save` çağrısı **exports obj file java**‑stilinde çalışır ve etkili bir şekilde **save scene as obj** gerçekleştirir. Oluşturulan `sphere.obj` herhangi bir standart 3D görüntüleyicide açılabilir.

## Yaygın sorunlar ve çözümler

| Sorun | Çözüm |
|-------|----------|
| **Sphere appears too small in the viewer** | Yarıçap değerinin doğru ayarlandığını doğrulayın; bir ölçekleme dönüşümü uygulamadığınız sürece birimlerin keyfi olduğunu unutmayın. |
| **Exported OBJ has no material** | Aspose.3D yalnızca geometri yazar; doku gerekiyorsa küreye bir malzeme ekleyin (`sphere.setMaterial(...)`). |
| **License exception at runtime** | `Scene` oluşturulmadan önce geçici ya da kalıcı bir lisans dosyasının yüklendiğinden emin olun. |

## Sıkça Sorulan Sorular

**Q: Where can I find the documentation for Aspose.3D for Java?**  
A: Kapsamlı rehberlik için [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresine bakabilirsiniz.

**Q: How do I download Aspose.3D for Java?**  
A: Kütüphaneyi sürüm sayfasından indirin: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Is there a free trial available for Aspose.3D for Java?**  
A: Evet, [Aspose.3D Free Trial](https://releases.aspose.com/) adresini ziyaret ederek ücretsiz deneme ile özellikleri keşfedebilirsiniz.

**Q: Where can I get support for Aspose.3D for Java?**  
A: Yardım ve tartışmalar için [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) adresindeki Aspose topluluğuna katılın.

**Q: How can I obtain a temporary license for Aspose.3D?**  
A: [Temporary License](https://purchase.aspose.com/temporary-license/) adresini ziyaret ederek geçici bir lisans edinin.

**Q: Can I use this code with other 3D formats like STL?**  
A: Kesinlikle – `scene.save` çağırırken `FileFormat` enum'ını değiştirin, örneğin `FileFormat.STL`.

---

**Last Updated:** 2026-10-03  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## İlgili öğreticiler

- [How to Set Normals on 3D Objects in Java Using Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [How to Embed Texture in FBX with Java – Apply Materials to 3D Objects using Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [How to Change Plane Orientation and Export OBJ in Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}