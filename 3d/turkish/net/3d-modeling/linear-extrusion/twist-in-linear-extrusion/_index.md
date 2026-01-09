---
date: 2026-01-09
description: Aspose.3D kullanarak .NET'te 3D sahne oluşturmayı öğrenin ve lineer ekstrüzyon
  bükme teknikleriyle bükülmüş ekstrüzyonu keşfedin.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: 3D Sahne Oluştur .NET – Doğrusal Ekstrüzyonda Burulma
url: /tr/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahne .NET Oluşturma – Doğrusal Ekstrüzyonda Burulma

## Giriş

.NET geliştirme dünyası sürekli evrim geçirirken, 3D grafiklerin gücünden yararlanmak heyecan verici bir çabadır. **Aspose.3D for .NET**, geliştiricileri **3D sahne .NET** uygulamaları oluşturma konusunda güçlendiren değerli bir araç seti olarak ortaya çıkıyor; bu uygulamalar hem etkileyici hem de görsel olarak çarpıcıdır. Bu kapsamlı rehberde, ilgi çekici özellik — Doğrusal Ekstrüzyon ile Burulma — ü inceleyecek ve modellerinize dinamik burulmalar ekleyebilmeniz için her adımı ayrıntılı olarak göstereceğiz.

## Hızlı Yanıtlar
- **“create 3d scene .net” ne anlama geliyor?** Aspose.3D kütüphanesini .NET ortamında kullanarak programlı bir şekilde 3‑B sahne oluşturmayı ifade eder.  
- **Bir ekstrüzyona nasıl burulma eklerim?** `LinearExtrusion` nesnesinin `Twist` özelliğini ayarlayın; değer derece cinsinden dönüş açısıdır.  
- **Aspose.3D için lisansa ihtiyacım var mı?** Değerlendirme için ücretsiz deneme sürümü yeterlidir; üretim kullanımı için ticari lisans gereklidir.  
- **Hangi .NET sürümleri destekleniyor?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6 ve sonrası.  
- **`Slices` değeri neyi etkiler?** Daha fazla dilim, daha pürüzsüz bir burulma sağlar ancak bellek ve işlem süresini artırır.

## Doğrusal Ekstrüzyon ile Burulma Nedir?
Doğrusal ekstrüzyon, bir 2‑B profili düz bir yol boyunca süpürürken, **burulma** özelliği profili kademeli olarak döndürerek helisel bir etki yaratır. Bu teknik, yaylar, burulmuş sütunlar veya dekoratif öğeler modellemek için mükemmeldir.

## Neden Aspose.3D Bu İş İçin Kullanılmalı?
- **Basit API** – `LinearExtrusion` ve `RectangleShape` gibi sezgisel sınıflar.  
- **Tam .NET entegrasyonu** – C#, VB.NET ve F# ile sorunsuz çalışır.  
- **Çapraz‑platform çıktı** – OBJ, STL, FBX ve birçok diğer formata dışa aktarım.

## Önkoşullar

Bu 3D yolculuğa başlamadan önce aşağıdaki önkoşulların karşılandığından emin olun:

- Aspose.3D for .NET: Aspose.3D kütüphanesini kurduğunuzdan emin olun. Kurulu değilse, [buradan](https://releases.aspose.com/3d/net/) indirebilirsiniz.

- Temel .NET Geliştirme Bilgisi: Bu öğretici, .NET geliştirme konusunda temel bir anlayış varsayar.

## Ad Alanlarını İçe Aktarma

Her .NET projesinde, ad alanlarının doğru kullanımı kritik öneme sahiptir. Aspose.3D işlevselliğinden tam olarak yararlanmak için gerekli ad alanlarını içe aktararak başlayın. İşte size rehber olacak bir kod parçacığı:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Linear Extrusion Twist ile 3d scene .net nasıl oluşturulur

Aşağıda, **3D sahne .NET** oluşturup doğrusal ekstrüzyona bir burulma uygulamanın tam adım adım açıklaması yer almaktadır.

### Adım 1: Temel Profili Başlatma

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Bir dikdörtgen profil tanımlayarak başlıyoruz. İsterseniz köşeleri yumuşatmak için `RoundingRadius` değerini ayarlayın.

### Adım 2: 3D Sahne Oluşturma

```csharp
// Create a scene 
Scene scene = new Scene();
```

`Scene` nesnesi, tüm 3‑B nesnelerinin yaşayacağı tuval görevi görür.

### Adım 3: Sol ve Sağ Düğümleri Oluşturma

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Düğümler, geometrinin konteynerleridir. Burada, burulmamış bir ekstrüzyonu (sol) ve burulmuş bir ekstrüzyonu (sağ) karşılaştırabilmek için iki düğüm oluşturuyoruz. Görsel ayrım için sol düğüm X‑ekseni üzerinde 15 birim kaydırılır.

### Adım 4: Sol Düğümde Burulsuz Doğrusal Ekstrüzyon

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Burada `Twist` **0°** olarak ayarlanmıştır; bu, düz bir ekstrüzyon üretir. **100** `Slices` değeri, pürüzsüz bir yüzey sağlar.

### Adım 5: Sağ Düğümde Burulmalı Doğrusal Ekstrüzyon

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

`Twist = 90` ayarı, profilin ekstrüzyon uzunluğu boyunca tam 90 derece dönmesini sağlar ve belirgin bir heliks oluşturur.

### Adım 6: 3D Sahneyi Kaydetme

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Sahne, OBJ dosyası olarak dışa aktarılır; bu dosyayı çoğu 3‑B görüntüleyicide açabilir veya diğer iş akışlarına aktarabilirsiniz.

## Yaygın Sorunlar ve Çözümleri

| Sorun | Neden Oluşur | Çözüm |
|-------|--------------|------|
| **Burulma düz görünüyor** | `Slices` değeri çok düşük, bu da kaba geometri oluşturur. | Daha yüksek `Slices` değeri (ör. 200) kullanarak daha pürüzsüz bir burulma elde edin. |
| **Yüksek `Slices` ile performans düşüyor** | Daha fazla çokgen, daha fazla bellek/CPU gerektirir. | Görsel kaliteyi korurken en düşük `Slices` değerini kullanın veya ekstrüzyondan sonra geometri sadeleştirmeyi etkinleştirin. |
| **Kaydetme sırasında dosya bulunamadı** | Çıktı dizini yolu geçersiz. | Tam mutlak bir yol sağlayın veya `Save` çağrısından önce dizinin var olduğundan emin olun. |

## Sık Sorulan Sorular

**S: Linear Extrusion with a Twist'i başka şekillere de uygulayabilir miyim?**  
C: Kesinlikle! Dikdörtgen dışındaki çeşitli temel profillerle deney yapabilir, tasarım olanaklarını genişletebilirsiniz.

**S: 'Twist' özelliği doğrusal ekstrüzyonda ne işe yarar?**  
C: 'Twist' özelliği, ekstrüzyon sürecindeki dönüş derecesini belirler ve nihai 3D şekli etkiler.

**S: Çok sayıda dilim kullanırken performans kaygıları var mı?**  
C: Daha yüksek dilim sayısı detay ekler ancak performansı etkileyebilir. Uygulamanızın gereksinimlerine göre bir denge kurun.

**S: Linear Extrusion'ı diğer Aspose.3D özellikleriyle birleştirebilir miyim?**  
C: Elbette! Aspose.3D zengin bir özellik seti sunar. Daha karmaşık tasarımlar için Linear Extrusion'ı diğer işlevlerle birleştirmekten çekinmeyin.

**S: Aspose.3D desteği ve tartışmaları için bir topluluk var mı?**  
C: Evet, destek ve etkileşimli tartışmalar için [Aspose Forum](https://forum.aspose.com/c/3d/18) topluluğuna katılabilirsiniz.

---

**Son Güncelleme:** 2026-01-09  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}