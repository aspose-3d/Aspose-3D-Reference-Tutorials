---
date: 2025-11-30
description: Java'da Aspose kullanarak bir 3D küre yarıçapını nasıl değiştireceğinizi
  öğrenin. Bu adım‑adım rehber, Aspose.3D Java kütüphanesini, yarıçapı nasıl ayarlayacağınızı,
  küreyi sahneye eklemeyi ve OBJ dosyasını Java ile yazmayı kapsar.
language: tr
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Aspose Nasıl Kullanılır: Aspose.3D ile Java''da 3D Küre Yarıçapını Değiştirme'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Kullanımı: Java’da Aspose.3D ile 3D Küre Yarıçapını Değiştirme

## Giriş

Java’da 3D modellerle çalışmak için **Aspose’un nasıl kullanılacağını** arıyorsanız doğru yerdesiniz. Bu öğreticide bir kürenin boyutunu değiştirme, sahneye ekleme ve sonunda **Aspose.3D Java kütüphanesi** bir OBJ dosyası yazma adımlarını adım adım göstereceğiz. Sonunda, herhangi bir Java tabanlı 3D uygulamasına ekleyebileceğiniz yeniden kullanılabilir bir kod parçacığına sahip olacaksınız.

## Hızlı Yanıtlar
- **Bu kılavuzun temel amacı nedir?** Aspose.3D ile Java’da bir kürenin yarıçapını nasıl değiştireceğinizi göstermek.  
- **Hangi kütüphaneyi kullanıyoruz?** Aspose.3D Java kütüphanesi (tam özellikli bir **java 3d library**).  
- **Yarıçapı nasıl ayarlarım?** `Sphere` nesnesi üzerinde `sphere.setRadius(double)` metodunu çağırın.  
- **OBJ’ye dışa aktarabilir miyim?** Evet – `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)` kullanın.  
- **Lisans gerekiyor mu?** Geliştirme için ücretsiz deneme sürümü yeterlidir; üretim için lisans gereklidir.

## Aspose.3D for Java Nedir?

Aspose.3D, geliştiricilerin dış bağımlılık olmadan 3D dosyaları oluşturmasını, düzenlemesini ve dönüştürmesini sağlayan bir **java 3d library**’dir. OBJ, FBX, STL gibi popüler formatları destekler ve oyunlar, CAD araçları ve bilimsel görselleştirmeler için idealdir.

## Neden Aspose.3D ile Küre Boyutunu Değiştirmelisiniz?

- **Yerel 3D motoru gerekmez** – tüm işlemler nesne modeli üzerinde gerçekleşir.  
- **Çapraz platform** – Java çalıştırabilen herhangi bir işletim sisteminde çalışır.  
- **Yüksek hassasiyetli geometri** – sadece yaklaşık ölçekleme değil, tam yarıçap değerleri ayarlayabilirsiniz.  

## Ön Koşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- Java programlamaya temel bir anlayış.  
- Aspose.3D kütüphanesi yüklü – [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresinden indirebilirsiniz.  
- Makinenizde Java Development Kit (JDK) kurulu.

## Paketleri İçe Aktarma

Projeye gerekli sınıfları eklemek için:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Adım 1: Bir Sahne Başlatma

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Burada tüm geometrimizi tutacak yeni bir **3D sahne** oluşturuyoruz.

## Adım 2: Bir Küre Başlatma

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

`Sphere` nesnesi mükemmel bir küre primitive’ini temsil eder. Şu anda varsayılan yarıçapı 1.0’dir.

## Adım 3: Kürenin Yarıçapını Nasıl Ayarlarsınız

```java
// set radius
sphere.setRadius(10);
```

Bu satır **yarıçapı nasıl ayarlayacağınızı** gösterir. İstediğiniz boyutu elde etmek için `10` yerine herhangi bir `double` değer koyabilirsiniz.

## Adım 4: Küreyi Sahneye Ekleme

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Bu çağrı **küreyi sahneye ekler** (veya “add sphere to scene”) kök düğümün altında bir çocuk düğüm oluşturarak.

## Adım 5: OBJ Dosyası Yazma (Java)

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Son olarak, `scene.save` kullanarak **OBJ dosyasını Java tarzında** yazıyoruz. Çıktı dosyası `sphere.obj` herhangi bir Wavefront OBJ formatını destekleyen 3D görüntüleyicide açılabilir.

## Yaygın Sorunlar ve Çözümler

| Sorun | Çözüm |
|-------|----------|
| **Küre görüntüleyicide çok küçük görünüyor** | Yarıçap değerinin doğru ayarlandığını doğrulayın; bir ölçekleme dönüşümü uygulamadığınız sürece birimler keyfidir. |
| **Dışa aktarılan OBJ’de materyal yok** | Aspose.3D yalnızca geometriyi yazar; doku gerekiyorsa küreye bir materyal ekleyin (`sphere.setMaterial(...)`). |
| **Çalışma zamanında lisans istisnası** | `Scene` oluşturulmadan önce geçici ya da kalıcı bir lisans dosyasının yüklendiğinden emin olun. |

## Sık Sorulan Sorular

### S: Aspose.3D for Java dokümantasyonunu nereden bulabilirim?

C: Kapsamlı bilgi ve kullanım kılavuzları için [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresine bakabilirsiniz.

### S: Aspose.3D for Java’yı nasıl indirebilirim?

C: Kütüphaneyi sürüm sayfasından indirebilirsiniz: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### S: Aspose.3D for Java için ücretsiz deneme sürümü var mı?

C: Evet, ücretsiz deneme sürümüyle özellikleri keşfetmek için [Aspose.3D Free Trial](https://releases.aspose.com/) adresini ziyaret edin.

### S: Aspose.3D for Java için destek nereden alınır?

C: Yardım ve tartışmalar için Aspose topluluğuna katılın: [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18).

### S: Aspose.3D için geçici bir lisans nasıl alınır?

C: [Temporary License](https://purchase.aspose.com/temporary-license/) sayfasını ziyaret ederek geçici lisans edinebilirsiniz.

### S: Bu kodu STL gibi diğer 3D formatlarıyla kullanabilir miyim?

C: Kesinlikle – `scene.save` çağrısında `FileFormat` enum’unu değiştirin, örneğin `FileFormat.STL`.

## Sonuç

Artık **Aspose’u nasıl kullanacağınızı** öğrenerek bir kürenin yarıçapını değiştirdiniz, sahneye eklediniz ve sonucu Java’da bir OBJ dosyası olarak dışa aktardınız. Diğer primitive’lerle deneler yapabilir, materyaller ekleyebilir veya daha zengin 3D modeller oluşturmak için birden fazla dönüşüm zinciri oluşturabilirsiniz.

---

**Son Güncelleme:** 2025-11-30  
**Test Edilen Sürüm:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}