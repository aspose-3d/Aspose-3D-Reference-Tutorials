---
date: 2025-12-18
description: Aspose.3D for Java kullanarak 3D sahne oluşturmayı ve OBJ dosyasını kaydetmeyi
  öğrenin. Lineer ekstrüzyon yönü için adım adım rehberimizi izleyin.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D Sahne Oluştur – Extrüzyon Yönünü Ayarla Aspose.3D Java
url: /tr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Sahne Oluştur – Extrüzyon Yönünü Ayarlama Aspose.3D Java

## Introduction

Bu öğreticide, Aspose.3D for Java ile **3d sahne oluşturma** nesnelerini nasıl oluşturacağınızı ve extrüzyon yönünü nasıl kontrol edeceğinizi öğreneceksiniz. Mimari görselleştirmeler, ürün prototipleri veya oyun varlıkları oluşturuyor olun, lineer extrüzyonu ustalaşmak, karmaşık şekilleri hızlıca modelleme esnekliği sağlar. Java’da düğüm eklemekten **3d model obj** dosyalarını dışa aktarmaya** kadar her adımı adım adım göstereceğiz, böylece sonucu anında görebileceksiniz.

## Quick Answers
- **“create 3d scene” ne anlama geliyor?** Aspose.3D `Scene` nesnesini başlatmak anlamına gelir; bu nesne tüm geometri, ışıklar ve kameraları tutar.  
- **Extrüzyon yönünü nasıl ayarlarım?** `LinearExtrusion` örneğinde `setDirection(Vector3)` metodunu kullanın.  
- **Dışa aktarmak için hangi formatı kullanmalıyım?** OBJ formatı (`FileFormat.WAVEFRONTOBJ`) 3‑D iş akışları için yaygın olarak desteklenir.  
- **Aspose.3D için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme sürümü yeterlidir; üretim için ticari lisans gereklidir.  
- **Java’da daha fazla düğüm ekleyebilir miyim?** Evet—gerektiği kadar nesne eklemek için `scene.getRootNode().createChildNode()` kullanın.

## What is a “create 3d scene” workflow?

**“create 3d scene”** iş akışı, boş bir `Scene` nesnesiyle başlar, geometri ekler (örneğin extrüde profiller), dönüşümlerle konumlandırır ve sonunda sahneyi OBJ gibi bir dosya formatına kaydeder. Bu desen, Aspose.3D ile oluşturulan çoğu 3‑D uygulamanın temelini oluşturur.

## Why set extrusion direction?

Extrüzyon yönünü ayarlamak, şekli extrüde edilirken eğmenize, döndürmenize veya kaydırmanıza olanak tanır; böylece ek post‑işleme olmadan nihai geometri üzerinde kontrol sahibi olursunuz. Özellikle şu durumlarda faydalıdır:

- Konik sütunlar veya özel şekilli borular oluşturma.  
- Mekanik parçalarda standart dışı eksenlerle extrüzyonları hizalama.  
- Görsel efektler için sanatsal şekiller üretme.

## Prerequisites

İlerlemeye başlamadan önce şunlara sahip olduğunuzdan emin olun:

- Temel Java bilgisi.  
- Aspose.3D kütüphanesi kurulu – [buradan](https://releases.aspose.com/3d/java/) indirin.  
- Eclipse veya IntelliJ IDEA gibi bir IDE.

## Import Packages

İlk olarak, gerekli Aspose.3D sınıflarını içe aktarın:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Extrüde edilecek 2‑D profili oluşturun. Bu örnekte yuvarlatılmış bir dikdörtgen kullanıyoruz:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro ipucu:** Yuvarlama yarıçapını ayarlayarak, extrüzyondan önce dikdörtgen köşelerinin ne kadar keskin ya da yumuşak görüneceğini kontrol edin.

## Step 2: Create a Scene

Şimdi nesnelerimizi barındıracak **3d sahneyi oluşturuyoruz**:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

Sahnenin kök düğümüne iki alt düğüm (sol ve sağ) ekleyecek ve sol düğümü biraz yana kaydıracağız:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

Profili, sol düğümde varsayılan Z‑eksen yönünü kullanarak extrüde edin. Ayrıca tam 360° bükülme ayarlayıp, pürüzsüzlük için dilim sayısını artırıyoruz:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

Burada **yönü nasıl ayarlayacağımızı** gösteriyoruz; özel bir `Vector3` sağlayarak. Bu, extrüzyonu (0.3, 0.2, 1) vektörüne doğru eğiyor:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

Son olarak, sonucu herhangi bir 3‑D görüntüleyicide görmek için **obj dosyasını kaydediyoruz**:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Oluşturulan OBJ dosyasını açtığınızda, iki extrüde dikdörtgen göreceksiniz: biri varsayılan yönle, diğeri ise ayarladığımız vektöre göre eğilmiş.

## Common Issues and Solutions

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| OBJ dosyası boş görünüyor | Sahne kaydedilmemiş veya yol hatalı | `MyDir`'in yazılabilir bir klasöre işaret ettiğini ve dosya adının `.obj` ile bittiğini doğrulayın. |
| Extrüzyon düz görünüyor | `setSlices` değeri çok düşük | Daha pürüzsüz geometri için `setSlices` değerini artırın (örnek: 200). |
| Yön değişmemiş gibi | Vektör normalize edilmemiş | Normalize bir `Vector3` kullanın veya istenen eğimi yansıtacak şekilde değerleri ayarlayın. |

## Frequently Asked Questions

### Q1: Aspose.3D'yi diğer programlama dilleriyle kullanabilir miyim?
A1: Aspose.3D, .NET ve Java dahil çeşitli dilleri destekler.

### Q2: Aspose.3D için ücretsiz deneme sürümü mevcut mu?
A2: Evet, Aspose.3D özelliklerini ücretsiz deneme sürümüyle keşfedebilirsiniz [burada](https://releases.aspose.com/).

### Q3: Aspose.3D for Java için ayrıntılı belgeleri nerede bulabilirim?
A3: Kapsamlı dokümantasyon [burada](https://reference.aspose.com/3d/java/) mevcuttur.

### Q4: Aspose.3D için destek nasıl alabilirim?
A4: Yardım ve sorularınız için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### Q5: Aspose.3D için geçici lisanslar mevcut mu?
A5: Evet, geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

---

**Son Güncelleme:** 2025-12-18  
**Test Edilen:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}