---
date: 2026-01-14
description: Aspose.3D for .NET kullanarak 3D sahnelerde küpü nasıl canlandıracağınızı
  öğrenin. Bu kılavuz, animasyon eğrisi oluşturmayı, anahtar kareleri bağlamayı ve
  3D özellikleri canlandırmayı gösterir.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET ile 3D Ortamlarda Küpü Nasıl Canlandırılır
url: /tr/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile 3D Sahnelere Küp Nasıl Canlandırılır

## Giriş

.NET'te 3D sahne oluşturma ve animasyon dünyasına dalıyorsanız, Aspose.3D sizin başvuru aracınızdır. Bu adım adım rehberde, **küp nasıl canlandırılır** nesnelerini özelliklerini canlandırarak, animasyon eğrileri oluşturarak ve anahtar kareler bağlayarak inceleyeceğiz. Sonunda, popüler 3D formatlarına aktarabileceğiniz tamamen canlandırılmış bir küp elde edeceksiniz.

## Hızlı Yanıtlar
- **Hangi kütüphane kullanılıyor?** Aspose.3D for .NET  
- **Bu öğreticinin kapsadığı birincil görev nedir?** 3D sahnede küp nasıl canlandırılır  
- **Ana adımlar?** Ad alanlarını içe aktar, bir sahne oluştur, anahtar kareleri bağla, dosyayı kaydet  
- **Lisans gerekli mi?** Öğrenme için ücretsiz deneme yeterlidir; üretim için ticari lisans gerekir  
- **Desteklenen çıktı formatı?** FBX (ASCII 7500) ve Aspose.3D tarafından desteklenen diğerleri  

## Aspose.3D'de “küp nasıl canlandırılır” nedir?
Bir küpü canlandırmak, zaman içinde anahtar kare verileri kullanarak dönüşüm özelliklerini (örneğin Translation, Rotation veya Scale) değiştirmek anlamına gelir. Aspose.3D, sahne düğümlerinde doğrudan **animasyon eğrileri** oluşturmak, **anahtar kareleri bağlamak** ve **3D özelliklerini canlandırmak** için temiz bir API sağlar.

## Neden Aspose.3D ile bir küp canlandırılır?
- **Tam .NET entegrasyonu** – .NET Framework, .NET Core ve .NET 5/6 ile çalışır.  
- **Harici bağımlılık yok** – basit animasyonlar için Unity veya diğer motorlara ihtiyaç yok.  
- **Dışa aktarma esnekliği** – canlandırılmış sahneler, sonraki işlem hatları için FBX, OBJ, GLTF vb. formatlarda kaydedilebilir.

## Önkoşullar

Bu heyecan verici yolculuğa başlamadan önce, aşağıdaki önkoşulların yerine getirildiğinden emin olun:

- Aspose.3D for .NET: Kütüphanenin kurulu olduğundan emin olun. [Aspose.3D web sitesinden](https://releases.aspose.com/3d/net/) indirebilirsiniz.  
- C# Bilgisi: C# programlama diline aşina olmak, örnekleri anlamak ve uygulamak için gereklidir.  
- Entegre Geliştirme Ortamı (IDE): Örneklerle birlikte kodlamak için Visual Studio gibi tercih ettiğiniz IDE'yi kullanın.  
- Temel 3D Sahne Kavramları: Temel 3D sahne kavramlarına hakim olmak öğrenme sürecinizi kolaylaştıracaktır.

## Ad Alanlarını İçe Aktarma

C# kodunuzda, Aspose.3D için gerekli ad alanlarını içe aktardığınızdan emin olun. İşte gereken set:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Adım 1: Sahne Nesnesini Başlatma

Düğüm ve animasyonlarımızın hepsini tutacak boş bir sahne oluşturun.

```csharp
Scene scene = new Scene();
```

## Adım 2: Polygon Builder Kullanarak Mesh Oluşturma

Yardımcı yöntem `Common.CreateMeshUsingPolygonBuilder()` kullanarak basit bir küp mesh'i oluşturuyoruz.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Adım 3: Küp Düğümleri Oluşturma

Küp mesh'ini sahneye kök düğümün bir alt düğümü olarak ekleyin. **cube1** düğüm adı, daha sonra anahtar kareleri bağladığımızda kullanılacak.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Adım 4: Translation Özelliğini Bulma

Küpün konumunu canlandırmak için, düğümün dönüşümündeki **Translation** özelliğini bulmamız gerekir.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Adım 5: Bind Point Oluşturma

`BindPoint`, bir sahne özelliğini animasyon eğrisine bağlar. Burada translation özelliğini bağlıyoruz.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Adım 6: X Bileşeninde Animasyon Eğrisi Bağlama

Şimdi **X** ekseni için bir animasyon eğrisi oluşturuyoruz. Bu, **animasyon eğrisi oluşturma** adımını gösterir ve **anahtar kareleri bağlamayı** gösterir.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Adım 7: Z Bileşeninde Animasyon Eğrisi Bağlama

Benzer şekilde, küpe daha dinamik bir hareket yolu vermek için **Z** eksenini canlandırıyoruz.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Adım 8: 3D Sahneyi Kaydetme

Canlandırılmış sahneyi bir FBX dosyasına dışa aktarın. `FBX7500ASCII` formatı 3D araçları tarafından geniş çapta desteklenir.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Adım 9: Başarı Mesajını Görüntüleme

Kullanıcıya animasyonun başarıyla eklendiğine dair geri bildirim verin.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| Hareket gözlemlenmedi | Anahtar kare zamanları oynatma aralığıyla eşleşmiyor | Sahnenin animasyon zaman çizelgesinin anahtar kare zamanlarını (bu örnekte 0‑5 saniye) kapsadığından emin olun. |
| Yanlış dosya yolu | `output` var olmayan bir dizine işaret ediyor | Önce dizini oluşturun veya mutlak bir yol kullanın. |
| Lisans istisnası | Üretimde geçerli bir lisans olmadan çalıştırmak | `Scene` oluşturulmadan önce Aspose.3D lisansınızı uygulayın. |

## Sıkça Sorulan Sorular

### Q1: Aspose.3D belgelerini nerede bulabilirim?
A1: Belgelere [buradan](https://reference.aspose.com/3d/net/) ulaşabilirsiniz.

### Q2: Aspose.3D for .NET'i nasıl indirebilirim?
A2: İndirmeyi [sürüm sayfasından](https://releases.aspose.com/3d/net/) yapabilirsiniz.

### Q3: Ücretsiz deneme mevcut mu?
A3: Evet, ücretsiz denemeyi [buradan](https://releases.aspose.com/) alabilirsiniz.

### Q4: Aspose.3D için destek nereden alınır?
A4: Destek için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### Q5: Geçici bir lisans alabilir miyim?
A5: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

## Ek FAQ (AI‑Optimizeli)

**S: Rotasyon veya ölçek gibi diğer özellikleri canlandırabilir miyim?**  
C: Kesinlikle. Aynı şekilde `cube1.Transform.FindProperty("Rotation")` veya `"Scale"` kullanıp anahtar kare dizilerini bağlayabilirsiniz.

**S: Aspose.3D Bezier ve Linear dışındaki anahtar kare enterpolasyon tiplerini destekliyor mu?**  
C: Evet, daha fazla kontrol için `Interpolation.Step` ve `Interpolation.Cubic` da desteklenir.

**S: Dışa aktarmadan önce animasyonu nasıl ön izleyebilirim?**  
C: Aspose.3D API'si basit bir görüntüleyici sunar; alternatif olarak, dışa aktarılan FBX'i Autodesk FBX Review gibi bir 3D görüntüleyicide açabilirsiniz.

**S: Birden fazla küpü aynı anda canlandırmak mümkün mü?**  
C: Her küp için ayrı düğümler oluşturun, ilgili özelliklerini alın ve bağımsız anahtar kare dizilerini bağlayın.

## Sonuç

Tebrikler! Aspose.3D for .NET kullanarak bir 3D sahnede **küp nasıl canlandırılır** konusunu yeni öğrendiniz. Artık **animasyon eğrileri oluşturma**, **anahtar kareleri bağlama** ve **3D özelliklerini canlandırma** konusunda bilginiz var ve statik geometrileri hayata geçirebiliyorsunuz. Rotasyonlar, ölçeklendirme veya hatta morf hedefleriyle denemeler yaparak animasyon araç setinizi genişletebilirsiniz.

---

**Son Güncelleme:** 2026-01-14  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}