---
date: 2026-03-28
description: Aspose.3D for .NET kullanarak 3D sahnelerde küpü nasıl canlandıracağınızı
  öğrenin ve canlandırılmış sahneyi FBX olarak dışa aktarın. Bu kılavuz, animasyon
  eğrisi oluşturmayı, anahtar kareleri bağlamayı ve 3D özellikleri canlandırmayı gösterir.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET ile 3D Ortamlarda Küpü Nasıl Canlandırabilirsiniz
url: /tr/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile 3D Sahnelere Küp Nasıl Canlandırılır

## Giriş

Eğer .NET'te 3D sahne oluşturma ve animasyon dünyasına dalıyorsanız, Aspose.3D sizin başvuru aracınızdır. Bu adım adım rehberde, **küp nasıl canlandırılır** nesnelerini özelliklerini canlandırarak, animasyon eğrileri oluşturarak ve anahtar kareleri bağlayarak inceleyeceğiz. Sonunda, popüler 3D formatlarına dışa aktarabileceğiniz tamamen canlandırılmış bir küp elde edeceksiniz.

## Hızlı Yanıtlar
- **Hangi kütüphane kullanılıyor?** Aspose.3D for .NET  
- **Bu öğreticide hangi temel görev ele alınıyor?** 3D sahnede küp nasıl canlandırılır  
- **Ana adımlar?** Ad alanlarını içe aktar, sahne oluştur, anahtar kareleri bağla, dosyayı kaydet  
- **Lisans gerekli mi?** Öğrenme için ücretsiz deneme yeterli; üretim için ticari lisans gerekir  
- **Desteklenen çıktı formatı?** FBX (ASCII 7500) ve Aspose.3D tarafından desteklenen diğer formatlar  

## Aspose.3D'de “küp nasıl canlandırılır” nedir?

Bir küpü canlandırmak, zaman içinde anahtar kare verileri kullanarak dönüşüm özelliklerini (örneğin Çeviri, Rotasyon veya Ölçek) değiştirmek anlamına gelir. Aspose.3D, **animasyon eğrileri** oluşturmak, **anahtar kareleri bağlamak** ve **3D özelliklerini canlandırmak** doğrudan sahne düğümlerinde sağlayan temiz bir API sunar.

## Neden Aspose.3D ile bir küp canlandırılır?

- **Full .NET integration** – .NET Framework, .NET Core ve .NET 5/6 ile çalışır.  
- **No external dependencies** – basit animasyonlar için Unity veya diğer motorlara ihtiyaç yoktur.  
- **Export flexibility** – canlandırılmış sahneler FBX, OBJ, GLTF vb. formatlarda kaydedilebilir, sonraki işlem hatları için.  

## Önkoşullar

Bu heyecan verici yolculuğa başlamadan önce, aşağıdaki önkoşulların yerine getirildiğinden emin olun:

- Aspose.3D for .NET: Kütüphanenin kurulu olduğundan emin olun. [Aspose.3D web sitesinden](https://releases.aspose.com/3d/net/) indirebilirsiniz.  
- C# Bilgisi: C# programlama diline aşina olmak, örnekleri anlamak ve uygulamak için gereklidir.  
- Entegre Geliştirme Ortamı (IDE): Örneklerle birlikte kodlamak için Visual Studio gibi tercih ettiğiniz IDE'yi kullanın.  
- Temel 3D Sahne Kavramları: Temel 3D sahne kavramlarına hakim olmak öğrenme yolculuğunuzu kolaylaştıracaktır.  

## Ad Alanlarını İçe Aktarın

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

## Adım 1: Sahne Nesnesini Başlatın

Düğüm ve animasyonlarımızı tutacak boş bir sahne oluşturun.

```csharp
Scene scene = new Scene();
```

## Adım 2: Polygon Builder Kullanarak Mesh Oluşturun

`Common.CreateMeshUsingPolygonBuilder()` yardımcı yöntemi kullanarak basit bir küp mesh'i oluşturuyoruz.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Adım 3: Küp Düğümlerini Oluşturun

Küp mesh'ini sahneye kök düğümün bir çocuğu olarak ekleyin. **cube1** düğüm adı, anahtar kareleri bağladığımızda daha sonra kullanılacak.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Adım 4: Çeviri Özelliğini Bulun

Küpün konumunu canlandırmak için, düğümün dönüşümündeki **Translation** (Çeviri) özelliğini bulmamız gerekir.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Adım 5: Bir Bind Noktası Oluşturun

`BindPoint` bir sahne özelliğini animasyon eğrisine bağlar. Burada çeviri (Translation) özelliğini bağlıyoruz.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Adım 6: X Bileşeninde Animasyon Eğrisini Bağlayın

Şimdi **X** ekseni için bir animasyon eğrisi oluşturuyoruz. Bu, **animasyon eğrisi oluşturma** adımını gösterir ve **anahtar kareleri bağlamayı** gösterir.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Adım 7: Z Bileşeninde Animasyon Eğrisini Bağlayın

Benzer şekilde, küpe daha dinamik bir hareket yolu vermek için **Z** eksenini canlandırıyoruz.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Adım 8: 3D Sahneyi Kaydedin

Canlandırılmış sahneyi bir FBX dosyasına dışa aktarın. `FBX7500ASCII` formatı 3D araçları tarafından yaygın olarak desteklenir.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Adım 9: Başarı Mesajını Göster

Kullanıcıya animasyonun başarıyla eklendiğine dair geri bildirim verin.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Canlandırılmış Sahneyi FBX'e Dışa Aktarın

Bir küpü canlandırdıktan sonra en yaygın görevlerden biri, diğer 3D uygulamaları tarafından kullanılabilmesi için **canlandırılmış sahneyi FBX olarak dışa aktarmaktır**. Yukarıdaki kod zaten sahneyi FBX7500ASCII formatında kaydeder; bu, anahtar kare verilerini korur ve Autodesk Maya, Blender ve Unity gibi araçlarla sorunsuz çalışır. Oluşturulan `.fbx` dosyasını açtığınızda, küpün X ve Z eksenlerinde anahtar kare dizileriyle tam olarak tanımlandığı gibi hareket ettiğini görmelisiniz.

## Yaygın Sorunlar ve Çözümler

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| Hareket gözlemlenmedi | Anahtar kare zamanları oynatma aralığıyla eşleşmiyor | Sahnenin animasyon zaman çizelgesinin anahtar kare zamanlarını (bu örnekte 0‑5 saniye) kapsadığından emin olun. |
| Yanlış dosya yolu | `output` var olmayan bir dizine işaret ediyor | Önce dizini oluşturun veya mutlak bir yol kullanın. |
| Lisans istisnası | Üretimde geçerli bir lisans olmadan çalıştırmak | `Scene` oluşturulmadan önce Aspose.3D lisansınızı uygulayın. |

## Sıkça Sorulan Sorular

### S1: Aspose.3D belgelerini nereden bulabilirim?
A1: Belgeler [burada](https://reference.aspose.com/3d/net/) mevcuttur.

### S2: Aspose.3D for .NET'i nasıl indirebilirim?
A2: [sürüm sayfasından](https://releases.aspose.com/3d/net/) indirebilirsiniz.

### S3: Ücretsiz deneme mevcut mu?
A3: Evet, ücretsiz denemeyi [buradan](https://releases.aspose.com/) alabilirsiniz.

### S4: Aspose.3D için destek nereden alabilirim?
A4: Destek için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S5: Geçici bir lisans alabilir miyim?
A5: Evet, geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

## Ek SSS (AI‑Optimizeli)

**S: Rotasyon veya ölçek gibi diğer özellikleri de canlandırabilir miyim?**  
A: Kesinlikle. `cube1.Transform.FindProperty("Rotation")` ya da `"Scale"` kullanın ve aynı şekilde anahtar kare dizilerini bağlayın.

**S: Aspose.3D Bezier ve Linear dışındaki anahtar kare interpolasyon tiplerini destekliyor mu?**  
A: Evet, daha fazla kontrol için `Interpolation.Step` ve `Interpolation.Cubic` tiplerini de destekler.

**S: Dışa aktarmadan önce animasyonu nasıl ön izleyebilirim?**  
A: Aspose.3D API'sinde basit bir görüntüleyici sağlar; alternatif olarak, dışa aktarılan FBX'i Autodesk FBX Review gibi bir 3D görüntüleyicide yükleyebilirsiniz.

**S: Aynı anda birden fazla küpü canlandırmak mümkün mü?**  
A: Her küp için ayrı düğümler oluşturun, ilgili özelliklerini alın ve bağımsız anahtar kare dizilerini bağlayın.

## Sonuç

Tebrikler! Aspose.3D for .NET kullanarak bir 3D sahnede **küp nasıl canlandırılır** konusunu yeni öğrendiniz. Artık **animasyon eğrileri oluşturmayı**, **anahtar kareleri bağlamayı** ve **canlandırılmış sahneyi FBX olarak dışa aktarmayı** biliyorsunuz, böylece statik geometrileri hayata geçirebilirsiniz. Rotasyonlar, ölçeklendirme veya hatta morf hedefleriyle denemeler yaparak animasyon araç setinizi genişletebilirsiniz.

---

**Son Güncelleme:** 2026-03-28  
**Test Edilen Versiyon:** Aspose.3D 24.11 for .NET  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}