---
date: 2026-03-26
description: Aspose.3D for .NET kullanarak silindir oluşturmayı ve OBJ dosyası dışa
  aktarmayı öğrenin. Bu başlangıç seviyesindeki rehber, 3D sahne kurulumunu ve OBJ
  dışa aktarmayı kapsar.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Kayma Altlı Silindir Nasıl Oluşturulur – Aspose.3D for .NET
url: /tr/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Silindir Oluşturma ve Kesme Altı – Aspose.3D for .NET

## Giriş
Eğer .NET ortamında özelleştirilmiş bir kesme altına sahip **silindir** nesneleri oluşturmanın nasıl yapılacağını merak ediyorsanız, doğru yerdesiniz. Bu öğreticide, bir 3‑D sahneyi kurmaktan modeli OBJ dosyası olarak dışa aktarmaya kadar her adımı adım adım göstereceğiz—böylece **Aspose.3D for .NET** kullanarak *başlangıç 3D modelleme* becerilerinizi geliştirebilirsiniz.

## Hızlı Yanıtlar
- **3D modeline başlamak için temel sınıf nedir?** `Scene` tüm geometri için kök konteyneri oluşturur.  
- **Modeli OBJ'ye dışa aktaran yöntem hangisidir?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Test için lisansa ihtiyacım var mı?** Ücretsiz bir deneme sürümü mevcuttur — SSS'deki deneme bağlantısına bakın.  
- **Kesme açısını değiştirebilir miyim?** Evet, `ShearBottom` özelliğini bir `Vector2` değeriyle değiştirin.  
- **Bu başlangıç seviyesindekiler için uygun mu?** Kesinlikle; API düşük seviyeli mesh işlemlerini soyutlar.

## 3D Sahne Nedir?
*3D sahne*, tüm geometrik varlıkları, ışıkları, kameraları ve dönüşümleri tutan hiyerarşik bir konteynerdir. Aspose.3D'de `Scene` sınıfı modellerinizi düzenlemenin ve daha sonra dışa aktarmanın temiz bir yolunu sunar.

## Neden OBJ Dışa Aktarılır?
OBJ, birçok 3‑D uygulaması (Blender, Maya, Unity) tarafından içe aktarılabilen, yaygın olarak desteklenen, metin tabanlı bir formattır. OBJ'ye dışa aktarmak, silindir modellerinizi .NET dışına paylaşmanıza veya daha fazla düzenlemenize olanak tanır.

## Önkoşullar
- C# ve .NET geliştirme hakkında temel bilgi.  
- **Aspose.3D for .NET** yüklü – **[buradan](https://releases.aspose.com/3d/net/)** indirebilirsiniz.  
- Kodlama için hazır bir .NET IDE'si (Visual Studio, Rider veya VS Code).

## Ad Alanlarını İçe Aktarma
İlk olarak, API tiplerinin tanınması için gerekli ad alanlarını kapsam içine getirin.

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

## Adım 1: 3D Sahne Oluşturma
`Scene` nesnesi model hiyerarşinizin kökü olarak görev yapar.

```csharp
Scene scene = new Scene();
```

## Adım 2: Silindir 1 Oluşturma
İlk silindiri yarıçapı 2, yüksekliği 10 ve 20 radyal segment ile oluşturuyoruz.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Adım 3: Silindir 1 için Kesme Altını Özelleştirme
Bir kesme dönüşümü uygulayın, fan‑silindir oluşturmayı etkinleştirin ve istenen şekli elde etmek için diğer özellikleri ayarlayın.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Adım 4: Silindir 1'i Sahneye Ekle
İlk silindiri bir çeviri dönüşümü kullanarak uygun bir konuma yerleştirin.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Adım 5: Silindir 2 Oluştur
İkinci silindir aynı temel boyutlarla ancak özel kesme olmadan oluşturulur—yan yana karşılaştırma için mükemmeldir.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Adım 6: Silindir 2'yi Sahneye Ekle
İkinci silindiri sahne grafiğine basitçe ekliyoruz.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Adım 7: Sahneyi OBJ Dosyası Olarak Dışa Aktar
Son olarak, tüm sahneyi bir OBJ dosyasına kaydediyoruz, böylece herhangi bir standart 3‑D görüntüleyicide açılabilir.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Yaygın Sorunlar ve Çözümler
| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **OBJ dosyası boş** | Sahneye geometri eklenmemiştir. | Her iki silindirin de `scene.RootNode`'a eklendiğinden emin olun. |
| **Kesme hatalı görünüyor** | `ShearBottom` açının tanjantını bekler. | `Math.Tan(angleInRadians)` kullanın veya yaklaşık 47.5° için verilen `0.83` değerini kullanın. |
| **Dosya yolu hataları** | Geçersiz veya eksik dizin. | `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")` kullanın. |

## Sıkça Sorulan Sorular
### Aspose.3D for .NET başlangıç seviyesindekiler için uygun mu?
Kesinlikle! Aspose.3D for .NET yüksek seviyeli bir API sunar ve 3‑D modellemenin matematiksel kısmını soyutlayarak geliştiricilerin her seviyede rahatça kullanabilmesini sağlar.

### Farklı kesme açıları uygulayabilir miyim?
Evet, her `Cylinder` örneğinin kendi `ShearBottom` özelliği vardır; böylece her nesneye benzersiz bir açı atayabilirsiniz.

### Deneme sürümü mevcut mu?
Evet, ücretsiz deneme sürümünü **[buradan](https://releases.aspose.com/)** keşfedebilirsiniz.

### Ek destek nereden bulunur?
Topluluk yardımı, kod örnekleri ve tartışmalar için **[Aspose.3D forumunu](https://forum.aspose.com/c/3d/18)** ziyaret edin.

### Geçici lisans nasıl alınır?
Geçici lisansınızı **[buradan](https://purchase.aspose.com/temporary-license/)** temin edebilirsiniz.

**Ek Soru & Cevap**

**S: Modeli farklı bir formatta, örneğin STL olarak nasıl dışa aktarırım?**  
C: `scene.Save` çağrısında `FileFormat.WavefrontOBJ` yerine `FileFormat.STL` kullanın.

**S: Silindirleri oluşturduktan sonra animasyon ekleyebilir miyim?**  
C: Evet, Aspose.3D tarafından sağlanan `Animation` sınıflarını kullanarak düğüm dönüşümlerine anahtar‑çerçeve animasyonları ekleyebilirsiniz.

**S: API .NET Core'u destekliyor mu?**  
C: Kütüphane .NET Core, .NET 5+ ve .NET 6+ ile tamamen uyumludur.

---

**Son Güncelleme:** 2026-03-26  
**Test Edilen Versiyon:** Aspose.3D for .NET (en son sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}