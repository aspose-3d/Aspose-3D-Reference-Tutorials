---
date: 2026-03-28
description: Aspose.3D for .NET kullanarak malzeme özelliklerini listelemeyi, difüz
  rengi değiştirmeyi ve 3D malzeme niteliklerini düzenlemeyi öğrenin. Adım adım kod
  örnekleri dahil.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Aspose.3D ile 3B Ortamlarda Malzeme Özelliklerini Listele
url: /tr/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahnellerde Aspose.3D ile Malzeme Özelliklerini Listeleme

## Giriş

Eğer bir 3D modelin **malzeme özelliklerini** listelemeniz ve ardından difüz renk gibi ayarları değiştirmeniz gerekiyorsa, doğru yerdesiniz. Aspose.3D for .NET, C# kodunuzdan çıkmadan malzeme niteliklerini incelemenizi, almanızı ve değiştirmenizi sağlayan temiz, nesne‑yönelimli bir API sunar. Bu öğreticide bir sahneyi yüklemeyi, malzeme özelliklerini enumerate etmeyi ve difüz bileşen gibi değerleri değiştirmeyi adım adım göstereceğiz—böylece modellerinize istediğiniz görünümü verebilirsiniz.

## Hızlı Yanıtlar
- **Birincil hedef nedir?** Malzeme özelliklerini listelemek ve değiştirmek (ör. difüz renk).  
- **Hangi kütüphane gereklidir?** Aspose.3D for .NET.  
- **Lisans gerekir mi?** Üretim kullanımı için geçici veya tam lisans gereklidir.  
- **Desteklenen dosya formatları?** FBX, OBJ, STL, STL‑ASCII, 3MF ve daha fazlası.  
- **Tipik uygulama süresi?** Temel bir özellik‑listeleme betiği için yaklaşık 10‑15 dakika.

## **list material properties** nedir?
Malzeme özelliklerini listelemek, bir malzemenin `PropertyCollection`'ı üzerinde döngü yaparak her özellik adını ve mevcut değerini okumak anlamına gelir. Bu, hata ayıklama, görsel inceleme veya kullanıcıların çalışma zamanında malzeme ayarlarını değiştirmesine olanak tanıyan UI kontrolleri oluşturmak için faydalıdır.

## Aspose.3D'yi **malzeme özelliklerine erişmek** için neden kullanmalısınız?
- **Harici dönüştürücüler yok** – yerel .NET nesneleriyle doğrudan çalışın.  
- **Zengin özellik modeli** – standart PBR değerlerine ek olarak özel FBX‑spesifik nitelikleri destekler.  
- **Çapraz platform** – .NET Framework, .NET Core ve .NET 5/6+ üzerinde çalışır.  

## Önkoşullar

- Projenize Aspose.3D for .NET kurulu. İndirmek için [buraya](https://releases.aspose.com/3d/net/) tıklayın.  
- Diskte 3‑D kaynak dosyalarınızı tutacak bir klasör (ör. gömülü dokulara sahip bir FBX dosyası).  

Temel şeyleri hallettiniz, şimdi koda dalalım.

## Ad Alanlarını İçe Aktarma

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Adım 1: 3D Sahneyi Yükleme

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Adım 2: İlk düğümün **malzeme özelliklerine erişme**

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Adım 3: **Malzeme özelliklerini listeleme** – her ad/ değer çiftini görün

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Adım 4: **Difüzü nasıl değiştirirsiniz** – Diffuse özelliğini değiştirin

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Adım 5: **Özelliği ada göre al** – güçlü tipli bir örnek elde edin

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Adım 6: Bir özelliğin kendi alt özelliklerinde dolaşma (ileri düzey)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## **Difüzün ötesinde 3D malzeme rengini değiştirme**
Eğer speküler, ortam veya yayılıcı renkleri etkilemeniz gerekiyorsa, yukarıdaki `props["..."]` atamasında `"Diffuse"` yerine `"Specular"` veya `"Ambient"` yazmanız yeterlidir. Aynı `Vector3` veya `Vector4` yapıları geçerlidir.

## **C# içinde malzeme rengini güncelleme**
Bir malzemenin görsel görünümünü değiştirmek, `PropertyCollection` içinde ilgili özelliği güncellemeye indirgenir. Difüz, speküler ya da herhangi bir özel renk niteliğini değiştirmek isteyin, desen aynı kalır:

1. Özelliği tam adıyla (büyük/küçük harf duyarlı) alın.  
2. Yeni bir `Vector3` (RGB) veya `Vector4` (RGBA) değeri atayın.  

API doğrudan C# nesneleriyle çalıştığı için, **C# içinde malzeme rengini güncelleme** kodunu ara dosyalar veya dönüştürücüler olmadan yapabilirsiniz. Bu, gerçek zamanlı editörler veya toplu işleme hatları için mükemmeldir.

## Yaygın Tuzaklar ve İpuçları
- **Özellik adı büyük/küçük harf duyarlılığı** – Aspose.3D özellik anahtarları büyük/küçük harfe duyarlıdır; liste çıktısında gösterilen tam adı kullanın.  
- **Eksik özellik** – Tüm malzemeler her PBR niteliğini ortaya çıkarmaz. Erişmeden önce `props.ContainsKey("Specular")` kontrol edin.  
- **Değişiklikleri kaydetme** – Özellikleri değiştirdikten sonra `scene.Save("output.fbx");` çağırarak değişiklikleri kalıcı hale getirin.

## Sonuç

Artık Aspose.3D for .NET kullanarak **malzeme özelliklerini listelemeyi**, **bir özelliği ada göre almayı** ve **difüz rengi değiştirmeyi** (veya başka herhangi bir malzeme niteliğini) öğrendiniz. Farklı özellik tipleriyle deney yaparak 3‑D varlıklarınızın görünümünü ince ayar yapın ve **C# içinde malzeme rengini güncelleme**yi tek bir kod satırıyla yapabileceğinizi unutmayın.

## SSS

### S1: Aspose.3D for .NET'i diğer 3D dosya formatlarıyla kullanabilir miyim?
C1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekler, FBX, STL ve daha fazlası dahil.

### S2: Aspose.3D for .NET için geçici lisansı nasıl alabilirim?
C2: Geçici lisans almak için [burayı](https://purchase.aspose.com/temporary-license/) ziyaret edin.

### S3: Aspose.3D kullanıcıları için bir topluluk forumu var mı?
C3: Evet, destek ve tartışmaları [Aspose.3D forumunda](https://forum.aspose.com/c/3d/18) bulabilirsiniz.

### S4: Aspose.3D for .NET için ayrıntılı belgeleri nerede bulabilirim?
C4: Kapsamlı rehberlik için [belgelere](https://reference.aspose.com/3d/net/) bakın.

### S5: Aspose.3D for .NET'i satın almadan önce ücretsiz deneyebilir miyim?
C5: Elbette! Özelliklerini keşfetmek için [ücretsiz deneme sürümünü](https://releases.aspose.com/) indirin.

## Sıkça Sorulan Sorular

**S: `Vector3(1, 0, 1)` neyi temsil eder?**  
C: Doğrusal renk uzayında difüz rengi magenta olarak ayarlar (kırmızı = 1, yeşil = 0, mavi = 1).

**S: Özellikleri değiştirdikten sonra `scene.Save` çağırmam gerekiyor mu?**  
C: Evet, sahneyi kaydetmek değişikliklerinizi diske yazar; aksi takdirde değişiklikler yalnızca bellekte kalır.

**S: Özel FBX niteliklerini listeleyebilir miyim?**  
C: Kesinlikle. `PropertyCollection` herhangi bir özel niteliği içerir ve `GetProperty("customName")` ile erişebilirsiniz.

**S: Birden fazla malzemeyi toplu olarak güncellemenin bir yolu var mı?**  
C: `scene.RootNode.ChildNodes` üzerinden döngü yaparak her malzeme için özellik‑değiştirme adımlarını tekrarlayın.

**S: Aspose.3D .NET 6'yı destekliyor mu?**  
C: Evet, kütüphane .NET 6 ve sonrasıyla tam uyumludur.

---

**Last Updated:** 2026-03-28  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}