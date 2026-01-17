---
date: 2026-01-17
description: Aspose.3D for .NET kullanarak bir kutuya PBR malzeme uygulamayı, PBR
  malzeme oluşturmayı ve fiziksel tabanlı render ile STL ASCII dosyalarını dışa aktarmayı
  öğrenin.
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: Bir Kutuya PBR Malzeme Nasıl Uygulanır
url: /tr/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Bir Kutunun Üzerine PBR Malzeme Uygulama

## Giriş

3D grafiklerin büyüleyici dünyasına hoş geldiniz! Bu adım‑adım kılavuzda, Aspose.3D for .NET kullanarak bir kutuya **pbr nasıl uygulanır** malzemesini öğreneceksiniz. PBR malzemesi oluşturmayı, bir mesh'e eklemeyi ve sonunda **STL ASCII dışa aktarma** yaparak modeli herhangi bir sonraki iş akışında kullanabilmenizi göstereceğiz. İster bir oyun prototipi ister bir ürün görselleştirmesi oluşturuyor olun, bu iş akışını ustalaşmak .NET uygulamalarınızda gerçekçi, fiziksel tabanlı renderleme (PBR) kapısını açar.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Bir kutuya PBR malzeme uygulamak ve STL ASCII olarak dışa aktarmak.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for .NET (how to use aspose).  
- **Lisans gerekli mi?** Evet, üretim için geçici veya tam lisans gereklidir.  
- **Desteklenen çıktı formatı?** STL ASCII (export stl ascii) ve birçok diğer 3D formatı.  
- **Ne kadar sürer?** Temel bir uygulama için yaklaşık 10‑15 dakika.

## PBR Malzeme Nedir?
Physically Based Rendering (PBR), ışığın gerçek dünya yüzeyleriyle etkileşimini simüle eden bir gölgelendirme modelidir. Metalik ve pürüzlülük gibi özellikleri ayarlayarak, karmaşık gölgelendiricileri elle ayarlamadan son derece gerçekçi sonuçlar elde edebilirsiniz.

## Neden Fiziksel Tabanlı Renderleme (PBR) Kullanmalı?
- **Realism:** Malzemeler ışığa gerçek fiziğe uygun bir şekilde tepki verir.  
- **Consistency:** Aynı malzeme herhangi bir ışık ortamında doğru görünür.  
- **Efficiency:** Modern GPU'lar PBR hesaplamaları için optimize edilmiştir, bu da size ücretsiz performans sağlar.

## Ön Koşullar

Koda geçmeden önce aşağıdakilere sahip olduğunuzdan emin olun:

### Aspose.3D for .NET'i İndirin ve Kurun
Kütüphaneyi indirme ve kurma hakkında ayrıntılı talimatlar için [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) sayfasını ziyaret edin.

### Lisans Edinin
Aspose.3D'in tam potansiyelini açmak için geçerli bir lisans edinin. Geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilir veya tam lisansı [buradan](https://purchase.aspose.com/buy) satın alabilirsiniz.

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

## Adım 1: Bir Sahne Başlatın
Aşağıdaki kod parçacığını kullanarak bir 3D sahneyi başlatarak başlayın:

```csharp
Scene scene = new Scene();
```

## Adım 2: PBR Malzeme Oluşturun
Şimdi kutumuza gerçekçi bir görünüm kazandıracak **pbr malzemesi oluşturuyoruz**:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Adım 3: Malzeme Özelliklerini Ayarlayın
Malzeme özelliklerini ince ayar yaparak neredeyse metalik ve çok pürüzlü hale getirin—fırçalanmış metal bir kutu için mükemmel:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Adım 4: Bir Kutu Oluşturun
PBR malzemesinin uygulanacağı bir kutu oluşturun:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Adım 5: PBR Malzemesini Kutuya Ekleyin
Önceden yapılandırılmış **add pbr material**'i oluşturulan kutu düğümüne atayın:

```csharp
boxNode.Material = mat;
```

## Adım 6: 3D Sahneyi STL ASCII Olarak Kaydedin
Son olarak modeli herhangi bir standart 3D görüntüleyicide veya dilimleyicide açabilmek için **export stl ascii** yapın:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Tebrikler! Aspose.3D for .NET kullanarak bir 3D sahnede kutuya başarıyla PBR malzemesi uyguladınız.

## Yaygın Hatalar ve İpuçları
- **License not found:** Lisans dosyasının herhangi bir Aspose çağrısından önce yüklendiğinden emin olun; aksi takdirde kütüphane değerlendirme modunda çalışır.  
- **Incorrect file path:** Farklı işletim sistemlerinde eksik yol ayırıcılarından kaçınmak için `Path.Combine` kullanın.  
- **Roughness vs. Metallic:** Her iki faktörü de çok yüksek ayarlamak yüzeyi düz gösterebilir; dengeli bir görünüm için 0.5‑0.9 arasında değerlerle deney yapın.

## Sonuç
Aspose.3D for .NET ile 3D grafiklere adım atmak, sonsuz yaratıcı olasılıkların kapılarını açar. Sezgisel API'si ve güçlü özellikleri sayesinde görsel olarak çarpıcı sahneler oluşturmak geliştiriciler için keyifli bir deneyim haline gelir. Sonraki adımda kutuyu daha karmaşık bir örgü ile değiştirin veya farklı PBR dokularıyla deney yaparak ışığın nasıl tepki verdiğini görün.

## Sıkça Sorulan Sorular

**Q1: Aspose.3D diğer 3D dosya formatlarıyla uyumlu mu?**  
A1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekler, projenizde esneklik sağlar.

**Q2: Aspose.3D'yi ticari uygulamalarda kullanabilir miyim?**  
A2: Kesinlikle! Aspose.3D, uygulamalarınıza sorunsuz entegrasyon için ticari lisanslar sunar.

**Q3: Deneme sürümü mevcut mu?**  
A3: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) indirerek Aspose.3D'nin yeteneklerini keşfedebilirsiniz.

**Q4: Topluluk desteği ve tartışmalarını nerede bulabilirim?**  
A4: Destek ve tartışmalar için [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) topluluğuna katılın.

**Q5: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
A5: Değerlendirme amaçlı geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---