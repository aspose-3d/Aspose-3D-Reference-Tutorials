---
title: Sahne Varlıklarından Bilgi Çıkarma
linktitle: Sahne Varlıklarından Bilgi Çıkarma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D sahnelerinizi zahmetsizce geliştirin. Değerli varlık bilgilerini adım adım eklemeyi öğrenin. Dinamik bir 3D deneyimi için hemen indirin.
weight: 10
url: /tr/net/3d-scene/information-to-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sahne Varlıklarından Bilgi Çıkarma

## giriiş

Değerli bilgiler elde etmek ve 3D sahnelerinizi geliştirmek için Aspose.3D for .NET'in kullanımına ilişkin bu kapsamlı eğitime hoş geldiniz. Aspose.3D, geliştiricilerin .NET uygulamalarında 3D sahneleri sorunsuz bir şekilde işlemesine olanak tanıyan güçlü bir kütüphanedir. Bu eğitimde, bir sahneye varlık bilgisi ekleme gibi çok önemli bir göreve odaklanacağız.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

-  Aspose.3D for .NET: Kütüphanenin kurulu olduğundan emin olun. adresinden indirebilirsiniz.[Aspose.3D for .NET sayfası](https://releases.aspose.com/3d/net/).

## Ad Alanlarını İçe Aktar

.NET projenize Aspose.3D işlevlerine erişmek için gerekli ad alanlarını eklediğinizden emin olun:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 1. Adım: 3B Sahneyi Başlatın

```csharp
Scene scene = new Scene();
```

 kullanarak yeni bir 3B sahne oluşturun.`Scene` sınıf.

## Adım 2: Uygulama ve Satıcı Bilgilerini Ayarlayın

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

3B sahnenizle ilişkili uygulama ve satıcı adlarını tanımlayın.

## Adım 3: Ölçü Birimlerini Tanımlayın

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Sahnenizde kullanılan ölçü birimlerini belirtin. Bu örnekte, 1 kutbu 60 cm'ye eşit olan "direk" adı verilen eski Mısır birimlerini kullanıyoruz.

## Adım 4: Sahneyi Kaydedin

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Eklenen varlık bilgileriyle birlikte sahneyi 3D destekli bir dosya formatında kaydedin. Çıkış dizinini gerektiği gibi ayarlayın.

## Adım 5: Başarı Mesajını Görüntüleyin

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Kullanıcıya varlık bilgilerinin başarıyla eklendiğini ve dosyanın kaydedildiğini bildirin.

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak 3D sahnelerinize temel varlık bilgilerini nasıl çıkaracağınızı ve ekleyeceğinizi başarıyla öğrendiniz. Bu bilgi, daha bilgilendirici ve ilgi çekici 3D içerik oluşturmak için sonsuz olasılıkların kapısını açar.

## SSS'ler

### S1: Aspose.3D for .NET'i diğer programlama dilleriyle kullanabilir miyim?

Cevap1: Aspose.3D öncelikli olarak .NET dillerini destekler ancak diğer diller için birlikte çalışabilirlik seçeneklerini de keşfedebilirsiniz.

### S2: Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?

 C2: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S3: Aspose.3D ile ilgili sorgular için nasıl destek alabilirim?

 A3: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk ve destek için.

### S4: Aspose.3D for .NET için geçici bir lisans satın alabilir miyim?

 Cevap4: Evet, geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Aspose.3D for .NET'in ayrıntılı belgelerini nerede bulabilirim?

 A5: Bkz.[dokümantasyon](https://reference.aspose.com/3d/net/) derinlemesine bilgi için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
