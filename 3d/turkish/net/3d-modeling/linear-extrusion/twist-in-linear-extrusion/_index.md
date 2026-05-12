---
date: 2026-03-23
description: Aspose.3D for .NET kullanarak bükülmüş ekstrüzyon oluşturmayı öğrenin.
  Bu adım adım rehber, lineer ekstrüzyon bükülme tekniklerini kapsar.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Doğrusal Ekstrüzyonda Bükülmeli Ekstrüzyon Nasıl Oluşturulur
url: /tr/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

#Doğru Ekstrüzyonda Burulmalı Ekstrüzyon Nasıl Oluşturulur

## Giriiş

Eğer göz alıcı 3D görsellere ihtiyaç duyan .NET uygulamalarını geliştiriyorsanız, **ekstrüzyon nasıl oluşturulur** temel bir beceri olduğunu yakında keşfedeceksiniz. Aspose.3D for .NET, basit 2‑D profilleri 3‑D modellere dönüştürmek için temiz ve yüksek performanslı bir API sunar—özellikle bir burulmaya eklediğinizde. Bu öğretildiğinde sahneyi kaydederken son OBJ kayıtlarını kaydedene kadar her adım adım adım gösterirz, doğru yönde ekstrüzyon burulması gücü aksiyonunu içinde görebileceksiniz.

## Hızlı Yanıtlar
- **Ekstrüzyon için birincil sınıf nedir?** 'LinearExtrusion'
- **Hangi özellik döndürmeyi ekler?** `Twist`
- **Kaç dilim düzgün sonuçlar verir?** Yaklaşık 100 dilim (gerektiği gibi ayarlayın)
- **Başka şekiller kullanabilir miyim?** Evet, daireler, çokgenler veya özel eğriler gibi herhangi bir 'IProfile'
- **Örnekte hangi dosya formatı kullanıldı?** Wavefront OBJ (`.obj`)

## Önkoşullar

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Aspose.3D for .NET Yüklü. Henüz indirmeyi başardıysanız **[buradan](https://releases.aspose.com/3d/net/)** edinebilirsiniz.
- Çalışan bir .NET geliştirme ortamı (Visual Studio, VS Code veya tercih ettiğiniz herhangi bir IDE).
- C# söz dizimi ve nesne‑yönelimli kavramlara temel bilgililik.

## Ad Alanlarını İçe Aktar

Her .NET projesinde reklamın doğru kullanımı çok önemlidir. Aspose.3D tedavisinden etkili bir şekilde faydalanmak için gerekli reklam alanlarını içeri aktararak başlayın. İşte size rehber olacak bir kod parçası:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım Adım Kılavuz

### Adım 1: Temel Profili Başlatın

Ekstrüde edilecek şekli tanımlayarak başlıyoruz. Bu örnekte kenarları hafif bir eğri vermek için küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Adım 2: 3B Sahne Oluşturun

`Scene` nesnesi, tüm 3‑D varlıkların yaşadığı bir tuval görevi görür. Bunu ekstrüzyonunuzun sahnesi olarak düşünebilirsiniz.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Adım 3: Sol ve Sağ Düğümleri Ekleyin

Düğümler, nesneleri hiyerarşik olarak düzenlemenizi sağlar. Bir düz ekstrüzyon ve bir de burulmuş versiyon için iki kardeş düğüm oluşturacağız.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Adım 4: Sol Düğümde Bükme ile Doğrusal Ekstrüzyon Gerçekleştirin

`Twist` özelliği, profil ekstrüde edilirken ne kadar döneceğini kontrol eder. **0** olarak ayarlandığında klasik düz bir ekstrüzyon elde edilir.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Adım 5: Sağ Düğümde Bükme ile Doğrusal Ekstrüzyon Gerçekleştirin

Şimdi aynı profile %90’lık bir burulma uyguluyoruz. Bu, **linear extrusion twist** etkisini net bir şekilde gösterir.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Adım 6: 3B Sahneyi Kaydedin

Son olarak sahneyi, herhangi bir 3‑D görüntüleyicide açabileceğiniz bir formata dışa aktarın. Örnekte Wavefront OBJ kullanılmıştır, ancak Aspose.3D birçok başka formatı da destekler.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Bükülmeli Doğrusal Ekstrüzyon Neden Kullanılır?

- **Hızlı prototipleme:** 2 boyutlu çizimleri manuel modelleme yapmadan 3 boyutlu parçalara dönüştürün.
- **Tasarım esnekliği:** Spiral, helisel nervürler veya dekoratif özellikler oluşturmak için `Büküm` değerini ayarlayın.
- **Performans dostu:** `Dilimler` parametresi, görsel kalite ve çalışma hızı arasında denge kurmanızı sağlar.

## Sık Karşılaşılan Sorunlar ve İpuçları

- **Çok fazla dilim:** 100 dilim pürüzsüz görünse de, aşırı yüksek değerler işleme hızını yavaşlatabilir. Performans endişe kaynağı haline gelirse daha düşük sayılarla test edin.
- **Negatif bükülme değerleri:** Negatif bir `Büküm` ters yönde döndürür; aynalı tasarımlar için kullanışlıdır.
- **Dosya yolları:** Çıktı dizininin mevcut olduğundan ve yazma izinlerinizin olduğundan emin olun; aksi takdirde `scene.Save` bir istisna fırlatacaktır.

## Çözüm

Bu öğretilirde **ekstrüzyon nasıl oluşturulur**, Aspose.3D for .NET kullanarak bir burulma ile gösterildik. `Twist` ve `Slices` özelliklerini ayarlayarak basit burulmuş çubuklardan karmaşık helisel yapılara kadar çok çeşitli sunulabilir oluşturabilirsiniz; toplamda sadece birkaç satır kodla mümkün.

## Sıkça Sorulan Sorular

**S: Diğer şekillere bükümlü doğrusal ekstrüzyon uygulayabilir miyim?**
C: Kesinlikle! 'IProfile' uygulayan herhangi bir sınıf ("CircleShape", "PolygonShape" veya özel bir spline gibi) bir bükülme ile ekstrüze edilebilir.

**S: 'Twist' özelliği aslında neyi temsil ediyor?**
A: Ekstrüzyon uzunluğu boyunca profile uygulanan toplam dönüş açısını (derece cinsinden) belirtir.

**S: Dilim sayısını artırmak bellek kullanımını etkiler mi?**
C: Evet, daha fazla dilim daha fazla köşe ve yüz oluşturur, bu da ek bellek tüketir ve düşük özellikli cihazlarda performansı etkileyebilir.

**S: Doğrusal ekstrüzyonu diğer Aspose.3D özellikleriyle birleştirebilir miyim?**
C: Kesinlikle. Daha zengin modeller oluşturmak için ekstrüzyondan sonra malzemeler, dokular veya hatta Boolean işlemleri uygulayabilirsiniz.

**S: Diğer geliştiricilerle yardım veya fikir alışverişi yapabileceğim yer neresi?**
C: Destek, örnekler ve tartışmalar için **[Aspose Forum](https://forum.aspose.com/c/3d/18)** adresindeki Aspose.3D topluluğuna katılın.

---

**Son Güncelleme:** 23.03.2026
**Test Edilen Sürüm:** Aspose.3D 24.11 for .NET
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}