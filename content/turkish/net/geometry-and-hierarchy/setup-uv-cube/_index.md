---
title: 3D Sahnelerde Cube'da UV Ayarlama
linktitle: 3D Sahnelerde Cube'da UV Ayarlama
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak 3 boyutlu bir küp üzerinde UV eşlemeyi ayarlamayı öğrenin. Hassas doku eşlemeyle görsel olarak etkileyici sahneler oluşturun.
type: docs
weight: 18
url: /tr/net/geometry-and-hierarchy/setup-uv-cube/
---
## giriiş

Büyüleyici ve görsel olarak çekici 3D sahneler oluşturmak genellikle geometrik şekiller üzerinde UV haritalamanın ayarlanması gibi titiz bir süreci içerir. Bu eğitimde Aspose.3D for .NET kullanarak bir küp üzerinde UV'nin nasıl kurulacağını keşfedeceğiz. Aspose.3D, 3D modelleme ve manipülasyon için kapsamlı özellikler sağlayan güçlü bir .NET kütüphanesidir.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

1. Aspose.3D for .NET Library: Aspose.3D kütüphanesinin kurulu olduğundan emin olun. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).

2. Geliştirme Ortamı: Gerekli araçlarla bir .NET geliştirme ortamı kurun.

Şimdi öğreticiye devam edelim.

## Ad Alanlarını İçe Aktar

Öncelikle .NET uygulamanızdaki Aspose.3D işlevlerine erişmek için gerekli ad alanlarını içe aktarın.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Adım 1: Küp için UV'leri tanımlayın

Küpün her köşesi için UV koordinatlarını tanımlayın. Bu, küpün her köşesi için U ve V değerlerinin belirtilmesini içerir.

```csharp
// ExStart:UV'leri Tanımlayın
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:UV'leri tanımlayın
```

## Adım 2: UV İndekslerini Tanımlayın

Küpün her çokgeni için UV koordinatlarının indekslerini belirtin. Bu, UV'lerin küp yüzeylerine nasıl eşlendiğini tanımlar.

```csharp
// ExStart:UV Endekslerini Tanımlayın
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd:UV Endekslerini Tanımlayın
```

## Adım 3: Bir Ağ Oluşturun

Çokgen oluşturucu yöntemini kullanarak bir ağ oluşturmak için Aspose.3D kitaplığını kullanın. Bu, 3D küpümüzün temelini oluşturacak.

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:Mesh Oluştur
```

## Adım 4: UV Elementi Oluşturun

UV eşleme verilerini depolamak için ağda bir UV öğesi oluşturun.

```csharp
// ExStart:CreateUVElement
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ExEnd:UVElement Oluştur
```

## Adım 5: UV Verilerini Mesh'e Kopyalayın

Önceden tanımlanmış UV koordinatlarını ve endekslerini ağın UV köşe öğesine kopyalayın.

```csharp
// ExStart:UVData'yı Kopyala
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ExEnd:UVVerilerini Kopyala
```

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak bir küp üzerinde UV haritalamayı başarıyla kurdunuz. Bu, hassas doku eşlemeyle karmaşık ve görsel olarak etkileyici 3D sahneler oluşturma olanaklarını açar.

## SSS'ler

### S1: .NET için Aspose.3D nedir?

Cevap1: Aspose.3D for .NET, .NET uygulamalarında 3D modelleme ve manipülasyon için güçlü bir kütüphanedir.

### S2: Aspose.3D belgelerini nerede bulabilirim?

 A2: Belgeler mevcut[Burada](https://reference.aspose.com/3d/net/).

### S3: Ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S4: Aspose.3D için nasıl destek alabilirim?

 Cevap4: Destek forumunu ziyaret edin[Burada](https://forum.aspose.com/c/3d/18).

### S5: Geçici lisanslar mevcut mu?

 Cevap5: Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).