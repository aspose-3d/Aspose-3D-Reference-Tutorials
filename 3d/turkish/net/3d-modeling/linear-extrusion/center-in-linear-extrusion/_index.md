---
title: Doğrusal Ekstrüzyonda Merkez
linktitle: Doğrusal Ekstrüzyonda Merkez
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D modelleme dünyasını keşfedin. Doğrusal ekstrüzyon tekniklerini ortalayın, çarpıcı tasarımlar yaratın ve yaratıcılığınızı ortaya çıkarın.
weight: 10
url: /tr/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Doğrusal Ekstrüzyonda Merkez

## giriiş

Aspose.3D for .NET kullanarak doğrusal ekstrüzyona hakim olmaya yönelik bu kapsamlı kılavuza hoş geldiniz. 3D modelleme becerilerinizi geliştirmek ve çarpıcı ekstrüzyonlar oluşturmak istiyorsanız doğru yerdesiniz. Bu derste, tasarımlarınızı tamamen yeni bir seviyeye taşımak için özellikle merkezleme yönüne odaklanarak doğrusal ekstrüzyon tekniğini inceleyeceğiz.

## Önkoşullar

Bu heyecan verici yolculuğa çıkmadan önce aşağıdaki ön koşulların yerine getirildiğinden emin olun:

- C# programlama dilinin temel anlayışı.
- Makinenizde Visual Studio yüklü.
-  Aspose.3D for .NET kütüphanesini şu adresten indirebilirsiniz:[Aspose.3D .NET Belgeleri](https://reference.aspose.com/3d/net/).
-  Şuraya erişiminiz olduğundan emin olun:[Aspose.3D .NET Belgeleri](https://reference.aspose.com/3d/net/) Eğitim boyunca referans olması için.

## Ad Alanlarını İçe Aktar

İşleri başlatmak için gerekli ad alanlarını içe aktaralım. Bunlar 3D modelleme şaheserimizin temelini oluşturacak.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım 1: Temel Profili Başlatın

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2. Adım: 3B Sahne Oluşturun

```csharp
Scene scene = new Scene();
```

## 3. Adım: Sol ve Sağ Düğümler Oluşturun

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Adım 4: Sol Düğümde Doğrusal Ekstrüzyon Gerçekleştirin

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Adım 5: Referans için Zemin Düzlemini Ayarlayın

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Adım 6: Sağ Düğümde Doğrusal Ekstrüzyon Gerçekleştirin

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Adım 7: Referans için Zemin Düzlemini Ayarlayın (Sağ Düğüm)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Adım 8: 3D Sahneyi Kaydet

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak merkezlemeli doğrusal ekstrüzyon sanatında başarıyla ustalaştınız. Farklı parametrelerle denemeler yapmaktan ve bu tekniğin sunduğu geniş olanakları keşfetmekten çekinmeyin.

## SSS'ler

### S1: Aspose.3D for .NET'i diğer programlama dilleriyle kullanabilir miyim?

Cevap1: Aspose.3D öncelikli olarak C# ve VB.NET gibi .NET dillerini destekler.

### S2: Aspose.3D ile ilgili sorgular için desteği nerede bulabilirim?

 A2: Ziyaret edin[Aspose.3D Forumu](https://forum.aspose.com/c/3d/18) özel destek ve tartışmalar için.

### S3: Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S4: Aspose.3D for .NET için nasıl geçici lisans alabilirim?

 Cevap4: Geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Aspose.3D for .NET lisansını nereden satın alabilirim?

 Cevap5: Lisansınızı satın alın[Burada](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
