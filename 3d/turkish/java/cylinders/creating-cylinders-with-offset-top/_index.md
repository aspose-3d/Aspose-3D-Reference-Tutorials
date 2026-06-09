---
date: 2026-04-08
description: Aspose.3D for Java'da üst kısmı kaydırılmış bir silindir nasıl oluşturulur,
  Java çocuğu düğüm eklenir, üst kaydırma ayarlanır, 3D model oluşturulur ve Aspose
  geçici lisansı kullanılarak OBJ dışa aktarılır, öğrenin.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose Geçici Lisansı – Üst Kaydırmalı Silindir Oluştur (Java)
second_title: Aspose.3D Java API
title: Aspose Geçici Lisansı – Üstü Kaydırmalı Silindir Oluştur (Java)
url: /tr/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Geçici Lisansı – Üstü Kaydırmalı Silindir Oluşturma (Java)

## Giriş

Java tabanlı bir 3D sahnede **silindir** nesnelerini özel bir üst kaydırma ile oluşturmak istiyorsanız, Aspose.3D bu süreci basitleştirir. Bu öğreticide sahneyi kurmaktan modeli OBJ dosyası olarak dışa aktarmaya kadar her adımı adım adım göstereceğiz; böylece üstü kaydırmalı silindirleri uygulamalarınıza güvenle entegre edebilirsiniz. Rehberin sonunda **aspose temporary license** ile bu özellikleri tam bir satın alma yapmadan nasıl değerlendirebileceğinizi de öğreneceksiniz.

## Hızlı Yanıtlar
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java  
- **Silindirin üstünü kaydırabilir miyim?** Evet, `setOffsetTop` kullanarak  
- **Java'da bir alt düğüm nasıl eklenir?** Kök düğümde `createChildNode` çağırın  
- **Hangi formata dışa aktarabilirim?** Wavefront OBJ (`java export obj`)  
- **Test için lisansa ihtiyacım var mı?** Değerlendirme için bir **aspose temporary license** mevcuttur  

## Aspose Geçici Lisansı Nedir?

Bir **aspose temporary license**, geliştirme ve test sırasında Aspose.3D for Java’nın tam özellik setini açan kısa vadeli, ücretsiz bir değerlendirme anahtarıdır. Değerlendirme filigranlarını kaldırır ve OBJ, STL veya FBX gibi 3D model dosyalarını, ücretli bir lisans gibi oluşturmanıza izin verir.

## Aspose.3D for Java Neden Kullanılmalı?

- **Yüksek seviyeli API:** Düşük seviyeli mesh verilerini yönetmenize gerek yok.  
- **Çapraz platform:** Herhangi bir JVM uyumlu ortamda çalışır.  
- **Yerleşik dışa aktarıcılar:** Direkt olarak OBJ, STL, FBX ve daha fazlasına kaydedebilir.  
- **Genişletilebilir:** Kolayca alt düğümler ekleyebilir, dönüşümler uygulayabilir ve diğer Java kütüphaneleriyle entegre edebilirsiniz.  

## Önkoşullar

İlerlemeye başlamadan önce şunların yüklü olduğundan emin olun:

- **Java Development Kit (JDK)** – uyumlu bir sürüm yüklü.  
- **Aspose.3D for Java kütüphanesi** – resmi siteden en son JAR'ı indirin [burada](https://releases.aspose.com/3d/java/).  
- Seçtiğiniz bir IDE (Eclipse, IntelliJ IDEA, NetBeans, vb.).  

## Paketleri İçe Aktarma

İhtiyacımız olan sınıfları içe aktaralım. Bu ifadeleri Java dosyanızın en üstüne ekleyin:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Adım Adım Kılavuz

### Adım 1: Java 3D Sahnesi Oluşturma

Bir **java 3d sahnesi**, tüm 3D nesneleri için bir kapsayıcı görevi görür.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Adım 2: Üstü Kaydırmalı Silindiri Başlatma

Burada **silindir nasıl oluşturulur** sorusuna özel bir kaydırma ile yanıt veriyoruz. Yapıcı, yarıçap, yükseklik, dilimler, yığınlar ve silindirin kapalı olup olmadığını tanımlar. Ardından `setOffsetTop` ile üst kısmı kaydırıyoruz.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Adım 3: Java'da Alt Düğüm Ekle – İlk Silindiri Bağla

Sahnenin kök düğümünün altında bir alt düğüm oluşturur ve silindiri istenen konuma taşırız.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Adım 4: İkinci Silindiri Başlat (Kaydırma Yok)

Karşılaştırma amacıyla, kaydırma olmadan normal bir silindir ekliyoruz.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Adım 5: Java'da Alt Düğüm Ekle – İkinci Silindiri Bağla

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Adım 6: Java OBJ Dışa Aktar – Sahneyi OBJ Olarak Kaydet

Son olarak, **java export obj** komutuyla tüm sahneyi (her iki silindiri) Wavefront OBJ dosyası olarak kaydediyoruz; bu format 3D araçları tarafından yaygın olarak desteklenir.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Programı çalıştırdığınızda, belirtilen dizinde `CustomizedOffsetTopCylinder.obj` dosyasını bulacaksınız; bu dosya Blender, Maya veya başka bir OBJ‑uyumlu görüntüleyicide açılmaya hazırdır.

## Java'da 3D Model Nasıl Oluşturulur ve OBJ Olarak Dışa Aktarılır

`Scene.save(..., FileFormat.WAVEFRONTOBJ)` ifadesi ile **aspose temporary license** kombinasyonu, **3d model** dosyalarını harici dönüştürücülere ihtiyaç duymadan hızlıca üretmenizi sağlar. Bu, prototipleme sırasında veya tasarımcılarla varlık paylaşırken özellikle kullanışlıdır.

## Gerçek Dünya Kullanım Senaryoları

- **Mimari görselleştirme:** Üstü kaydırmalı silindirler, tavana doğru incelen sütunları modellemek için kullanılır.  
- **Mekanik parçalar:** Üst yüzeyi kasıtlı olarak kaydırılmış pistonlar veya dişli muhafazaları oluşturur.  
- **Oyun varlıkları:** Çeşitli sütun şekillerini anında üretir, elle hazırlanmış mesh ihtiyacını azaltır.

## Yaygın Sorunlar ve Çözümleri

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| **OBJ dosyası boş** | Sahne doğru kaydedilmedi veya yol hatalı. | Çıktı dizininin var olduğunu ve yazma izinlerinizin olduğunu doğrulayın. |
| **Kaydırma uygulanmadı** | Eski bir Aspose.3D sürümü kullanılıyor. | `setOffsetTop` desteklenen en son kütüphaneye güncelleyin. |
| **Alt düğüm görünmüyor** | Dönüşüm uygulanmadı. | Alt düğüm oluşturduktan sonra `getTransform().setTranslation` çağırdığınızdan emin olun. |

## Sık Sorulan Sorular

**S: Aspose.3D farklı Java IDE'leriyle uyumlu mu?**  
C: Evet, Eclipse, IntelliJ IDEA, NetBeans ve diğer IDE'lerle sorunsuz çalışır.

**S: Oluşturulan 3D nesnelere doku uygulayabilir miyim?**  
C: Kesinlikle! `Material` sınıfını kullanarak dokular ve yüzey özellikleri atayabilirsiniz.

**S: Aspose.3D için lisans seçenekleri var mı?**  
C: Çeşitli lisans modelleri mevcuttur; bunları [burada](https://purchase.aspose.com/buy) keşfedebilirsiniz.

**S: Yardım nasıl alabilirim veya deneyimlerimi paylaşabilirim?**  
C: Destek ve tartışma için Aspose.3D topluluk forumuna [buradan](https://forum.aspose.com/c/3d/18) katılabilirsiniz.

**S: Test için geçici bir lisans mevcut mu?**  
C: Evet, bir **aspose temporary license** değerlendirme için [buradan](https://purchase.aspose.com/temporary-license/) alınabilir.

---

**Son Güncelleme:** 2026-04-08  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12 (en son)  
**Yazar:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}