---
title: Fan Silindiri Oluşturma
linktitle: Fan Silindiri Oluşturma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D tasarım dünyasının kilidini açın! Çarpıcı fanlı ve fansız silindirleri zahmetsizce oluşturun. Deneme sürümünüzü şimdi indirin.
type: docs
weight: 10
url: /tr/net/working-with-cylinder/create-fan-cylinder/
---
## giriiş
Aspose.3D for .NET ile 3D modelleme ve görselleştirme dünyasına hoş geldiniz! Bu adım adım kılavuzda, Aspose.3D for .NET kullanarak büyüleyici bir fan silindirinin nasıl oluşturulacağını keşfedeceğiz. Aspose.3D, .NET uygulamalarında 3D içerikle çalışmak için kapsamlı yetenekler sağlayan güçlü bir kütüphanedir.
## Önkoşullar
3D modellemenin heyecan verici dünyasına dalmadan önce aşağıdaki ön koşullara sahip olduğunuzdan emin olun:
- .NET programlamanın temel anlayışı.
- Makinenizde Visual Studio yüklü.
-  İndirebileceğiniz Aspose.3D for .NET kütüphanesi[Burada](https://releases.aspose.com/3d/net/).
- 3D tasarım yoluyla yaratıcılığınızı açığa çıkarmaya gerçek bir ilgi.
## Ad Alanlarını İçe Aktar
Aspose.3D işlevselliğini .NET projenizde kullanılabilir hale getirmek için gerekli ad alanlarını içe aktararak işe başlayalım.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Aspose.3D ad alanlarını içe aktar
```
Artık hepimiz hazır olduğumuza göre, fan silindiri oluşturma sürecini yönetilebilir adımlara ayıralım.
## 1. Adım: Bir Sahne Oluşturun
```csharp
// Bir Sahne Oluşturun
Scene scene = new Scene();
```
Yeni bir 3D sahneyi başlatarak başlayın. Bu, fan silindirimizin hayat bulacağı tuval görevi görüyor.
## Adım 2: Bir Fan Silindiri Oluşturun
```csharp
// Bir silindir oluştur
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Yarıçap, yükseklik ve çözünürlük gibi parametreleri belirterek fan silindirinizin özelliklerini tanımlayın.
## Adım 3: Fan Silindiri Özelliklerini Özelleştirin
```csharp
// GenerateFanCylinder'ı true olarak ayarlayın
fan.GenerateFanCylinder = true;
// ThetaLength'i Ayarla
fan.ThetaLength = MathUtils.ToRadian(270);
```
ThetaLength'i kullanarak fan parçasının oluşturulmasını etkinleştirerek ve açısal süpürmeyi ayarlayarak fan silindirinizi özelleştirin.
## Adım 4: Fan Silindirini Sahneye Konumlandırın
```csharp
// ChildNode'u oluştur
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Fan silindirini alt düğüm olarak sahnenin kök düğümüne ekleyin ve onu 3B alan içinde konumlandırın.
## Adım 5: Fansız Silindir Oluşturun
```csharp
// Fansız bir silindir oluşturun
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Fan parçası olmayan bir silindir oluşturarak Aspose.3D'nin esnekliğini keşfedin.
## Adım 6: Fansız Silindir Özelliklerini Özelleştirin
```csharp
// GenerateFanCylinder'ı false olarak ayarlayın
nonfan.GenerateFanCylinder = false;
// ThetaLength'i Ayarla
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Fan parçasının oluşumunu devre dışı bırakarak fansız silindiri ayırt edin.
## Adım 7: Fansız Silindiri Sahneye Konumlandırın
```csharp
// ChildNode'u oluştur
scene.RootNode.CreateChildNode(nonfan);
```
Benzer şekilde, fan olmayan silindiri sahnenin kök düğümüne bir alt düğüm olarak ekleyin.
## Adım 8: Sahneyi Kaydedin
```csharp
// Sahneyi kaydet
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Başyapıtınızı istediğiniz formatta ve konumda kaydedin. Artık Aspose.3D for .NET'i kullanarak başarılı bir şekilde fanlı ve fansız silindir oluşturdunuz!
## Çözüm
Aspose.3D for .NET ile 3D modellemeye yönelik bu uygulamalı kılavuzu tamamladığınız için tebrikler! Fanlı ve fansız silindirleri kolaylıkla üreterek yaratıcılığınızı dijital alanda serbest bıraktınız.
## Sıkça Sorulan Sorular
### Aspose.3D for .NET'i diğer .NET çerçeveleriyle kullanabilir miyim?
Evet, Aspose.3D çeşitli .NET çerçeveleriyle uyumludur ve geliştirme projelerinizde çok yönlülük sağlar.
### Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?
 Evet, ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).
### Aspose.3D for .NET'in ayrıntılı belgelerini nerede bulabilirim?
 Belgeler mevcut[Burada](https://reference.aspose.com/3d/net/).
### Aspose.3D for .NET için nasıl destek alabilirim?
 Destek forumunu ziyaret edin[Burada](https://forum.aspose.com/c/3d/18) topluluktan ve Aspose uzmanlarından yardım almak için.
### Aspose.3D for .NET için geçici lisanslar mevcut mu?
 Evet, geçici lisanslar alınabilir[Burada](https://purchase.aspose.com/temporary-license/).