---
title: Özelleştirilmiş Kesme Alt Silindiri
linktitle: Özelleştirilmiş Kesme Alt Silindiri
second_title: Aspose.3D .NET API'si
description: Ayrıntılı adım adım kılavuzumuzla Aspose.3D for .NET'i kullanarak özelleştirilmiş kesme alt silindirleri oluşturmayı öğrenin. Bugün 3D modelleme becerilerinizi geliştirin!
type: docs
weight: 12
url: /tr/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## giriiş
Aspose.3D for .NET'i kullanarak özelleştirilmiş bir kesme alt silindiri oluşturmaya yönelik kapsamlı kılavuzumuza hoş geldiniz. 3D modelleme becerilerinizi geliştirmek ve projelerinize benzersiz özellikler eklemek istiyorsanız doğru yerdesiniz. Bu eğitimde, anlaşılır açıklamalar ve kod parçacıkları kullanarak süreç boyunca size adım adım yol göstereceğiz.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdakilere sahip olduğunuzdan emin olun:
- C# ve .NET programlamanın temel anlayışı.
-  Aspose.3D for .NET kütüphanesi kuruldu. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).
- .NET programlama için kurulmuş bir geliştirme ortamı.
## Ad Alanlarını İçe Aktar
C# kodunuzda gerekli ad alanlarını içe aktararak başlayın:
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
Aspose.3D'yi kullanarak bir 3D sahne oluşturarak başlayın:
```csharp
Scene scene = new Scene();
```
## Adım 2: Silindir 1'i Oluşturun
İlk silindiri oluşturun ve özelliklerini ayarlayın:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Adım 3: Silindir 1 için Kesme Tabanını Özelleştirin
İlk silindire özelleştirilmiş bir kesme tabanı uygulayın:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Xy düzleminde (z ekseni) 47,5 derecelik kayma
```
## Adım 4: Silindir 1'i Sahneye Ekleyin
İlk silindiri sahneye ekleyin ve çevirisini ayarlayın:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Adım 5: Silindir 2'yi Oluşturun
Benzer özelliklere sahip ikinci bir silindir oluşturun:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Adım 6: Silindir 2'yi Sahneye Ekleyin
İkinci silindiri kayma tabanı olmayan sahneye ekleyin:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Adım 7: Sahneyi Kaydedin
Sahneyi belge dizininize Wavefront OBJ dosyası olarak kaydedin:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak başarıyla özelleştirilmiş bir kesme alt silindiri oluşturdunuz. Bu eğitimin amacı, 3D modelleme ve programlama konusunda farklı düzeylerde uzmanlığa sahip kullanıcılar için adım adım bir kılavuz sağlamaktır.
## Sıkça Sorulan Sorular
### Aspose.3D for .NET yeni başlayanlar için uygun mu?
Kesinlikle! Aspose.3D for .NET, kullanıcı dostu bir arayüz sunarak hem yeni başlayanlar hem de deneyimli geliştiriciler için erişilebilir olmasını sağlar.
### Silindirlere farklı kesme açıları uygulayabilir miyim?
Evet, her silindir için kesme tabanını ayrı ayrı özelleştirerek benzersiz efektler elde edebilirsiniz.
### Deneme sürümü mevcut mu?
 Evet, ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).
### Ek desteği nerede bulabilirim?
 Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.
### Geçici lisansı nasıl alabilirim?
Geçici lisansınızı alın[Burada](https://purchase.aspose.com/temporary-license/).