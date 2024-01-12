---
title: 3B Sahnelerde Düğümün Dönüşüm Matrisine Göre Dönüştürülmesi
linktitle: 3B Sahnelerde Düğümün Dönüşüm Matrisine Göre Dönüştürülmesi
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak düğümleri 3D sahnelerde zahmetsizce dönüştürün. Öğreticiyle adım adım düğüm dönüşümlerini öğrenin.
type: docs
weight: 21
url: /tr/net/geometry-and-hierarchy/transformation-node-matrix/
---
## giriiş

3D grafiklerin ve görselleştirmelerin dinamik alanında, bir sahnedeki nesneleri manipüle etme yeteneği çok önemli bir husustur. Aspose.3D for .NET, geliştiricilerin dönüşüm matrislerini kullanarak düğümleri sorunsuz bir şekilde dönüştürmesine olanak tanır ve 3D sahnelere bir yaratıcılık ve kontrol katmanı ekler. Bu eğitim, 3B sahnedeki bir düğümü adım adım dönüştürme sürecinde size rehberlik edecektir.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

1. Aspose.3D for .NET Kütüphanesi: .NET projenizde Aspose.3D kütüphanesinin kurulu olduğundan emin olun. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).

2. Geliştirme Ortamı: Çalışan bir .NET geliştirme ortamı kurun ve henüz yapmadıysanız, dönüşümleri uygulayacağınız yeni bir proje oluşturun.

## Ad Alanlarını İçe Aktar

Gerekli ad alanlarını .NET projenize aktararak başlayın. Bu ad alanları, 3B sahne manipülasyonu için gerekli sınıfları ve yöntemleri sağlar.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Artık temel konuları ele aldığımıza göre, dönüşüm sürecini adım adım bir kılavuza ayıralım.

## Adım 1: Sahneyi ve Düğümü Başlatın

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Sahne nesnesini başlat
Scene scene = new Scene();

// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("cube");
```

Bu adımda yeni bir 3 boyutlu sahne ve o sahnenin içinde "cube" isimli bir düğüm oluşturuyoruz.

## Adım 2: Mesh Oluşturun ve Geometriyi Ayarlayın

```csharp
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Düğümü Mesh geometrisine yönlendirin
cubeNode.Entity = mesh;
```

Burada, çokgen oluşturucu yöntemini kullanarak bir ağ oluşturuyoruz ve onu düğüme atayarak küpümüzün geometrisini oluşturuyoruz.

## 3. Adım: Özel Çeviri Matrisini Ayarlayın

```csharp
//Özel çeviri matrisini ayarla
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Düğüme uygulanan spesifik dönüşümü belirlemek için özel bir çeviri matrisi tanımlayın. İstediğiniz dönüşüm için matris değerlerini gerektiği gibi ayarlayın.

## Adım 4: Sahneye Düğüm Ekleyin

```csharp
// Sahneye küp ekle
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Küp düğümünü sahneye dahil ederek genel 3B ortamın bir parçası haline getirin.

## Adım 5: Sahneyi Kaydedin

```csharp
// Belgeler dizininin yolu.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// 3B sahneyi desteklenen dosya formatlarında kaydedin
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Çıkış dizinini ve dosya adını belirtin, ardından 3B sahneyi istediğiniz dosya formatında kaydedin. Bu örnekte onu FBX7500ASCII formatında kaydediyoruz.

## Çözüm

Tebrikler! Aspose.3D for .NET ile 3 boyutlu bir sahnede bir dönüşüm matrisini kullanarak bir düğümü başarıyla dönüştürdünüz. Bu yetenek, çeşitli ve görsel olarak büyüleyici 3D uygulamaların kapılarını açar.

## SSS'ler

### S1: 3D grafiklerde dönüşüm matrisi nedir?

A1: Dönüşüm matrisi, 3B uzaydaki nesnelere çeşitli dönüşümler (öteleme, döndürme, ölçeklendirme) uygulamak için kullanılan matematiksel bir temsildir.

### S2: Tek bir düğüme birden çok dönüşüm uygulayabilir miyim?

Cevap2: Evet, ilgili matrisleri çarparak ve sonucu düğüme uygulayarak birden fazla dönüşümü birleştirebilirsiniz.

### S3: 3D sahneleri kaydetmek için desteklenen başka dosya formatları var mı?

 Cevap3: Aspose.3D for .NET, STL, GLTF, OBJ ve daha fazlası dahil olmak üzere çeşitli dosya formatlarını destekler. Bakın[dokümantasyon](https://reference.aspose.com/3d/net/) kapsamlı bir liste için.

### S4: Aspose.3D for .NET için nasıl geçici lisans alabilirim?

 A4: Ziyaret edin[geçici lisans sayfası](https://purchase.aspose.com/temporary-license/) Değerlendirme amacıyla geçici bir lisans almak için Aspose web sitesinde.

### S5: Nereden yardım alabilirim veya Aspose.3D topluluğuyla bağlantı kurabilirim?

 A5: ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) Aspose.3D'yi kullanarak sorular sormak, deneyimleri paylaşmak ve diğer geliştiricilerle bağlantı kurmak için.