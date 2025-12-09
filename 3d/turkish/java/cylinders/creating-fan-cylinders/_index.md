---
date: 2025-12-09
description: Aspose.3D for Java kullanarak özel fan silindirleri oluştururken, alt
  düğüm eklemeyi, 3D nesneleri konumlandırmayı ve sahneyi OBJ olarak kaydetmeyi öğrenin.
language: tr
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java ile Fan Silindirleri Oluşturmak için Çocuk Düğüm Ekle
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Çocuk Düğüm Ekleyerek Aspose.3D for Java ile Fan Silindirleri Oluşturma

## Giriş

3‑D sahneye **çocuk düğüm eklemeye** ve göz alıcı fan silindirleri oluşturmaya hazır mısınız? Bu öğreticide, sahneyi kurmaktan, 3D nesneleri konumlandırmaya, son olarak **sahneyi OBJ olarak kaydetmeye** kadar her adımı Aspose.3D for Java kullanarak adım adım göstereceğiz. İster bir oyun varlığını iyileştiriyor olun, ister hızlı bir prototip oluşturuyor olun, burada yer alan kavramlar 3‑D modelleriniz üzerinde sağlam bir kontrol sağlayacak.

## Hızlı Yanıtlar
- **“add child node” ne yapar?** Yeni bir nesneyi sahne grafiğine ekler ve dönüşümleri ebeveyninden devralır.  
- **Bir 3D nesneyi nasıl konumlandırabilirim?** Düğümün dönüşümüne bir çeviri (veya dönüş/ölçekleme) uygulayarak.  
- **Dışa aktarma için hangi dosya formatı kullanılır?** Örnek modeli Wavefront OBJ dosyası olarak kaydeder.  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Değerlendirme için ücretsiz deneme çalışır; üretim için lisans gereklidir.  
- **Hangi IDE en iyisidir?** JDK 8+ destekleyen herhangi bir Java IDE (IntelliJ IDEA, Eclipse, VS Code) uygundur.

## Aspose.3D'de “add child node” nedir?
Çocuk düğüm eklemek, sahne hiyerarşisinde mevcut bir ebeveynin altına yeni bir düğüm oluşturmaktır. Çocuk, ebeveynin koordinat sistemini devralır, bu da **3d nesne** örneklerini birbirine göre konumlandırmayı kolaylaştırır.

## Fan silindirleri oluştururken neden çocuk düğüm eklenir?
- **Modüler tasarım:** Her silindir (fan veya fan olmayan) kendi düğümünde bulunur, sonraki düzenlemeleri basitleştirir.  
- **Dönüşüm mirası:** Ebeveyni taşıdığınızda, döndürdüğünüzde veya ölçeklediğinizde tüm çocuklar otomatik olarak izler.  
- **Daha temiz sahne grafiği:** Karmaşık modellerin okunabilirliğini ve hata ayıklamasını artırır.

## Önkoşullar

- **Java Development Kit (JDK)** – [resmi siteden](https://www.oracle.com/java/technologies/javase-downloads.html) indirin.  
- **Aspose.3D for Java** – En son kütüphaneyi [indirme bağlantısından](https://releases.aspose.com/3d/java/) alın.

## Paketleri İçe Aktarma

Java projenize gerekli paketleri içe aktararak başlayın. Bu adım, Aspose.3D tarafından sağlanan işlevlere erişim için kritik öneme sahiptir.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Bir Sahne Oluşturma

İlk olarak, tüm nesnelerimizi barındıracak boş bir 3‑D sahne oluşturuyoruz.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Adım 2: Bir Fan Silindiri Oluşturma

Sonra, fan (kısmi tarama) olarak render edilecek bir silindir inşa ediyoruz.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Adım 3: Çocuk Düğüm Ekle & 3D Nesneyi Konumlandırma

Şimdi sahneye **çocuk düğüm ekliyoruz** ve çevirisini ayarlayarak **3d nesneyi konumlandırıyoruz**. İşte fan silindirinin sahne grafiğinin bir parçası haline geldiği yer.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Adım 4: Fan Olmayan Bir Silindir Oluşturma

Aspose.3D'nin esnekliğini göstermek için, fan içermeyen normal bir silindir daha oluşturup başka bir çocuk düğüm olarak ekliyoruz.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Adım 5: Sahneyi OBJ Olarak Kaydetme

Son olarak **sahneyi OBJ olarak kaydediyoruz**, böylece sonucu herhangi bir standart 3‑D görüntüleyicide inceleyebilirsiniz.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Tebrikler! **çocuk düğüm eklemeyi** başarıyla tamamladınız, nesnelerinizi konumlandırdınız ve modeli dışa aktardınız.

## Yaygın Sorunlar ve İpuçları

| Sorun | Çözüm |
|-------|----------|
| **Kaydetme sırasında dosya bulunamadı** | Hedef dizinin mevcut olduğundan ve yazma izninizin olduğundan emin olun. |
| **Silindir düz görünüyor** | Yarıçap ve yükseklik değerlerini kontrol edin; Aspose.3D birimlerin aynı ölçekte olmasını bekler. |
| **Fan dilimi eksik görünüyor** | `ThetaLength` değerini (radyan cinsinden) istenen açıyı kapsayacak şekilde ayarlayın. |
| **Sahne görüntüleyicide görünmüyor** | Gerekirse OBJ dosyasının ilgili `.mtl` (malzeme) dosyasıyla kaydedildiğini doğrulayın. |

## Sıkça Sorulan Sorular

**S:** *Aspose.3D diğer Java 3D modelleme kütüphaneleriyle uyumlu mu?*  
**C:** Evet, Aspose.3D diğer Java 3‑D kütüphaneleriyle birlikte çalışır, ihtiyacınıza göre özellikleri birleştirmenize olanak tanır.

**S:** *Oluşturulan fan silindirlerinin görünümünü daha da özelleştirebilir miyim?*  
**C:** Kesinlikle. `Material` ve `Light` sınıflarını kullanarak malzemeler, dokular ve aydınlatma uygulayabilirsiniz.

**S:** *Aspose.3D için ek destek veya yardım nereden bulunur?*  
**C:** Topluluk yardımı ve resmi yanıtlar için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S:** *Aspose.3D için ücretsiz bir deneme mevcut mu?*  
**C:** Evet, satın almadan önce [ücretsiz deneme](https://releases.aspose.com/) ile Aspose.3D'yi keşfedebilirsiniz.

**S:** *Aspose.3D için geçici bir lisans nasıl alınır?*  
**C:** Test ve geliştirme amaçlı geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Sonuç

Bu rehberde **çocuk düğüm eklemeyi**, **3d nesneyi konumlandırmayı** ve **sahneyi OBJ olarak kaydetmeyi** gösterdik; ayrıca Aspose.3D for Java ile özelleştirilmiş fan silindirleri oluşturduk. Bu temel yapı taşları, karmaşık 3‑D hiyerarşileri inşa etmenize ve bunları herhangi bir sonraki iş akışı için dışa aktarmanıza esneklik sağlar.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}