---
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Büküm Ofsetini Kullanma
linktitle: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Büküm Ofsetini Kullanma
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java ile 3D modelleme becerilerinizi geliştirin. Bu kapsamlı eğitimde Doğrusal Ekstrüzyonda Büküm Ofsetini kullanmayı öğrenin.

type: docs
weight: 15
url: /tr/java/linear-extrusion/using-twist-offset/
---
## giriiş

3D grafiklerin dinamik dünyasında, doğrusal ekstrüzyon sanatında ustalaşmak oyunun kurallarını değiştiriyor. Aspose.3D for Java ile Twist Offset özelliğini doğrusal ekstrüzyon prosesinize dahil ederek 3D modelleme becerilerinizi geliştirebilirsiniz. Bu eğitim, Aspose.3D for Java kullanarak Doğrusal Ekstrüzyonda Büküm Ofsetini kullanma adımlarında size rehberlik edecek ve çarpıcı 3D sahneler oluşturmanız için gerekli araçları sağlayacaktır.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Java Ortamı: Sisteminizde bir Java geliştirme ortamının kurulu olduğundan emin olun.
-  Aspose.3D for Java: Aspose.3D kütüphanesini aşağıdaki adresten indirip yükleyin:[İndirme: {link](https://releases.aspose.com/3d/java/).
-  Dokümantasyon: Kendinizi tanıyın[Aspose.3D for Java belgeleri](https://reference.aspose.com/3d/java/).

## Paketleri İçe Aktar

Aspose.3D for Java'yı kullanmaya başlamak için Java projenizde gerekli paketleri içe aktarın. Sorunsuz entegrasyon için gerekli kitaplıkları eklediğinizden emin olun.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 1. Adım: Ortamı Ayarlayın

Java geliştirme ortamınızı kurarak ve Aspose.3D for Java'nın doğru şekilde kurulduğundan emin olarak başlayın.

## Adım 2: Temel Profili Başlatın

Ekstrüzyon için bir taban profili oluşturun; bu durumda yuvarlama yarıçapı 0,3 olan bir RectangleShape oluşturun.

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
// Ekstrüzyona tabi tutulacak taban profilini başlatın
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 3. Adım: 3B Sahne Oluşturun

Ekstrüzyona tabi tutulan nesnelerinizi barındıracak bir 3 boyutlu sahne oluşturun.

```java
// Bir sahne yarat
Scene scene = new Scene();
```

## 4. Adım: Düğümler Oluşturun

Farklı varlıkları temsil etmek için sahne içinde düğümler oluşturun.

```java
// Sol düğüm oluştur
Node left = scene.getRootNode().createChildNode();
// Sağ düğüm oluştur
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 5: Doğrusal Ekstrüzyonu Gerçekleştirin

Çeşitli özelliklere sahip hem sol hem de sağ düğümlerde doğrusal ekstrüzyondan yararlanın.

```java
// Bükme ve dilimleme özelliğini kullanarak sol düğümde doğrusal ekstrüzyon gerçekleştirin
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Büküm, büküm ofseti ve dilimler özelliğini kullanarak sağ düğümde doğrusal ekstrüzyon gerçekleştirin
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Adım 6: 3D Sahneyi Kaydedin

Yeni oluşturduğunuz 3D sahnenizi belirtilen dosya formatıyla kaydedin.

```java
// 3D sahneyi kaydet
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak Doğrusal Ekstrüzyonda Twist Offset'i başarıyla uyguladınız. Bu güçlü özellik, 3D modelleme çalışmalarınız için bir olasılıklar dünyasının kapılarını açarak karmaşık ve büyüleyici sahneler oluşturmanıza olanak tanır.

## SSS'ler

### S1: Aspose.3D for Java'yı ticari olmayan projelerde kullanabilir miyim?

 C1: Evet, Aspose.3D for Java hem ticari hem de ticari olmayan projelerde kullanılabilir. Kontrol edin[lisanslama seçenekleri](https://purchase.aspose.com/buy) daha fazla ayrıntı için.

### S2: Aspose.3D for Java desteğini nerede bulabilirim?

 A2: Ziyaret edin[Java forumu için Aspose.3D](https://forum.aspose.com/c/3d/18) yardım almak ve toplulukla bağlantı kurmak için.

### S3: Aspose.3D for Java'nın ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümünü şuradan keşfedebilirsiniz:[sürümler sayfası](https://releases.aspose.com/).

### S4: Aspose.3D for Java için nasıl geçici lisans edinebilirim?

 Cevap4: adresini ziyaret ederek projeniz için geçici bir lisans alın[bu bağlantı](https://purchase.aspose.com/temporary-license/).

### S5: Ek örnekler ve eğitimler mevcut mu?

 A5: Evet, bkz.[dokümantasyon](https://reference.aspose.com/3d/java/) Daha fazla örnek ve ayrıntılı eğitimler için.