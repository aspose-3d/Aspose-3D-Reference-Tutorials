---
date: 2026-02-20
description: Aspose.3D for Java kullanarak 3D sahne oluşturmayı ve lineer ekstrüzyon
  bükülmesi uygulamayı öğrenin. Kolay adım adım rehberle OBJ dosyalarını dışa aktarın.
linktitle: Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Doğrusal Ekstrüzyonda Burulma ile 3D Sahne Oluşturma – Aspose.3D for Java
url: /tr/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lineer Ekstrüzyonda Twist ile 3D Sahne Oluşturma – Aspose.3D for Java

## Introduction

Bu uygulamalı **java 3d tutorial**'da **3d sahne** nesneleri oluşturmayı, *lineer ekstrüzyon twist* uygulamayı ve sonunda Aspose.3D for Java kullanarak **obj java** dosyalarını dışa aktarmayı öğreneceksiniz. İster bir oyun varlığı, bir CAD prototipi ya da bir görsel efekt oluşturuyor olun, ekstrüzyon sırasında bir twist eklemek modellerinize düz ekstrüzyonla elde edilmesi zor olan dinamik, spiral benzeri bir görünüm kazandırır.

## Quick Answers
- **Ekstrüzyonda “twist” ne anlama gelir?** Profil, ekstrüzyon yolu boyunca kademeli olarak döndürülür.  
- **Hangi kütüphane twist özelliğini sağlar?** Aspose.3D for Java.  
- **Sonucu OBJ olarak dışa aktarabilir miyim?** Evet – `FileFormat.WAVEFRONTOBJ` kullanın.  
- **Bu eğitim için lisansa ihtiyacım var mı?** Üretim kullanımı için geçici ya da tam lisans gereklidir.  
- **Hangi Java sürümü gereklidir?** Java 8 veya üzeri.

## What is a “twist” in linear extrusion?

Twist, ekstrüde edilen şeklin her dilimini belirli bir açıyla döndüren bir dönüşümdür. Açıyı kontrol ederek, düz ekstrüzyonlara görsel ilgi katan spiraller, vida şekilleri veya hafif torklar oluşturabilirsiniz.

## Why use Aspose.3D for Java?

- **Çapraz format desteği:** OBJ, FBX ve STL dahil olmak üzere onlarca 3D formatını içe ve dışa aktarabilirsiniz.  
- **Saf Java API:** Yerel bağımlılıkları yoktur, bu da herhangi bir Java projesine kolay entegrasyon sağlar.  
- **Yüksek performanslı geometri motoru:** Twist gibi karmaşık işlemleri hız kaybı olmadan gerçekleştirir.

## Prerequisites

- **Java Development Kit (JDK) 8+** makinenizde kurulu olmalı.  
- **Aspose.3D for Java** – [download link](https://releases.aspose.com/3d/java/) üzerinden indirin.  
- Temel Java sözdizimi ve 3‑D kavramlarına aşina olun.  
- Referans için resmi [Aspose.3D documentation](https://reference.aspose.com/3d/java/) adresine erişin.

## Import Packages

İlk olarak, gerekli Aspose.3D sınıflarını projenize ekleyin.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set the Document Directory

Oluşturulan OBJ dosyasının kaydedileceği konumu tanımlayın. Yer tutucuyu sisteminizdeki gerçek bir klasör yolu ile değiştirin.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Step 2: Initialize the Base Profile

Ekstrüde edilecek şekli oluşturun. Burada kenarları daha yumuşak bir görünüme sahip olması için küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Step 3: Create a Scene to Host Your Nodes

`Scene` nesnesi, tüm 3‑D varlıkların (mesh'ler, ışıklar, kameralar vb.) konteyneridir.  

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Step 4: Add Left and Right Nodes

İki kardeş düğüm oluşturacağız: biri twist olmadan (karşılaştırma için) ve diğeri 90‑derecelik bir twist ile.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Step 5: Perform Linear Extrusion with Twist

`LinearExtrusion` yapıcı metodu profil ve ekstrüzyon uzunluğunu alır.  
- `setTwist(0)` → dönüş yok (düz ekstrüzyon).  
- `setTwist(90)` → uzunluk boyunca tam 90‑derecelik dönüş.  
Her iki düğüm de pürüzsüz geometri için 100 dilim kullanır.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Step 6: Save the 3D Scene as OBJ

Son olarak, sahneyi bir OBJ dosyasına yazarak herhangi bir standart 3‑D görüntüleyicide açabilirsiniz.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Common Issues & Tips

- **Dosya yolu hataları:** `MyDir` değişkeninin işletim sisteminize uygun bir yol ayırıcı (`/` veya `\\`) ile bittiğinden emin olun.  
- **Twist açısı çok yüksek:** 360° üzerindeki açıların geometri çakışmasına neden olabileceğini unutmayın; öngörülebilir sonuçlar için 0‑360° arasında tutun.  
- **Performans:** `setSlices` değerini artırmak pürüzsüzlüğü artırır ancak bellek tüketimini artırabilir; çoğu durum için 100 dilim iyi bir dengedir.

## Frequently Asked Questions (Original)

### Q1: Aspose.3D for Java'yi diğer 3D dosya formatlarıyla çalışmak için kullanabilir miyim?

A1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekler; bu sayede farklı dosya türlerini içe aktarabilir, dışa aktarabilir ve manipüle edebilirsiniz.

### Q2: Aspose.3D for Java için desteği nereden bulabilirim?

A2: Topluluk desteği ve tartışmalar için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

### Q3: Aspose.3D for Java için ücretsiz deneme sürümü var mı?

A3: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişebilirsiniz.

### Q4: Aspose.3D for Java için geçici lisans nasıl alabilirim?

A4: [Geçici lisans sayfasından](https://purchase.aspose.com/temporary-license/) geçici lisans edinebilirsiniz.

### Q5: Aspose.3D for Java'yi nereden satın alabilirim?

A5: Aspose.3D for Java'yi [satın alma sayfasından](https://purchase.aspose.com/buy) temin edebilirsiniz.

## Additional FAQ (AI‑Optimized)

**S: Twist yönünü değiştirebilir miyim?**  
C: Evet – `setTwist()` içinde negatif bir açı kullanarak ters yönde döndürme yapabilirsiniz.

**S: Ekstrüzyon boyunca farklı twist değerleri uygulamak mümkün mü?**  
C: Aspose.3D şu anda tek tip bir twist uygular; değişken twist için birden fazla segmenti manuel olarak oluşturmanız gerekir.

**S: Dışa aktarılan OBJ dosyasını nasıl görüntülerim?**  
C: Herhangi bir standart 3‑D görüntüleyici (ör. Blender, MeshLab) OBJ dosyalarını açabilir.

**S: Kütüphane, twisted ekstrüzyonlarda doku haritalamayı destekliyor mu?**  
C: Evet – ekstrüzyondan sonra düğümün mesh'ine malzeme veya UV koordinatları atayabilirsiniz.

## Conclusion

Artık **3D sahne** oluşturduğunuz, **lineer ekstrüzyon twist** uyguladığınız ve sonucu Aspose.3D for Java kullanarak OBJ dosyası olarak dışa aktardığınız için tebrikler. Farklı profiller, twist açıları ve dilim sayılarıyla deneyler yaparak oyunlar, simülasyonlar veya 3‑D baskı için benzersiz geometriler yaratabilirsiniz.

---

**Son Güncelleme:** 2026-02-20  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}