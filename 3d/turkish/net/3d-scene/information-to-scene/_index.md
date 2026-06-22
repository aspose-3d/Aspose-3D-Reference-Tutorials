---
date: 2026-03-26
description: Aspose.3D for .NET kullanarak bir 3D sahneye satıcı bilgisi eklemeyi
  ve FBX dosyalarını kaydetmeyi öğrenin. Hazır çalışan kodlarla adım adım bu kılavuzu
  izleyin.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Aspose.3D Kullanarak Satıcı Bilgisi Ekleme ve FBX Sahnesini Kaydetme
url: /tr/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D Kullanarak Satıcı Bilgilerini Ekleme ve FBX Sahnesini Kaydetme

## Giriiş

Aspose.3D for .NET ile 3D sahneye **satıcı ekleme** ayrıntılarını ve ardından **FBX kaydetme** dosyalarını gösteren bu kapsamlı eğitime hoş geldiniz. İster mimari görselleştirmeler, oyun varlıkları veya mühendislik modelleri oluşturuyor olun, satıcı ve uygulama meta verilerini gömmek, sahnelerinizi daha bilgilendirici ve daha kolay yönetilebilir hale getirir. Süreci adım adım inceleyelim.

## Hızlı Yanıtlar
- **“satıcı ekle” ne anlıyor musunuz?**Uygulama ve satıcı reklamlarını AssetInfo'nun bozulmasında saklar.
- **Hangi formatı satıcının saklanması?**FBX (ASCII veya ikili) kaydedildiğinde meta verileri korur.
- **FBX nasıl sınıflandırılır?**`scene.Save(path, FileFormat.FBX7500ASCII)` veya ikili takaslarını kullanın.
- **Lisans gerekli mi?**Geliştirme için ücretsiz deneme sürümü çalışır; üretim için ticari lisans gereklidir.
- **Ölçüm birimlerini etkileyebilir mi?**Evet, `AssetInfo.UnitName` ve `AssetInfo.UnitScaleFactor` parametrelerini ayarlar.

## “satıcı nasıl eklenir” bir 3D sahnede nedir?
Satıcı bilgilerini öğrenir, bir `Scene` nesnesinin `AssetInfo` özelliklerini doldurmayı belirtir gelir. Bu özellikler dosyayla birlikte taşınması ve FBX'i kullanan herkesin hangi uygulama tarafından kapsandığını ve satıcının kimin görmesini sağlar.

## Neden satıcı bilgisi geliştirilsin?
- **İzlenebilirlik:** Büyük hatlarda bir modelin hızlı bir şekilde belirleyin.
- **Uyumluluk:** Bazı sektörler varlık yönetimi için açık satıcı pazarlaması gerektirir.
- **Otomasyon:** Betikler, satıcı meta sistemlerine göre dosyaları filtreleyebilir veya işleyebilir.

## Önkoşullar

- Aspose.3D for .NET Yüklü. [Aspose.3D for .NET sayfasından](https://releases.aspose.com/3d/net/) indirebilirsiniz.

## Ad Alanlarını İçe Aktar

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Tedarikçi Bilgilerini Ekleme

### Adım 1: 3B Sahneyi Başlatma

```csharp
Scene scene = new Scene();
```

Yeni bir `Scene` oluşturmak, üzerinde çalışabileceğiniz temiz bir tuval sağlar.

### Adım 2: Uygulama ve Tedarikçi Bilgilerini Ayarlama

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Burada, `ApplicationName` ve `ApplicationVendor` alanlarına anlamlı dizeler atayarak **satıcı ekleme** verisini nasıl ekleyeceğimizi gösteriyoruz.

### Adım 3: Ölçü Birimlerini Tanımlama

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Birim sistemini belirtmek, FBX dosyasını açan herkesin boyutları doğru yorumlamasını sağlar. Bu örnekte, bir “pole” 60 cm’ye eşittir.

## FBX Sahnesini Kaydetme

### Adım 4: Sahneyi Kaydetme (fbx nasıl kaydedilir)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Bu satır, FBX 7.5.0’ın ASCII sürümünü kullanarak **fbx kaydetme** yöntemini gösterir. Binary tercih ederseniz, `FBX7500ASCII` yerine `FBX7500Binary` kullanın.

> **Pro ipucu:** Seçtiğiniz formatla uyumlu olacak şekilde dosya uzantısı `.fbx`'i tutarlı kullanın; aksi takdirde bazı görüntüleyiciler içeriği yanlış yorumlayabilir.

### Adım 5: Başarı Mesajını Görüntüleme

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Dostça bir konsol mesajı, satıcı meta verileriyle tamamlanmış sahnenin diske yazıldığını doğrular.

## Yaygın Sorunlar ve Çözümler

| Sorun | Çözüm |
|----------|----------|
| **Görünümde satıcı bilgisi görünmüyor** | Dosyayı **FBX ASCII** veya **Binary** olarak kaydettiğinizden emin olun; bazı eski görüntüleyiciler yalnızca bir format okur. |
| **Yolun içerdiği** | Yolu çift tırnak içerisine alın veya güvenli bir dosya yolu oluşturmak için `Path.Combine` kullanın. |
| **Birim görünümü yanlış görünüyor** | `UnitScaleFactor`ı iki kez kontrol edin; bu, metreye göre bir çarpandır. |
| **Lisans istisnası** | Test için ücretsiz deneme yazılımı kullanın; üretim ürünü için tam lisans gerektirir. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for .NET'ı diğer programlama dilleriyle kullanabilir miyim?**  
C: Aspose.3D öncelikle .NET dillerini destekler, ancak diğer diller için birlikte çalışabilirlik seçeneklerini keşfedebilirsiniz.

**S: Aspose.3D for .NET için ücretsiz bir deneme sürümü mevcut mu?**  
C: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişebilirsiniz.

**S: Aspose.3D‑ile ilgili sorular için nasıl destek alabilirim?**  
C: Topluluk ve destek için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Aspose.3D for .NET için geçici bir lisans satın alabilir miyim?**  
C: Evet, geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

**S: Aspose.3D for .NET için ayrıntılı belgeleri nerede bulabilirim?**  
C: Derinlemesine bilgi için [belgelere](https://reference.aspose.com/3d/net/) bakın.

---

**Son Güncelleme:** 2026-03-26  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}