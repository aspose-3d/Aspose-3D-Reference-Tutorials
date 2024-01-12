---
title: Doğrusal Ekstrüzyonda Büküm
linktitle: Doğrusal Ekstrüzyonda Büküm
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D grafiklerin büyüleyici dünyasını keşfedin. Twist ile Doğrusal Ekstrüzyonu adım adım öğrenin.
type: docs
weight: 14
url: /tr/net/linear-extrusion/twist-in-linear-extrusion/
---
## giriiş

Sürekli gelişen .NET geliştirme dünyasında, 3D grafiklerin gücünden yararlanmak heyecan verici bir çabadır. Aspose.3D for .NET, geliştiricilerin sürükleyici ve görsel olarak etkileyici uygulamaları sorunsuz bir şekilde oluşturmasına olanak tanıyan değerli bir araç seti olarak ortaya çıkıyor. Bu kapsamlı kılavuzda ilgi çekici bir özelliği inceleyeceğiz: Twist ile Doğrusal Ekstrüzyon. Bu eğitim size süreci adım adım anlatacak ve Aspose.3D for .NET'in potansiyelini ortaya çıkaracak.

## Önkoşullar

Bu 3D yolculuğa çıkmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET: Aspose.3D kütüphanesini yüklediğinizden emin olun. Değilse indirebilirsiniz[Burada](https://releases.aspose.com/3d/net/).

- Temel .NET Geliştirme Bilgisi: Bu eğitimde .NET geliştirme konusunda temel bir anlayış varsayılmaktadır.

## Ad Alanlarını İçe Aktar:

Herhangi bir .NET projesinde ad alanlarının doğru kullanımı çok önemlidir. Aspose.3D'nin işlevselliklerinden etkili bir şekilde yararlanmak için gerekli ad alanlarını içe aktararak başlayın. İşte size yol gösterecek bir pasaj:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Şimdi Aspose.3D for .NET kullanarak Twist ile Doğrusal Ekstrüzyon'un ilgi çekici sürecini sindirilebilir adımlara ayıralım:

## Adım 1: Temel Profili Başlatın

```csharp
// Ekstrüzyona tabi tutulacak taban profilini başlatın
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Ekstrüzyon için temel profili ayarlayarak başlayın. Bu örnekte, belirtilen yuvarlama yarıçapına sahip bir dikdörtgen şekli kullanıyoruz.

## 2. Adım: 3B Sahne Oluşturun

```csharp
// Bir sahne oluştur
Scene scene = new Scene();
```

Tüm sihrin gerçekleşeceği bir 3 boyutlu sahne oluşturun. Bu, 3 boyutlu şaheserimiz için tuval görevi görüyor.

## 3. Adım: Sol ve Sağ Düğümler Oluşturun

```csharp
// Sol düğüm oluştur
var left = scene.RootNode.CreateChildNode();
// Sağ düğüm oluştur
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Sahne içinde sol ve sağ düğümler oluşturun. Sol düğümün çevirisini uygun şekilde konumlandıracak şekilde ayarlayın.

## Adım 4: Sol Düğümde Büküm ile Doğrusal Ekstrüzyon Gerçekleştirin

```csharp
// Twist özelliği, profilin ekstrüzyonu sırasında dönme derecesini tanımlar
// Bükme ve dilimleme özelliğini kullanarak sol düğümde doğrusal ekstrüzyon gerçekleştirin
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Sihir yapılan yer burasıdır. Döndürme derecesini tanımlamak için büküm özelliğini birleştirerek sol düğümde doğrusal ekstrüzyon gerçekleştirin. Daha ince ayrıntılar için dilim sayısını ayarlayın.

## Adım 5: Sağ Düğümde Büküm ile Doğrusal Ekstrüzyon Gerçekleştirin

```csharp
// Bükme ve dilimleme özelliğini kullanarak sağ düğümde doğrusal ekstrüzyon gerçekleştirin
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Ekstrüzyondaki değişiklikleri gözlemlemek için farklı büküm değerleriyle deneyler yaparak işlemi sağ düğüme yansıtın.

## Adım 6: 3D Sahneyi Kaydedin

```csharp
// 3D sahneyi kaydet
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Son olarak, 3B şaheserinizi istediğiniz çıktı dizinine kaydedin. Dosya adını tercihinize göre ayarlayın.

## Çözüm

Bu eğitimde Aspose.3D for .NET'i kullanarak Twist ile Doğrusal Ekstrüzyonun büyüleyici dünyasını keşfettik. Bu özellik yaratıcı olasılıkların kapılarını açarak geliştiricilerin uygulamalarına dinamik görsel öğeleri zahmetsizce eklemelerine olanak tanır.

## SSS'ler

### S1: Doğrusal Ekstrüzyonu Twist ile diğer şekillere uygulayabilir miyim?

A1: Kesinlikle! Sayısız tasarım olanağının kilidini açarak dikdörtgenlerin ötesinde çeşitli taban profillerini deneyebilirsiniz.

### S2: 'Büküm' özelliği doğrusal ekstrüzyonda nasıl bir rol oynuyor?

Cevap2: 'Büküm' özelliği, ekstrüzyon işlemi sırasında son 3 boyutlu şekli etkileyen dönüş derecesini belirler.

### S3: Çok sayıda dilim kullanıldığında performansla ilgili hususlar var mı?

Cevap3: Daha fazla sayıda dilim ayrıntı eklese de performansı etkileyebilir. Uygulamanızın gereksinimlerine göre bir denge kurun.

### S4: Doğrusal Ekstrüzyonu diğer Aspose.3D özellikleriyle birleştirebilir miyim?

A4: Kesinlikle! Aspose.3D zengin bir dizi özellik sunar. Daha karmaşık tasarımlar için Doğrusal Ekstrüzyonu diğer işlevlerle birleştirmekten çekinmeyin.

### S5: Aspose.3D desteği ve tartışmaları için bir topluluk var mı?

 C5: Evet, Aspose.3D topluluğuna şu adresten katılın:[Aspose Forumu](https://forum.aspose.com/c/3d/18) Destek ve ilgi çekici tartışmalar için.