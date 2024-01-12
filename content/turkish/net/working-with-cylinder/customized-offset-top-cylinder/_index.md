---
title: Özelleştirilmiş Ofset Üst Silindir
linktitle: Özelleştirilmiş Ofset Üst Silindir
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D grafiklerin harikalarını keşfedin. Özelleştirilmiş ofset üst silindirleri zahmetsizce oluşturmayı öğrenin. Kodlama deneyiminizi şimdi yükseltin!
type: docs
weight: 11
url: /tr/net/working-with-cylinder/customized-offset-top-cylinder/
---
## giriiş
Aspose.3D for .NET ile 3D grafik manipülasyonu dünyasına hoş geldiniz! Bu eğitimde, .NET uygulamalarındaki 3D sahneler, nesneler ve formatlarla çalışmak için güçlü bir kütüphane olan Aspose.3D'yi kullanarak özelleştirilmiş bir üst silindir oluşturma sürecinde size rehberlik edeceğiz.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:
- Temel C# programlama dili bilgisi.
- Makinenizde Visual Studio yüklü.
- Aspose.3D for .NET kütüphanesini indirip projenizde referans olarak kullanabilirsiniz.
Şimdi adım adım kılavuza başlayalım!
## Ad Alanlarını İçe Aktar
Öncelikle C# kodunuza gerekli ad alanlarını içe aktardığınızdan emin olun:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## 1. Adım: Bir Sahne Oluşturun
```csharp
// Bir sahne oluştur
Scene scene = new Scene();
```
Bu, Aspose.3D'yi kullanarak yeni bir 3D sahneyi başlatır.
## Adım 2: Silindiri Başlatın
```csharp
// Silindiri başlat
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Burada yarıçap, yükseklik ve dilimler gibi belirli parametrelere sahip bir silindir oluşturuyoruz.
## Adım 3: İlk Silindir için OffsetTop'u Ayarlayın
```csharp
// OffsetTop'u Ayarla
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Bu, ilk silindir için özelleştirilmiş bir ofset üst kısmı ayarlar.
## Adım 4: İlk Silindir için ChildNode Oluşturun
```csharp
// ChildNode'u oluştur
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
İlk silindiri alt düğüm olarak sahneye konumunu ayarlayarak ekliyoruz.
## Adım 5: İkinci Silindiri Başlatın
```csharp
// Özelleştirilmiş OffsetTop olmadan ikinci silindiri başlatın
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
İkinci bir silindir, özelleştirilmiş ofset üst kısmı olmadan başlatılır.
## Adım 6: İkinci Silindir için ChildNode Oluşturun
```csharp
// ChildNode'u oluştur
scene.RootNode.CreateChildNode(cylinder2);
```
İkinci silindiri alt düğüm olarak sahneye ekliyoruz.
## Adım 7: Sahneyi Kaydedin
```csharp
// Kaydetmek
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Bu, özelleştirilmiş ofset üst silindiri de dahil olmak üzere 3 boyutlu sahneyi Wavefront OBJ formatında kaydeder.
Artık Aspose.3D for .NET'i kullanarak özelleştirilmiş bir ofset üst silindiri başarıyla oluşturdunuz!
## Çözüm
Bu eğitimde, özelleştirilmiş bir ofset üst silindir oluşturmak için Aspose.3D for .NET ile çalışmanın temellerini inceledik. Bu kitaplık, .NET uygulamalarınızda 3B grafik manipülasyonu için sonsuz olasılıkların kapısını açar.
## SSS
### S: Aspose.3D for .NET belgelerini nerede bulabilirim?
 C: Belgeler mevcut[Burada](https://reference.aspose.com/3d/net/).
### S: Aspose.3D for .NET'i nasıl indirebilirim?
 Cevap: İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).
### S: Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?
 C: Evet, ücretsiz deneme sürümünden yararlanabilirsiniz[Burada](https://releases.aspose.com/).
### S: Aspose.3D for .NET desteğini nereden alabilirim?
 C: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) destek için.
### S: Aspose.3D for .NET için geçici bir lisans alabilir miyim?
 C: Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).