---
date: 2026-05-04
description: Aspose.3D for Java kullanarak sahneyi FBX formatına nasıl dışa aktaracağınızı
  ve uygulama adını java olarak nasıl ayarlayacağınızı öğrenin. Bu adım adım kılavuz,
  ölçü birimlerini nasıl tanımlayacağınızı ve 3D sahne bilgilerini nasıl alacağınızı
  da gösterir.
keywords:
- export scene to fbx
- set application name java
- aspose 3d java
linktitle: Java'da FBX Nasıl Kaydedilir ve 3D Sahne Bilgileri Nasıl Alınır
second_title: Aspose.3D Java API
title: Sahneyi FBX'e Aktarmak ve Java'da 3D Sahne Bilgilerini Almak
url: /tr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da Sahneyi FBX Olarak Dışa Aktarma ve 3D Sahne Bilgilerini Alma

## Giriş

Eğer 3D sahnelerinizden faydalı meta verileri çıkarırken **how to export scene to FBX** konusunda net, uygulamalı bir rehber arıyorsanız, doğru yerdesiniz. Bu öğreticide, **Aspose.3D Java** kütüphanesini kullanarak her adımı adım adım göstereceğiz: bir sahne oluşturmak, **setting the application name**, **defining measurement units**, ve sonunda **exporting the scene to FBX**. Sonunda, sonraki işlem hatları için ihtiyaç duyduğunuz varlık bilgilerini taşıyan, kullanıma hazır bir FBX dosyanız olacak.

## Hızlı Yanıtlar
- **What is the primary goal?** Özel varlık bilgileri içeren bir sahneyi FBX olarak dışa aktar.
- **Which library is used?** Aspose.3D for Java.
- **Do I need a license?** Geliştirme için ücretsiz deneme sürümü çalışır; üretim için ticari lisans gereklidir.
- **Can I change the measurement units?** Evet – `setUnitName` ve `setUnitScaleFactor` kullanın.
- **Where is the output saved?** `scene.save(...)` içinde belirttiğiniz yola kaydedilir.

## Ön Koşullar

Başlamadan önce şunlara sahip olduğunuzdan emin olun:

- Java çekirdek sözdizimi konusunda sağlam bir anlayış.  
- **Aspose.3D for Java** indirilmiş ve projenize eklenmiş (resmi siteden alabilirsiniz) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Sevdiğiniz Java IDE'si (IntelliJ IDEA, Eclipse, NetBeans, vb.) düzgün bir şekilde yapılandırılmış.

## Paketleri İçe Aktarma

Java kaynak dosyanızda, sahne işleme ve dosya formatı desteği sağlayan Aspose.3D sınıflarını içe aktarın.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Gereksiz bağımlılıkları önlemek ve derleme sürelerini iyileştirmek için import listesini minimal tutun.

## FBX dosyasını kaydetme süreci nedir?

Aşağıda, bir sahneye **asset information** eklemeyi ve ardından **scene to FBX** dışa aktarmayı gösteren kısa, adım adım bir rehber bulunmaktadır.

### Adım 1: 3D Sahneyi Başlatma

İlk olarak, boş bir `Scene` nesnesi oluşturun. Bu, tüm geometri, ışıklar, kameralar ve varlık meta verileri için bir kapsayıcı olacaktır.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Java'da uygulama adını nasıl ayarlarsınız

Özel meta veriler eklemek, sonraki araçların dosyanın kaynağını tanımlamasına yardımcı olur. Dosyayı kaydetmeden önce `AssetInfo` nesnesini kullanarak **set the application name** (ve satıcı) ayarlayın.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Neden önemli:** Birçok işlem hattı, varlıkları kaynak uygulamaya göre filtreler veya etiketler; bu adım büyük projeler için vazgeçilmezdir.

### Adım 3: Ölçüm Birimlerini Tanımlama

Aspose.3D, sahnenizin kullandığı birim sistemini belirtmenize olanak tanır. Bu örnekte, özel bir ölçek faktörüyle “pole” adlı antik Mısır birimini kullanıyoruz.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **İpucu:** Modellerinizin gerçek dünya boyutuna uyması için `unitScaleFactor` değerini ayarlayın; 1.0, seçilen birimle 1‑bir‑1 eşleşmeyi temsil eder.

### Adım 4: Sahneyi FBX Olarak Dışa Aktarma

Artık varlık bilgileri eklendiğine göre, sahneyi bir FBX dosyası olarak kaydediyoruz. `FileFormat.FBX7500ASCII` seçeneği, hata ayıklama için kullanışlı olan insan tarafından okunabilir bir ASCII FBX üretir.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Unutmayın:** `"Your Document Directory"` ifadesini mutlak bir yol ya da projenizin çalışma dizinine göre bir yol ile değiştirin.

### Adım 5: Başarı Mesajını Yazdırma

Basit bir konsol çıktısı, işlemin başarılı olduğunu doğrular ve dosyanın nereye yazıldığını bildirir.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Neden Aspose.3D ile sahneyi FBX Olarak Dışa Aktarırsınız?

FBX'e dışa aktarmak yaygın bir gereksinimdir çünkü FBX, oyun motorları, DCC araçları ve AR/VR işlem hatları tarafından geniş çapta desteklenir. Aspose.3D, ağır bir 3D oluşturma uygulamasına ihtiyaç duymadan dışa aktarılan dosya üzerinde—meta veri, birimler ve geometri—tam kontrol sağlar. Bu, otomatik varlık üretimini, toplu işleme ve sunucu‑tarafı dönüşümleri hızlı ve güvenilir kılar.

## Yaygın Kullanım Durumları

- **Game asset pipelines** – sürüm takibi için yaratıcı bilgilerini doğrudan FBX dosyalarına gömün.  
- **Architectural visualization** – render motorlarına aktarırken ölçekleme hatalarını önlemek için proje‑özel birimleri saklayın.  
- **Automated reporting** – sonraki analiz araçlarının okuyabileceği meta verilerle anlık FBX dosyaları oluşturun.  
- **Cloud‑based 3D services** – GUI olmadan programatik olarak sahneler oluşturup dışa aktarın, SaaS platformları için mükemmeldir.

## Sorun Giderme ve İpuçları

| Sorun | Çözüm |
|-------|----------|
| **Dosya kaydedildikten sonra bulunamadı** | `MyDir`'in mevcut bir klasöre işaret ettiğini ve uygulamanızın yazma izinlerine sahip olduğunu doğrulayın. |
| **Birimler dış görüntüleyicide yanlış görünüyor** | `unitScaleFactor`'ı iki kez kontrol edin; bazı görüntüleyiciler temel birim olarak metre bekler. |
| **Varlık meta verileri eksik** | `scene.getAssetInfo()` metodunu kaydetmeden **önce** çağırdığınızdan emin olun; `save()` sonrası yapılan değişiklikler kalıcı olmaz. |
| **Büyük sahnelerde performans darboğazı** | Bellek kullanımını azaltmak için kaydetmeden önce `scene.optimize()` kullanın. |
| **ASCII FBX çok büyük** | `FileFormat.FBX7500` kullanarak ikili FBX'e geçin (SSS'ye bakın). |

## Sıkça Sorulan Sorular

**Q: Çıktı formatını ikili FBX'e nasıl değiştiririm?**  
A: `scene.save(...)` çağırırken `FileFormat.FBX7500ASCII` yerine `FileFormat.FBX7500` kullanın.

**Q: Yerleşik varlık alanlarının ötesinde özel kullanıcı tanımlı meta veri ekleyebilir miyim?**  
A: Evet, ek anahtar‑değer çiftleri eklemek için `scene.getUserData().add("Key", "Value")` kullanın.

**Q: Aspose.3D, OBJ veya GLTF gibi diğer dışa aktarma formatlarını destekliyor mu?**  
A: Evet. Gerektiğinde `FileFormat` enumunu `OBJ` veya `GLTF2` olarak değiştirmeniz yeterlidir.

**Q: Hangi Java sürümü gereklidir?**  
A: Aspose.3D for Java, Java 8 ve üzerini destekler.

**Q: Mevcut bir FBX dosyasını yükleyip, varlık bilgilerini değiştirip tekrar kaydetmek mümkün mü?**  
A: Kesinlikle. Dosyayı `new Scene("input.fbx")` ile yükleyin, `scene.getAssetInfo()`'ı değiştirin, ardından kaydedin.

## Sonuç

Artık **exporting a scene to FBX** sırasında uygulama adı, satıcı ve özel ölçüm birimleri gibi değerli varlık bilgilerini gömerek eksiksiz, üretim‑hazır bir iş akışına sahipsiniz. Bu yaklaşım varlık yönetimini kolaylaştırır, manuel kayıt tutmayı azaltır ve sonraki araçların ihtiyaç duyduğu tüm bağlamı almasını sağlar. Diğer dışa aktarma formatlarını keşfetmek, özel kullanıcı verileri eklemek veya bu kodu daha büyük otomasyon işlem hatlarına entegre etmekten çekinmeyin.

---

**Son Güncelleme:** 2026-05-04  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}