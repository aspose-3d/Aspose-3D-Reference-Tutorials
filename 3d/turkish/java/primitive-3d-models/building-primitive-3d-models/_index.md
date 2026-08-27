---
date: 2026-06-03
description: Aspose.3D for Java kullanarak sahneyi FBX olarak dışa aktarmayı ve 3D
  silindir, kutu ve diğer ilkel modelleri oluşturmayı öğrenin.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Aspose.3D for Java ile İlkel 3D Modeller Oluşturma
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Sahneyi FBX olarak dışa aktar ve Aspose.3D Java ile silindir oluştur
url: /tr/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sahneyi FBX olarak dışa aktar ve Aspose.3D Java ile silindir oluştur

## Giriş

Java kodundan doğrudan **3D silindir oluşturmanız** (veya başka bir temel şekil) gerektiğinde, Aspose.3D bu görevi zahmetsiz hale getirir. Bu öğreticide, ortamı kurmaktan **sahneyi FBX olarak dışa aktarmaya** kadar tüm iş akışını adım adım göstereceğiz; böylece hemen programlı olarak 3D geometri üretmeye başlayabilirsiniz. Kütüphanenin primitive'leri nasıl işlediğini, bunları bir sahne grafiğinde nasıl düzenleyeceğinizi ve sonucu Unity, Blender veya başka bir 3D aracın okuyabileceği bir formatta nasıl kaydedeceğinizi göreceksiniz.

## Hızlı Yanıtlar

- **Java'da 3D silindir oluşturmamı sağlayan kütüphane hangisidir?** Aspose.3D for Java.  
- **Sahneyi hangi formata dışa aktarabilirim?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Geliştirme için lisansa ihtiyacım var mı?** Test için ücretsiz deneme sürümü yeterlidir; üretim için kalıcı bir lisans gereklidir.  
- **Desteklenen ana primitive'lar nelerdir?** Box, Cylinder, Sphere, Cone, and more than 10 additional shapes.  
- **Kod Java 8 ve üzeri ile uyumlu mu?** Evet, Aspose.3D JDK 8+ hedeflemektedir.

## 3D silindir primitive'i nedir?

Silindir primitive'i, yarıçap ve yükseklik ile tanımlanan temel bir geometrik şekildir. Birçok 3D iş akışında, borular, tekerlekler veya mimari sütunlar gibi daha karmaşık modellerin yapı taşı olarak hizmet eder. Aspose.3D, hazır bir `Cylinder` sınıfı sağlar, böylece köşeleri manuel olarak hesaplamanıza gerek kalmaz.

## Java için Aspose.3D neden kullanılmalı?

Aspose.3D for Java, yerel kütüphanelere ihtiyaç duymayan kapsamlı, saf‑Java bir 3D motoru sunar ve bu da çapraz‑platform geliştirme için idealdir. Geniş bir içe ve dışa aktarma formatı yelpazesini destekler, hiyerarşik organizasyon için sağlam bir sahne grafiği sağlar ve minimal kodla geometri oluşturmanıza olanak tanıyan yerleşik primitive'lar içerir. Bu özellikler birlikte geliştirmeyi hızlandırır ve bakım yükünü azaltır.

- **Tam özellikli 3D motoru** – popüler **30'dan fazla** formatın (FBX, OBJ, STL, GLTF, 3DS, vb.) içe ve dışa aktarımını destekler.  
- **Saf Java API** – yerel bağımlılık yok, çapraz‑platform projeler için mükemmeldir.  
- **Sağlam sahne grafiği** – nesneleri hiyerarşik olarak düzenlemenizi sağlar, büyük sahneleri yönetmeyi kolaylaştırır.  
- **Kolay lisanslama** – ücretsiz deneme ile başlayın, ardından yayına alındığında kalıcı bir lisansa yükseltin.

## Ön Koşullar

1. **Java Development Kit (JDK)** – Makinenizde yüklü JDK 8 veya daha yeni bir sürüm.  
2. **Aspose.3D for Java library** – [download page](https://releases.aspose.com/3d/java/) üzerinden indirin ve kurun.  

## Paketleri İçe Aktar

Aspose.3D çekirdek ad alanını içe aktararak başlayın. Bu, `Scene`, `Box`, `Cylinder` ve dosya‑format sabitlerine erişmenizi sağlar.

```java
import com.aspose.threed.*;
```

Artık kütüphane referans alındığına göre, bir sahne oluşturalım ve bazı primitive geometriler ekleyelim.

## Sahneyi FBX olarak nasıl dışa aktarır ve 3D primitive'lar oluştururuz?

Yeni bir `Scene` nesnesi yükleyin, primitive düğümlerini (Box, Cylinder, vb.) ekleyin ve ardından FBX7500ASCII formatı ile `save` metodunu çağırın. Sadece birkaç satırda, herhangi bir büyük 3D editörde açılabilen tam özellikli bir FBX dosyası elde eder ve oyun motorları, render pipeline'ları veya AR/VR uygulamalarıyla sorunsuz entegrasyon sağlarsınız.

### Adım 1: Bir Scene Nesnesi Başlat

`Scene` sınıfı, Aspose.3D'nin bellekte tüm düğümleri, ışıkları, kameraları ve materyalleri tutan üst‑seviye konteyneridir.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Adım 2: 3D kutu modeli oluştur

`Box` sınıfı, dikdörtgen prizma temsil eder ve koordinat sistemini test etmek için faydalıdır. Sahnenin kök düğümünün çocuğu olarak eklemek, onu orijine konumlandırır.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Adım 3: 3D silindir modeli oluştur

`Cylinder` sınıfı, Aspose.3D'nin yerleşik silindir primitive'idir. Varsayılan boyutlarla (yarıçap = 1, yükseklik = 2) gelir ancak yapıcı (constructor) üzerinden bunları özelleştirebilirsiniz.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Adım 4: Çizimi FBX formatında kaydet

Sahneyi birleştirdikten sonra, diğer araçların (ör. Unity, Blender) okuyabilmesi için dışa aktarın. Geniş çapta desteklenen ve insan tarafından okunabilir `FBX7500ASCII` formatını kullanıyoruz.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Dosya bulunamadı** kaydederken | `myDir` var olmayan bir klasöre işaret ediyor | Dizinin mevcut olduğundan emin olun veya `new File(myDir).mkdirs();` ile oluşturun. |
| **Boş sahne** dışa aktardıktan sonra | `save` çağrılmadan önce düğüm eklenmemiş | `createChildNode` çağrılarının yürütüldüğünü doğrulayın (`scene.getRootNode().getChildCount()` ile hata ayıklayın). |
| **Lisans istisnası** | Üretimde geçerli bir lisans olmadan çalıştırmak | `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` kullanarak geçici veya kalıcı bir lisans uygulayın. |

## Sıkça Sorulan Sorular

**Q: Aspose.3D for Java'ı diğer programlama dilleriyle kullanabilir miyim?**  
A: Aspose.3D öncelikle Java'yı destekler, ancak .NET ve C++ için de sürümler mevcuttur.

**Q: Aspose.3D karmaşık 3D modelleme görevleri için uygun mu?**  
A: Kesinlikle. Mesh manipülasyonu, malzeme atama ve animasyon gibi kapsamlı özellikler sunar; bu da hem basit primitive'lar hem de karmaşık modeller için uygundur.

**Q: Ek yardım ve destek nereden bulunabilir?**  
A: Topluluk desteği ve tartışmalar için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**Q: Aspose.3D'yi satın almadan önce deneyebilir miyim?**  
A: Evet, satın alma kararından önce bir [ücretsiz deneme](https://releases.aspose.com/) inceleyebilirsiniz.

**Q: Aspose.3D için geçici bir lisans nasıl elde ederim?**  
A: Web sitesi üzerinden bir [geçici lisans](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

## Sonuç

Artık **sahneyi FBX olarak dışa aktarmayı** ve Aspose.3D for Java kullanarak **3D silindir**, kutu ve diğer primitive modelleri oluşturmayı öğrendiniz. Sphere, Cone veya Torus gibi ek primitive'larla denemeler yapmaktan ve modellerinize gerçekçi bir görünüm kazandırmak için malzeme atamaları keşfetmekten çekinmeyin. Kendiniz rahat olduğunuzda, oluşturulan FBX dosyalarını oyun motorlarına, AR/VR pipeline'larına veya herhangi bir sonraki 3D iş akışına entegre edebilirsiniz.

---

**Son Güncelleme:** 2026-06-03  
**Test Edilen:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Yazar:** Aspose

## İlgili Öğreticiler

- [Java'da Sahneyi FBX Olarak Dışa Aktarma ve 3D Sahne Bilgilerini Alma](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Java'da FBX Dışa Aktarma ve Düğüm Hiyerarşileri Oluşturma](/3d/java/geometry/build-node-hierarchies/)
- [Aspose.3D for Java ile Silindir Modelleri Oluşturma](/3d/java/cylinders/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}