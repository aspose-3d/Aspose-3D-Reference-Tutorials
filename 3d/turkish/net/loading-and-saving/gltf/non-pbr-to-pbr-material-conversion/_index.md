---
title: PBR'den PBR'ye Malzeme Dönüşümü
linktitle: PBR'den PBR'ye Malzeme Dönüşümü
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i keşfedin - PBR olmayan malzemeleri zahmetsizce PBR'ye dönüştürün. Kapsamlı eğitim ve güçlü API.
type: docs
weight: 16
url: /tr/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## giriiş

PBR Olmayan (Fiziksel Tabanlı İşleme) PBR malzemelerine dönüştürmek için Aspose.3D for .NET'in kullanımına ilişkin bu adım adım kılavuza hoş geldiniz. Aspose.3D, geliştiricilerin .NET uygulamalarında 3D dosya formatlarıyla sorunsuz bir şekilde çalışmasına olanak tanıyan güçlü bir API'dir.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

-  Aspose.3D for .NET: Aspose.3D for .NET kütüphanesinin kurulu olduğundan emin olun. İndirme linkini bulabilirsiniz[Burada](https://releases.aspose.com/3d/net/).

- Temel C# Anlayışı: Bu eğitimde, C# programlama konusunda temel bir anlayışa sahip olduğunuz varsayılmaktadır.

- IDE (Entegre Geliştirme Ortamı): .NET geliştirme için Visual Studio gibi tercih ettiğiniz IDE'yi seçin.

## Ad Alanlarını İçe Aktar

C# kodunuzda gerekli ad alanlarını içe aktararak başlayın:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1. Adım: Yeni bir 3D Sahneyi Başlatın

Aşağıdaki kodu kullanarak yeni bir 3B sahne oluşturarak başlayın:

```csharp
// ExStart:PBR'den PBR'ye Malzeme
// yeni bir 3D sahneyi başlat
var scene = new Scene();
```

## Adım 2: 3B Nesne Oluşturun

Ardından, örneğin bir kutu gibi bir 3B nesne oluşturun:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Adım 3: Malzeme Dönüşümünü Yapılandırın

PBR olmayandan PBR'ye dönüştürme için malzeme dönüştürme seçeneklerini ayarlayın:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Adım 4: GLTF 2.0 Formatında Kaydetme

Dönüştürülen sahneyi GLTF 2.0 formatında kaydedin:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:PBR'den PBR'ye Malzeme
```

Her ayrıntının doğru şekilde yapılandırıldığından emin olarak, özel kullanım durumunuz için bu adımları gerektiği kadar tekrarlayın.

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak PBR olmayan malzemeleri PBR malzemelerine nasıl dönüştüreceğinizi başarıyla öğrendiniz. Bu güçlü araç, .NET uygulamalarınızda 3D grafik manipülasyonu için sonsuz olasılıkların kapısını açar.

## SSS'ler

### S1: Aspose.3D tüm 3D dosya formatlarıyla uyumlu mudur?

Cevap1: Evet, Aspose.3D çok çeşitli 3D dosya formatlarını destekleyerek projelerinizde esneklik sağlar.

### S2: Aspose.3D'yi ticari uygulamalar için kullanabilir miyim?

 A2: Kesinlikle! Aspose.3D ticari bir üründür ve satın alabilirsiniz.[Burada](https://purchase.aspose.com/buy).

### S3: Test için geçici bir lisansa ihtiyacım var mı?

 Cevap3: Evet, test amaçlı olarak geçici bir lisans alabilirsiniz.[Burada](https://purchase.aspose.com/temporary-license/).

### S4: Aspose.3D desteğini nerede bulabilirim?

 A4: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.

### S5: Ücretsiz deneme sürümü var mı?

 Cevap5: Evet, ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).