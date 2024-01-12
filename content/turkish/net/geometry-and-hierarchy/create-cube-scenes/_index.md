---
title: 3D'de Küp Sahneleri Oluşturma
linktitle: 3D'de Küp Sahneleri Oluşturma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile büyüleyici 3D küp sahnelerini zahmetsizce oluşturun. Kütüphaneyi indirin, adım adım kılavuzumuzu izleyin ve serbest bırakın.
type: docs
weight: 12
url: /tr/net/geometry-and-hierarchy/create-cube-scenes/
---
## giriiş

3D tasarımın büyüleyici dünyasına dalmaya hazır mısınız? Bu eğitimde, Aspose.3D for .NET'i kullanarak büyüleyici küp sahneleri oluşturma sürecinde size rehberlik edeceğiz. Aspose.3D, geliştiricilerin sürükleyici 3D deneyimlerini sorunsuz bir şekilde oluşturmasına olanak tanıyan güçlü ve çok yönlü bir kitaplıktır.

## Önkoşullar

Bu yaratıcı yolculuğa çıkmadan önce ihtiyacınız olan her şeye sahip olduğunuzdan emin olalım:

1.  Aspose.3D for .NET Kütüphanesi: Kütüphaneyi şuradan indirip yükleyin:[Belgeleri sunun](https://reference.aspose.com/3d/net/).

2. Geliştirme Ortamı: Tercih ettiğiniz .NET geliştirme ortamını kurun.

3. C# ile Temel Bilgi: Bu eğitimde C# programlama konusunda temel bilgiye sahip olduğunuz varsayılmaktadır.

## Ad Alanlarını İçe Aktar

Şimdi gerekli ad alanlarını C# kodunuza aktararak işe başlayalım:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## 1. Adım: Sahneyi Başlatın

Yeni bir 3B sahne oluşturarak başlayın:

```csharp
// ExStart:CubeScene Oluştur
// Sahne nesnesini başlat
Scene scene = new Scene();
```

## Adım 2: Küp için Bir Düğüm Oluşturun

Şimdi sahne içerisinde küpümüzü temsil edecek bir düğüm ekleyelim:

```csharp
// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("cube");
```

## Adım 3: Ağı Oluşturun

Çokgen oluşturucu yöntemini kullanarak küpünüz için bir ağ oluşturmak üzere Common sınıfını kullanın:

```csharp
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Adım 4: Düğümü Mesh Geometrisine Yönlendirin

Mesh geometrisini küp düğümüyle ilişkilendirin:

```csharp
// Düğümü Mesh geometrisine yönlendirin
cubeNode.Entity = mesh;
```

## Adım 5: Sahneye Düğüm Ekleyin

Küp düğümünü sahnenin kök düğümlerine yerleştirin:

```csharp
// Bir sahneye Düğüm ekleme
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Adım 6: 3D Sahneyi Kaydedin

Çıkış dizinini belirtin ve 3B sahneyi desteklenen bir dosya formatında kaydedin (bu durumda FBX):

```csharp
// Belgeler dizininin yolu.
var output = "Your Output Directory" + "CubeScene.fbx";

// 3B sahneyi desteklenen dosya formatlarında kaydedin
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Adım 7: Başarı Mesajını Görüntüleyin

Kullanıcıya küp sahnesinin başarıyla oluşturulduğunu bildirin:

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

Tebrikler! Aspose.3D for .NET'i kullanarak ilk 3D küp sahnenizi oluşturdunuz. Olasılıkların kilidini açmak için farklı şekiller, dokular ve ışıklandırmayı deneyin.

## Çözüm

Bu eğitimde Aspose.3D for .NET kullanarak büyüleyici 3D küp sahneleri oluşturma sürecini inceledik. Artık bu bilgiyle donanmış olarak yaratıcılığınızı serbest bırakabilir ve 3D vizyonlarınızı hayata geçirebilirsiniz.

## SSS'ler

### S1: Aspose.3D farklı 3D dosya formatlarıyla uyumlu mudur?

Cevap1: Evet, Aspose.3D, FBX, STL ve daha fazlası dahil olmak üzere çeşitli dosya formatlarını destekler.

### S2: Küpün görünümünü özelleştirebilir miyim?

A2: Kesinlikle! İstediğiniz görünümü elde etmek için malzemeler, renkler ve dokularla denemeler yapın.

### S3: Ek destek ve kaynakları nerede bulabilirim?

 A3: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk yardımı ve tartışmalar için.

### S4: Ücretsiz deneme sürümü mevcut mu?

 Cevap4: Evet, ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).

### S5: Aspose.3D için nasıl geçici lisans alabilirim?

 Cevap5: Geçici bir lisans edinin[Burada](https://purchase.aspose.com/temporary-license/).