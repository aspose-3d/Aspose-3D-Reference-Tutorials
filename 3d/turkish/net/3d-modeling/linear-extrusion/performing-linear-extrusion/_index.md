---
date: 2026-01-07
description: Aspose.3D for .NET kullanarak 2D bir profili doğrusal ekstrüde etmeyi
  ve 3D model OBJ'yi dışa aktarmayı öğrenin. Bu doğrusal ekstrüzyon öğreticisi adım
  adım size rehberlik eder.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET ile Doğrusal Ekstrüzyon Nasıl Yapılır
url: /tr/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile nasıl linear extrude yapılır

## Giriş

Welcome to our **linear extrusion tutorial**! In this guide you’ll discover **how to linear extrude** a 2‑D profile and turn it into a fully fledged 3‑D object using Aspose.3D for .NET. Whether you’re building a CAD‑style application or just need to **export 3d model obj** files for downstream processing, this step‑by‑step walkthrough will give you the confidence to add powerful geometry creation to your projects.

## Hızlı Yanıtlar
- **What is linear extrusion?** 2‑D bir şekli düz bir yol boyunca uzatarak 3‑D bir katı oluşturma.  
- **Which library do we use?** Aspose.3D for .NET.  
- **Do I need a license?** Test için geçici bir lisans yeterlidir; üretim için tam lisans gereklidir.  
- **Can I export to OBJ?** Evet – son sahne Wavefront OBJ dosyası olarak kaydedilir.  
- **How many lines of code?** Açıklayıcı yorumlarla birlikte 30 satırdan az C# kodu.

## Linear Extrusion Nedir?

Linear extrusion, düz bir profili (örneğin bir dikdörtgen veya daire) düz bir hat boyunca süpürerek, isteğe bağlı olarak bükülme, ölçekleme veya ofset ekler. Sonuç, diğer 3‑D araçlarda kullanılmak üzere renderlanabilen, düzenlenebilen veya dışa aktarılabilen bir katıdır.

## Neden Linear Extrusion İçin Aspose.3D Kullanmalı?

* **Zero‑dependency:** Harici CAD çekirdeklerine ihtiyaç yok.  
* **Full .NET support:** .NET Framework, .NET Core ve .NET 5/6+ ile çalışır.  
* **Export flexibility:** OBJ, STL, FBX ve birçok diğer formata doğrudan kaydedebilir.  
* **Rich API:** Dilimleri, bükülmeyi ve ofsetleri birkaç özellik ile kontrol edebilirsiniz.

## Ön Koşullar

1. **Aspose.3D installed** – indirmek için [buraya](https://releases.aspose.com/3d/net/) tıklayın.  
2. **Documentation access** – kurulum rehberini [buradan](https://reference.aspose.com/3d/net/) izleyin.  
3. Gerekli ad alanlarının referans edildiği bir .NET geliştirme ortamı (Visual Studio, VS Code veya Rider).

## Ad Alanlarını İçe Aktarma

Aspose.3D işlevselliğini açmak için gerekli ad alanlarını ekleyin:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Bu ad alanları `Scene`, `LinearExtrusion`, `RectangleShape` ve `Vector3` gibi yardımcı sınıflara erişim sağlar.

## Linear Extrusion Gerçekleştirme

Aşağıda tam iş akışı yer almaktadır. Her adım, ilgili kod bloğundan önce sade bir dille açıklanır, böylece kodun ne yaptığını tahmin etmeden ilerleyebilirsiniz.

### Adım 1: Temel Profili Başlatma

İlk olarak, ekstrüde edilecek 2‑D şekli oluşturun. Bu örnekte küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Neden Önemli:* Profil, son 3‑D nesnenin kesitini tanımlar. Farklı siluetler elde etmek için `RoundingRadius`, genişlik veya yüksekliği ayarlayın.

### Adım 2: Linear Extrusion Uygulama

Şimdi profili Z‑ekseni boyunca 10 birim süpürüyoruz, pürüzsüzlük için 100 dilim ekliyoruz, geometrinin merkezlenmesini sağlıyor ve bir ofsetle tam 360° bükülme uyguluyoruz.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro ipucu:* Performans ve görsel kaliteyi dengelemek için `Slices` ile oynayın ve spiral etkiler için `Twist` ile deney yapın.

### Adım 3: Sahne Oluşturma

`Scene`, tüm 3‑D varlıkların konteyneri olarak görev yapar—onu bir tuval gibi düşünün.

```csharp
Scene scene = new Scene();
```

### Adım 4: Extrusion'ı Sahneye Ekleyin

Ekstrüde edilmiş geometriyi sahnenin kök düğümüne ekleyin, böylece renderlanabilir hiyerarşinin bir parçası olur.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Adım 5: 3‑D Modeli Kaydetme

Son olarak, sahneyi yaygın desteklenen bir OBJ dosyasına dışa aktarın. Bu, Aspose.3D'nin **export 3d model obj** yeteneğini gösterir.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Oluşturulan `LinearExtrusion.obj` dosyasını herhangi bir 3‑D görüntüleyicide açtığınızda, kodun tarif ettiği gibi bükülmüş bir dikdörtgen prizma göreceksiniz.

## Yaygın Hatalar ve İpuçları

| Sorun | Neden Oluşur | Nasıl Düzeltilir |
|-------|----------------|------------|
| **Profil görünmüyor** | Extrusion'ı sahneye eklemeyi unutmak. | `CreateChildNode`'un çağrıldığından emin olun. |
| **Bükülme düz görünüyor** | `Slices` çok düşük, kaba bir geometri oluşturuyor. | Daha pürüzsüz bir bükülme için `Slices`'ı artırın (ör. 200). |
| **Dışa aktarım başarısız** | Çıktı klasörü mevcut değil veya yazma izni eksik. | `RunExamples.GetOutputFilePath` kullanın veya klasörü manuel olarak oluşturun. |
| **Beklenmeyen ölçekleme** | `Center` false olarak ayarlandığında geometri kayar. | Bir ofsete ihtiyacınız yoksa `Center = true` olarak ayarlayın. |

## Sıkça Sorulan Sorular

### S1: Aspose.3D yeni başlayanlar için uygun mu?
C1: Kesinlikle! Aspose.3D kullanıcı dostu bir API sunar ve bu öğretici, linear extrusion temelini adım adım gösterir.

### S2: Aspose.3D'yi ticari projelerde kullanabilir miyim?
C2: Evet, Aspose.3D hem kişisel hem de ticari kullanım için lisans seçenekleri sunar. Detaylar için [buraya](https://purchase.aspose.com/buy) bakın.

### S3: Test için geçici lisansları nasıl alabilirim?
C3: Test amaçlı geçici lisanslar almak için [bu linke](https://purchase.aspose.com/temporary-license/) gidin.

### S4: Topluluk desteğini nereden bulabilirim?
C4: Canlı bir toplulukla bağlantı kurmak ve yardım almak için [Aspose.3D Forumuna](https://forum.aspose.com/c/3d/18) katılın.

### S5: Ücretsiz deneme sürümü var mı?
C5: Elbette! Aspose.3D'nin yeteneklerini doğrudan deneyimlemek için ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) indirin.

**Son Güncelleme:** 2026-01-07  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## HEDEF ANAHTAR KELİMELER:

**Primary Keyword (HIGHEST PRIORITY):**
how to linear extrude

**Secondary Keywords (SUPPORTING):**
export 3d model obj, linear extrusion tutorial

**Anahtar Kelime Entegrasyon Stratejisi:**
1. Primary keyword: 3-5 kez kullanın (başlık, meta, ilk paragraf, H2 başlığı, gövde)
2. Secondary keywords: Her biri 1-2 kez kullanın (başlıklar, gövde metni)
3. Tüm anahtar kelimeler doğal bir şekilde entegre edilmelidir - okunabilirlik, anahtar kelime sayısından önceliklidir
4. Bir anahtar kelime doğal olarak uymuyorsa, anlamsal bir varyasyon kullanın veya atlayın