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

## Introduction

Welcome to this comprehensive tutorial that shows **satıcı ekleme** details to a 3D scene and then **FBX kaydetme** files with Aspose.3D for .NET. Whether you’re building architectural visualizations, game assets, or engineering models, embedding vendor and application metadata makes your scenes more informative and easier to manage downstream. Let’s walk through the process step by step.

## Quick Answers
- **“add vendor” ne anlama geliyor?** Uygulama ve satıcı adlarını sahnenin AssetInfo bloğunda saklar.  
- **Hangi format satıcı bilgilerini destekler?** FBX (ASCII veya binary) kaydedildiğinde meta verileri korur.  
- **FBX nasıl kaydedilir?** `scene.Save(path, FileFormat.FBX7500ASCII)` veya ikili eşdeğerini kullanın.  
- **Lisans gerekli mi?** Geliştirme için ücretsiz deneme sürümü çalışır; üretim için ticari lisans gereklidir.  
- **Ölçüm birimlerini değiştirebilir miyim?** Evet, `AssetInfo.UnitName` ve `AssetInfo.UnitScaleFactor` değerlerini ayarlayın.

## “how to add vendor” bir 3D sahnede nedir?
Satıcı bilgisi eklemek, bir `Scene` nesnesinin `AssetInfo` özelliklerini doldurmak anlamına gelir. Bu özellikler dosyayla birlikte taşınır ve FBX dosyasını kullanan herkesin hangi uygulama tarafından oluşturulduğunu ve satıcının kim olduğunu görmesini sağlar.

## Neden satıcı bilgisi eklenir?
- **İzlenebilirlik:** Büyük hatlarda bir modelin kaynağını hızlıca belirleyin.  
- **Uyumluluk:** Bazı sektörler varlık yönetimi için açık satıcı etiketlemesi gerektirir.  
- **Otomasyon:** Betikler, satıcı meta verilerine göre dosyaları filtreleyebilir veya işleyebilir.

## Prerequisites

- Aspose.3D for .NET yüklü. [Aspose.3D for .NET sayfasından](https://releases.aspose.com/3d/net/) indirebilirsiniz.

## Import Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## How to Add Vendor Information

### Step 1: Initialize a 3D Scene

```csharp
Scene scene = new Scene();
```

Yeni bir `Scene` oluşturmak, üzerinde çalışabileceğiniz temiz bir tuval sağlar.

### Step 2: Set Application and Vendor Information

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Burada, `ApplicationName` ve `ApplicationVendor` alanlarına anlamlı dizeler atayarak **satıcı ekleme** verisini nasıl ekleyeceğimizi gösteriyoruz.

### Step 3: Define Measurement Units

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Birim sistemini belirtmek, FBX dosyasını açan herkesin boyutları doğru yorumlamasını sağlar. Bu örnekte, bir “pole” 60 cm’ye eşittir.

## How to Save FBX Scene

### Step 4: Save the Scene (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Bu satır, FBX 7.5.0’ın ASCII sürümünü kullanarak **fbx kaydetme** yöntemini gösterir. Binary tercih ederseniz, `FBX7500ASCII` yerine `FBX7500Binary` kullanın.

> **Pro ipucu:** Seçtiğiniz formatla uyumlu olacak şekilde dosya uzantısı `.fbx`'i tutarlı kullanın; aksi takdirde bazı görüntüleyiciler içeriği yanlış yorumlayabilir.

### Step 5: Display Success Message

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Dostça bir konsol mesajı, satıcı meta verileriyle tamamlanmış sahnenin diske yazıldığını doğrular.

## Common Issues and Solutions

| Sorun | Çözüm |
|-------|----------|
| **Görünümde satıcı bilgisi görünmüyor** | Dosyayı **FBX ASCII** veya **Binary** olarak kaydettiğinizden emin olun; bazı eski görüntüleyiciler yalnızca bir formatı okur. |
| **Yol boşluk içeriyor** | Yolu çift tırnak içine alın veya güvenli bir dosya yolu oluşturmak için `Path.Combine` kullanın. |
| **Birim ölçeği yanlış görünüyor** | `UnitScaleFactor`'ı iki kez kontrol edin; bu, metreye göre bir çarpandır. |
| **Lisans istisnası** | Test için ücretsiz deneme sürümünü kullanın; üretim sürümleri için tam lisans edinin. |

## Frequently Asked Questions

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