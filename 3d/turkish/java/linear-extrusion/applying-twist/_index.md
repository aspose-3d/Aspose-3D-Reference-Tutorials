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

## Giriiş

Bu uygulamalı **java 3d öğretici**'da **3d sahne** görüntü oluşturmayı, *lineer ekstrüzyon büküm* uygulamasını ve sonunda Aspose.3D for Java'yı kullanarak **obj java** bölgesel olarak ayrılan bölümü kullanır. Bir oyun varlığı, bir CAD prototipi ya da bir görsel efektler oluşturulmuş olun, ekstrüzyon sırasında bir büküm seçme modellerinize düz yapıyla elde edilmesi zor olan dinamik, spiral benzeri bir görünüm kazandırır.

## Hızlı Yanıtlar
- **Ekstrüzyonda “twist” ne anlama gelir?** Profil, ekstrüzyon yolu boyunca süreç boyunca yürütülür.
- **Hangi esnekliği büküm özelliği sağlar?** Aspose.3D for Java.
- **Sonucu OBJ olarak ayrılabilir miyim?** Evet – `FileFormat.WAVEFRONTOBJ` kullanın.
- **Bu eğitim için lisansa gerek var mı?** Üretim kullanımı için geçici ya da tam lisans gereklidir.
- **Hangi Java sürümü gereklidir?** Java8 veya üzeri.

## Doğrusal ekstrüzyonda "bükülme" nedir?

Büküm, ekstrüde edilen şeklin her diliminin belirli bir açısıyla döndürülen bir dönüşümüdür. Açıyı kontrol ederek, düz ekstrüzyonlara görsel ilgi katan spiraller, vida şekilleri veya torklar hafif oluşturabilirsiniz.

## Java için Aspose.3D'yi neden kullanmalısınız?

- **Çapraz format desteği:** OBJ, FBX ve STL dahil olmak üzere onlarca 3D formatını içinde ve saklanabilir.
- **Saf Java API:** Yerel bağımlılıkları yoktur, ancak herhangi bir Java projesine kolay entegrasyon sağlar.
- **Yüksek performanslı geometri motoru:** Twist gibi karmaşık işlemlerde hız kaybı olmadan.

## Önkoşullar

- **Java Development Kit (JDK) 8+** makinenizde kurulmuş olmalı.
- **Aspose.3D for Java** – [indirme bağlantısı](https://releases.aspose.com/3d/java/) üzerinden indirin.
- Temel Java söz dizimi ve 3-D kavramlarına ulaşılabilir.
- Referans için resmi [Aspose.3D dokümantasyonuna](https://reference.aspose.com/3d/java/) erişin.

## Paketleri İçe Aktar

İlk olarak, gerekli Aspose.3D sınıflarını projenize ekleyin.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Belge Dizinini Ayarlayın

Oluşturulan OBJ dosyalarının kaydedileceği konumu tanımlayın. Yer tutucuyu sisteminizdeki gerçek bir klasör yolu ile aydınlandı.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Adım 2: Temel Profili Başlatın

Ekstrüde edilecek şekli oluşturun. Burada kenarları daha yumuşak bir görünüme sahip olması için küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Adım 3: Düğümlerinizi Barındırmak İçin Bir Sahne Oluşturun

`Scene` nesnesi, tüm 3‑D varlıkların (mesh'ler, ışıklar, kameralar vb.) konteyneridir.  

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Adım 4: Sol ve Sağ Düğümleri Ekleyin

İki kardeş düğüm oluşturacağız: biri twist olmadan (karşılaştırma için) ve diğeri 90‑derecelik bir twist ile.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Adım 5: Bükme ile Doğrusal Ekstrüzyon Gerçekleştirin

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

## Adım 6: 3B Sahneyi OBJ Olarak Kaydedin

Son olarak, sahneyi bir OBJ dosyasına yazarak herhangi bir standart 3‑D görüntüleyicide açabilirsiniz.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Yaygın Sorunlar ve İpuçları

- **Dosya yolu hataları:** `MyDir` değişkeninin çalışma sisteminize uygun bir yol ayırma (`/` veya `\\`) ile bittiğinden emin olun.
- **Büküm açısı çok yüksek:** 360° üzerindeki açıların geometrisinin çakışmasına neden olabileceğini unutmayın; Öngörülebilir sonuçlar için 0‑360° arasında tutun.
- **Performans:** `setSlices` değerini artırma pürüzsüzlüğünü artırır ancak bellek tüketimini artırabilir; Çoğu durum için 100 dilim iyi bir dengedir.

## Sıkça Sorulan Sorular (Orijinal)

### S1: Aspose.3D for Java'yi diğer 3D dosya formatlarıyla çalışmak için kullanabilir miyim?

A1: Evet, Aspose.3D çeşitli 3D dosya formatlarını sunar; bu sayede farklı dosya türlerini içe aktarabilir, düzenleyebilir ve manipüle edebilirsiniz.

### S2: Aspose.3D for Java için desteği nereden bulabilirim?

C2: Topluluk desteği ve tartışmalar için [Aspose.3D forumu](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

### S3: Aspose.3D for Java için ücretsiz deneme sürümü var mı?

C3: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişebilirsiniz.

### S4: Aspose.3D for Java için geçici lisans nasıl alınabilir?

Cevap4: [Geçici lisans sayfasından](https://purchase.aspose.com/temporary-license/) geçici lisans edinebilirsiniz.

### S5: Aspose.3D for Java'yı nereden satın alabilirim?

Cevap5: Aspose.3D for Java'yi [satın alma sayfasının](https://purchase.aspose.com/buy) temin edebilirsiniz.

## Ek SSS (Yapay Zeka İçin Optimize Edilmiş)

**S: Twist yönü olabilir mi?**
C: Evet – `setTwist()` içinde negatif bir açıyı kullanarak ters yönde döndürme yapabilirsiniz.

**S: Ekstrüzyon boyunca farklı büküm değerlerinin gösterilmesi mümkün mü?**
C: Aspose.3D şu anda tek tip bir büküm uygular; Değişken büküm için birden fazla segmenti manuel olarak oluşturmanız gerekir.

**S: Dışa aktarılan OBJ verileri nasıl görüntülerim?**
C: Herhangi bir standart 3‑D görüntüleyici (ör. Blender, MeshLab) OBJ pencerelerini açabilirsiniz.

**S: Kütüphane, bükülmüş ekstrüzyonlarda doku haritalamasını içerir mi?**
C: Evet – ekstrüzyondan sonra düğümün mesh'ine malzeme veya UV koordinatlarını atayabilirsiniz.

## Çözüm

Artık **3D sahnesi** oluşturduğunuz, **lineer ekstrüzyon büküm** uyguladığınız ve sonucu Aspose.3D for Java kullanarak OBJ dosyasını kullanarak aktardığınız için tebrikler. Farklı profiller, büküm açıları ve kesit parçalarıyla deneyler yaparak oyunlar, simülasyonlar veya 3‑D baskı için benzersiz geometriler yaratabilirsiniz.

---

**Son Güncelleme:** 2026-02-20
**Edilen'i Test Edin:** Java 24.11 için Aspose.3D
**Yazar:** Aspose 

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}