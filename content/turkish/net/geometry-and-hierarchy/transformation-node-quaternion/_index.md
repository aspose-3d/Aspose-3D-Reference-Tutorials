---
title: 3B Sahnelerde Düğümün Kuaterniyonla Dönüştürülmesi
linktitle: 3B Sahnelerde Düğümün Kuaterniyonla Dönüştürülmesi
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak 3D düğümleri kuaterniyonlarla dönüştürmeyi öğrenin. Yeni başlayanlar için adım adım kılavuz.
type: docs
weight: 20
url: /tr/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## giriiş

Aspose.3D for .NET kullanarak 3D sahnelerde bir düğümü dörde bir dönüştürmeye ilişkin adım adım kılavuza hoş geldiniz. Bu eğitimde Aspose.3D for .NET'in güçlü yeteneklerini keşfedeceğiz ve kuaterniyonlar kullanarak bir 3D düğüme dönüşüm ekleme sürecini inceleyeceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET: Aspose.3D kütüphanesinin kurulu olduğundan emin olun. adresinden indirebilirsiniz.[yayın sayfası](https://releases.aspose.com/3d/net/).

- Geliştirme Ortamı: .NET geliştirme ortamınızı gerekli araçlar ve yapılandırmalarla kurun.

- 3B Kavramların Temel Anlaşılması: 3B grafiklere ve kavramlara aşina olmak faydalı olacaktır.

## Ad Alanlarını İçe Aktar

.NET projenize Aspose.3D için gerekli ad alanlarını ekleyin:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Adım 1: Sahne Nesnesini Başlatın

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Sahne nesnesini başlat
Scene scene = new Scene();
```

## Adım 2: Düğüm Sınıfı Nesnesini Başlatın

```csharp
// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("cube");
```

## Adım 3: Polygon Builder'ı kullanarak Mesh Oluşturun

```csharp
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Adım 4: Düğümü Mesh Geometrisine Noktalayın

```csharp
// Düğümü Mesh geometrisine yönlendirin
cubeNode.Entity = mesh;
```

## Adım 5: Kuaterniyon kullanarak Döndürmeyi Ayarlayın

```csharp
// Döndürmeyi ayarla
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Adım 6: Çeviriyi Ayarlayın

```csharp
// Çeviriyi ayarla
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Adım 7: Sahneye Küp Ekleyin

```csharp
// Sahneye küp ekle
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Adım 8: 3D Sahneyi Kaydet

```csharp
// Belgeler dizininin yolu.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// 3B sahneyi desteklenen dosya formatlarında kaydedin
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak 3D sahnelerde bir düğümü dörtlü olarak nasıl dönüştüreceğinizi başarıyla öğrendiniz. Şuraya başvurarak daha fazla özellik ve olasılığı keşfedin:[dokümantasyon](https://reference.aspose.com/3d/net/).

## SSS'ler

### S1: 3D grafiklerde kuaterniyon nedir?

Cevap1: Kuaterniyonlar, 3B uzaydaki dönüşleri temsil etmek için kullanılan matematiksel varlıklardır.

### S2: Aspose.3D for .NET'i nasıl indirebilirim?

 Cevap2: Kitaplığı şuradan indirebilirsiniz:[yayın sayfası](https://releases.aspose.com/3d/net/).

### S3: Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?

 C3: Evet, şu adresten ücretsiz deneme alabilirsiniz:[Burada](https://releases.aspose.com/).

### S4: Aspose.3D for .NET desteğini nerede bulabilirim?

 A4: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) Destek ve tartışmalar için.

### S5: Aspose.3D için geçici lisansı nasıl edinebilirim?

 Cevap5: Geçici bir lisans alın[Burada](https://purchase.aspose.com/temporary-license/).
