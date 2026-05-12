---
date: 2026-03-23
description: Aspose.3D for .NET ile lineer ekstrüzyona bükülme eklemeyi öğrenin ve
  asp.net 3D modelleme projeleri için ekstrüzyonun nasıl kullanılacağını keşfedin.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET kullanarak Doğrusal Ekstrüzyona Burulma Nasıl Eklenir
url: /tr/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Linear Extrusion'da Twist Eklemek Aspose.3D for .NET ile Nasıl Yapılır

## Giriş

Eğer lineer ekstrüzyona **twist ekleme** konusunda net, adım adım bir rehber arıyorsanız doğru yerdesiniz. Bu öğreticide Aspose.3D for .NET ile tam süreci gösterecek, **ekstrüzyonun nasıl kullanılacağını** dinamik 3D şekiller oluşturmak için, *asp.net 3d modeling* senaryolarına uygun bir şekilde anlatacağız. Sonunda twist offset, dilimler ve sonucu OBJ dosyası olarak kaydetmeyi gösteren çalıştırılabilir bir örnek elde edeceksiniz.

## Hızlı Cevaplar
- **“twist offset” ne işe yarar?** Twist'in başlangıç noktasını ekstrüzyon ekseni boyunca kaydırır.  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Test için geçici bir lisans yeterlidir; üretim için tam lisans gereklidir.  
- **Hangi .NET sürümleri destekleniyor?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Dilime sayısını değiştirebilir miyim?** Evet—mesh pürüzsüzlüğünü kontrol etmek için `Slices` özelliğini ayarlayın.  
- **Çıktı formatı sadece OBJ ile mi sınırlı?** Hayır, Aspose.3D birçok formatı destekler; OBJ burada basitlik açısından kullanılmıştır.

## Linear Extrusion'da Twist Offset Nedir?

Bir twist offset, twist işlemi uygulanırken eklenen translasyonel kaymayı tanımlar. Twist, ekstrüzyonun tam başlangıç noktasının etrafında dönmek yerine, belirtilen offset vektöründen itibaren dönmeye başlar; bu da son şekil üzerinde daha fazla sanatsal kontrol sağlar.

## Neden Aspose.3D for .NET Kullanmalı?

- **Full‑featured API** – Profilleri, dönüşümleri ve geniş dosya formatı yelpazesini yönetir.  
- **Cross‑platform** – .NET Core ile Windows, Linux ve macOS'ta çalışır.  
- **Performance‑optimized** – Manuel matematik yapmadan temiz mesh'ler üretir.  
- **Excellent documentation** – Geliştirmeyi hızlandıran çok sayıda örnek sunar.

## Önkoşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- Aspose.3D for .NET Library: Kütüphaneyi [release page](https://releases.aspose.com/3d/net/) üzerinden indirin ve kurun.  
- Geliştirme Ortamınız: Visual Studio, Rider veya C# destekleyen herhangi bir IDE.

## Ad Alanlarını İçe Aktarma

İlk olarak, temel 3D sınıflarına erişmenizi sağlayacak ad alanlarını içe aktarın.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Bu ifadeler `Scene`, `LinearExtrusion`, `Vector3` ve diğer gerekli tipleri kodunuzda kullanılabilir hâle getirir.

## Adım Adım Kılavuz

### Adım 1: Temel Profili Başlat

Basit bir dikdörtgen profil oluşturuyor ve kenarların tamamen keskin olmaması için küçük bir yuvarlama yarıçapı ekliyoruz.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Adım 2: Bir Sahne Oluştur

`Scene`, tüm düğümleri, ışıkları, kameraları ve geometrileri tutan bir kapsayıcı görevi görür.

```csharp
Scene scene = new Scene();
```

### Adım 3: Düğümler Oluştur

Sahne köküne iki çocuk düğüm eklenir—biri düz ekstrüzyon, diğeri twisted versiyon için. Sol düğüm görsel ayrım için X‑ekseni üzerinde kaydırılır.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Adım 4: Sol Düğümde Lineer Ekstrüzyon (Twist Offset Yok)

Burada tam 360° twist ve pürüzsüzlük için 100 dilim içeren temel bir ekstrüzyon gösteriyoruz.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Adım 5: Sağ Düğümde Twist Offset ile Lineer Ekstrüzyon

Şimdi `(3, 0, 0)` twist offset uyguluyoruz. Bu, twist'in başlangıç noktasını X‑ekseni boyunca üç birim kaydırarak gözle görülür bir kaydırılmış heliks oluşturur.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Adım 6: 3D Sahneyi Kaydet

Son olarak sahneyi bir OBJ dosyasına yazıyoruz. Ortamınıza göre çıktı yolunu değiştirin.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|--------------|------|
| **Twist düz görünüyor** | `Slices` değeri çok düşük, bu da kaba bir mesh oluşturur. | Daha pürüzsüz bir dönüş için `Slices` değerini (ör. 200) artırın. |
| **Nesne merkezin dışında** | `TwistOffset` dünya koordinatlarını kullanır; düğüm zaten çevrilmiş olabilir. | Offset'i düğümün yerel dönüşümüne göre uygulayın veya düğüm çevirisini buna göre ayarlayın. |
| **Dosya kaydedilmedi** | Çıktı yolu hatalı veya yazma izni eksik. | Dizin mevcut mu kontrol edin ve uygulamanın yazma izni olduğundan emin olun. |
| **Lisans istisnası** | Geçerli bir lisans olmadan deneme dışı bir derleme çalıştırılıyor. | Sahneyi oluşturmadan önce geçici ya da kalıcı bir lisans yükleyin. |

## Sık Sorulan Sorular

### S1: Aspose.3D for .NET'i diğer programlama dilleriyle kullanabilir miyim?

A1: Aspose.3D öncelikle .NET dillerini destekler, ancak Aspose Java ve diğer platformlar için benzer kütüphaneler sunar.

### S2: Aspose.3D for .NET için geçici bir lisans nasıl alınır?

A2: Test amaçlı geçici lisans edinmek için [bu linki](https://purchase.aspose.com/temporary-license/) ziyaret edin.

### S3: Aspose.3D for .NET için bir topluluk forumu var mı?

A3: Kesinlikle! Diğer geliştiricilerle etkileşimde bulunmak ve destek almak için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresine katılın.

### S4: Ek örnekler ve dokümantasyon mevcut mu?

A4: Ayrıntılı kılavuzlar ve örnekler için [documentation](https://reference.aspose.com/3d/net/) sayfasını inceleyin.

### S5: Aspose.3D for .NET'i nereden satın alabilirim?

A5: Tam potansiyeli açmak için satın alma işlemini [bu linkten](https://purchase.aspose.com/buy) gerçekleştirebilirsiniz.

### S6: Modeli OBJ dışındaki formatlara dışa aktarabilir miyim?

A6: Evet—Aspose.3D FBX, STL, 3MF ve daha birçok formatı destekler. `Save` çağrısındaki `FileFormat` enum değerini değiştirmeniz yeterlidir.

### S7: “twist ekleme” normal bir rotasyondan nasıl farklıdır?

A7: Twist, profilin ekstrüzyon uzunluğu boyunca kademeli olarak döndürülmesini sağlar; normal bir rotasyon ise tek bir sabit açı uygular. Offset, dönüş başlamadan önce bir translasyon kayması ekler.

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D for .NET (latest release)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}