---
date: 2026-03-23
description: Aspose.3D for .NET kullanarak dilimlerle lineer ekstrüzyonun nasıl yapılacağını
  öğrenin. Adım adım kod örnekleriyle ayrıntılı 3D modeller oluşturun.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET Kullanarak Dilimlerle Lineer Ekstrüzyon Nasıl Yapılır
url: /tr/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile Dilim Kullanarak Doğrusal Ekstrüzyon Nasıl Yapılır

## Giriş

Aspose.3D for .NET kullanarak 3D tasarım dünyasına hoş geldiniz! Bu öğreticide **dilimlerle doğrusal ekstrüzyonun** nasıl yapılacağını keşfedeceksiniz; bu teknik, modellerinizdeki detay seviyesini kontrol etmenizi sağlar. İster deneyimli bir geliştirici olun, ister yeni başlıyor olun, her adımı sizinle birlikte yürütüp, her eylemin nedenini açıklayacak ve hemen uygulayabileceğiniz pratik ipuçları sunacağız.

## Hızlı Yanıtlar
- **Dilimli doğrusal ekstrüzyon nedir?** 2B bir profili 3B’ye uzatırken kaç ara kesit (dilim) üretileceğini belirleyen bir yöntemdir.  
- **Neden dilimler kullanılır?** Daha fazla dilim, daha pürüzsüz eğriler; daha az dilim, hafif bir ağ (mesh) sağlar.  
- **Önkoşullar?** Aspose.3D for .NET, .NET uyumlu bir IDE ve temel C# bilgisi.  
- **Tipik çalışma süresi?** Örnek, modern bir PC’de bir saniyenin altında çalışır.  
- **Çıktı formatı?** Örnek Wavefront OBJ’ye kaydedilir, ancak Aspose.3D birçok formatı destekler.

## Dilimli Doğrusal Ekstrüzyon Nedir?

Doğrusal ekstrüzyon, bir 2‑B şekli (profil) düz bir hat boyunca uzatarak 3‑B bir katı oluşturur. **Slices** özelliği, ekstrüzyonun başlangıcı ile sonu arasına kaç ara kesit ekleneceğini belirler; bu da pürüzlülük ve çokgen sayısını etkiler.

## Dilimleri Neden Kullanmalıyız?

- **Ağ Yoğunluğunu Kontrol Et:** Görsel kalite ile dosya boyutu arasındaki dengeyi ince ayar yap.  
- **Performansı Optimize Et:** Gerçek zamanlı uygulamalar için daha az dilim, yüksek çözünürlüklü renderlar için daha çok dilim kullan.  
- **Yaratıcı Esneklik:** Farklı nesnelerde farklı dilim sayılarıyla tasarım amacını vurgula.

## Önkoşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- Aspose.3D for .NET Kütüphanesi – indirmek için [buraya](https://releases.aspose.com/3d/net/) tıklayın.  
- C# destekli bir IDE (Visual Studio, Rider, VS Code vb.).  
- C# sözdizimi ve nesne‑yönelimli kavramlara temel aşinalık.  
- 3‑B geometriyle deneme yapma merakı!

## Ad Alanlarını İçe Aktar

İlk olarak, temel Aspose.3D sınıflarına erişmenizi sağlayacak ad alanlarını içe aktarın.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım‑Adım Kılavuz

### Adım 1: Temel Profili Başlat

Köşeleri tamamen keskin olmayan, küçük bir yuvarlama yarıçapına sahip basit bir dikdörtgen şekliyle başlıyoruz.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Adım 2: 3B Sahneyi Oluştur

`Scene`, tüm düğümler, ağlar, ışıklar ve kameralar için bir kapsayıcı görevi görür.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Adım 3: Sol ve Sağ Düğümleri Ekle

Sahnenin kökünün altında iki kardeş düğüm oluşturacağız. Sol düğüm düşük dilim sayısı alırken, sağ düğüm yüksek dilim sayısı alacak; böylece görsel farkı karşılaştırabilirsiniz.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Adım 4: Sol Düğümde Doğrusal Ekstrüzyon Yap (Düşük Detay)

Burada dikdörtgeni sadece **2 dilim** ile ekstrüde ediyoruz. Bu, hızlı ön izlemeler için uygun kaba bir ağ üretir.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Adım 5: Sağ Düğümde Doğrusal Ekstrüzyon Yap (Yüksek Detay)

Şimdi **10 dilim** kullanarak çok daha pürüzsüz bir sonuç elde ediyoruz. Geometrinin nasıl daha ince hale geldiğine dikkat edin.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Adım 6: 3B Sahneyi Kaydet

Son olarak sahneyi bir OBJ dosyasına yazdırın. `"Your Output Directory"` ifadesini makinenizde geçerli bir yol ile değiştirin.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|--------------|------|
| **Dosya oluşturulmadı** | Çıktı yolu geçersiz veya yazma izni yok. | Mutlak bir yol kullanın ve klasörün var olduğundan emin olun. |
| **Nesne düz görünüyor** | `Slices` 1 veya 0 olarak ayarlanmış. | Görünür bir ekstrüzyon için `Slices` değerini en az 2 yapın. |
| **Beklenmeyen geometri** | Yuvarlama yarıçapı, dikdörtgen boyutuna göre çok büyük. | `RoundingRadius` değerini, dikdörtgenin en kısa kenarının yarısından küçük bir değere ayarlayın. |

## Sık Sorulan Sorular

**S: Ekstrüzyon yönünü değiştirebilir miyim?**  
C: Evet. Düğümün `Transform` özelliğini kullanarak ekstrüde edilen geometriyi kaydetmeden önce döndürebilir veya taşıyabilirsiniz.

**S: Aspose.3D başka ekstrüzyon tiplerini destekliyor mu?**  
C: Kesinlikle. `LinearExtrusion` dışında `RevolveExtrusion`, `SweepExtrusion` ve daha fazlasını kullanabilirsiniz.

**S: Hangi dosya formatlarına dışa aktarabilirim?**  
C: Aspose.3D OBJ, STL, FBX, 3MF, Collada ve birçok başka formatı destekler. Sadece `FileFormat` enum’ını değiştirin.

**S: Programatik olarak bir materyal ayarlamak mümkün mü?**  
C: Evet. Düğüm oluşturulduktan sonra, `Entity` koleksiyonuna bir `Material` atayın.

**S: Dilim sayısı bellek kullanımını nasıl etkiler?**  
C: Daha fazla dilim, vertex ve yüz sayısını artırır; bu da bellek tüketimini orantılı olarak yükseltir. Hedef platformunuz için uygun dengeyi bulmak amacıyla profil oluşturmayı kullanın.

## Orijinal SSS'ler

### S1: Aspose.3D for .NET'i başka programlama dilleriyle kullanabilir miyim?

C1: Aspose.3D öncelikle .NET için tasarlanmıştır, ancak .NET bağlayıcılarıyla Python gibi dillerde birlikte çalışabilirlik seçeneklerini keşfedebilirsiniz.

### S2: Aspose.3D for .NET için ayrıntılı belgeleri nereden bulabilirim?

C2: Aspose.3D'nin yetenekleri ve kullanımı hakkında derinlemesine bilgi için [buradaki](https://reference.aspose.com/3d/net/) belgeleri inceleyin.

### S3: Aspose.3D for .NET için ücretsiz deneme sürümü var mı?

C3: Evet, kütüphanenin özelliklerini satın almadan önce keşfetmek için ücretsiz denemenizi [buradan](https://releases.aspose.com/) alabilirsiniz.

### S4: Aspose.3D for .NET için teknik destek nasıl alınır?

C4: Yardım almak ve toplulukla etkileşime geçmek için Aspose.3D forumuna [buradan](https://forum.aspose.com/c/3d/18) ulaşın.

### S5: Aspose.3D for .NET için geçici bir lisans kullanabilir miyim?

C5: Evet, değerlendirme amaçlı geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

## Sonuç

Artık Aspose.3D for .NET kullanarak dilimlerle **doğrusal ekstrüzyon** yapmayı, farklı dilim sayıların etkisini görmeyi ve çalışmalarınızı dışa aktarmayı öğrendiniz. Başka profillerle deney yapın, `Slices` değerini oynatın ve materyal ya da ışık ekleyerek üretim‑hazır 3‑B varlıklar oluşturun.

---

**Son Güncelleme:** 2026-03-23  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET (yazım anındaki en yeni sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}