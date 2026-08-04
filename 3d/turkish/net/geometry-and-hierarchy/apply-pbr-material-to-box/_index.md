---
date: 2026-04-12
description: Aspose.3D for .NET kullanarak bir kutuya pbr malzeme uygulamayı, pbr
  malzeme oluşturmayı ve fiziksel tabanlı renderleme ile STL ASCII dosyalarını dışa
  aktarmayı öğrenin.
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: PBR Malzemesini Kutuya Uygulama
second_title: Aspose.3D .NET API
title: Bir Kutuya PBR Malzeme Nasıl Uygulanır
url: /tr/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kutuya PBR Malzemesi Nasıl Uygulanır

## Giriş

3D grafiklerin büyüleyici dünyasına hoş geldiniz! Bu adım adım öğreticide, **bir kutuya pbr** malzemesinin nasıl uygulanacağını Aspose.3D for .NET kullanarak öğreneceksiniz. PBR malzemesi oluşturmayı, bir mesh'e eklemeyi ve sonunda **STL ASCII dışa aktarmayı** adım adım göstereceğiz, böylece modeli herhangi bir sonraki iş akışında kullanabilirsiniz. İster bir oyun prototipi, bir ürün görselleştirici, ister 3D baskı için hızlı bir prototip oluşturuyor olun, bu iş akışını öğrenmek .NET uygulamalarınızda gerçekçi, fiziksel tabanlı render (PBR) kapısını açar.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Bir kutuya PBR malzemesi uygulamak ve STL ASCII olarak dışa aktarmak.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for .NET (aspose nasıl kullanılır).  
- **Lisans gerekiyor mu?** Evet, üretim için geçici veya tam lisans gereklidir.  
- **Desteklenen çıktı formatı?** STL ASCII (export stl ascii) ve birçok diğer 3D formatı.  
- **Ne kadar sürer?** Temel bir uygulama için yaklaşık 10‑15 dakika.

## PBR Malzemesi Nedir?
Fiziksel Tabanlı Render (PBR), ışığın gerçek dünya yüzeyleriyle nasıl etkileşime girdiğini simüle eden bir gölgelendirme modelidir. Metalik ve pürüzlülük gibi özellikleri ayarlayarak, karmaşık shader'ları elle ayarlamadan son derece gerçekçi sonuçlar elde edebilirsiniz.

## Fiziksel Tabanlı Render (PBR) Neden Kullanılır?
- **Gerçekçilik:** Malzemeler ışığa gerçek fizik kurallarına uygun bir şekilde tepki verir.  
- **Tutarlılık:** Aynı malzeme her ışık ortamında doğru görünür.  
- **Verimlilik:** Modern GPU'lar PBR hesaplamaları için optimize edilmiştir, bu da size ücretsiz performans sağlar.

## Ön Koşullar

Kodun içine dalmadan önce aşağıdakilere sahip olduğunuzdan emin olun:

### Aspose.3D for .NET'i İndirin ve Kurun
Detaylı indirme ve kurulum talimatları için [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) sayfasını ziyaret edin.

### Lisans Edinin
Aspose.3D'nin tam potansiyelini açmak için geçerli bir lisans alın. Geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) veya tam lisansı [buradan](https://purchase.aspose.com/buy) edinebilirsiniz.

## Ad Alanlarını İçe Aktarın
İlk olarak, Aspose.3D for .NET'in yeteneklerinden faydalanmak için gerekli ad alanlarını içe aktardığınızdan emin olun:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Adım Adım Kılavuz

### Adım 1: Bir Sahne Başlatın
Boş bir 3D sahne oluşturarak başlayın. Bu konteyner, daha sonra ekleyeceğiniz tüm geometri, malzeme ve ışıkları tutacaktır.

```csharp
Scene scene = new Scene();
```

### Adım 2: PBR Malzemesi Oluşturun
Şimdi kutumuza gerçekçi bir görünüm kazandıracak **pbr malzemesi oluşturuyoruz**. `PbrMaterial` sınıfı, fiziksel tabanlı render için ihtiyaç duyduğunuz tüm parametreleri sunar.

```csharp
PbrMaterial mat = new PbrMaterial();
```

### Adım 3: Malzeme Özelliklerini Ayarlayın
Malzeme özelliklerini ince ayar yapın. Bu örnekte yüzeyi neredeyse tamamen metalik ve çok pürüzlü yapıyoruz—fırçalanmış metal bir kutu için mükemmel.

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### Adım 4: Bir Kutu Mesh'i Oluşturun
Basit bir kutu geometrisi üretin. Bu, anahtar kelimenin referans verdiği **create box mesh** adımıdır.

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### Adım 5: PBR Malzemesini Kutuya Uygulayın
Az önce oluşturduğumuz kutu düğümüne önceden yapılandırılmış **add pbr material** atayın.

```csharp
boxNode.Material = mat;
```

### Adım 6: STL ASCII Dışa Aktarın (STL Nasıl Dışa Aktarılır)
Son olarak, modeli herhangi bir standart 3D görüntüleyici veya dilimleyicide açabilmek için **export stl ascii** yapın. `FileFormat.STLASCII` kullanmak, insan tarafından okunabilir bir dosya garantiler.

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## Yaygın Tuzaklar ve İpuçları
- **Lisans bulunamadı:** Lisans dosyasının herhangi bir Aspose çağrısından *önce* yüklendiğinden emin olun; aksi takdirde kütüphane değerlendirme modunda çalışır.  
- **Yanlış dosya yolu:** Farklı işletim sistemlerinde eksik yol ayırıcılarından kaçınmak için `Path.Combine` kullanın.  
- **Roughness ve Metallic dengesi:** Her iki faktörü de çok yüksek ayarlamak yüzeyi düz gösterebilir; dengeli bir görünüm için `0.5‑0.9` arasında değerlerle deney yapın.  
- **Performans ipucu:** Aynı malzemeyi birden fazla mesh'e uygulamanız gerekiyorsa tek bir `PbrMaterial` örneğini yeniden kullanın; bu bellek yükünü azaltır.

## Sıkça Sorulan Sorular

**S1: Aspose.3D diğer 3D dosya formatlarıyla uyumlu mu?**  
C1: Evet, Aspose.3D geniş bir 3D dosya formatı yelpazesini destekler, bu da projelerinizde esneklik sağlar.

**S2: Aspose.3D'yi ticari uygulamalarda kullanabilir miyim?**  
C2: Kesinlikle! Aspose.3D, üretim yazılımlarına sorunsuz entegrasyon için ticari lisanslar sunar.

**S3: Deneme sürümü mevcut mu?**  
C3: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) indirerek Aspose.3D'nin yeteneklerini keşfedebilirsiniz.

**S4: Topluluk desteği ve tartışmalarını nerede bulabilirim?**  
C4: Destek ve tartışmalar için Aspose.3D topluluğuna [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) üzerinden katılabilirsiniz.

**S5: Aspose.3D için geçici bir lisans nasıl alınır?**  
C5: Değerlendirme amaçları için geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

## Sonuç
Aspose.3D for .NET ile 3D grafiklere adım atmak, sonsuz yaratıcı olasılıkların kapılarını açar. Sezgisel API'si ve sağlam özellikleri sayesinde görsel açıdan çarpıcı sahneler oluşturmak geliştiriciler için keyifli bir deneyim haline gelir. Artık **kutuya pbr malzemesi nasıl uygulanır** ve **STL ASCII nasıl dışa aktarılır** bildiğinize göre, kutuyu daha karmaşık bir mesh ile değiştirin veya ışığın gerçek zamanlı tepkisini görmek için doku haritalarıyla deney yapın.

---

**Last Updated:** 2026-04-12  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}