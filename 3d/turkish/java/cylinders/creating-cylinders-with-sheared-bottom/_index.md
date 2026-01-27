---
date: 2026-01-27
description: Java 3D modellemeyi, Aspose.3D for Java kullanarak altı kaydırılmış silindirler
  oluşturarak öğrenin. Bu başlangıç seviyesindeki 3D öğretici, Aspose 3D'nin nasıl
  kurulacağını, kaydırma dönüşümünün nasıl uygulanacağını ve OBJ dosyasının Java ile
  nasıl dışa aktarılacağını gösterir.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D Modelleme – Aspose.3D ile Kesilmiş Alt Silindirler
url: /tr/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modelleme – Kesilmiş Alt Silindirler ile Aspose.3D

## Giriş

Bu **java 3d modeling** eğitimine hoş geldiniz! Bu adım‑adım rehberde, alt kısmı kesilmiş bir silindir oluşturmayı, Java için Aspose.3D kütüphanesini kullanarak göstereceğiz. **beginner 3d tutorial** izleseniz ya da mevcut bir modele özel bir kesme dönüşümü eklemek isteseniz, sahneyi nasıl kuracağınızı, kesmeyi nasıl uygulayacağınızı ve sonunda diğer araçlarda kullanmak için **export OBJ file java** nasıl dışa aktaracağınızı tam olarak göreceksiniz.

## Hızlı Yanıtlar
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java  
- **Maven üzerinden Aspose 3D kurulabilir mi?** Evet – Aspose.3D bağımlılığını `pom.xml` dosyanıza ekleyin  
- **Geliştirme için lisans gerekli mi?** Test için geçici bir lisans yeterlidir; üretim için tam lisans gerekir  
- **Hangi dosya formatı gösteriliyor?** Wavefront OBJ (`.obj`)  
- **Örnek ne kadar sürede çalışır?** Tipik bir iş istasyonunda bir saniyeden az  

## Önkoşullar

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Sisteminizde Java Development Kit (JDK) kurulu olduğundan emin olun.  
- **Aspose 3D'yi kurun** – kütüphaneyi resmi siteden [buradan](https://releases.aspose.com/3d/java/) indirin.  
- Aspose.3D bağımlılığını yönetmek için bir IDE veya yapı aracı (Maven/Gradle).  

## Paketleri İçe Aktarma

İlk olarak sahne, geometri ve dosya işleme için ihtiyaç duyacağımız sınıfları içe aktaracağız.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Sahne Oluşturma

Bir sahne, tüm 3‑D nesnelerinin konteyneridir. Boş bir sahne oluşturarak başlayacağız.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Adım 2: Silindir 1 Oluşturma – Silindiri Nasıl Kesilir

Şimdi ilk silindiri oluşturacağız ve alt kısmına **kesme dönüşümü** uygulayacağız. Bu, API üzerinden **silindiri nasıl kesilir** geometrisini doğrudan göstermektedir.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Adım 3: Silindir 2 Oluşturma – Standart Silindir (Kesme Yok)

Karşılaştırma amacıyla, alt kısmı **kesilmemiş** ikinci bir silindir ekleyeceğiz.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Adım 4: Sahneyi Kaydet – OBJ Dosyasını Java ile Dışa Aktarma

Son olarak sahneyi bir Wavefront OBJ dosyasına dışa aktaracağız ve **export obj file java** kullanımını göstereceğiz.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Java 3D Modelleme İçin Bunun Önemi

Bir primitive’e kesme eklemek, dış modelleme araçlarına başvurmadan daha organik şekiller oluşturmanızı sağlar. Bu teknik şu durumlar için kullanışlıdır:

- Eğimli temellerin gerektiği mimari görselleştirmeler.  
- Geometriyi hafif tutarken özel ayak izlerine ihtiyaç duyan oyun varlıkları.  
- Boyutları programlı olarak ayarlamak istediğiniz hızlı prototipleme.  

## Yaygın Sorunlar ve Çözümleri

| Issue | Solution |
|-------|----------|
| **Kesme çok aşırı görünüyor** | `Vector2` değerlerini ayarlayın; bu değerler kesme faktörünü (0‑1 aralığı) temsil eder. |
| **OBJ dosyası görüntüleyicide açılmıyor** | Hedef dizinin var olduğunu ve yazma izinlerinizin bulunduğunu doğrulayın. |
| **Çalışma zamanında lisans istisnası** | Sahneyi oluşturmadan önce geçici veya kalıcı bir lisans uygulayın (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'yı diğer Java 3D kütüphaneleriyle birlikte kullanabilir miyim?**  
C: Aspose.3D bağımsız çalışacak şekilde tasarlanmıştır. Diğer kütüphanelerle entegre edebilirsiniz, ancak çoğu 3‑D görev için zaten tam özellikli bir API sunar.

**S: Aspose.3D, 3D modellemeye yeni başlayanlar için uygun mu?**  
C: Kesinlikle. API açıktır ve bu **beginner 3d tutorial** temel kavramları minimum kodla gösterir.

**S: Aspose.3D for Java için ek destek nereden bulunabilir?**  
C: Topluluk yardımı ve resmi yanıtlar için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**S: Aspose.3D için geçici bir lisans nasıl alınır?**  
C: Geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

**S: Tam bir Aspose.3D for Java lisansı nereden satın alınır?**  
C: Satın alma seçenekleri [burada](https://purchase.aspose.com/buy) mevcuttur.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Son Güncelleme:** 2026-01-27  
**Test Edilen Versiyon:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose