---
date: 2026-01-14
description: Aspose.3D for .NET kullanarak sahneye kamera eklemeyi ve sahneyi FBX
  olarak dışa aktarmayı öğrenin – kamera hedeflerini ayarlamak ve 3D animasyonlar
  oluşturmak için adım adım bir rehber.
linktitle: Add Camera to Scene and Set Up Targets for 3D Animation
second_title: Aspose.3D .NET API
title: Sahneye Kamera Ekle ve 3D Animasyon İçin Hedefleri Ayarla
url: /tr/net/animation/setup-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sahneye Kamera Ekleme ve 3D Animasyon İçin Hedefleri Ayarlama

## Giriş

3D animasyon oluşturuyorsanız, ilk ihtiyacınız iyi konumlandırılmış bir kameradır. Bu öğreticide **sahneye kamera ekleme** yöntemini, hedefini tanımlamayı ve sonunda Aspose.3D for .NET kullanarak **sahneyi FBX olarak dışa aktarmayı** öğreneceksiniz. Her adımı adım adım inceleyecek, neden önemli olduğunu açıklayacak ve güvenle etkileyici 3D animasyonlar oluşturmanız için pratik ipuçları vereceğiz.

## Hızlı Yanıtlar
- **Kamera eklemek için ilk adım nedir?** Kamera düğümünü barındıracak bir `Scene` nesnesi başlatın.  
- **Bu kılavuzda dışa aktarım için hangi dosya formatı kullanılıyor?** FBX (`.fbx`).  
- **Örnek kodu çalıştırmak için lisansa ihtiyacım var mı?** Değerlendirme için ücretsiz deneme çalışır; üretim için ticari lisans gereklidir.  
- **Hangi .NET sürümleri destekleniyor?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Kamera konumunu oluşturduktan sonra değiştirebilir miyim?** Evet – istediğiniz zaman `cameraNode.Transform.Translation` değerini değiştirin.

## “Sahneye kamera ekleme” nedir?
Bir sahneye kamera eklemek, bir `Camera` varlığı oluşturmak, bunu sahne grafiğindeki bir düğüme bağlamak ve hedef bir noktaya “bakacak” şekilde konumlandırmak anlamına gelir. Bu, sahne render edildiğinde veya dışa aktarıldığında izleyicinin bakış açısını belirler.

## Neden kamera hedefleri ayarlanmalı ve FBX olarak dışa aktarılmalı?
- **Görüş noktasını kontrol edin** – hassas kamera konumlandırması, animasyonunuzu tam olarak hayal ettiğiniz gibi çerçevelemenizi sağlar.  
- **Birliktelik** – FBX, oyun motorları, Maya, Blender ve diğer 3D araçlar tarafından yaygın olarak desteklenir, varlıkları paylaşmayı kolaylaştırır.  
- **Yeniden kullanılabilir varlıklar** – kamera ve hedefi kaydettikten sonra sahneyi birden fazla projede yeniden kullanabilirsiniz.

## Ön Koşullar

Öğreticiye başlamadan önce aşağıdaki ön koşullara sahip olduğunuzdan emin olun:

- C# ve .NET framework'ünün temel bilgisi.  
- Aspose.3D for .NET kütüphanesi yüklü. Bunu [buradan](https://releases.aspose.com/3d/net/) indirebilirsiniz.  
- 3D programlama için hazır bir geliştirme ortamı.

## Ad Alanlarını İçe Aktarma

İşleme başlamak için gerekli ad alanlarını projenize içe aktarın. Bu ad alanları, Aspose.3D for .NET'in gücünden yararlanmak için gereklidir:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Adım‑Adım Kılavuz

### Adım 1: Scene Nesnesini Başlatma

İlk olarak sahne nesnesini başlatın. Bu, 3D animasyonunuzun hayata geçeceği tuval görevi görür.

```csharp
// ExStart:SetupTargetAndCamera
// Initialize scene object
Scene scene = new Scene();
```

### Adım 2: Kamera Düğümü Oluşturma

Sonra, kamerayı tutacak bir alt düğüm oluşturun. Düğüne anlamlı bir ad vermek, sahne hiyerarşisini düzenli tutmaya yardımcı olur.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Adım 3: Kamerayı Konumlandırma

Kamera düğümünün çevirisini (translation) belirtin. Bu, kameranın 3D uzaydaki başlangıç konumunu belirler.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Adım 4: Kamera Hedefini Tanımlama

Kameranın bakması için bir hedef noktası gerekir. Odak noktası olarak işlev gören başka bir alt düğüm oluşturur ve bunu kameranın `Target` özelliğine atarız.

```csharp
cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
```

### Adım 5: Yapılandırılmış Sahneyi Kaydetme

Son olarak, sahneyi bir FBX dosyasına (veya desteklenen başka bir formata) dışa aktarın. `"Your Output Directory"` ifadesini dosyanın kaydedilmesini istediğiniz gerçek yol ile değiştirin.

```csharp
var output = "Your Output Directory" + "camera-test.fbx";
scene.Save(output);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Çözüm |
|-------|----------|
| **Kamera yanlış açıda görünüyor** | Hedef düğümünün beklediğiniz konumda olduğundan emin olun. Ayrıca yönelimi kontrol etmek için `cameraNode.GetEntity<Camera>().UpVector` değerini ayarlayabilirsiniz. |
| **Dışa aktarılan FBX diğer araçlarda açılmıyor** | Aspose.3D'nin güncel bir sürümünü kullandığınızdan emin olun (kütüphane otomatik olarak uyumlu bir FBX sürümü yazar). |
| **`scene.Save` sırasında yol bulunamadı hatası** | Mutlak bir yol kullanın veya `Save` çağrısı öncesinde çıkış dizininin var olduğundan emin olun. |

## SSS'ler

### S1: Aspose.3D diğer 3D modelleme araçlarıyla uyumlu mu?
**C1:** Aspose.3D çeşitli dosya formatlarını destekler, popüler 3D modelleme araçlarıyla uyumluluğu sağlar.

### S2: Aspose.3D'yi oyun geliştirme için kullanabilir miyim?
**C2:** Kesinlikle! Aspose.3D, geliştiricilerin oyunlar için 3D varlıkları kolayca oluşturmasını sağlar.

### S3: Aspose.3D için ek destek nereden bulunabilir?
**C3:** Topluluk desteği ve tartışmalar için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S4: Ücretsiz deneme mevcut mu?
**C4:** Evet, ücretsiz denemeyi [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

### S5: Geçici lisansı nasıl alabilirim?
**C5:** Geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Sonuç

Artık **sahneye kamera ekleme**, hedefini ayarlama ve sonucu Aspose.3D for .NET kullanarak bir FBX dosyası olarak dışa aktarma konusunda bilgi sahibisiniz. Bu temellerle daha zengin animasyonlar oluşturabilir, birden fazla kamera ile deneyler yapabilir ve dışa aktarılan sahneleri oyun motorlarına ya da görsel efekt akışlarına entegre edebilirsiniz.

---

**Last Updated:** 2026-01-14  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}