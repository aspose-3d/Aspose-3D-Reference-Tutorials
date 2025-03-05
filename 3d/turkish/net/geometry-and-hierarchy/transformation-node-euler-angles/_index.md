---
title: Düğümün Euler Açılarına Göre Dönüştürülmesi
linktitle: Düğümün Euler Açılarına Göre Dönüştürülmesi
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D düğümleri zahmetsizce dönüştürmeyi öğrenin. Projelerinizde çarpıcı sonuçlar için adım adım kılavuzumuzu izleyin.
type: docs
weight: 19
url: /tr/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## giriiş

Aspose.3D for .NET kullanarak 3 boyutlu sahnelerde düğümlerin Euler açılarına göre dönüştürülmesine ilişkin bu kapsamlı eğitime hoş geldiniz. Bu kılavuzda, 3 boyutlu grafiklerin heyecan verici dünyasına dalacağız ve Euler açılarını kullanarak bir düğüme dönüşümler ekleme sürecini keşfedeceğiz. Aspose.3D for .NET, 3D sahneler ve ağlarla çalışmak için güçlü araçlar sunarak projelerinde çok yönlülük ve verimlilik arayan geliştiriciler için mükemmel bir seçimdir.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET Library: Aspose.3D kütüphanesinin kurulu olduğundan emin olun. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).

- Geliştirme Ortamı: Visual Studio gibi tercih ettiğiniz .NET geliştirme ortamını kurun.

## Ad Alanlarını İçe Aktar

Aspose.3D for .NET tarafından sağlanan işlevselliğe erişmek için gerekli ad alanlarını içe aktararak başlayın:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Şimdi, daha net bir anlayış için örneği birden çok adıma ayıralım.

## Adım 1: Sahne Nesnesini Başlatın

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Sahne nesnesini başlat
Scene scene = new Scene();
```

 kullanarak yeni bir 3B sahne oluşturarak başlayın.`Scene` sınıf.


## Adım 2: İlkel Kutuyu Kullanarak Mesh Oluşturun

```csharp
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = (new Box()).ToMesh();
```

 Bir yöntemi çağırın (bu durumda,`CreateMeshUsingPolygonBuilder` bir gelenekten`Common`sınıfı) 3B nesne için bir ağ oluşturmak üzere kullanın.

## Adım 3: Ağ için bir konteyner düğümü oluşturun

```csharp
// Düğümü Mesh geometrisine yönlendirin
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

 kullanarak sahne içinde bir düğüm oluşturun.`Node` sınıf. Bu düğüm 3 boyutlu nesnemiz için konteyner görevi görecek.

## Adım 4: Euler Açılarını ve Çeviriyi Ayarlayın

```csharp
// Euler açıları
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Çeviriyi ayarla
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Düğümün 3 boyutlu alanda konumlandırılması için Euler açılarını ve ötelemeyi tanımlayın.

## Adım 5: 3D Sahneyi Kaydedin

```csharp
// Belgeler dizininin yolu.
var output = "TransformationToNode.fbx";

// 3B sahneyi desteklenen dosya formatlarında kaydedin
scene.Save(output);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Çıkış dizinini belirtin ve dönüştürülen düğüm dahil 3B sahneyi istenen dosya formatında (bu durumda FBX7500ASCII) kaydedin.

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak 3D sahnelerde bir düğümü Euler açılarına göre nasıl dönüştüreceğinizi başarıyla öğrendiniz. Bu güçlü kütüphane, 3D grafik geliştirmede sonsuz olasılıkların kapısını açar.

## SSS'ler

### S1: Aspose.3D diğer 3D modelleme araçlarıyla uyumlu mu?

Cevap1: Aspose.3D, çeşitli 3D dosya formatlarını destekleyerek popüler modelleme araçlarıyla uyumluluğu artırır.

### S2: Tek bir düğüme birden çok dönüşüm uygulayabilir miyim?

C2: Evet, karmaşık efektler elde etmek için birden fazla dönüşümü birleştirip uygulayabilirsiniz.

### S3: Ek Aspose.3D belgelerini nerede bulabilirim?

 A3: Bkz.[dokümantasyon](https://reference.aspose.com/3d/net/) detaylı bilgi ve örnekler için.

### S4: Aspose.3D for .NET'i kullanmak için lisansa ihtiyacım var mı?

 Cevap4: Evet, lisans alabilirsiniz[Burada](https://purchase.aspose.com/buy) veya bir tanesini keşfedin[ücretsiz deneme](https://releases.aspose.com/).

### S5: Yardıma mı ihtiyacınız var veya özel sorularınız mı var?

 A5: ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği için.