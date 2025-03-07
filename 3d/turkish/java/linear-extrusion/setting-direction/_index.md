---
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Yönü Ayarlama
linktitle: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Yönü Ayarlama
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java ile doğrusal ekstrüzyona hakim olun! Kusursuz 3D programlama için kılavuzumuzu takip edin. Büyüleyici bir deneyim için hemen indirin.
weight: 12
url: /tr/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Doğrusal Ekstrüzyonda Yönü Ayarlama

## giriiş

Aspose.3D for Java kullanarak doğrusal ekstrüzyonda yön ayarlamaya ilişkin adım adım kılavuzumuza hoş geldiniz. Aspose.3D, geliştiricilerin 3D dosyalar ve sahnelerle sorunsuz bir şekilde çalışmasına olanak tanıyan güçlü bir Java kütüphanesidir. Bu eğitimde, doğrusal ekstrüzyonda yön belirleme gibi özel bir göreve odaklanarak 3D programlamadaki yeterliliğinizi geliştireceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Java programlama dili hakkında temel bilgiler.
-  Aspose.3D kütüphanesi kuruldu. Şuradan indirebilirsiniz[Burada](https://releases.aspose.com/3d/java/).
- Eclipse veya IntelliJ gibi Java için entegre bir geliştirme ortamı (IDE).

## Paketleri İçe Aktar

Projenizi başlatmak için gerekli paketleri içe aktardığınızdan emin olun:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Temel Profili Başlatın

 Ekstrüzyona tabi tutulacak taban profilini başlatarak başlayın. Bu örnekte, bir kullanıyoruz`RectangleShape` 0,3 yuvarlama yarıçapı ile:

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Adım 2: Bir Sahne Oluşturun

Daha sonra, kalıptan çıkarılan nesneleri içerecek bir 3B sahne oluşturun:

```java
Scene scene = new Scene();
```

## 3. Adım: Düğümler Oluşturun

Sahne içinde sol ve sağ düğümler oluşturun:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 4: Sol Düğümde Doğrusal Ekstrüzyon Gerçekleştirin

 kullanarak sol düğümde doğrusal ekstrüzyon gerçekleştirin.`LinearExtrusion`büküm ve dilimler gibi belirtilen parametrelere sahip sınıf:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Adım 5: Yönlü Sağ Düğümde Doğrusal Ekstrüzyon Gerçekleştirin

 Sağ düğümde doğrusal ekstrüzyon gerçekleştirin ve`setDirection` Ekstrüzyon yönünü tanımlama özelliği:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Adım 6: 3D Sahneyi Kaydet

3B sahneyi istediğiniz dosya formatında kaydedin. Bu örnekte onu Wavefront OBJ dosyası olarak kaydediyoruz:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonda yönü nasıl ayarlayacağınızı başarıyla öğrendiniz. Bu eğitim, 3D programlama becerilerinizi geliştirir ve yaratıcı projeler için yeni olanakların kapısını açar.

## SSS'ler

### S1: Aspose.3D'yi diğer programlama dilleriyle kullanabilir miyim?

Cevap1: Aspose.3D, .NET ve Java dahil olmak üzere çeşitli programlama dillerini destekler.

### Q2. Aspose.3D'nin ücretsiz deneme sürümü mevcut mu?

 Cevap2: Evet, Aspose.3D'nin özelliklerini ücretsiz deneme sürümüyle keşfedebilirsiniz[Burada](https://releases.aspose.com/).

### S3: Aspose.3D for Java'nın ayrıntılı belgelerini nerede bulabilirim?

 A3: Kapsamlı belgeler mevcut[Burada](https://reference.aspose.com/3d/java/).

### S4: Aspose.3D için nasıl destek alabilirim?

 A4: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) herhangi bir yardım veya sorularınız için.

### S5: Aspose.3D için geçici lisanslar mevcut mu?

 Cevap5: Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
