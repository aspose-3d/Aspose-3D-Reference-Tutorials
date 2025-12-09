---
date: 2025-12-06
description: Aspose.3D for Java kullanarak FBX dosyalarını nasıl kaydedeceğinizi ve
  sahne bilgilerini nasıl alacağınızı öğrenin. Bu adım adım kılavuz, uygulama adını
  ayarlamayı, ölçü birimlerini tanımlamayı ve sahneyi FBX olarak dışa aktarmayı kapsar.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Java'da FBX Nasıl Kaydedilir ve 3D Sahne Bilgileri Nasıl Alınır
url: /tr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# FBX Nasıl Kaydedilir ve Java'da 3D Sahne Bilgileri Nasıl Alınır

## Giriş

Eğer 3D sahnelerinizden yararlı meta verileri çıkartırken **fbx dosyalarını nasıl kaydedeceğinize** dair net, uygulamalı bir rehber arıyorsanız, doğru yerdesiniz. Bu öğreticide **Aspose.3D Java** kütüphanesini kullanarak her adımı adım adım göstereceğiz: bir sahne oluşturma, **uygulama adını ayarlama**, **ölçüm birimlerini tanımlama**, ve nihayet **sahneyi FBX olarak dışa aktarma**. Sonunda, aşağı akış boru hatları için ihtiyaç duyduğunuz varlık bilgilerini taşıyan kullanıma hazır bir FBX dosyanız olacak.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Özel varlık bilgileri içeren bir FBX dosyası kaydetmek.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java.  
- **Lisans gerekli mi?** Geliştirme için ücretsiz deneme sürümü çalışır; üretim için ticari lisans gereklidir.  
- **Ölçüm birimlerini değiştirebilir miyim?** Evet – `setUnitName` ve `setUnitScaleFactor` kullanın.  
- **Çıktı nerede kaydedilir?** `scene.save(...)` içinde belirttiğiniz yola.

## Ön Koşullar

Başlamadan önce, şunların olduğundan emin olun:

- Java çekirdek sözdizimi hakkında sağlam bir anlayış.  
- **Aspose.3D for Java**'ı indirin ve projenize ekleyin (resmi [Aspose 3D indirme sayfasından](https://releases.aspose.com/3d/java/) alabilirsiniz).  
- Favori Java IDE'niz (IntelliJ IDEA, Eclipse, NetBeans vb.) düzgün şekilde yapılandırılmış.

## Paketleri İçe Aktarma

Java kaynak dosyanızda, sahne işleme ve dosya formatı desteği sağlayan Aspose.3D sınıflarını içe aktarın.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro ipucu:** Gereksiz bağımlılıkları önlemek ve derleme sürelerini iyileştirmek için içe aktarma listesini minimumda tutun.

## FBX dosyası kaydetme süreci nedir?

Aşağıda, bir sahneye **varlık bilgisi ekleme** ve ardından **sahneyi FBX olarak dışa aktarma** adımlarını gösteren özlü, adım adım bir rehber bulunmaktadır.

### Adım 1: 3D Sahneyi Başlatma

İlk olarak, boş bir `Scene` nesnesi oluşturun. Bu, tüm geometri, ışıklar, kameralar ve varlık meta verileri için bir kapsayıcı olacaktır.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Adım 2: Uygulama ve Satıcı Bilgilerini Ayarlama

Özel meta veri eklemek, aşağı akış araçlarının dosyanın kaynağını tanımlamasına yardımcı olur. Burada `AssetInfo` nesnesi kullanarak **uygulama adını** ve satıcıyı ayarlıyoruz.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Neden önemli?** Birçok boru hattı, varlıkları kaynak uygulamaya göre filtreler veya etiketler; bu adım büyük projeler için hayati öneme sahiptir.

### Adım 3: Ölçüm Birimlerini Tanımlama

Aspose.3D, sahnenizin kullandığı birim sistemini belirtmenizi sağlar. Bu örnekte, özel bir ölçek faktörüyle “pole” adlı antik Mısır birimini kullanıyoruz.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **İpucu:** Modellerinizin gerçek dünya boyutuna uyması için `unitScaleFactor`'ı ayarlayın; 1.0, seçilen birimle 1‑bir‑1 eşleşmeyi temsil eder.

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

Basit bir konsol çıktısı, işlemin başarılı olduğunu onaylar ve dosyanın nereye yazıldığını size bildirir.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Ortak Kullanım Senaryoları

- **Oyun varlık boru hatları** – sürüm takibi için yaratıcı bilgilerini doğrudan FBX dosyalarına gömün.  
- **Mimari görselleştirme** – render motorlarına aktarırken ölçekleme hatalarını önlemek için proje‑özel birimleri depolayın.  
- **Otomatik raporlama** – aşağı akış analiz araçlarının okuyabileceği meta verilerle anlık FBX dosyaları oluşturun.

## Sorun Giderme ve İpuçları

| Sorun | Çözüm |
|-------|----------|
| **Kaydetme sonrası dosya bulunamadı** | `MyDir`'in mevcut bir klasöre işaret ettiğini ve uygulamanızın yazma izinlerine sahip olduğunu doğrulayın. |
| **Birimler dış görüntüleyicide yanlış görünüyor** | `unitScaleFactor`'ı iki kez kontrol edin; bazı görüntüleyiciler temel birim olarak metre bekler. |
| **Varlık meta verileri eksik** | `scene.getAssetInfo()` metodunu kaydetmeden **önce** çağırdığınızdan emin olun; `save()` sonrası yapılan değişiklikler kalıcı olmaz. |

## SSS

### Q1: Aspose.3D tüm Java IDE'leriyle uyumlu mu?
A1: Evet, Aspose.3D tüm büyük Java IDE'leriyle sorunsuz çalışacak şekilde tasarlanmıştır.

### Q2: Aspose.3D'yi ticari projelerde kullanabilir miyim?
A2: Kesinlikle. Aspose.3D, geliştiriciler için ticari lisanslar sunar ve lisans gereksinimlerine uymanızı sağlar.

### Q3: Aspose.3D için ek destek nereden bulunabilir?
A3: Herhangi bir soru veya yardım için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### Q4: Aspose.3D için ücretsiz deneme sürümü mevcut mu?
A4: Evet, özellikleri ücretsiz deneme sürümüyle [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

### Q5: Aspose.3D için geçici bir lisans nasıl alınır?
A5: Test amaçlı geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Sıkça Sorulan Sorular

**S: Çıktı formatını ikili FBX'e nasıl değiştiririm?**  
C: `scene.save(...)` çağırırken `FileFormat.FBX7500ASCII` yerine `FileFormat.FBX7500` kullanın.

**S: Yerleşik varlık alanlarının ötesinde özel kullanıcı tanımlı meta veri ekleyebilir miyim?**  
C: Evet, ek anahtar‑değer çiftlerini gömmek için `scene.getUserData().add("Key", "Value")` kullanın.

**S: Aspose.3D, OBJ veya GLTF gibi diğer dışa aktarma formatlarını destekliyor mu?**  
C: Evet. Gerektiğinde `FileFormat` enumunu `OBJ` veya `GLTF2` olarak değiştirmeniz yeterlidir.

**S: Hangi Java sürümü gereklidir?**  
C: Aspose.3D for Java, Java 8 ve üzerini destekler.

**S: Mevcut bir FBX dosyasını yükleyip varlık bilgilerini değiştirip tekrar kaydetmek mümkün mü?**  
C: Kesinlikle. Dosyayı `new Scene("input.fbx")` ile yükleyin, `scene.getAssetInfo()`'ı değiştirin ve ardından kaydedin.

---

**Son Güncelleme:** 2025-12-06  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}