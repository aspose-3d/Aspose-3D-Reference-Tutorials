---
date: 2026-01-09
description: Aspose.3D for .NET kullanarak 3D sahne oluşturmayı, wavefront OBJ ihracatını
  ve lineer ekstrüzyonda bükme ofsetini nasıl yapacağınızı öğrenin.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Doğrusal Ekstrüzyonda Burulma Ofseti ile 3D Sahne Nasıl Oluşturulur
url: /tr/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahne Oluşturma: Doğrusal Ekstrüzyonda Burulma Ofseti

## Giriş

**3d sahne** nesnelerini hızlıca oluşturmak ve dinamik geometri eklemek istiyorsanız, Aspose.3D for .NET tam da ihtiyacınız olan araçları sunar. Bu **Aspose 3D öğreticisinde** *burulma ofseti* tekniğini **doğrusal ekstrüzyon burulması** yaparken nasıl uygulayacağınızı adım adım gösterecek ve sonunda **Wavefront OBJ** dosyalarını dışa aktaracağız. Sonunda, renderlama ya da daha ileri işleme için hazır, tam özellikli bir 3‑D modeliniz olacak.

## Hızlı Yanıtlar
- **“burulma ofseti” ne işe yarar?** Burulmanın başlangıç noktasını ekstrüzyon ekseni boyunca kaydırır.  
- **Wavefront OBJ dosyasını dışa aktaran yöntem hangisidir?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Test için geçici bir lisans yeterlidir; üretim ortamı için tam lisans gereklidir.  
- **Hangi .NET sürümleri destekleniyor?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Pürüzsüz burulmalar için kaç dilim önerilir?** Kalite ve performans arasında iyi bir denge sağlamak için yaklaşık 100 dilim yeterlidir.

## **create 3d scene** nedir?

3‑D sahne oluşturmak, geometri, ışıklar, kameralar ve dönüşümler içeren hiyerarşik bir yapı kurmak anlamına gelir. Aspose.3D, eklediğiniz tüm düğümleri tutan kök konteyner görevi gören bir `Scene` sınıfı sağlar.

## Neden **linear extrusion twist** kullanmalı?

Burulmalı doğrusal ekstrüzyon, 2‑D bir profili spiral bir 3‑D nesneye dönüştürmenizi sağlar—vida, yay veya dekoratif sütunlar için mükemmeldir. Burulma ofseti eklemek, dönüşün başlangıcını daha fazla kontrol etmenizi sağlar ve asimetrik tasarımlara imkan tanır.

## Önkoşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- Aspose.3D for .NET Kütüphanesi: Kütüphaneyi [release sayfasından](https://releases.aspose.com/3d/net/) indirin ve kurun.  
- Geliştirme Ortamınız: .NET geliştirme için Visual Studio 2022 (veya herhangi bir C# IDE) hazır olmalı.

## Ad Alanlarını İçe Aktarın

Aspose.3D işlevselliğine erişmek için gerekli ad alanlarını içe aktararak başlayın.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım‑Adım Kılavuz

### Adım 1: Temel Profili Başlat  

Ekstrüzyon yapılacak profil olarak küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanacağız.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Adım 2: Bir Sahne Oluştur  

Bu, **create 3d scene** düğümlerini ekleyeceğimiz konteynerdir.

```csharp
Scene scene = new Scene();
```

### Adım 3: Düğümler Oluştur  

Kök düğüme iki kardeş düğüm eklenir – biri normal ekstrüzyon, diğeri ofsetli versiyon için.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Adım 4: Sol Düğümde Doğrusal Ekstrüzyon (temel burulma)  

Burada, herhangi bir ofset olmadan klasik bir **linear extrusion twist** gösteriyoruz.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Adım 5: Sağ Düğümde **Burulma Ofseti** ile Doğrusal Ekstrüzyon  

Şimdi `TwistOffset` vektörünü sağlayarak **how to twist offset** tekniğini uyguluyoruz.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Adım 6: **Wavefront OBJ** Dışa Aktar  

Son olarak, oluşturulan sahneyi bir OBJ dosyasına kaydediyoruz; böylece herhangi bir standart 3‑D görüntüleyicide açabilirsiniz.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Yaygın Sorunlar ve İpuçları

- **Burulma düz görünüyor mu?** Daha pürüzsüz geometri için `Slices` değerini artırın.  
- **Ofset görünmüyor mu?** `TwistOffset` vektörünün sıfır olmadığından ve ekstrüzyon yönüyle hizalandığından emin olun.  
- **OBJ dosyasında dokular eksik mi?** OBJ yalnızca geometriyi saklar; gerekiyorsa malzeme tanımları için MTL dosyalarını kullanın.

## Sıkça Sorulan Sorular

**S: Aspose.3D for .NET'i başka programlama dilleriyle kullanabilir miyim?**  
C: Aspose.3D öncelikle .NET dillerine yöneliktir, ancak Java ve diğer platformlar için eşdeğer kütüphaneler mevcuttur.

**S: Aspose.3D for .NET için geçici bir lisans nasıl alınır?**  
C: Test amaçlı geçici lisans almak için [bu bağlantıyı](https://purchase.aspose.com/temporary-license/) ziyaret edin.

**S: Aspose.3D for .NET için bir topluluk forumu var mı?**  
C: Kesinlikle! Diğer geliştiricilerle etkileşimde bulunmak ve yardım almak için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresine katılın.

**S: Ek örnekler ve dokümantasyon bulunuyor mu?**  
C: Kapsamlı kılavuzlar ve örnekler için [dokümantasyonu](https://reference.aspose.com/3d/net/) inceleyin.

**S: Aspose.3D for .NET'i nereden satın alabilirim?**  
C: Tam potansiyelini açmak için [bu bağlantıyı](https://purchase.aspose.com/buy) kullanarak satın alın.

## Sonuç

Bu **aspose 3d tutorial** içinde **create 3d scene** oluşturmayı, **linear extrusion twist** uygulamayı, **twist offset** kontrol etmeyi ve **Wavefront OBJ** dosyalarını dışa aktarmayı öğrendiniz. Bu teknikler, birkaç satır kodla herhangi bir 3‑D projeye sofistike, burulmuş geometri eklemenizi sağlar.

---

**Son Güncelleme:** 2026-01-09  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}