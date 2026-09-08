---
date: 2026-09-08
description: Java'da bir küre ağı oluşturarak ve Google Draco'yu Aspose.3D aracılığıyla
  kullanarak 3d model boyutunu nasıl küçültebileceğinizi öğrenin. Tam iş akışını dakikalar
  içinde öğrenin.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: 3d Model Boyutunu Nasıl Küçültülür – Java'da Google Draco Kullanarak Küre
  Ağı Oluşturma
og_description: Java'da bir küre ağı oluşturarak ve Google Draco'yu Aspose.3D ile
  kullanarak 3d model boyutunu nasıl küçültebileceğinizi öğrenin. .drc dosyasını dakikalar
  içinde %95'e kadar küçültebilirsiniz.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Java küre ağı ve Draco ile 3d model boyutunu nasıl küçültülür
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Java küre ağı ve Draco ile 3d model boyutunu nasıl küçültülür
url: /tr/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java küre ağı ve Draco ile 3d model boyutunu nasıl azaltılır

## Giriş

Eğer yüksek kaliteli geometriyi korurken **3d model boyutunu** hızlı bir şekilde **küçültmek** istiyorsanız, doğru yerdesiniz. Bu eğitimde **Aspose.3D for Java** ile bir küre ağı oluşturup ardından **Google Draco** kullanarak bu ağı sıkıştıracağız. Sonunda orijinaline göre çok daha küçük bir `.drc` dosyasına sahip olacaksınız; bu da web tabanlı görüntüleyiciler, mobil oyunlar veya bant genişliği sınırlı herhangi bir Java uygulaması için mükemmeldir.

## Hızlı cevaplar
- **Bu eğitim neyi kapsıyor?** Java'da bir küre ağı oluşturmak ve Aspose.3D aracılığıyla Google Draco ile sıkıştırmak.  
- **Ana kütüphane?** Aspose.3D for Java (hem ağ oluşturma hem de Draco dışa aktarımı için kullanılır).  
- **Tipik uygulama süresi?** Temel bir küre için yaklaşık 10‑15 dakika.  
- **Temel önkoşul?** Aspose.3D JAR'larının sınıf yolunda bulunduğu bir Java geliştirme ortamı.  
- **Sonuç?** Sıkıştırılmamış bir ağ ile karşılaştırıldığında **3d model boyutunu** %95'e kadar azaltan bir `.drc` dosyası.

## 3d model boyutunu nasıl azaltılır?

`Sphere` sınıfı, verilen yarıçap ve teselleştirme parametrelerine göre üçgenlenmiş bir küre geometrisi üretir. Kürenizi `new Sphere(1.0, 32, 32)` ile oluşturup `scene.save("sphere.drc", SaveFormat.Draco)` kullanarak doğrudan Draco'ya dışa aktarın. `scene.save` yöntemi mevcut sahneyi belirtilen formatta bir dosyaya yazar. Aspose.3D dönüşümü dahili olarak yönetir, böylece manuel kodlama adımlarından kaçınırsınız. Draco dışa aktarımı, geometri kuantizasyonu ve vertex tekrarlamasını otomatik olarak uygular; bu da genellikle %80‑95 daha küçük dosyalar üretirken görsel bütünlüğü korur.

## “3d model boyutunu azaltma” 3d geliştirme bağlamında ne anlama gelir?

**3d model boyutunu küçültmek**, görsel kalitede belirgin bir düşüş olmadan aktarılması veya depolanması gereken geometri verisi miktarını azaltmak anlamına gelir. Draco, vertex konumlarını, normalleri ve diğer öznitelikleri son derece sıkışık bir ikili formatta kodlayarak bunu başarır. Aspose.3D ile birleştirildiğinde, tüm iş akışı Java içinde kalır; böylece yerel ikili dosyalarla uğraşmak zorunda kalmazsınız.

## Aspose.3D ile Google Draco ağ sıkıştırması neden kullanılmalı?

Google Draco, Aspose.3D ile birleştirildiğinde, ağ dosyalarını dramatik şekilde küçülten ve Java projelerine entegrasyonu kolaylaştıran verimli bir işlem hattı sunar. Kütüphane tüm düşük seviyeli kodlamayı yönetir, bu sayede geliştiriciler yerel Draco ikili dosyalarıyla uğraşmadan geometri oluşturumuna odaklanabilir; bu da daha hızlı geliştirme ve web ile mobil için daha küçük varlıklar anlamına gelir.

- **Büyük boyut azaltma:** Draco, tipik modellerde ağ verisini %95'e kadar azaltabilir; 5 MB bir OBJ dosyasını 0.3 MB `.drc`'ye dönüştürür.  
- **Hızlı çalışma zamanı çözümleme:** Unity, Unreal ve three.js gibi motorlar Draco'yu yerel olarak çözer, bu da daha hızlı yükleme süreleri sağlar.  
- **Sorunsuz Java entegrasyonu:** Aspose.3D, yerel Draco kütüphanesini soyutlayarak Java ekosisteminde kalmanıza olanak tanır.  
- **Tek durak Aspose 3D dışa aktarımı:** Geometri oluşturmak için kullandığınız aynı API, dışa aktarımı da yönetir; bu da işlem hattını basitleştirir.

## Önkoşullar

- **Java Development Kit (JDK)** – sürüm 8 veya daha yeni.  
- **Aspose.3D for Java** – en son JAR'ları **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** adresinden indirin.  
- **Google Draco'ya temel aşinalık** – Aspose.3D'nin sarmalayıcısını kullanacaksınız, bu yüzden yerel Draco kurulumu gerekli değildir.

## Paketleri içe aktar

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Adım adım kılavuz

### Adım 1: projeyi kurun

Yeni bir Java projesi oluşturun (herhangi bir IDE çalışır) ve tüm Aspose.3D JAR'larını sınıf yoluna ekleyin. Kaynak dosyalarınızı netlik için `com.example.draco` gibi bir paket içinde tutun.

### Adım 2: Java'da küre ağı nasıl oluşturulur

`Sphere` sınıfı, Aspose.3D'nin yerleşik geometri üreticisi olup, yapılandırılabilir bir yarıçap ve teselleştirme ile üçgenlenmiş bir ağ üretir.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro ipucu:** `Sphere` sınıfı, varsayılan 1.0 yarıçapıyla üçgenlenmiş bir ağ üretir. Sıkıştırmadan önce farklı bir detay seviyesine ihtiyacınız varsa, özel yarıçap, teselleştirme veya malzeme parametreleri geçirebilirsiniz.

### Adım 3: ağı Draco formatına dışa aktar

Küre bir `Scene` nesnesine eklendikten sonra `scene.save("sphere.drc", SaveFormat.Draco)` metodunu çağırın. Aspose.3D otomatik olarak optimal sıkıştırma ayarlarını seçer, ancak en küçük dosyayı istiyorsanız `DracoCompressionOptions` ayarlarını değiştirerek ince ayar yapabilirsiniz. `DracoCompressionOptions`, kuantizasyon ve sıkıştırma seviyesi gibi Draco sıkıştırma ayarlarını özelleştirmenizi sağlar.

### Adım 4: çıktıyı doğrula

Oluşturulan `.drc` dosyasını bir Draco görüntüleyiciyle (ör. three.js `DRACOLoader`) açarak geometrinin doğru render edildiğinden emin olun. Dosya boyutunda dramatik bir azalma göreceksiniz; genellikle on kat ya da daha fazla.

## Yaygın kullanım senaryoları

| Senaryo | Model boyutunu neden azaltmalı? | Bu eğitim nasıl yardımcı olur |
|----------|-------------------------------|------------------------------|
| Web tabanlı ürün yapılandırıcıları | Yavaş bağlantılarda daha hızlı sayfa yüklemeleri | Draco sıkıştırmalı `.drc` dosyaları saniyeler içinde yüklenir |
| Mobil AR/VR uygulamaları | Cihazlarda daha düşük bellek ayak izi | Daha küçük ağlar uygulamanın yanıt vermesini sağlar |
| Bulut tabanlı render sahneleri | Bant genişliği maliyetlerini azaltır | Aspose.3D'den Draco'ya tek tıkla dışa aktarım |

## Yaygın sorunlar ve çözümler

| Sorun | Sebep | Çözüm |
|-------|-------|-------|
| **`NoClassDefFoundError` Draco sınıfları için** | Aspose.3D JAR'ları sınıf yolunda değil | *Tüm* Aspose.3D JAR dosyalarının dahil edildiğini ve sürümün belgelerle eşleştiğini doğrulayın. |
| **Çıktı dosyası boş** | `MyDir` var olmayan bir klasöre işaret ediyor | Dosyayı yazmadan önce dizini programatik olarak oluşturun (`Files.createDirectories(Paths.get(MyDir))`). |
| **Sıkıştırılmış ağ bozuk görünüyor** | Düşük sıkıştırma seviyesi veya yetersiz teselleştirme kullanılması | `DracoCompressionLevel.OPTIMAL`'a geçin ve kürenin teselleştirmesini artırın (ör. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL`, Draco çıktısı için en yüksek sıkıştırma kalitesini seçer. |

## Sıkça Sorulan Sorular

**S: Aspose.3D farklı 3d dosya formatlarıyla uyumlu mu?**  
C: Evet, Aspose.3D OBJ, FBX, STL, GLTF ve daha birçok formatı destekler; bu da **Aspose 3d export** işlem hatları için çok yönlü bir seçim yapar.

**S: Google Draco'yu başka programlama dillerinde sıkıştırma için kullanabilir miyim?**  
C: Kesinlikle. Draco, C++, Python ve JavaScript için yerel kütüphaneler sunar. Bu eğitim Java'ya odaklanmıştır, ancak kavramlar diller arasında geçerlidir.

**S: Ek Aspose.3D belgelerini nerede bulabilirim?**  
C: Tam API referansları ve daha fazla örnek için **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** adresini ziyaret edin.

**S: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
C: **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)** adresindeki geçici lisans seçeneklerini inceleyin.

**S: Aspose.3D desteği için bir topluluk forumu var mı?**  
C: Evet, **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)** adresindeki tartışmaya katılabilirsiniz.

## Sonuç

Bu rehberde, Java'da bir küre ağı oluşturarak ve ardından Aspose.3D aracılığıyla Google Draco ile sıkıştırarak **3d model boyutunu nasıl küçültebileceğinizi** gösterdik. Bu özlü adımları izleyerek ağ dosyalarını dramatik şekilde küçültebilir, yükleme sürelerini iyileştirebilir ve Java tabanlı 3d uygulamalarınızı yanıt verebilir ve bant genişliği dostu tutabilirsiniz.

---

**Son Güncelleme:** 2026-09-08  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose

## İlgili Eğitimler

- [3D Dosya Boyutunu Azalt – Aspose.3D for Java ile Sahneleri Sıkıştır](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Aspose.3D for Java kullanarak kürelerden Draco nokta bulutu oluştur](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Aspose.3D kullanarak Java'da Optimize Görüntüleme için Ağları Nasıl Üçgenleştireceğinizi Öğrenin](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}