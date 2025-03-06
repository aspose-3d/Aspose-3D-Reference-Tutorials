---
title: 3D Sahneyi Sıkıştırılmış AMF Formatına Aktarma
linktitle: Sahneyi Sıkıştırılmış AMF'ye Aktarma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET kullanarak 3D sahneleri sıkıştırılmış AMF formatına nasıl aktaracağınızı öğrenin. Bu adım adım kılavuzla geliştirme becerilerinizi geliştirin.
weight: 11
url: /tr/net/loading-and-saving/amf/export-scene-compressed-amf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahneyi Sıkıştırılmış AMF Formatına Aktarma

## giriiş

3D modelleme ve görüntülemenin dinamik dünyasında verimlilik ve esneklik çok önemlidir. Aspose.3D for .NET, geliştiricilerin 3D sahneleri sıkıştırılmış AMF (Katmanlı Üretim Dosyası) formatına sorunsuz bir şekilde aktarmalarına olanak tanır ve kaliteden ödün vermeden en uygun dosya boyutunu sağlar. Bu eğitim size süreç boyunca adım adım rehberlik edecek ve hem yeni başlayanların hem de deneyimli geliştiricilerin Aspose.3D for .NET'in özelliklerinden faydalanmasını kolaylaştıracak.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

- 3D modelleme kavramlarının temel anlayışı
- Makinenizde Visual Studio yüklü
-  Aspose.3D for .NET kitaplığı. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/)
- 3D geliştirme becerilerinizi geliştirme arzusu!

## Ad Alanlarını İçe Aktar

Aspose.3D for .NET'in işlevselliğinden yararlanmak için projenizde gerekli ad alanlarını içe aktardığınızdan emin olun:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1. Adım: 3D Sahne Yükleyin

Aspose.3D for .NET'i kullanarak bir 3D sahne yükleyerek başlayın. Bir sahne nesnesi oluşturun ve ona kutular gibi varlıklar ekleyin:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Adım 2: Ölçek Dönüşümü

Daha sonra sahnedeki başka bir kutuya ölçek dönüşümü uygulayın:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Adım 3: Euler Açılarını Ayarlayın

Dönüşüm için Euler açılarını ayarlayın:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Adım 4: Sıkıştırılmış AMF Dosyasını Kaydetme

Son olarak, 3B sahneyi istediğiniz çıktı dizinindeki sıkıştırılmış bir AMF dosyasına kaydedin:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Çözüm

Tebrikler! Aspose.3D for .NET kullanarak bir 3D sahneyi sıkıştırılmış AMF formatına başarıyla aktardınız. Bu güçlü kitaplık, 3D geliştiricilere verimli ve görsel açıdan etkileyici modeller oluşturmalarına olanak tanıyan bir olasılıklar dünyasının kapılarını açar.

## SSS'ler

### S1: Aspose.3D popüler 3D modelleme yazılımıyla uyumlu mu?

Cevap1: Aspose.3D, çeşitli dosya formatlarını destekleyerek popüler 3D modelleme araçlarıyla uyumlu olmasını sağlar.

### S2: AMF'nin yanı sıra diğer dosya formatları için sıkıştırmayı etkinleştirebilir miyim?

Cevap2: Evet, Aspose.3D çeşitli dosya formatları için sıkıştırmayı etkinleştirme seçenekleri sunar.

### S3: Aspose.3D hem yeni başlayanlar hem de ileri düzey geliştiriciler için uygun mu?

A3: Kesinlikle! Aspose.3D yeni başlayanlar için basitlik, deneyimli geliştiriciler için ise gelişmiş özellikler sunar.

### S4: Dışa aktarılabilecek 3B sahnelerin boyutunda herhangi bir sınırlama var mı?

Cevap4: Aspose.3D, değişen karmaşıklıktaki sahneleri işlemek için tasarlanmıştır ve katı boyut sınırlamaları yoktur.

### S5: Ek desteği ve topluluk tartışmalarını nerede bulabilirim?

 A5: ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) Destek ve tartışmalar için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
