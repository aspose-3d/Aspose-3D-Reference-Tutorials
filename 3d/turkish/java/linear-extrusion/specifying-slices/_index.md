---
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Dilimleri Belirleme
linktitle: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Dilimleri Belirleme
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonda dilimleri belirtmeyi öğrenin. Bu adım adım kılavuzla 3D modelleme becerilerinizi geliştirin.
type: docs
weight: 13
url: /tr/java/linear-extrusion/specifying-slices/
---
## giriiş

Karmaşık 3D modeller oluşturmak çoğu zaman yaratıcılıktan fazlasını gerektirir; elinizdeki araçların tam olarak anlaşılmasını gerektirir. Aspose.3D for Java bu açıdan ezber bozan bir yazılımdır. Bu öğreticide belirli bir hususa odaklanacağız: doğrusal ekstrüzyonda dilimleri belirleme.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

1. Java Ortamı: Sisteminizde bir Java geliştirme ortamının kurulu olduğundan emin olun.
2.  Aspose.3D for Java: Aspose.3D kütüphanesini indirin ve yükleyin. Gerekli paketleri bulabilirsiniz[Burada](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktar

Java projenizde Aspose.3D kütüphanesini içe aktarın. Bu, üzerinde çalışacağımız işlevlere erişim açısından çok önemlidir. Aşağıdaki import ifadesini kodunuza ekleyin:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Şimdi örneği birden çok adıma ayıralım.

## 1. Adım: Sahneyi Ayarlayın

Ekstrüzyona tabi tutulacak taban profilini başlatın; bu durumda,`RectangleShape` belirli bir yuvarlama yarıçapına sahip. İçinde çalışmak için bir 3B sahne oluşturun.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## 2. Adım: Düğümler Oluşturun

Sahne içinde sol ve sağ düğümler oluşturun. Uzamsal değişim için sol düğümün çevirisini ayarlayın.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 3: Dilimlerle Doğrusal Ekstrüzyon

Her iki düğümde de dilim sayısını belirterek doğrusal ekstrüzyon gerçekleştirin. Sihir yapılan yer burasıdır.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Adım 4: Sahneyi Kaydedin

3B sahneyi istediğiniz formatta, bu durumda bir Wavefront OBJ dosyası olarak kaydedin.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonda dilimleri nasıl belirleyeceğinizi başarıyla öğrendiniz. Bu beceri, 3D modelleme yolculuğunuzda yeni olanakların kapısını açar.

## SSS'ler

### S1: Aspose.3D for Java'yı nasıl indirebilirim?

 A1: Kütüphaneyi indirebilirsiniz[Burada](https://releases.aspose.com/3d/java/).

### S2: Aspose.3D belgelerini nerede bulabilirim?

 A2: Belgelere bakın[Burada](https://reference.aspose.com/3d/java/).

### S3: Ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).

### S4: Aspose.3D için nasıl destek alabilirim?

 Cevap4: Destek forumunu ziyaret edin[Burada](https://forum.aspose.com/c/3d/18).

### S5: Geçici bir lisans satın alabilir miyim?

 Cevap5: Evet, geçici lisans alınabilir[Burada](https://purchase.aspose.com/temporary-license/).