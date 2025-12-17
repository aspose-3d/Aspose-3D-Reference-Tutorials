---
date: 2025-12-17
description: Aspose.3D for Java kullanarak lineer ekstrüzyon bükülmesiyle bükülmüş
  3D model oluşturmayı ve OBJ dosyasını Java’da dışa aktarmayı öğrenin. Adım adım
  rehberimizi izleyin.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Bükülmüş 3D Model Oluşturma – Aspose.3D for Java ile Doğrusal Ekstrüzyonda
  Bükülme Uygulama
url: /tr/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Lineer Ekstrüzyonda Twist Uygulama

## Giriş

Bu adım‑adım öğreticide **twistli bir 3D model** oluşturmayı, Aspose.3D for Java kullanarak lineer ekstrüzyon sırasında bir twist uygulamayı öğreneceksiniz. Mimari görselleştirmeler, oyun varlıkları veya mühendislik prototipleri oluşturuyor olun, sadece birkaç satır kodla geometrinize dinamik, spiral bir görünüm kazandırabilirsiniz.

## Hızlı Yanıtlar
- **Ekstrüzyonda “twist” ne anlama gelir?** Şekil uzatılırken profil ekstrüzyon ekseni etrafında döner.  
- **Hangi API sınıfı twist'i yönetir?** `LinearExtrusion` sınıfı `setTwist` metodunu sağlar.  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Değerlendirme için ücretsiz deneme çalışır; üretim için ticari lisans gereklidir.  
- **Sonucu OBJ olarak dışa aktarabilir miyim?** Evet, `scene.save(..., FileFormat.WAVEFRONTOBJ)` kullanın.  
- **Hangi Java sürümü gerekiyor?** Java 8 veya üzeri tam olarak desteklenir.

## Ön Koşullar

Öğreticiye başlamadan önce aşağıdaki ön koşulların karşılandığından emin olun:

- Java Geliştirme Ortamı: Sisteminizde Java yüklü olduğundan emin olun.  
- Aspose.3D Kütüphanesi: Aspose.3D Java kütüphanesini [indirme bağlantısından](https://releases.aspose.com/3d/java/) indirin ve kurun.  
- Dokümantasyon: Kapsamlı rehberlik için [Aspose.3D dokümantasyonuna](https://reference.aspose.com/3d/java/) bakın.

## Paketleri İçe Aktarma

Kodlama sürecine başlamadan önce gerekli paketleri Java projenize içe aktarın. İşte bunun bir örneği:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Belge Dizini Ayarla

İlk olarak, oluşturulan 3D dosyasının nereye kaydedileceğini tanımlayın.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Temel Profili Başlat

Sonra, ekstrüde edilecek şekli oluşturun. Bu örnekte küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Bir Sahne Oluştur

`Scene` nesnesi tüm 3D düğümler için bir kapsayıcı görevi görür.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Düğümler Oluştur

Sahneye iki alt düğüm ekleyin – biri düz kalacak, diğeri twist alacak.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Lineer Ekstrüzyon Twist'i

Şimdi her iki düğümde **lineer ekstrüzyon twist'i** gerçekleştiriyoruz. Sol düğüm 0° twist alır (düz), sağ düğüm ise 90° twist alarak spiral bir şekil oluşturur. Ayrıca pürüzsüz geometri sağlamak için dilim sayısını ayarlıyoruz.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## OBJ Dosyasını Java ile Dışa Aktar

Son olarak, sahneyi yaygın olarak desteklenen OBJ formatında kaydedin. Bu, Aspose.3D'nin **OBJ dosyasını Java ile dışa aktarma** yeteneğini gösterir.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Neden Önemli

Twistli bir 3D model oluşturmak, harici modelleme araçlarına ihtiyaç duymadan güçlü bir görsel etki sağlar. Özellikle şunlar için faydalıdır:

- **Mekanik parçalar** helisel özellikler gerektiren (ör. yaylar, vidalar).  
- **Sanatsal tasarımlar** ince bir spiralin görsel ilgi kattığı durumlar.  
- **Oyun varlıkları** düşük poligonlu, prosedürel olarak oluşturulmuş geometriye fayda sağlayan.

## Yaygın Sorunlar ve İpuçları

| Sorun | Çözüm |
|-------|----------|
| Twist düz veya eksik görünüyor | Pürüzsüz dönüş için `setSlices` değerinin yeterince yüksek (ör. 100) olduğundan emin olun. |
| OBJ dosyası görüntüleyicide açılmıyor | Çıktı yolunun (`MyDir`) doğru olduğundan ve dosyanın yazma izinlerine sahip olduğundan emin olun. |
| Beklenmeyen ölçekleme | Kaynak profilinizin birim sistemini kontrol edin; Aspose.3D varsayılan olarak metre biriminde çalışır. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'ı diğer 3D dosya formatlarıyla çalışmak için kullanabilir miyim?**  
C: Evet, Aspose.3D FBX, STL, 3MF gibi geniş bir format yelpazesini destekler.

**S: Aspose.3D for Java için desteği nereden bulabilirim?**  
C: Topluluk yardımı ve resmi destek için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Ücretsiz deneme sürümü mevcut mu?**  
C: Evet, [buradan](https://releases.aspose.com/) bir deneme sürümü indirebilirsiniz.

**S: Test için geçici bir lisans nasıl alabilirim?**  
C: [Geçici lisans sayfasından](https://purchase.aspose.com/temporary-license/) geçici bir lisans edinin.

**S: Tam lisansı nereden satın alabilirim?**  
C: Aspose.3D for Java'ı [satın alma sayfasından](https://purchase.aspose.com/buy) satın alın.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---