---
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Twist Uygulamak
linktitle: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Twist Uygulamak
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java'yı kullanarak 3D modellerinize nasıl yenilik ekleyeceğinizi öğrenin. Gelişmiş doğrusal ekstrüzyon efektleri için adım adım kılavuzumuzu izleyin.
weight: 14
url: /tr/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Doğrusal Ekstrüzyonda Twist Uygulamak

## giriiş

Aspose.3D for Java kullanarak doğrusal ekstrüzyonda bir değişiklik uygulamaya yönelik bu adım adım eğitime hoş geldiniz. Aspose.3D, geliştiricilerin 3D dosya formatlarıyla çalışmasına olanak tanıyan, 3D sahneleri oluşturmak, değiştirmek ve işlemek için güçlü işlevsellik sunan güçlü bir Java kütüphanesidir. Bu eğitimde, 3D modellerinizi geliştirmek için doğrusal ekstrüzyon işlemi sırasında büküm efektinin nasıl uygulanacağını keşfedeceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Java Geliştirme Ortamı: Sisteminizde Java'nın kurulu olduğundan emin olun.
-  Aspose.3D Library: Java için Aspose.3D kütüphanesini şuradan indirip yükleyin:[İndirme: {link](https://releases.aspose.com/3d/java/).
-  Dokümantasyon: Bkz.[Aspose.3D belgeleri](https://reference.aspose.com/3d/java/) kapsamlı rehberlik için.

## Paketleri İçe Aktar

Kodlama işlemine başlamadan önce gerekli paketleri Java projenize aktarın. İşte bunun nasıl yapılacağına dair bir örnek:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. Adım: Belge Dizinini Ayarlayın

3B sahnenizin kaydedileceği belge dizinini ayarlayarak başlayın.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Adım 2: Temel Profili Başlatın

Ekstrüzyona tabi tutulacak taban profilini başlatın. Bu örnekte yuvarlama yarıçapına sahip bir dikdörtgen şekli kullanıyoruz.

```java
// ExStart:BaseProfile'ı Başlat
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:BaseProfile'ı Başlat
```

## 3. Adım: Bir Sahne Oluşturun

Ekstrüzyona tabi tutulan düğümleri barındırmak için bir 3B sahne oluşturun.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## 4. Adım: Düğümler Oluşturun

Sahne içinde sol ve sağ düğümler oluşturun. Sol düğümün çevirisini ayarlayın.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Adım 5: Twist ile Doğrusal Ekstrüzyon Gerçekleştirin

Bükme ve dilimleme özelliklerini uygulayarak hem sol hem de sağ düğümlerde doğrusal ekstrüzyon gerçekleştirin.

```java
// ExStart:Twist ile Doğrusal Ekstrüzyon
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:Bükümlü Doğrusal Ekstrüzyon
```

## Adım 6: 3D Sahneyi Kaydet

3B sahneyi Wavefront OBJ dosya formatında kaydedin.

```java
// ExStart:3DScene'i Kaydet
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:3DScene'i Kaydet
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonda başarılı bir şekilde büküm uyguladınız. Bu eğitimde, 3D modelleme yeteneklerinizi geliştirmenize yardımcı olacak ayrıntılı, adım adım bir kılavuz sağlanmıştır.

## SSS'ler

### S1: Aspose.3D for Java'yı diğer 3D dosya formatlarıyla çalışmak için kullanabilir miyim?

Cevap1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekleyerek farklı dosya türlerini içe aktarmanıza, dışa aktarmanıza ve değiştirmenize olanak tanır.

### S2: Aspose.3D for Java desteğini nerede bulabilirim?

 A2: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.

### S3: Aspose.3D for Java'nın ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümüne şuradan erişebilirsiniz:[Burada](https://releases.aspose.com/).

### S4: Aspose.3D for Java için nasıl geçici lisans alabilirim?

 Cevap4: Geçici bir lisans alın[geçici lisans sayfası](https://purchase.aspose.com/temporary-license/).

### S5: Aspose.3D for Java'yı nereden satın alabilirim?

 Cevap5: Java için Aspose.3D'yi şu adresten satın alın:[satın alma sayfası](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
