---
date: 2025-12-09
description: Aspose'ı kullanarak Java'da kesik tabanlı özelleştirilmiş silindirler
  oluşturmayı öğrenin; Java 3D modelleme ve sahneleri OBJ olarak kaydetme için mükemmeldir.
language: tr
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Aspose Nasıl Kullanılır: Java''da Kaydırılmış Altlı Silindirler Oluşturma'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Kullanımı: Java’da Altı Kesik Silindir Oluşturma

## Giriş

Bu uygulamalı öğreticide **Aspose** kullanarak altı kesik bir silindir oluşturmayı keşfedeceksiniz—*java 3d modelleme* projelerinde sıkça ihtiyaç duyulan bir teknik. Sahneyi kurmaktan son modeli OBJ dosyası olarak kaydetmeye kadar her adımı adım adım göstereceğiz. Sonunda, herhangi bir Java tabanlı 3D uygulamasına ekleyebileceğiniz yeniden kullanılabilir bir kod parçacığı elde edeceksiniz.

## Hızlı Yanıtlar
- **“Shear bottom” ne demektir?** Silindirin tabanını XY düzleminde belirli bir açıyla eğtirir.  
- **3D matematiğini hangi kütüphane yönetir?** Aspose.3D for Java `Cylinder` ve `Vector2` sınıflarını sağlar.  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Değerlendirme için geçici bir lisans yeterlidir; üretim için tam lisans gerekir.  
- **Modeli başka formatlara dışa aktarabilir miyim?** Evet—`scene.save(..., FileFormat.WAVEFRONTOBJ)` kullanarak OBJ dosyası alabilirsiniz.  
- **Hangi Java sürümü gereklidir?** JDK 8 veya üzeri yeterlidir.

## “how to use aspose” 3D modelleme bağlamında ne anlama geliyor?

Aspose.3D for Java, 3D geometri, dosya formatları ve dönüşümlerinin karmaşıklığını soyutlayan yüksek seviyeli bir API’dir. Düşük seviyeli vertex tamponlarıyla uğraşmak yerine `new Cylinder(...)` gibi sezgisel yöntemleri çağırır ve Aspose ağır işleri halleder.

## Neden Aspose for Java 3D Modelleme Kullanmalı?

- **Hızlı geliştirme:** Birkaç satır kodla karmaşık şekiller oluşturun.  
- **Geniş format desteği:** OBJ, STL, FBX ve daha fazlasına dışa aktarın.  
- **Çapraz platform:** Java’yı destekleyen her işletim sisteminde çalışır.  
- **Tutarlı API:** Aynı kod masaüstü, sunucu veya Android ortamlarında kullanılabilir.

## Ön Koşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- **Java Development Kit (JDK) 8+** IDE’nizde yüklü ve yapılandırılmış.  
- **Aspose.3D for Java** kütüphanesi proje sınıf yolunuza eklenmiş. Resmi siteden [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.  
- **Geçici veya tam lisans** (deneme çalıştırmaları için isteğe bağlı).

## Paketleri İçe Aktarma

Başlamak için gerekli Aspose.3D sınıflarını ve Java yardımcılarını içe aktarın:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Bir Sahne Oluşturma

*Scene*, tüm 3D nesneleri, ışıkları ve kameraları tutan konteynerdir. Silindirlerinizi yerleştireceğiniz sahne olarak düşünebilirsiniz.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Adım 2: Silindir 1’i Oluşturma (Altı Kesik)

Şimdi ilk silindiri oluşturup altına bir kesme dönüşümü uygulayacağız. `setShearBottom` yöntemi, X ekseni boyunca kesme faktörünü X bileşeni, Y ekseni boyunca kesme faktörünü Y bileşeni olarak temsil eden bir `Vector2` alır.

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

> **İpucu:** `0.83` kesme faktörü yaklaşık 47.5°’e karşılık gelir; ihtiyacınız olan tam açıyı elde etmek için bu değeri ayarlayın.

## Adım 3: Silindir 2’yi Oluşturma (Standart)

Karşılaştırma amacıyla, kesme uygulanmamış ikinci bir silindir ekleyeceğiz. Bu, dışa aktarılan OBJ dosyasında görsel farkı doğrudan görmenizi sağlar.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Adım 4: Sahneyi Kaydetme (Sahneyi OBJ Olarak Kaydetme)

Son olarak sahneyi diske kalıcı olarak kaydediyoruz. `FileFormat.WAVEFRONTOBJ` sabiti, Aspose’a OBJ dosyası yazmasını söyler; bu dosya Blender ve Maya gibi 3D editörleri tarafından geniş çapta desteklenir.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Not:** `"Your Document Directory"` ifadesini ortamınıza uygun mutlak ya da göreli bir yol ile değiştirin.

## Yaygın Sorunlar ve Çözümleri

| Sorun | Neden | Çözüm |
|-------|-------|----------|
| **Silindir düz görünüyor** | Kesme faktörünün 0‑1 aralığının dışında olması | 0 ile 1 arasında bir değer kullanın; ön izleme yaparak yavaşça ayarlayın. |
| **OBJ dosyası görüntüleyicide açılmıyor** | Malzeme tanımları eksik | Her node’a basit bir malzeme ekleyin veya sadece geometriyi test etmek için STL olarak dışa aktarın. |
| **LicenseException oluşuyor** | Geçerli lisans dosyası yok | `Aspose.3D.lic` dosyasını proje köküne koyun veya `License` sınıfını kullanarak programatik olarak yükleyin. |

## Sık Sorulan Sorular

### S1: Aspose.3D for Java’yı diğer Java 3D kütüphaneleriyle birlikte kullanabilir miyim?
**C:** Aspose.3D for Java bağımsız çalışacak şekilde tasarlanmıştır. Diğer kütüphanelerle entegre edebilirsiniz, ancak çoğu 3D modelleme görevini tek başına tamamlayabilir.

### S2: Aspose.3D yeni başlayanlar için uygun mu?
**C:** Evet, Aspose.3D düşük seviyeli detayları soyutlayan kullanıcı dostu bir API sunar; hem yeni başlayanlar hem de deneyimli geliştiriciler için uygundur.

### S3: Aspose.3D for Java için ek destek nereden bulabilirim?
**C:** Topluluk desteği, öğreticiler ve tartışmalar için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S4: Aspose.3D için geçici bir lisans nasıl alabilirim?
**C:** Geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

### S5: Aspose.3D for Java’yı satın alabilir miyim?
**C:** Evet, Aspose.3D for Java’yı [buradan](https://purchase.aspose.com/buy) satın alabilirsiniz.

## Sonuç

**Aspose** kullanarak bir kesik alt ve bir standart silindir oluşturup sonucu OBJ dosyası olarak kaydetmeyi adım adım gösterdik. Bu teknik, özel parçalar, mimari öğeler veya oyun varlıkları gibi daha karmaşık 3D modeller için bir yapı taşıdır. Projenizin ihtiyaçlarına göre farklı kesme değerleri, yarıçaplar ve yükseklikler deneyerek özelleştirebilirsiniz.

---

**Son Güncelleme:** 2025-12-09  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11 (yazım anındaki en yeni)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}