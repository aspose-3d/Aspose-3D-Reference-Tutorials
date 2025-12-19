---
date: 2025-12-19
description: Aspose.3D for Java ile Lineer Ekstrüzyonda Twist Ofset kullanarak 3D
  sahne oluşturmayı ve 3D obj'yi dışa aktarmayı öğrenin.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Twist Offset ile 3D sahne oluşturma – Aspose.3D Java
url: /tr/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Twist Offset ile 3d scene oluşturma – Aspose.3D for Java

## Giriş

Dinamik 3D grafik dünyasında, **create 3d scene**'i lineer ekstrüzyonla oluşturmayı öğrenmek bir oyun değiştiricidir. Aspose.3D for Java ile Twist Offset özelliğini lineer ekstrüzyon sürecinize dahil ederek 3D modelleme becerilerinizi yükseltebilirsiniz. Bu öğretici, Aspose.3D for Java kullanarak Linear Extrusion’da Twist Offset’i nasıl kullanacağınızı adım adım göstererek etkileyici 3D sahneler oluşturmanız için gerekli araçları sunar.

## Hızlı Yanıtlar
- **Twist Offset ne yapar?** Twist’in başlangıcını ekstrüzyon yolu boyunca kaydırır, geometrinin kontrolünü artırır.  
- **Hangi dosya formatı dışa aktarım için kullanılır?** Örnek modeli Wavefront OBJ (`.obj`) olarak kaydeder.  
- **Geliştirme için lisansa ihtiyacım var mı?** Test için ücretsiz deneme yeterlidir; üretim için ticari lisans gereklidir.  
- **Hangi Java sürümü gereklidir?** Java 8 veya üzeri.  
- **Dilim sayısını değiştirebilir miyim?** Evet – `setSlices` metodu twist’in pürüzsüzlüğünü tanımlar.

## Önkoşullar

Öğreticiye başlamadan önce aşağıdaki önkoşulları yerine getirdiğinizden emin olun:

- Java Ortamı: Sisteminizde bir Java geliştirme ortamı kurulu olduğundan emin olun.  
- Aspose.3D for Java: Aspose.3D kütüphanesini [download link](https://releases.aspose.com/3d/java/) adresinden indirin ve kurun.  
- Dokümantasyon: [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) ile tanışın.  

## Paketleri İçe Aktarma

Java projenizde Aspose.3D for Java'yi kullanmaya başlamak için gerekli paketleri içe aktarın. Sorunsuz entegrasyon için gereken kütüphaneleri eklediğinizden emin olun.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Adım 1: Ortamı Kurun

Java geliştirme ortamınızı kurun ve Aspose.3D for Java'nin doğru şekilde yüklendiğinden emin olun.

## Adım 2: Temel Profili Başlatın

Bu örnekte, yuvarlama yarıçapı 0.3 olan bir `RectangleShape` ile ekstrüzyon için temel profil oluşturun.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Adım 3: 3D Scene Oluşturun

Ekstrüde edilmiş nesnelerinizi barındıracak bir 3D scene oluşturun.

```java
// Create a scene
Scene scene = new Scene();
```

## Adım 4: Düğümler Oluşturun

Sahnedeki farklı varlıkları temsil edecek düğümler üretin.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 5: Lineer Ekstrüzyon Yapın

Sol ve sağ düğümler üzerinde çeşitli özelliklerle lineer ekstrüzyon uygulayın.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Adım 6: 3D Scene'i Kaydedin

Yeni oluşturduğunuz 3D scene'i belirtilen dosya formatı ile kaydedin.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 3d modeli nasıl kaydeder ve 3d obj olarak dışa aktarılır

Önceki adımda kullanılan `scene.save` çağrısı **3d modeli** bir OBJ dosyası olarak kaydeder; bu, yaygın olarak desteklenen **export 3d obj** formatıdır. `FileFormat` enum'ını ayarlayarak dosya adını değiştirebilir veya başka bir desteklenen format (ör. STL, FBX) seçebilirsiniz.

## Sonuç

Tebrikler! Aspose.3D for Java kullanarak Linear Extrusion’da Twist Offset’i başarıyla uyguladınız. Bu güçlü özellik, **create 3d scene** oluştururken karmaşık bükülmeler ve kaydırmalar eklemenize ve ardından **save 3d model**'i sonraki işlem hatları için hazır bir formatta saklamanıza olanak tanır.

## SSS

### Q1: Aspose.3D for Java'yı ticari olmayan projelerde kullanabilir miyim?

A1: Evet, Aspose.3D for Java hem ticari hem de ticari olmayan projelerde kullanılabilir. Daha fazla bilgi için [licensing options](https://purchase.aspose.com/buy) sayfasına bakın.

### Q2: Aspose.3D for Java için destek nereden bulabilirim?

A2: Yardım ve toplulukla iletişim için [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

### Q3: Aspose.3D for Java için ücretsiz deneme mevcut mu?

A3: Evet, [releases page](https://releases.aspose.com/) üzerinden ücretsiz deneme sürümünü keşfedebilirsiniz.

### Q4: Aspose.3D for Java için geçici bir lisans nasıl alınır?

A4: Projeniz için geçici lisansı [this link](https://purchase.aspose.com/temporary-license/) üzerinden alabilirsiniz.

### Q5: Ek örnekler ve öğreticiler mevcut mu?

A5: Daha fazla örnek ve derinlemesine öğreticiler için [documentation](https://reference.aspose.com/3d/java/) sayfasına bakın.

## Sık Sorulan Sorular

**S: Bu öğretici bir Aspose 3d öğretici serisinin parçası mı?**  
C: Evet – bu, kütüphanenin belirli bir özelliğini gösteren resmi bir **aspose 3d tutorial**dır.

**S: Dikdörtgen yerine farklı bir şekil kullanabilir miyim?**  
C: Kesinlikle. Herhangi bir `IProfile` uygulaması (ör. `CircleShape`, özel `PolygonShape`) ekstrüde edilebilir.

**S: `setTwistOffset`'i atlamam durumunda ne olur?**  
C: Ekstrüzyon, profilin orijinden twist yapmaya başlayacak ve simetrik bir bükülme oluşacaktır.

**S: Twist'in pürüzsüzlüğünü nasıl artırabilirim?**  
C: `setSlices`'a verilen değeri artırın; daha yüksek dilim sayısı daha pürüzsüz bir geometri üretir.

**S: OBJ dışındaki hangi dosya formatlarını dışa aktarabilirim?**  
C: Aspose.3D, `FileFormat` enum'ı aracılığıyla STL, FBX, GLTF, 3MF ve birkaç başka formatı destekler.

---

**Son Güncelleme:** 2025-12-19  
**Test Edilen Versiyon:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## HEDEF ANAHTAR KELİMELER:

**Birincil Anahtar Kelime (EN YÜKSEK ÖNCELİK):**  
create 3d scene  

**İkincil Anahtar Kelimeler (DESTEKLEYİCİ):**  
save 3d model, export 3d obj, aspose 3d tutorial