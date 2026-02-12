---
date: 2026-02-12
description: Aspose.3D for Java kullanarak sahneyi FBX formatına nasıl dışa aktaracağınızı
  ve 3D sahne bilgilerini nasıl alacağınızı öğrenin. Bu adım adım kılavuz, uygulama
  adını ayarlamayı, ölçü birimlerini tanımlamayı ve sahneyi FBX’e dışa aktarmayı kapsar.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Sahneyi FBX'e Aktarmak ve Java'da 3D Sahne Bilgilerini Almak
url: /tr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahneyi FBX Olarak Dışa Aktarma ve Java’da 3D Sahne Bilgilerini Alma

## Giriş

**Sahneyi FBX olarak nasıl dışa aktaracağınızı** ve 3D sahnelerinizden faydalı meta verileri nasıl çıkaracağınızı gösteren net, uygulamalı bir kılavuz arıyorsanız doğru yerdesiniz. Bu öğreticide **Aspose.3D Java** kütüphanesini kullanarak her adımı adım adım inceleyeceğiz: bir sahne oluşturma, **uygulama adını ayarlama**, **ölçüm birimlerini tanımlama** ve nihayet **sahneyi FBX olarak dışa aktarma**. Sonunda, aşağı akış hatları için gereken varlık bilgilerini taşıyan kullanıma hazır bir FBX dosyanız olacak.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Özel varlık bilgileri içeren bir sahneyi FBX olarak dışa aktarmak.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java.  
- **Lisans gerekli mi?** Geliştirme için ücretsiz deneme yeterli; üretim için ticari lisans gerekir.  
- **Ölçüm birimlerini değiştirebilir miyim?** Evet – `setUnitName` ve `setUnitScaleFactor` kullanın.  
- **Çıktı nereye kaydedilir?** `scene.save(...)` içinde belirttiğiniz yola.

## Önkoşullar

Başlamadan önce şunlara sahip olun:

- Temel Java sözdizimini iyi derecede bilmek.  
- **Aspose.3D for Java** indirilmiş ve projenize eklenmiş olmalı (resmi) [Aspose 3D indirme sayfası](https://releases.aspose.com/3d/java/).  
- Sevdiğiniz Java IDE (IntelliJ IDEA, Eclipse, NetBeans vb.) düzgün şekilde yapılandırılmış olmalı.

## Paketleri İçe Aktarma

Java kaynak dosyanızda sahne işleme ve dosya formatı desteği sağlayan Aspose.3D sınıflarını içe aktarın.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro ipucu:** Gereksiz bağımlılıkları önlemek ve derleme süresini iyileştirmek için import listesini minimumda tutun.

## FBX dosyası kaydetme süreci nedir?

Aşağıda, **varlık bilgilerini** sahneye ekleyip ardından **sahneyi FBX olarak dışa aktarmayı** gösteren kısa ve adım adım bir rehber bulacaksınız.

### Adım 1: 3D Sahneyi Başlatma

İlk olarak boş bir `Scene` nesnesi oluşturun. Bu nesne tüm geometri, ışık, kamera ve varlık meta verileri için kapsayıcı görevi görecek.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Adım 2: Uygulama ve Satıcı Bilgilerini Ayarlama

Özel meta veriler eklemek, aşağı akış araçlarının dosyanın kaynağını tanımlamasına yardımcı olur. Burada `AssetInfo` nesnesiyle **uygulama adını** ve satıcıyı ayarlıyoruz.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Neden önemli?** Birçok pipeline, varlıkları kaynak uygulamaya göre filtreler veya etiketler; bu adım büyük projeler için hayati öneme sahiptir.

### Adım 3: Ölçüm Birimlerini Tanımlama

Aspose.3D, sahnenizin kullandığı birim sistemini belirtmenize izin verir. Bu örnekte “pole” adı verilen antik Mısır birimini özel bir ölçek faktörüyle kullanıyoruz.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **İpucu:** `unitScaleFactor` değerini modellerinizin gerçek dünya boyutuna göre ayarlayın; 1.0, seçilen birimle bire bir eşleşmeyi temsil eder.

### Adım 4: Sahneyi FBX Olarak Dışa Aktarma

Varlık bilgileri eklendikten sonra sahneyi bir FBX dosyası olarak kaydediyoruz. `FileFormat.FBX7500ASCII` seçeneği, hata ayıklama için kullanışlı olan insan tarafından okunabilir bir ASCII FBX üretir.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Unutmayın:** `"Your Document Directory"` ifadesini mutlak bir yol ya da projenizin çalışma dizinine göre göreceli bir yol ile değiştirin.

### Adım 5: Başarı Mesajını Yazdırma

Basit bir konsol çıktısı, işlemin başarılı olduğunu ve dosyanın nereye yazıldığını onaylar.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Aspose.3D ile sahneyi FBX olarak dışa aktarmanın avantajları

FBX dışa aktarma yaygın bir gereksinimdir çünkü FBX, oyun motorları, DCC araçları ve AR/VR pipeline’ları tarafından geniş çapta desteklenir. Aspose.3D, dışa aktarılan dosya üzerinde—meta veri, birimler ve geometri—tam kontrol sağlar; ağır bir 3D modelleme uygulamasına ihtiyaç duymaz. Bu da otomatik varlık üretimi, toplu işleme ve sunucu‑tarafı dönüşümleri hızlı ve güvenilir kılar.

## Yaygın Kullanım Senaryoları

- **Oyun varlık pipeline’ları** – FBX dosyalarına doğrudan yaratıcı bilgisi ekleyerek sürüm takibi yapın.  
- **Mimari görselleştirme** – Projeye özgü birimleri saklayarak render motorlarına aktarırken ölçek hatalarını önleyin.  
- **Otomatik raporlama** – Aşağı akış analiz araçlarının okuyabileceği meta verilerle anlık FBX dosyaları üretin.  
- **Bulut‑tabanlı 3D hizmetleri** – GUI olmadan programatik olarak sahneler oluşturup dışa aktarın; SaaS platformları için ideal.

## Sorun Giderme ve İpuçları

| Sorun | Çözüm |
|-------|----------|
| **Kaydetme sonrası dosya bulunamıyor** | `MyDir`'in mevcut bir klasöre işaret ettiğini ve uygulamanızın yazma iznine sahip olduğunu doğrulayın. |
| **Birmler dış araçta yanlış görünüyor** | `unitScaleFactor` değerini tekrar kontrol edin; bazı görüntüleyiciler temel birim olarak metre bekler. |
| **Varlık meta verileri eksik** | `scene.save(...)` **öncesinde** `scene.getAssetInfo()` çağrısını yaptığınızdan emin olun; `save()` sonrası yapılan değişiklikler kaydedilmez. |
| **Büyük sahnelerde performans darboğazı** | Kaydetmeden önce `scene.optimize()` kullanarak bellek kullanımını azaltın. |
| **ASCII FBX çok büyük** | `FileFormat.FBX7500` kullanarak ikili FBX’e geçin (SSS’ye bakın). |

## SSS

### S1: Aspose.3D tüm Java IDE’leriyle uyumlu mu?

C1: Evet, Aspose.3D tüm büyük Java IDE’leriyle sorunsuz çalışacak şekilde tasarlanmıştır.

### S2: Aspose.3D’yi ticari projelerde kullanabilir miyim?

C2: Kesinlikle. Aspose.3D, geliştiriciler için ticari lisanslar sunar ve lisans gereksinimlerine uyum sağlamanızı garanti eder.

### S3: Aspose.3D için ek destek nereden bulunur?

C3: Her türlü soru ve yardım için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S4: Aspose.3D için ücretsiz deneme mevcut mu?

C4: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

### S5: Aspose.3D için geçici bir lisans nasıl alınır?

C5: Test amaçlı geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Sık Sorulan Sorular

**S: Çıktı formatını ikili FBX’e nasıl değiştiririm?**  
C: `scene.save(...)` çağrısında `FileFormat.FBX7500ASCII` yerine `FileFormat.FBX7500` kullanın.

**S: Yerleşik varlık alanlarının ötesinde özel kullanıcı tanımlı meta veri ekleyebilir miyim?**  
C: Evet, ek anahtar‑değer çiftleri eklemek için `scene.getUserData().add("Key", "Value")` kullanın.

**S: Aspose.3D OBJ veya GLTF gibi diğer dışa aktarma formatlarını destekliyor mu?**  
C: Destekler. `FileFormat` enum’ını ihtiyacınıza göre `OBJ` veya `GLTF2` olarak değiştirin.

**S: Hangi Java sürümü gereklidir?**  
C: Aspose.3D for Java, Java 8 ve üzeri sürümleri destekler.

**S: Mevcut bir FBX dosyasını yükleyip varlık bilgilerini değiştirip tekrar kaydedebilir miyim?**  
C: Kesinlikle. `new Scene("input.fbx")` ile dosyayı yükleyin, `scene.getAssetInfo()` üzerinden değişiklik yapın, ardından kaydedin.

## Sonuç

Artık **sahneyi FBX olarak dışa aktarırken** uygulama adı, satıcı ve özel ölçüm birimleri gibi değerli varlık bilgilerini gömmenizi sağlayan eksiksiz, üretim‑hazır bir iş akışına sahipsiniz. Bu yaklaşım varlık yönetimini kolaylaştırır, manuel kayıt tutmayı azaltır ve aşağı akış araçların ihtiyaç duyduğu tüm bağlamı almasını sağlar. Diğer dışa aktarma formatlarını keşfetmek, özel kullanıcı verileri eklemek veya bu kodu daha büyük otomasyon pipeline’larına entegre etmekten çekinmeyin.

---

**Son Güncelleme:** 2026-02-12  
**Test Edilen Sürümler:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}