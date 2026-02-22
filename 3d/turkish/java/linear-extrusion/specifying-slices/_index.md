---
date: 2026-02-22
description: Aspose.3D for Java kullanarak dilimlerle 3D ekstrüzyon oluşturmayı öğrenin.
  Bu adım adım rehber, lineer ekstrüzyon, yuvarlama yarıçapını ayarlama ve OBJ dışa
  aktarmayı kapsar.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Dilimlerle 3D Ekstrüzyon Oluştur – Aspose.3D for Java
url: /tr/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dilimlerle 3D Ekstrüzyon Oluşturma – Aspose.3D for Java

## Giriş

Daha pürüzsüz ve hassas görünen **3d extrusion** nesneleri oluşturmanız gerekiyorsa, dilim sayısını kontrol etmek anahtar faktördür. Bu öğreticide, Aspose.3D for Java ile lineer ekstrüzyon yaparken dilimleri nasıl belirteceğinizi adım adım göstereceğiz. Dilim sayısının neden önemli olduğunu, yuvarlama yarıçapının nasıl ayarlandığını ve sonucu herhangi bir 3D iş akışında kullanılabilecek bir OBJ dosyası olarak nasıl dışa aktaracağınızı göreceksiniz.

## Hızlı Yanıtlar
- **“dilimler” neyi kontrol eder?** Ekstrüzyon yüzeyini yaklaşık olarak oluşturmak için kullanılan ara kesit sayısı.  
- **Hangi yöntem dilim sayısını ayarlar?** `LinearExtrusion.setSlices(int)`  
- **Profilin yuvarlama yarıçapını değiştirebilir miyim?** Evet, `RectangleShape.setRoundingRadius(double)` ile.  
- **Bu örnekte hangi dosya formatı kullanılıyor?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Değerlendirme için ücretsiz deneme yeterlidir; üretim için ticari lisans gereklidir.

## Dilimlerle lineer ekstrüzyon nedir?

Lineer ekstrüzyon, bir 2‑D profil (örneğin bir dikdörtgen) alır ve onu düz bir hat boyunca uzatarak 3‑D katı oluşturur. **dilimler** belirterek Aspose.3D'e kaç ara adım oluşturulacağını söylersiniz; bu, yuvarlatılmış bir dikdörtgen gibi eğimli kenarların pürüzsüzlüğünü doğrudan etkiler.

## 3d extrusion oluşturmak için neden Aspose.3D for Java kullanılmalı?

* **Tam kontrol** – Dilim sayısını, yuvarlama yarıçapını ve dışa aktarma formatını programatik olarak ayarlayabilirsiniz.  
* **Çapraz platform** – Yerel bağımlılıklar olmadan herhangi bir Java‑destekli ortamda çalışır.  
* **Dışa aktarma esnekliği** – OBJ, FBX, STL ve birçok diğer formata doğrudan kaydedebilirsiniz.

## Önkoşullar

1. **Java Development Kit** – JDK 8 veya üzeri yüklü olmalı.  
2. **Aspose.3D for Java** – Kütüphaneyi resmi siteden [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.  
3. Tercih ettiğiniz bir IDE veya metin düzenleyici.

## Paketleri İçe Aktar

Aspose.3D ad alanını projenize ekleyin, böylece 3‑D modelleme sınıflarına erişebilirsiniz.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Adım‑Adım Kılavuz

### Adım 1: Sahneyi ayarla ve profili tanımla

İlk olarak bir `RectangleShape` oluşturup köşelerin pürüzsüz olması için **yuvarlama yarıçapı** ekliyoruz. Ardından tüm geometriyi tutacak yeni bir `Scene` başlatıyoruz.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Adım 2: Her ekstrüzyon için **Create child node** nesneleri oluştur

Her geometri parçası bir `Node` altında bulunur. Burada iki kardeş düğüm oluşturuyoruz – biri düşük dilimli ekstrüzyon, diğeri yüksek dilimli ekstrüzyon – ve sol düğümü biraz yana kaydırarak sonuçların karşılaştırılmasını kolaylaştırıyoruz.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Adım 3: Lineer ekstrüzyon gerçekleştir ve **set slices**

Şimdi gerçekten **3d extrusion** nesnelerini oluşturuyoruz. `LinearExtrusion` yapıcı fonksiyonu profili ve ekstrüzyon derinliğini alır. Bir **anonim iç sınıf** kullanarak `setSlices` ile pürüzsüzlüğü kontrol ediyoruz. Sol düğüm sadece 2 dilim (kaba) alırken, sağ düğüm 10 dilim (pürüzsüz) alır.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Adım 4: **Export OBJ** – sahneyi kaydet

Son olarak sahneyi, 3‑D editörler ve oyun motorları tarafından yaygın olarak desteklenen Wavefront OBJ dosyasına yazıyoruz. Bu, Aspose.3D'in **export obj java** yeteneğini gösterir.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Ekstrüzyon düz görünüyor** | Dilim sayısı 1 veya 0 olarak ayarlandı | `setSlices` metodunun değeri ≥ 2 olacak şekilde çağrıldığından emin olun. |
| **Yuvarlatılmış köşeler pürüzlü görünüyor** | Dilim sayısına göre yuvarlama yarıçapı çok küçük | Daha pürüzsüz eğriler için ya yarıçapı ya da dilim sayısını artırın. |
| **Kaydetme sırasında dosya bulunamadı** | `MyDir` var olmayan bir klasöre işaret ediyor | Klasörü önceden oluşturun veya mutlak bir yol kullanın. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'ı nasıl indirebilirim?**  
C: Kütüphaneyi [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.

**S: Aspose.3D dokümantasyonunu nereden bulabilirim?**  
C: Dokümantasyona [buradan](https://reference.aspose.com/3d/java/) ulaşabilirsiniz.

**S: Ücretsiz bir deneme mevcut mu?**  
C: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

**S: Aspose.3D için destek nasıl alabilirim?**  
C: Destek forumuna [buradan](https://forum.aspose.com/c/3d/18) ulaşabilirsiniz.

**S: Geçici bir lisans satın alabilir miyim?**  
C: Geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

---

**Son Güncelleme:** 2026-02-22  
**Test Edilen Sürüm:** Aspose.3D for Java 24.11 (yazım sırasında en son sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}