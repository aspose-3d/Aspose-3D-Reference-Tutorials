---
date: 2026-01-07
description: Aspose.3D for .NET ile lineer ekstrüzyon yaparken yer düzlemi eklemeyi
  öğrenin ve Wavefront OBJ dosyalarını dışa aktarın. 3‑B modellemede merkezleme ve
  yerleştirme tekniklerinde ustalaşın.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Doğrusal Ekstrüzyonda Zemin Düzlemi ve Merkez Ekle
url: /tr/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Linear Extrusion'da Zemin Düzlemi Ekleme ve Merkezleme

## Giriş

Aspose.3D for .NET kullanarak lineer ekstrüzyonu ustalaşmak için bu kapsamlı rehbere hoş geldiniz. Modellerinize **zemin düzlemi ekleme** ve **Wavefront OBJ** dosyalarını dışa aktarmak istiyor, aynı zamanda ekstrüzyonu merkezde tutmak istiyorsanız doğru yerdesiniz. Bu öğreticide, lineer ekstrüzyon tekniğine, özellikle merkezleme yönüne ve bir ground plane'in sonucu daha net görselleştirmenize nasıl yardımcı olduğuna değineceğiz.

## Hızlı Yanıtlar
- **“add ground plane” ne işe yarar?** Görsel bir referans sunar ve ekstrüzyonun X‑Z düzleminde nerede durduğunu kolayca görmenizi sağlar.  
- **Modeli dışa aktarmak için hangi format kullanılır?** Sahne bir Wavefront OBJ dosyası (`FileFormat.WavefrontOBJ`) olarak kaydedilir.  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme yeterlidir; üretim için kalıcı bir lisans gereklidir.  
- **Ekstrüzyon uzunluğunu değiştirebilir miyim?** Evet – `LinearExtrusion`'ın ikinci parametresini değiştirin.  
- **Merkezleme isteğe bağlı mı?** `Center = true` ayarı ekstrüzyonu profilin etrafına ortalar; `false` bir tarafa hizalar.

## Ön Koşullar

Bu heyecan verici yolculuğa başlamadan önce aşağıdaki ön koşulların yerine getirildiğinden emin olun:

- C# programlama diline temel bir anlayış.  
- Makinenizde Visual Studio yüklü.  
- Aspose.3D for .NET kütüphanesi, bunu [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) adresinden indirebilirsiniz.  
- Öğretici boyunca referans için [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) erişiminizin olduğundan emin olun.

## Ad Alanlarını İçe Aktarma

Başlamak için gerekli ad alanlarını içe aktaralım. Bunlar 3D modelleme başyapıtımızın temelini oluşturacak.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Adım 1: Temel Profili Başlatma

Ekstrüzyon yapılacak dikdörtgen bir profil tanımlayarak başlıyoruz. `RoundingRadius` köşelere hafif bir yuvarlama ekler.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Adım 2: 3D Sahne Oluşturma

`Scene` nesnesi tüm geometri, ışık ve kameralar için bir konteyner görevi görür.

```csharp
Scene scene = new Scene();
```

## Adım 3: Sol ve Sağ Düğümler Oluşturma

Kök altında iki kardeş düğüm oluşturulur. Biri ekstrüzyonu **merkezlemeden** gösterirken, diğeri **merkezleyerek** gösterir. Ayrıca sol düğümü çevirerek iki örneğin üst üste gelmesini önleriz.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Adım 4: Sol Düğümde Lineer Ekstrüzyon (Merkezleme Yok)

Burada profili merkezlemeden ekstrüzyon yapıyoruz. `Center = false` bayrağına dikkat edin.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Adım 5: Referans İçin Zemin Düzlemi Ekleme (Sol Düğüm)

İnce bir kutu eklemek bir **ground plane** görevi görür, böylece ekstrüzyonun tabana nasıl oturduğunu net bir şekilde görebilirsiniz.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Adım 6: Sağ Düğümde Lineer Ekstrüzyon (Merkezleme ile)

Şimdi aynı profili ekstrüzyon yapıyoruz ancak merkezlemeyi etkinleştiriyoruz. Geometri, profilin orijini etrafında simetrik olarak yerleştirilecektir.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Adım 7: Referans İçin Zemin Düzlemi Ekleme (Sağ Düğüm)

Sağ düğüme ikinci bir ground plane eklenir, böylece görsel karşılaştırma tutarlı kalır.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Adım 8: Wavefront OBJ Dosyasını Dışa Aktarma

Son olarak, sonucu herhangi bir standart 3‑D görüntüleyicide açabilmek için **Wavefront OBJ** dışa aktarırız.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Neden Ground Plane Eklenir?

Ground plane eklemek, ekstrüzyonun yüksekliği ve hizalaması hakkında anlık bir görsel ipucu sağlar. Bu öğreticide gösterildiği gibi, merkezli ve merkezsiz sonuçları karşılaştırmanız gerektiğinde özellikle faydalıdır.

## Yaygın Sorunlar ve İpuçları

- **Ground plane görünmüyor:** `Box` yapıcısındaki (`0.01`) plane kalınlığının ekstrüzyonu gizlemeyecek kadar küçük, ancak render edilmesi için yeterli büyük olduğundan emin olun.  
- **Dışa aktarma başarısız:** Çıktı dizininin var olduğunu ve yazma izinlerinizin olduğunu doğrulayın.  
- **Merkezlenmiş ekstrüzyon kaymış görünüyor:** `Center` özelliğini tekrar kontrol edin; `true` profili ortalar, `false` bir tarafa hizalar.

## Sık Sorulan Sorular

### S1: Aspose.3D for .NET'i başka programlama dilleriyle kullanabilir miyim?
C1: Aspose.3D öncelikle C# ve VB.NET gibi .NET dillerini destekler.

### S2: Aspose.3D ile ilgili sorular için nereden destek bulabilirim?
C2: Ayrı destek ve tartışmalar için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

### S3: Aspose.3D for .NET için ücretsiz deneme mevcut mu?
C3: Evet, ücretsiz denemeye [buradan](https://releases.aspose.com/) erişebilirsiniz.

### S4: Aspose.3D for .NET için geçici lisans nasıl alabilirim?
C4: Geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

### S5: Aspose.3D for .NET lisansını nereden satın alabilirim?
C5: Lisansınızı [buradan](https://purchase.aspose.com/buy) satın alabilirsiniz.

### S6: OBJ dışındaki diğer formatlara sahneyi dışa aktarabilir miyim?
C6: Evet, Aspose.3D STL, FBX ve GLTF gibi birçok formatı destekler. `Save` metodundaki `FileFormat` enum değerini değiştirmeniz yeterlidir.

### S7: Ekstrüzyonun dilim sayısını nasıl değiştiririm?
C7: Mesh yoğunluğunu kontrol etmek için `LinearExtrusion` yapıcısındaki `Slices` özelliğini ayarlayın.

---

**Son Güncelleme:** 2026-01-07  
**Test Edilen Versiyon:** Aspose.3D for .NET en son sürüm  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}