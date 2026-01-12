---
date: 2026-01-12
description: Aspose.3D for .NET kullanarak kesme alt silindir oluşturmayı ve 3D model
  .obj dosyasını nasıl dışa aktaracağınızı öğrenin. 3D modellemeyi ustalaşmak için
  bu adım adım rehberi izleyin.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET ile kayma alt silindiri nasıl oluşturulur
url: /tr/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Özelleştirilmiş Kayma Alt Silindir

## Giriş
Kapsamlı rehberimize hoş geldiniz; burada Aspose.3D for .NET ile **shear bottom cylinder** modelleri oluşturmayı öğreneceksiniz. Bir oyun varlığı, mekanik bir parça ya da görsel bir demo oluşturuyor olun, bu öğretici size silindirin alt kısmını nasıl şekillendireceğinizi, kayma uygulayacağınızı ve sonunda **3D model OBJ** dosyasını herhangi bir sonraki işlem hattında kullanmak üzere nasıl dışa aktaracağınızı tam olarak gösterir. Her adımı birlikte inceleyelim, böylece dakikalar içinde özel geometri üretmeye başlayabilirsiniz.

## Hızlı Yanıtlar
- **Shear bottom cylinder nedir?** Alt yüzeyi düz yerine eğimli (kaymalı) bir silindir.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for .NET.  
- **Modeli nasıl dışa aktarırım?** `scene.Save(..., FileFormat.WavefrontOBJ)` kullanın.  
- **Lisans gerekli mi?** Deneme sürümü mevcuttur; üretim için ticari lisans gereklidir.  
- **Gereken ön koşullar nelerdir?** .NET geliştirme ortamı ve Aspose.3D NuGet paketi.

## Shear bottom cylinder nedir?
Shear bottom cylinder, alt yüzeyi bir kayma işlemiyle dönüştürülmüş standart bir silindirik ağdır. Bu sayede köşeli tabanlar, rampalar veya manuel olarak köşe noktalarını düzenlemeden özel bağlayıcılar oluşturabilirsiniz.

## Bu görev için neden Aspose.3D kullanılmalı?
- **Tam kontrol** geometri parametreleri (yarıçap, yükseklik, segmentler) üzerinde.  
- **Yerleşik kayma desteği**, `ShearBottom` özelliği aracılığıyla, düşük seviyeli ağ manipülasyonundan sizi kurtarır.  
- **Tek tıkla dışa aktarım**, OBJ, FBX ve STL gibi popüler formatlara, diğer araçlarla entegrasyonu sorunsuz hâle getirir.

## Ön Koşullar
İlerlemeye başlamadan önce şunlara sahip olduğunuzdan emin olun:

- C# ve .NET hakkında temel bilgi.  
- Aspose.3D for .NET yüklü. **[burada](https://releases.aspose.com/3d/net/)** indirebilirsiniz.  
- .NET uyumlu bir IDE (Visual Studio, Rider veya VS Code).

## Ad Alanlarını İçe Aktarma
C# dosyanızda, gerekli ad alanlarını içe aktararak başlayın:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Adım 1: Bir Sahne Oluşturun
İlk olarak, tüm nesnelerimizi tutacak yeni bir 3‑D sahne örneği oluşturun.

```csharp
Scene scene = new Scene();
```

## Adım 2: Silindir 1 Oluşturun
Kaymalı bir alt ile özelleştireceğimiz birincil silindiri oluşturun.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Adım 3: Silindir 1 için Kayma Altını Özelleştirin
Kaymayı uygulayın, fan‑oluşturmayı etkinleştirin ve istediğiniz şekli elde etmek için diğer özellikleri ayarlayın.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Adım 4: Silindir 1'i Sahneye Ekleyin
Özelleştirilmiş silindiri sahneye yerleştirin ve iki nesneyi yan yana görebilmek için biraz sağa kaydırın.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Adım 5: Silindir 2 Oluşturun
Karşılaştırma için ikinci, sade bir silindir oluşturun.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Adım 6: Silindir 2'yi Sahneye Ekleyin
İkinci silindiri herhangi bir özel kayma olmadan ekleyin—bu, önceki adımların etkisini göstermeye yardımcı olur.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Adım 7: Sahneyi Kaydedin
Son olarak, tüm sahneyi bir OBJ dosyası olarak dışa aktarın, böylece Blender, Maya veya başka bir 3‑D görüntüleyicide açabilirsiniz.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Yaygın Sorunlar ve İpuçları
- **Kayma değerleri**: `Vector2`, X ve Y kayma faktörlerini alır. `0.83` değeri yaklaşık 47.5°'e karşılık gelir, ancak farklı açılar için ayarlayabilirsiniz.  
- **Dışa aktarım yolu**: Belirttiğiniz klasörün var olduğundan ve yazma izninizin bulunduğundan emin olun; aksi takdirde `scene.Save` bir istisna fırlatır.  
- **Performans**: Çok yüksek segmentli silindirler için, OBJ dosya boyutunu yönetilebilir tutmak amacıyla segment sayısını (`örnekte 20`) azaltmayı düşünün.

## Sık Sorulan Sorular

### Aspose.3D for .NET yeni başlayanlar için uygun mu?
Kesinlikle! Aspose.3D for .NET, kullanıcı dostu bir API sunar ve hem yeni başlayanlar hem de deneyimli geliştiriciler için erişilebilir kılar.

### Silindirlere farklı kayma açıları uygulayabilir miyim?
Evet, her silindir için `ShearBottom` özelliğini ayrı ayrı özelleştirerek benzersiz etkiler elde edebilirsiniz.

### Deneme sürümü mevcut mu?
Evet, ücretsiz deneme sürümünü **[burada](https://releases.aspose.com/)** keşfedebilirsiniz.

### Ek destek nereden bulunur?
Topluluk desteği ve tartışmalar için **[Aspose.3D forumu](https://forum.aspose.com/c/3d/18)** ziyaret edin.

### Geçici lisans nasıl alınır?
Geçici lisansınızı **[burada](https://purchase.aspose.com/temporary-license/)** alabilirsiniz.

**Additional Q&A**

**S: FBX formatına nasıl geçiş yaparım?**  
C: `scene.Save` çağrısında `FileFormat.WavefrontOBJ` yerine `FileFormat.FBX` kullanın.

**S: Dışa aktardıktan sonra silindiri animasyonlu hale getirebilir miyim?**  
C: OBJ animasyonu desteklemez; animasyonlu veri gerekiyorsa FBX veya GLTF kullanın.

**S: Daha büyük bir silindir yarıçapına ihtiyacım olursa ne yapmalıyım?**  
C: `Cylinder` yapıcısının ilk iki parametresini (ör. `new Cylinder(4, 4, …)`) ayarlayın.

## Sonuç
Artık Aspose.3D for .NET kullanarak **shear bottom cylinder** modelleri oluşturmayı ve bunları OBJ dosyaları olarak dışa aktarmayı öğrendiniz. Projenizin ihtiyaçlarına göre farklı kayma değerleri, segment sayıları ve dışa aktarım formatlarıyla deneyler yapın. İyi modellemeler!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}