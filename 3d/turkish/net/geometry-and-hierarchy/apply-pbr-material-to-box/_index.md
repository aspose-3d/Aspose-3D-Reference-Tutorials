---
title: PBR Malzemesinin Kutuya Uygulanması
linktitle: PBR Malzemesinin Kutuya Uygulanması
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D grafik dünyasını keşfedin. Fiziksel Tabanlı İşleme malzemelerini kullanarak zahmetsizce sürükleyici sahneler oluşturun.
weight: 10
url: /tr/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# PBR Malzemesinin Kutuya Uygulanması

## giriiş

3D grafiklerin büyüleyici dünyasına hoş geldiniz! Bu adım adım kılavuzda, güçlü Aspose.3D for .NET kütüphanesini keşfedeceğiz ve Fiziksel Tabanlı Rendering (PBR) malzemelerini kullanarak büyüleyici 3D sahnelerin nasıl oluşturulacağını öğreneceğiz. Aspose.3D, 3D grafiklerin karmaşık sürecini basitleştirir ve geliştiricilere birçok olasılık sunar.

## Önkoşullar

3D grafiklerin heyecan verici dünyasına dalmadan önce her şeyin ayarlandığından emin olalım:

### Aspose.3D for .NET'i indirin ve yükleyin

 Ziyaret edin[Aspose.3D for .NET belgeleri](https://reference.aspose.com/3d/net/) Kitaplığın indirilmesi ve kurulmasıyla ilgili ayrıntılı talimatlar için.

### Lisans Alın

Aspose.3D'nin tüm potansiyelini açığa çıkarmak için geçerli bir lisans edinin. Geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/) veya tam lisans satın alın[Burada](https://purchase.aspose.com/buy).

## Ad Alanlarını İçe Aktar

Öncelikle Aspose.3D for .NET'in özelliklerinden yararlanmak için gerekli ad alanlarını içe aktardığınızdan emin olun:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1. Adım: Bir Sahneyi Başlatın

Aşağıdaki kod parçacığını kullanarak bir 3B sahneyi başlatarak başlayın:

```csharp
Scene scene = new Scene();
```

## Adım 2: PBR Malzemesini Başlatın

Gerçekçi işleme elde etmek için bir PBR malzeme nesnesi oluşturun:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Adım 3: Malzeme Özelliklerini Ayarlayın

Malzemenin özelliklerine ince ayar yaparak onu neredeyse metalik ve çok pürüzlü hale getirin:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Adım 4: Bir Kutu Oluşturun

PBR malzemesinin uygulanacağı bir kutu oluşturun:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Adım 5: Malzemeyi Kutuya Uygulayın

PBR malzemesini oluşturulan kutu düğümüne atayın:

```csharp
boxNode.Material = mat;
```

## Adım 6: 3D Sahneyi Kaydedin

3B sahneyi istenen çıktı dizini ile STL formatında kaydedin:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Tebrikler! Aspose.3D for .NET'i kullanarak bir PBR malzemesini 3D sahnedeki bir kutuya başarıyla uyguladınız.

## Çözüm

Aspose.3D for .NET ile 3D grafiklere adım atmak, sonsuz yaratıcı olasılıkların kapılarını açar. Sezgisel API'si ve sağlam özellikleriyle, görsel açıdan etkileyici sahneler oluşturmak, geliştiriciler için keyifli bir deneyime dönüşüyor.

## SSS'ler

### S1: Aspose.3D diğer 3D dosya formatlarıyla uyumlu mudur?

Cevap1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekleyerek projelerinizde esneklik sağlar.

### S2: Aspose.3D'yi ticari uygulamalar için kullanabilir miyim?

A2: Kesinlikle! Aspose.3D, uygulamalarınıza kusursuz entegrasyon için ticari lisanslar sağlar.

### S3: Deneme sürümü mevcut mu?

 Cevap3: Evet, ücretsiz deneme sürümünü indirerek Aspose.3D'nin yeteneklerini keşfedebilirsiniz.[Burada](https://releases.aspose.com/).

### S4: Topluluk desteğini ve tartışmalarını nerede bulabilirim?

 Cevap4: Aspose.3D topluluğuna şu adresten katılın:[Aspose.3D Forumları](https://forum.aspose.com/c/3d/18) Destek ve tartışmalar için.

### S5: Aspose.3D için geçici lisansı nasıl edinebilirim?

 Cevap5: Geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/) değerlendirme amaçlı.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
