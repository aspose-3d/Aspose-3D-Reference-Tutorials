---
date: 2026-09-08
description: Aspose.3D kullanarak Java'da birimleri tanımlamayı ve bir sahneyi FBX
  olarak dışa aktarmayı öğrenin. Bu adım adım kılavuz, uygulama adının ayarlanması,
  ölçüm birimlerinin belirlenmesi ve 3D sahne bilgilerinin alınmasını gösterir.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Java'da FBX Kaydetme ve 3D Sahne Bilgilerini Alma
og_description: Aspose.3D ile Java'da birimleri tanımlamayı ve bir sahneyi FBX olarak
  dışa aktarmayı öğrenin. Kılavuz, uygulama adının ayarlanması, ölçüm birimlerinin
  belirlenmesi ve birkaç adımda 3D sahne bilgilerinin alınmasını kapsar.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Java'da birimleri tanımlama ve sahneyi FBX olarak dışa aktarma
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Java'da birimleri tanımlama ve sahneyi FBX olarak dışa aktarma
url: /tr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da birimleri tanımlama ve sahneyi FBX olarak dışa aktarma

## Giriş

Eğer 3D sahnelerinizden yararlı meta verileri çıkarırken **birimleri nasıl tanımlayacağınızı** ve **sahneyi FBX olarak dışa aktaracağınızı** gösteren net, uygulamalı bir rehber arıyorsanız doğru yerdesiniz. Bu öğreticide **Aspose.3D for Java** kütüphanesini kullanarak her adımı adım adım göstereceğiz: bir sahne oluşturma, **uygulama adını ayarlama**, **ölçüm birimlerini tanımlama**, ve nihayet **sahneyi FBX olarak dışa aktarma**. Sonunda, sonraki işlem hatları için ihtiyaç duyduğunuz varlık bilgilerini taşıyan kullanıma hazır bir FBX dosyanız olacak.

## Hızlı cevaplar
- **Birincil hedef nedir?** Özel varlık bilgilerini içeren bir sahneyi FBX olarak dışa aktarmak.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java.  
- **Lisans gerekli mi?** Geliştirme için ücretsiz deneme sürümü yeterlidir; üretim için ticari bir lisans gereklidir.  
- **Ölçüm birimlerini değiştirebilir miyim?** Evet – `setUnitName` ve `setUnitScaleFactor` kullanın.  
- **Çıktı nerede kaydedilir?** `scene.save(...)` içinde belirttiğiniz yola.  

## Önkoşullar

Başlamadan önce, aşağıdakilere sahip olduğunuzdan emin olun:

- Temel Java sözdizimi konusunda sağlam bir anlayış.  
- **Aspose.3D for Java** indirilmiş ve projenize eklenmiş (resmi [Aspose 3D indirme sayfasından](https://releases.aspose.com/3d/java/) alabilirsiniz).  
- Favori Java IDE'niz (IntelliJ IDEA, Eclipse, NetBeans vb.) düzgün bir şekilde yapılandırılmış.

## Paketleri içe aktar

Java kaynak dosyanızda, sahne işleme ve dosya formatı desteği sağlayan Aspose.3D sınıflarını içe aktarın.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro ipucu:** Gereksiz bağımlılıkları önlemek ve derleme sürelerini iyileştirmek için içe aktarma listesini minimumda tutun.

## FBX dosyası kaydetme süreci nedir?

Bir sahneyi FBX dosyası olarak kaydetmek için bir `Scene` oluşturur, istediğiniz varlık meta verilerini ayarlarsınız, ölçüm birimini tanımlarsınız ve ardından `scene.save(path, FileFormat.FBX7500ASCII)` çağrısını yaparsınız. Bu sıralama, geometriyi, malzemeleri ve meta verileri, sonraki araçlar tarafından incelenebilen veya içe aktarılabilen bir ASCII FBX dosyasına yazar.

### Adım 1: 3D sahneyi başlatma

`Scene` sınıfı, Aspose.3D'nin tüm geometri, ışıklar, kameralar ve meta verileri içeren bir bütün 3D sahneyi temsil eden üst‑seviye konteyneridir. İlk olarak, boş bir `Scene` nesnesi oluşturun. Bu, tüm geometri, ışıklar, kameralar ve varlık meta verileri için konteyner olacaktır.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Java'da uygulama adını nasıl ayarlarsınız

`AssetInfo` nesnesi, sahne için uygulama adı, satıcı ve sürüm gibi meta verileri depolar. Özel meta veri eklemek, sonraki araçların dosyanın kaynağını tanımlamasına yardımcı olur. Dosyayı kaydetmeden önce `AssetInfo` nesnesini kullanarak **uygulama adını** (ve satıcıyı) ayarlayın.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Neden önemli?**: Birçok işlem hattı, varlıkları kaynak uygulamaya göre filtreler veya etiketler; bu adım büyük projeler için hayati öneme sahiptir.

### Adım 3: ölçüm birimlerini tanımlama

Birim sistemi, sahnenin gerçek dünya ölçeğini belirler; Aspose.3D, birim adını ve metreye göre bir ölçek faktörünü belirtmenize izin verir. Bu örnekte, özel bir ölçek faktörüyle “pole” adlı antik Mısır birimini kullanıyoruz.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **İpucu:** Modellerinizin gerçek dünya boyutuna uyması için `unitScaleFactor` değerini ayarlayın; 1.0, seçilen birimle 1‑bir‑1 eşleşmeyi temsil eder.

### Adım 4: sahneyi FBX olarak dışa aktarma

Artık varlık bilgileri eklendiğine göre, sahneyi bir FBX dosyası olarak kaydediyoruz. `FileFormat.FBX7500ASCII` seçeneği, hata ayıklama için kullanışlı olan insan tarafından okunabilir bir ASCII FBX üretir.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Unutmayın:** `"Your Document Directory"` ifadesini mutlak bir yol ya da projenizin çalışma dizinine göre bir yol ile değiştirin.

## Neden Aspose.3D ile sahneyi FBX olarak dışa aktaralım?

Aspose.3D, **50+ giriş ve çıkış formatını** destekler ve tüm dosyayı belleğe yüklemeden çok sayfalı sahneleri işleyebilir; bu, dışa aktarılan dosya—meta veriler, birimler ve geometri—üzerinde tam kontrol sağlar ve ağır bir 3D oluşturma uygulamasına ihtiyaç duymaz. Bu, otomatik varlık üretimi, toplu işleme ve sunucu‑tarafı dönüşümleri hızlı ve güvenilir kılar.

## Ortak kullanım senaryoları

- **Oyun varlık işlem hatları** – sürüm takibi için yaratıcı bilgilerini doğrudan FBX dosyalarına gömün.  
- **Mimari görselleştirme** – render motorlarına aktarırken ölçekleme hatalarını önlemek için proje‑özel birimleri saklayın.  
- **Otomatik raporlama** – sonraki analiz araçlarının okuyabileceği meta verilerle anlık FBX dosyaları oluşturun.  
- **Bulut‑tabanlı 3D hizmetler** – bir GUI olmadan programatik olarak sahneler oluşturun ve dışa aktarın; SaaS platformları için mükemmeldir.

## Sorun giderme ve ipuçları

| Sorun | Çözüm |
|-------|----------|
| **Kaydetme sonrası dosya bulunamadı** | `MyDir`'in mevcut bir klasöre işaret ettiğini ve uygulamanızın yazma izinlerine sahip olduğunu doğrulayın. |
| **Birimler harici görüntüleyicide yanlış görünüyor** | `unitScaleFactor`'ı iki kez kontrol edin; bazı görüntüleyiciler temel birim olarak metre bekler. |
| **Varlık meta verileri eksik** | `scene.getAssetInfo()`'ı kaydetmeden **önce** çağırdığınızdan emin olun; `save()` sonrası yapılan değişiklikler kalıcı olmaz. |
| **Büyük sahnelerde performans darboğazı** | Bellek kullanımını azaltmak için kaydetmeden önce `scene.optimize()` kullanın. |
| **ASCII FBX çok büyük** | `FileFormat.FBX7500` kullanarak ikili FBX'e geçin (SSS'ye bakın). |

## Sıkça Sorulan Sorular

**S: Çıktı formatını ikili FBX'e nasıl değiştiririm?**  
C: `scene.save(...)` çağırırken `FileFormat.FBX7500ASCII` yerine `FileFormat.FBX7500` kullanın.

**S: Yerleşik varlık alanlarının ötesinde özel kullanıcı tanımlı meta veri ekleyebilir miyim?**  
C: Evet, ek anahtar‑değer çiftlerini gömmek için `scene.getUserData().add("Key", "Value")` kullanın.

**S: Aspose.3D, OBJ veya GLTF gibi diğer dışa aktarma formatlarını destekliyor mu?**  
C: Evet. Gerektiğinde `FileFormat` enum'ını `OBJ` veya `GLTF2` olarak değiştirmeniz yeterlidir.

**S: Hangi Java sürümü gereklidir?**  
C: Aspose.3D for Java, Java 8 ve üzerini destekler.

**S: Mevcut bir FBX dosyasını yükleyip varlık bilgilerini değiştirip tekrar kaydetmek mümkün mü?**  
C: Kesinlikle. Dosyayı `new Scene("input.fbx")` ile yükleyin, `scene.getAssetInfo()`'ı değiştirin ve ardından kaydedin.

---

**Son Güncelleme:** 2026-09-08  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

## İlgili Öğreticiler

- [3D Dosya Boyutunu Azalt – Aspose.3D for Java ile Sahneleri Sıkıştırma](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Java'da vector3 rengini ayarlama: Diffuse Rengini Değiştirme ve Aspose.3D kullanarak Java Sahnelerinde 3D Özellikleri Yönetme](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}