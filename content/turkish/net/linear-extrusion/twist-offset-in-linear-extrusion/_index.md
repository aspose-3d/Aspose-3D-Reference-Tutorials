---
title: Doğrusal Ekstrüzyonda Büküm Ofseti
linktitle: Doğrusal Ekstrüzyonda Büküm Ofseti
second_title: Aspose.3D .NET API'si
description: Doğrusal Ekstrüzyonda Büküm Ofseti hakkındaki adım adım kılavuzumuzla Aspose.3D for .NET'in büyüsünü keşfedin. 3D projelerinizi zahmetsizce yükseltin.
type: docs
weight: 15
url: /tr/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## giriiş

Geliştiricilerin 3D manipülasyonu kolaylıkla gerçekleştirmesini sağlayan çok yönlü bir kütüphane olan Aspose.3D for .NET dünyasına hoş geldiniz. Bu eğitimde ilgi çekici özelliklerden biri olan "Doğrusal Ekstrüzyonda Büküm Ofseti"ni inceleyeceğiz. 3D programlama becerilerinizi geliştirmeye hazırsanız, hemen konuya dalalım!

## Önkoşullar

Bu heyecan verici yolculuğa çıkmadan önce aşağıdaki ön koşulların yerine getirildiğinden emin olun:

-  Aspose.3D for .NET Kütüphanesi: Kütüphaneyi şuradan indirip yükleyin:[yayın sayfası](https://releases.aspose.com/3d/net/).

- Geliştirme Ortamınız: Geliştirme ortamınızın kurulduğundan ve kullanıma hazır olduğundan emin olun.

## Ad Alanlarını İçe Aktar

Aspose.3D for .NET tarafından sağlanan işlevselliğe erişmek için gerekli ad alanlarını içe aktararak başlayın. Kodunuzda bu şöyle görünebilir:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Şimdi, Doğrusal Ekstrüzyonda Büküm Ofsetinde ustalaşmak için örneği yönetilebilir adımlara ayıralım:

## Adım 1: Temel Profili Başlatın

Burada belirli bir yuvarlama yarıçapına sahip bir dikdörtgen şekliyle örneklenen bir taban profili oluşturarak başlayın.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Adım 2: Bir Sahne Oluşturun

Düğümlerinizi ve şekillerinizi barındırmak için bir 3B sahne oluşturun.

```csharp
Scene scene = new Scene();
```

## 3. Adım: Düğümler Oluşturun

Sahnenin içinde hem sol hem de sağda düğümler oluşturun.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Adım 4: Sol Düğümde Doğrusal Ekstrüzyon

Bükme ve dilimleme özelliğini kullanarak sol düğümde doğrusal ekstrüzyon gerçekleştirin.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Adım 5: Büküm Ofsetiyle Sağ Düğümde Doğrusal Ekstrüzyon

Sağ düğümde büküm, büküm ofseti ve dilimler özelliğini kullanarak doğrusal ekstrüzyon gerçekleştirin.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Adım 6: 3D Sahneyi Kaydet

Dosya formatını WavefrontOBJ olarak belirterek 3D sahneyi istediğiniz çıktı dizinine kaydedin.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Tebrikler! Aspose.3D for .NET'i kullanarak Doğrusal Ekstrüzyonda Büküm Ofsetini başarıyla uyguladınız.

## Çözüm

Bu eğitimde Aspose.3D for .NET'in güçlü özelliklerini araştırdık, özellikle Doğrusal Ekstrüzyonda Büküm Ofsetine odaklandık. Bu yeni keşfedilen becerilerle, 3D projelerinize dinamizm katmak için iyi bir donanıma sahipsiniz.

## SSS'ler

### S1: Aspose.3D for .NET'i diğer programlama dilleriyle kullanabilir miyim?

Cevap1: Aspose.3D öncelikle .NET dillerini destekler ancak Aspose, Java ve diğer platformlar için benzer kütüphaneler sağlar.

### S2: Aspose.3D for .NET için geçici lisansı nasıl edinebilirim?

 A2: Ziyaret edin[bu bağlantı](https://purchase.aspose.com/temporary-license/) Test amacıyla geçici bir lisans almak için.

### S3: Aspose.3D for .NET için bir topluluk forumu var mı?

A3: Kesinlikle! Şu adresteki topluluğa katılın:[Aspose.3D Forumu](https://forum.aspose.com/c/3d/18) diğer geliştiricilerle iletişim kurmak ve yardım istemek.

### S4: Ek örnekler ve belgeler mevcut mu?

 A4: Keşfedin[dokümantasyon](https://reference.aspose.com/3d/net/) Kapsamlı kılavuzlar ve örnekler için.

### S5: Aspose.3D for .NET'i nereden satın alabilirim?

 A5: Başa dön[bu bağlantı](https://purchase.aspose.com/buy) satın alma işlemi gerçekleştirin ve Aspose.3D'nin tüm potansiyelini ortaya çıkarın.