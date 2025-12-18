---
date: 2025-12-18
description: Aspose.3D for Java kullanarak lineer ekstrüzyonda zemin düzlemi eklemeyi
  ve merkez özelliğini ayarlamayı, adım adım kod örnekleriyle öğrenin.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Zemin Düzlemi ve Kontrol Merkezi
  Nasıl Eklenir
url: /tr/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Linear Extrusion'da Merkez Kontrolü

## Giriş

## Hızlı Yanıtlar
- **“add ground plane” ne yapar?** İncel bir referans geometrisi oluşturur ve ekstrüzyonun dünya eksenlerine göre konumunu görmenize yardımcı olur.  
- **Linear extrusion'ın merkezini nasıl ayarlarım?** `LinearExtrusion` nesnesindeki `setCenter(boolean)` metodunu kullanın.  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Test için geçici bir lisans yeterlidir; üretim için tam lisans gereklidir.  
- **Kaydetmek için hangi dosya formatı kullanılıyor?** Örnek Wavefront OBJ (`.obj`) formatına kaydeder.  
- **Hangi Java sürümü gerekiyor?** Java 8 veya üzeri yeterlidir.

## 3D sahnede “add ground plane” nedir?

Bir ground plane eklemek, X‑Z düzleminde yer alan ince dikdörtgen bir geometri (genellikle minimum kalınlığa sahip bir kutu) eklemek anlamına gelir. Görsel bir zemin görevi görür ve özellikle ekstrüzyon merkezleriyle çalışırken diğer nesnelerin yüksekliğini ve hizalamasını değerlendirmeyi kolaylaştırır.

## Linear extrusion'da merkez özelliği neden ayarlanmalı?

Varsayılan olarak, bir linear extrusion profilin orijinsinden başlar. Merkez özelliğini (`setCenter(true)`) ayarlamak, profili orijine göre ortalar; bu, simetrik tasarımlar için veya birden fazla nesne arasında tutarlı hizalama gerektiğinde faydalıdır.

## Önkoşullar

Bu öğreticiye başlamadan önce, aşağıdaki önkoşulların karşılandığından emin olun:

1. **Java Geliştirme Ortamı** – Makinenizde bir Java geliştirme ortamının kurulu olduğundan emin olun.  
2. **Aspose.3D for Java** – Aspose.3D kütüphanesini indirin ve kurun. Kütüphaneyi ve dokümantasyonunu [burada](https://reference.aspose.com/3d/java/) bulabilirsiniz.  
3. **Document Directory** – Java belgelerinizi saklamak için bir dizin oluşturun. Buna “Your Document Directory” adını verelim.

## Paketleri İçe Aktarma

Java geliştirme ortamınızda, Aspose.3D için gerekli paketleri içe aktarın. Bu, kodunuzun kütüphane tarafından sağlanan işlevlere erişmesini sağlar.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Temel Profili Oluşturma

Ekstrüde edilecek temel profili başlatın. Bu örnekte, 0.3 yuvarlama yarıçapına sahip bir dikdörtgen şekli kullanacağız.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Adım 2: 3D Sahne Oluşturma

Bir sahne oluşturarak 3D dünyanızın temelini inşa edin.

```java
Scene scene = new Scene();
```

## Adım 3: Sol ve Sağ Düğümleri Oluşturma

Sahnenizde sol ve sağ düğümler oluşturun. Bu düğümler 3D nesneleriniz için bir tuval görevi görür.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 4: Merkez Özelliği ile Linear Extrusion (Sol Düğüm)

Sol düğümde **ortalamadan** linear extrusion yapın ve dilim sayısını 3 olarak ayarlayın. `setCenter(false)` çağrısına dikkat edin – burada **merkez özelliği** *false* olarak ayarlanıyor.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Adım 5: Referans İçin Ground Plane Ekleme (Sol Düğüm)

Sol düğüme **ground plane ekleyerek** görsel temsili geliştirin. İnce kutu bir zemin görevi görür ve ekstrüzyonun yüksekliğini net bir şekilde görmenizi sağlar.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Adım 6: Merkez Özelliği ile Linear Extrusion (Sağ Düğüm)

Şimdi sağ düğümde linear extrusion yapın, bu sefer **ekstrüzyonu ortalayarak**. `setCenter(true)` çağrısı, **merkez özelliğini** *true* olarak nasıl ayarlayacağınızı gösterir.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Adım 7: Referans İçin Ground Plane Ekleme (Sağ Düğüm)

Sol taraf gibi, sağ düğüme de tutarlı bir görsel temel sağlamak için bir ground plane ekleyin.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Adım 8: 3D Sahneyi Kaydetme

3D sahnenizi Wavefront OBJ formatında kaydedin, böylece herhangi bir standart 3D görüntüleyicide açabilirsiniz.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümleri

| Sorun | Neden | Çözüm |
|-------|-------|------|
| Ground plane görünmüyor | Kutunun kalınlığı görüntüleyicinin ölçeği için çok küçük. | `Box`'ın ilk parametresini artırın veya görüntüleyicide uzaklaşın. |
| Extrusion kaymış görünüyor | `setCenter` değeri istenildiği gibi ayarlanmamış. | `setCenter`'a geçirilen boolean'ı tekrar kontrol edin. |
| Dosya kaydedilmiyor | Yanlış dizin yolu veya yazma izni eksik. | `MyDir`'in mevcut ve yazma izni olan bir klasöre işaret ettiğini doğrulayın. |

## Sıkça Sorulan Sorular

**S1: Aspose.3D for Java'ı ticari projelerde kullanabilir miyim?**  
C1: Evet, Aspose.3D for Java ticari kullanım için mevcuttur. Lisans detayları için [burayı](https://purchase.aspose.com/buy) ziyaret edin.

**S2: Ücretsiz deneme mevcut mu?**  
C2: Evet, Aspose.3D for Java ücretsiz denemesini [buradan](https://releases.aspose.com/) inceleyebilirsiniz.

**S3: Aspose.3D for Java için desteği nereden bulabilirim?**  
C3: Aspose.3D topluluk forumu destek almak ve deneyimlerinizi paylaşmak için harika bir yerdir. Forum'u [buradan](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S4: Test için geçici bir lisansa ihtiyacım var mı?**  
C4: Evet, test amaçlı geçici bir lisansa ihtiyacınız varsa, birini [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

**S5: Dokümantasyonu nereden bulabilirim?**  
C5: Aspose.3D for Java dokümantasyonu [burada](https://reference.aspose.com/3d/java/) mevcuttur.

## Sonuç

Linear extrusion'da merkezi kontrol etmek **ve** Aspose.3D for Java ile **ground plane eklemeyi** öğrenmek, 3D grafik geliştirmede heyecan verici olanaklar sunar. Yukarıdaki adımları izleyerek artık merkezlenmiş ekstrüzyonlar, görsel referans düzlemak ve sonucu OBJ olarak dışa aktarmak için yeniden kullanılabilir bir deseniniz var. Kendi proje ihtiyaçlarınıza göre farklı profiller, dilim sayıları ve dönüşümlerle denemeler yapmaktan çekinmeyin.

---

**Son Güncelleme:** 2025-12-18  
**Test Edilen Versiyon:** Aspose.3D 24.11 for Java (yazım zamanındaki en son sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}