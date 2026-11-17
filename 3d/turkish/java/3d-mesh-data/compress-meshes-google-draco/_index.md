---
date: 2026-11-17
description: Java'da bir küre ağı oluşturarak ve Google Draco'yu Aspose.3D üzerinden
  kullanarak 3D model boyutunu nasıl azaltılır. Tam iş akışını dakikalar içinde öğrenin.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: 3D Model Boyutunu Azaltma – Java'da Google Draco Kullanarak Küre Ağı Oluşturma
og_description: Java kullanarak Aspose.3D ve Google Draco ile küre ağı oluşturun ve
  3D modeli sıkıştırın. Bu öğreticide bir küre nasıl oluşturulur, .drc formatına nasıl
  dışa aktarılır ve dakikalar içinde %95'e varan boyut azaltımı nasıl sağlanır gösterilmektedir.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Java ve Draco ile küre ağı oluşturun ve 3D modeli sıkıştırın
schemas:
- author: Aspose
  dateModified: '2026-11-17'
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
title: Java küre ağı ve Draco ile 3D model boyutunu nasıl azaltılır
url: /tr/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java küre ağı ve Draco ile 3d model boyutunu nasıl azaltılır

## Giriş

Aspose.3D for Java, Java kodundan doğrudan 3‑D modellerin oluşturulmasını, manipüle edilmesini ve dönüştürülmesini sağlayan bir kütüphanedir. **3d model boyutunu azaltmak** için hızlı bir yol arıyorsanız ve hâlâ yüksek kaliteli geometri sunmak istiyorsanız doğru yerdesiniz. Bu öğreticide **Aspose.3D for Java** ile bir küre ağı oluşturmayı ve ardından **Google Draco** kullanarak bu ağı sıkıştırmayı adım adım göstereceğiz. Sonunda, orijinaline göre dramatik şekilde daha küçük bir `.drc` dosyasına sahip olacaksınız; bu, web‑tabanlı görüntüleyiciler, mobil oyunlar veya bant genişliği sınırlı herhangi bir Java uygulaması için mükemmeldir.

## Hızlı cevaplar
- **Bu öğreticinin kapsamı nedir?** Java'da bir küre ağı oluşturmak ve Aspose.3D aracılığıyla Google Draco ile sıkıştırmak.  
- **Ana kütüphane?** Aspose.3D for Java (hem ağ oluşturma hem de Draco dışa aktarma için kullanılır).  
- **Tipik uygulama süresi?** Temel bir küre için yaklaşık 10‑15 dakika.  
- **Temel önkoşul?** ClassPath'te Aspose.3D JAR'ları bulunan bir Java geliştirme ortamı.  
- **Sonuç?** Sıkıştırılmamış bir ağ ile karşılaştırıldığında **3d model boyutunu** %95'e kadar azaltan bir `.drc` dosyası.

## 3d model boyutunu nasıl azaltılır?

Sphere'ınızı yükleyin ve iki basit adımda sıkıştırın. İlk olarak, `new Sphere(1.0, 32, 32)` ile **küre ağı oluşturursunuz**. Ardından, `scene.save("sphere.drc", SaveFormat.Draco)` kullanarak sahneyi doğrudan Draco'ya dışa aktarırsınız. Aspose.3D, geometri kantitatizasyonu ve vertex tekrarlamasını otomatik olarak yönetir ve genellikle %80‑95 daha küçük dosyalar sunar, görsel kaliteyi korur.

`Sphere` sınıfı, Aspose.3D'nin yerleşik geometri üreteci olup üçgenlenmiş bir küre ağı oluşturur. Yarıçap ve tessellation parametrelerini kabul eder, sıkıştırmadan önce detay seviyesini kontrol etmenizi sağlar.

## 3d geliştirme bağlamında “3d model boyutunu azaltma” ne anlama geliyor?

**3d model boyutunu azaltmak**, görsel kaliteyi belirgin şekilde düşürmeden, aktarılması veya depolanması gereken geometri verisinin miktarını küçültmek anlamına gelir. Draco, vertex konumlarını, normalleri ve diğer öznitelikleri son derece sıkışık bir ikili formatta kodlayarak bunu başarır. Aspose.3D ile birlikte kullanıldığında, tüm iş akışı Java içinde kalır, böylece yerel ikili dosyalarla uğraşmanız gerekmez.

## Aspose.3D ile Google Draco ağ sıkıştırması neden kullanılmalı?

Google Draco, Aspose.3D ile birleştirildiğinde, ağ dosyalarını dramatik şekilde küçülten ve Java projelerine entegrasyonunu kolaylaştıran verimli bir işlem hattı sağlar. Kütüphane tüm düşük‑seviye kodlamayı yönetir, böylece geliştiriciler yerel Draco ikili dosyalarıyla uğraşmadan geometri oluşturumuna odaklanabilir; bu da daha hızlı geliştirme ve web ile mobil için daha küçük varlıklar anlamına gelir.

- **Büyük boyut azaltma:** Draco, tipik modeller için ağ verisini %95'e kadar azaltabilir, 5 MB OBJ'yi 0.3 MB `.drc`'ye dönüştürür.  
- **Hızlı çalışma zamanı çözümleme:** Unity, Unreal ve three.js gibi motorlar Draco'yu yerel olarak çözer, bu da daha hızlı yükleme süreleri sağlar.  
- **Sorunsuz Java entegrasyonu:** Aspose.3D, yerel Draco kütüphanesini soyutlayarak Java ekosisteminde kalmanızı sağlar.  
- **Tek durak Aspose 3D dışa aktarımı:** Geometri oluşturmak için kullandığınız aynı API dışa aktarmayı da yönetir, işlem hattını basitleştirir.  

Aspose.3D, **50+ giriş ve çıkış formatını** destekler — OBJ, FBX, STL, GLTF ve daha fazlası dahil — ve tüm dosyayı belleğe yüklemeden çok sayfalı modelleri işleyebilir.

## Önkoşullar

- **Java Development Kit (JDK)** – sürüm 8 veya daha yeni.  
- **Aspose.3D for Java** – en son JAR'ları **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** adresinden indirin.  
- **Google Draco'ya temel aşinalık** – Aspose.3D'nin sarmalayıcısını kullanacaksınız, bu yüzden yerel Draco kurulumu gerekmez.

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

Yeni bir Java projesi oluşturun (herhangi bir IDE çalışır) ve tüm Aspose.3D JAR'larını classpath'e ekleyin. Kaynak dosyalarınızı netlik için `com.example.draco` gibi bir pakette tutun.

### Adım 2: Java'da küre ağı nasıl oluşturulur

`Sphere` sınıfı, Aspose.3D'nin yerleşik geometri üreteci olup üçgenlenmiş bir küre ağı oluşturur.  

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

> **Pro tip:** `Sphere` sınıfı, varsayılan 1.0 yarıçapıyla üçgenlenmiş bir ağ oluşturur. Sıkıştırmadan önce farklı bir detay seviyesine ihtiyacınız varsa özel yarıçap, tessellation veya materyal parametreleri geçirebilirsiniz.

### Adım 3: ağı Draco formatına dışa aktar

`Scene` sınıfı, ağlar, ışıklar ve kameralar içerebilen tam bir 3‑D sahneyi temsil eder. `DracoCompressionOptions` sınıfı, kantitatizasyon ve sıkıştırma seviyesi gibi Draco sıkıştırma ayarlarını özelleştirmenizi sağlar. Küre bir `Scene` nesnesine eklendikten sonra `scene.save("sphere.drc", SaveFormat.Draco)` çağrısını yapın. Aspose.3D otomatik olarak optimal sıkıştırma ayarlarını seçer, ancak en küçük dosyayı istiyorsanız `DracoCompressionOptions` ayarlayarak ince ayar yapabilirsiniz. `DracoCompressionOptions` size

### Adım 4: çıktıyı doğrula

`DRACOLoader`, Draco‑sıkıştırılmış `.drc` dosyalarını yükleyen ve WebGL‑uyumlu geometriye dönüştüren bir three.js yardımcı programıdır. Oluşturulan `.drc` dosyasını bir Draco görüntüleyici (ör. three.js `DRACOLoader`) ile açarak geometrinin doğru render edildiğinden emin olun. Dosya boyutunda dramatik bir azalma fark edeceksiniz — genellikle on kat veya daha fazla.

## Yaygın kullanım senaryoları

| Senaryo | Model boyutunu neden azaltmalı? | Bu öğretici nasıl yardımcı olur |
|----------|-------------------------------|---------------------------------|
| Web tabanlı ürün yapılandırıcıları | Yavaş bağlantılarda daha hızlı sayfa yüklemeleri | Draco‑sıkıştırılmış `.drc` dosyaları saniyeler içinde yüklenir |
| Mobil AR/VR uygulamaları | Cihazlarda daha düşük bellek ayak izi | Daha küçük ağlar uygulamanın yanıt vermesini sağlar |
| Bulut‑renderlı sahneler | Bant genişliği maliyetlerini azalt | Aspose.3D'den Draco'ya tek tıkla dışa aktarım |

## Yaygın sorunlar ve çözümler

| Sorun | Neden | Çözüm |
|-------|-------|-------|
| **`Draco` sınıfları için `NoClassDefFoundError`** | Aspose.3D JAR'ları classpath'te değil | *Tüm* Aspose.3D JAR dosyalarının dahil edildiğini ve sürümün belgelerle eşleştiğini doğrulayın. |
| **Çıktı dosyası boş** | `MyDir` var olmayan bir klasöre işaret ediyor | Dosyayı yazmadan önce dizini programlı olarak oluşturun (`Files.createDirectories(Paths.get(MyDir))`). |
| **Sıkıştırılmış ağ bozulmuş görünüyor** | Düşük sıkıştırma seviyesi veya yetersiz tessellation kullanmak | `DracoCompressionLevel.OPTIMAL`'a geçin ve kürenin tessellation'ını artırın (ör. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL`, Draco çıktısı için en yüksek sıkıştırma kalitesini seçer. |

## Sıkça Sorulan Sorular

**S:** Aspose.3D farklı 3d dosya formatlarıyla uyumlu mu?  
**C:** Evet, Aspose.3D OBJ, FBX, STL, GLTF ve daha birçok formatı destekler, bu da **Aspose 3d export** işlem hatları için çok yönlü bir seçim yapar.

**S:** Google Draco'yu diğer programlama dillerinde sıkıştırma için kullanabilir miyim?  
**C:** Kesinlikle. Draco, C++, Python ve JavaScript için yerel kütüphaneler sunar. Bu öğretici Java'ya odaklanır, ancak kavramlar diller arasında geçerlidir.

**S:** Ek Aspose.3D belgelerini nerede bulabilirim?  
**C:** Tam API referansları ve daha fazla örnek için **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** adresini ziyaret edin.

**S:** Aspose.3D için geçici bir lisans nasıl alabilirim?  
**C:** **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)** adresindeki geçici lisans seçeneklerini inceleyin.

**S:** Aspose.3D desteği için bir topluluk forumu var mı?  
**C:** Evet, **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)** adresindeki tartışmaya katılın.

## Sonuç

Bu rehberde, Java'da bir küre ağı oluşturarak ve ardından Google Draco'yu Aspose.3D aracılığıyla kullanarak **3d model boyutunu** nasıl azaltacağınızı gösterdik. Bu kısa adımları izleyerek ağ dosyalarını dramatik şekilde küçültebilir, yükleme sürelerini iyileştirebilir ve Java‑tabanlı 3d uygulamalarınızı yanıt verir ve bant genişliği dostu tutabilirsiniz.

---

**Son Güncelleme:** 2026-11-17  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose

## İlgili öğreticiler

- [3D Dosya Boyutunu Azalt – Aspose.3D for Java ile Sahneleri Sıkıştır](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Aspose.3D for Java kullanarak kürelerden Draco nokta bulutu oluştur](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Aspose.3D kullanarak Java'da Optimize Edilmiş Render için Ağları Üçgenleştirmeyi Öğren](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}