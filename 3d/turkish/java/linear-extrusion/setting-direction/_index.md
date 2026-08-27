---
date: 2026-08-02
description: Aspose.3D for Java kullanarak lineer ekstrüzyonda ekstrüzyon yönünü nasıl
  değiştireceğinizi ve OBJ dosyalarını nasıl dışa aktaracağınızı öğrenin. Adım adım
  rehberimizi izleyin.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Ekstrüzyon Yönünü Değiştir – Aspose.3D Java
og_description: Aspose.3D for Java ile lineer ekstrüzyonda ekstrüzyon yönünü değiştirin
  ve OBJ dosyalarını dışa aktarın. Bu rehber, adım adım kod ve geliştiriciler için
  ipuçları sunar.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Ekstrüzyon Yönünü Değiştir – Aspose.3D Java Öğreticisi
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 3D Modellerde Ekstrüzyon Yönünü Değiştir – Aspose.3D Java
url: /tr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Modellerde Ekstrüzyon Yönünü Değiştirme – Aspose.3D Java

## Giriş

Bu kapsamlı öğreticide, Aspose.3D for Java ile lineer ekstrüzyon yaparken **ekstrüzyon yönünü nasıl değiştireceğinizi** keşfedeceksiniz. CAD benzeri bir araç geliştiriyor, bir oyun motoru için varlıklar hazırlıyor ya da 3‑D baskı için parçalar üretiyor olun, ekstrüzyon yönünü kontrol etmek tam olarak ihtiyacınız olan şekli oluşturmanızı sağlar. Bir profil başlatmaktan sonucu OBJ dosyası olarak kaydetmeye kadar her adımı adım adım göstereceğiz, böylece **3D model OBJ** dosyalarını doğrudan Java'dan dışa aktarabilirsiniz.

## Hızlı Yanıtlar
- **Lineer ekstrüzyonu gerçekleştiren sınıf hangisidir?** `LinearExtrusion`
- **Ekstrüzyon vektörünü ayarlayan metod hangisidir?** `setDirection(Vector3 direction)`
- **Sonuç OBJ olarak kaydedilebilir mi?** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Üretim için lisans gerekli mi?** A free trial is available; a license is mandatory for commercial use.
- **Aspose.3D ile en iyi çalışan IDE hangisidir?** IntelliJ IDEA and Eclipse are fully supported.

## Lineer Ekstrüzyon Nedir?

Lineer ekstrüzyon, bir dikdörtgen veya daire gibi bir 2‑D taslağı düz bir hat boyunca uzatarak 3‑D katı oluşturma işlemidir. Varsayılan olarak ekstrüzyon pozitif Z‑ekseni boyunca gerçekleşir, ancak Aspose.3D `setDirection` özelliği ile bu yolu değiştirmenize olanak tanır ve nihai geometri üzerinde tam kontrol sağlar.

## Lineer Ekstrüzyonda Ekstrüzyon Yönünü Neden Değiştirmelisiniz?

Ekstrüzyon yönünü değiştirmek, yeni geometrileri mevcut nesnelerle hizalamanızı, ekstra dönüşüm uygulamadan eğimli bileşenler oluşturmanızı ve sonraki işlem hatları (ör. 3‑D yazıcılar veya oyun motorları) tarafından gereken koordinat sistemine uyan modeller üretmenizi sağlar. Bu, son‑işlem adımlarına olan ihtiyacı ortadan kaldırır ve gereksiz dönüşlerden kaçınan yön vektörleri kullanıldığında dosya boyutu yükünü %15'e kadar azaltır.

## Ön Koşullar

- Java hakkında temel bilgi.
- Aspose.3D kütüphanesi yüklü. [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz. Tüm Aspose sürümlerine ana sayfadan [buradan](https://releases.aspose.com/) göz atabilirsiniz.
- Eclipse veya IntelliJ IDEA gibi bir IDE.

## Paketleri İçe Aktarma

`com.aspose.threed` ad alanı, temel 3‑D sınıflarını ve yardımcı tipleri sağlar.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Temel Profili Başlatma

`RectangleShape` sınıfı, ekstrüde edilecek 2‑D profili oluşturur. Küçük bir yuvarlama yarıçapı, kenarlara pürüzsüz bir görünüm kazandırır.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Adım 2: Bir Sahne Oluşturma

`Scene` sınıfı, Aspose.3D'nin tüm 3‑D düğümleri, ışıkları, kameraları ve materyalleri tutan üst‑seviye konteyneridir.

```java
Scene scene = new Scene();
```

## Adım 3: Düğümler Oluşturma

`Node`, sahne grafiğinde bir nesneyi temsil eder ve geometri, dönüşümler ve diğer özellikleri eklemenize olanak tanır.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 4: Sol Düğümde Lineer Ekstrüzyon Yapma

`LinearExtrusion`, bir 2‑D profili 3‑D bir ağ (mesh) haline getirerek ekstrüzyon işlemini gerçekleştirir.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Adım 5: Sağ Düğümde Yön ile Lineer Ekstrüzyon Yapma

Burada **ekstrüzyon yönünü değiştiriyoruz**. `setDirection` metoduna özel bir `Vector3` geçirerek, ekstrüzyon (0.3, 0.2, 1) vektörünü izler ve sahnenin koordinat sistemiyle hizalanan eğik bir şekil üretir.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Adım 6: 3D Sahneyi Kaydetme

`save` metodu, sahneyi belirtilen formatta bir dosyaya yazar.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| OBJ dosyası boş görünüyor | Profil bir düğüme eklenmedi | `createChildNode`'un geçerli bir düğümde çağrıldığından emin olun |
| Yön değişmemiş gibi görünüyor | `setDirection` ekstrüzyon zaten oluşturulduktan sonra çağrıldı | Yönü, gösterildiği gibi `LinearExtrusion` başlatıcısı içinde ayarlayın |
| Düşük çözünürlüklü ağ | `setSlices` değeri çok düşük | Dilim sayısını artırın (ör. 100 veya daha fazla) |

## Sonuç

Artık lineer bir ekstrüzyonda **ekstrüzyon yönünü nasıl değiştireceğinizi**, burulma ve dilim ayarlarını nasıl ince ayarlayacağınızı ve Aspose.3D for Java kullanarak **3D model OBJ** dosyalarını nasıl dışa aktaracağınızı biliyorsunuz. Bu teknikler, geometri oluşturma üzerinde ayrıntılı kontrol sağlar ve 3‑D varlıkları daha büyük işlem hatlarına entegre etmeyi kolaylaştırır.

## Sık Sorulan Sorular

**Q:** Aspose.3D'yi diğer programlama dilleriyle kullanabilir miyim?  
**A:** Evet—Aspose.3D .NET ve Java için API'ler sağlar, çapraz platform geliştirmeye olanak tanır.

**Q:** Aspose.3D için ücretsiz deneme sürümü mevcut mu?  
**A:** Kesinlikle. Tüm özellik setini ücretsiz deneme sürümüyle [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

**Q:** Aspose.3D for Java için ayrıntılı belgeleri nerede bulabilirim?  
**A:** Kapsamlı referans [burada](https://reference.aspose.com/3d/java/) mevcuttur.

**Q:** Aspose.3D için destek nasıl alabilirim?  
**A:** Topluluk ve ürün ekibinden yardım almak için resmi [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**Q:** Test için geçici lisanslar mevcut mu?  
**A:** Evet—geçici lisanslar [buradan](https://purchase.aspose.com/temporary-license/) alınabilir.

**Son Güncelleme:** 2026-08-02  
**Test Edilen:** Aspose.3D for Java (latest release)  
**Yazar:** Aspose

{{< blocks/products/products-backtop-button >}}

## İlgili Öğreticiler

- [Şekil Ekstrüzyonu Nasıl Yapılır - Java'da Lineer Ekstrüzyon ile 3D Modeller Oluşturma](/3d/java/linear-extrusion/)
- [Aspose.3D ile Java'da 3D Ekstrüzyon Oluşturma](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D Grafik Öğreticisi – Lineer Ekstrüzyonda Merkez](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}