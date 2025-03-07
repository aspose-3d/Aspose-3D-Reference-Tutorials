---
title: Doğrusal Ekstrüzyonda Yön
linktitle: Doğrusal Ekstrüzyonda Yön
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D modelleme dünyasının kilidini açın. Yönlü doğrusal ekstrüzyonu öğrenin, yaratıcılığı artırın ve sürükleyici uygulamaları zahmetsizce oluşturun.
weight: 11
url: /tr/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Doğrusal Ekstrüzyonda Yön

## giriiş

Yazılım geliştirmenin dinamik dünyasında, sürükleyici 3D modeller oluşturmak vazgeçilmez bir beceridir. Aspose.3D for .NET, geliştiricilere uygulamalarında 3D modellemenin potansiyelini kullanmaları için güçlü bir araç seti sağlar. Bu derste, doğrusal ekstrüzyonun ilgi çekici dünyasına dalacağız ve "Doğrusal Ekstrüzyonda Yön" özelliğinin nüanslarını keşfedeceğiz.

## Önkoşullar

Bu heyecan verici yolculuğa çıkmadan önce aşağıdaki ön koşulların yerine getirildiğinden emin olun:

-  Aspose.3D for .NET: Kitaplığı şuradan indirip yükleyin:[Aspose.3D .NET Belgeleri](https://reference.aspose.com/3d/net/).

- Geliştirme Ortamı: Çalışan bir .NET geliştirme ortamı kurduğunuzdan emin olun.

## Ad Alanlarını İçe Aktar

Aspose.3D'nin işlevselliğine erişmek için .NET projenize gerekli ad alanlarını içe aktarın. Kodunuzun başına aşağıdaki satırları ekleyin:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım 1: Temel Profili Başlatın

Ekstrüzyona tabi tutulacak taban profilini başlatarak başlayın. Bu örnekte yuvarlama yarıçapı 0,3 olan bir dikdörtgen şekli oluşturuyoruz.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2. Adım: 3B Sahne Oluşturun

Bir sahne oluşturarak 3D şaheserinizin temelini oluşturun.

```csharp
Scene scene = new Scene();
```

## 3. Adım: Düğümler Oluşturun

3B ortamınızın farklı bileşenlerini temsil etmek için sahne içinde düğümler oluşturun.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Adım 4: Yönsüz Doğrusal Ekstrüzyon

 kullanarak sol düğümde doğrusal ekstrüzyon gerçekleştirin.`Twist` Ve`Slices` özellikler.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Adım 5: Yönlü Doğrusal Ekstrüzyon

 Ekstrüzyon yeteneklerini birleştirerek genişletin`Direction` sağ düğümdeki özellik.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Adım 6: 3D Sahneyi Kaydedin

 3D sahneyi kaydederek eserinizi koruyun. Yer değiştirmek`"Your Output Directory"` İstenilen dizin ile.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Tebrikler! Aspose.3D for .NET ile hem geleneksel hem de yönlü yaklaşımları keşfederek doğrusal ekstrüzyonu başarıyla uyguladınız.

## Çözüm

Bu eğitimde Aspose.3D for .NET'i kullanarak 3D modellemenin büyüleyici dünyasında gezindik. Yönlü ve yönsüz doğrusal ekstrüzyon, görsel olarak etkileyici uygulamalar oluşturmak isteyen geliştiriciler için sonsuz olanaklar sunar. Aspose.3D ile 3D modellemenin gücü parmaklarınızın ucunda.

## SSS'ler

### S1: Aspose.3D for .NET için nasıl geçici lisans alabilirim?

 A1: Ziyaret edin[Geçici Lisans Ver](https://purchase.aspose.com/temporary-license/) geçici lisans almak için.

### S2: Aspose.3D desteğini nerede bulabilirim?

 A2: Katılın[Aspose.3D Forumu](https://forum.aspose.com/c/3d/18) yardım istemek ve toplulukla bağlantı kurmak.

### S3: Ücretsiz deneme sürümü mevcut mu?

 C3: Evet, aşağıdaki ücretsiz deneme sürümüyle özellikleri keşfedin:[Aspose.3D Sürümleri](https://releases.aspose.com/).

### S4: Aspose.3D for .NET'i nasıl satın alabilirim?

 A4: Şuraya gidin:[Satın Alma Sayfasını Belirleyin](https://purchase.aspose.com/buy) lisanslama seçenekleri ve satın alma ayrıntıları için.

### S5: Aspose.3D for .NET'in ayrıntılı belgelerini nerede bulabilirim?

 A5: Kapsamlı bölüme bakın[Aspose.3D .NET Belgeleri](https://reference.aspose.com/3d/net/) derinlemesine bilgi için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
