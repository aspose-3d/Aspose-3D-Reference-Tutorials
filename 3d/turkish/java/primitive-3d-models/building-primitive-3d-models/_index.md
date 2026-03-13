---
date: 2026-03-13
description: Aspose.3D for Java kullanarak 3D silindir, kutu ve diğer ilkel modelleri
  nasıl oluşturacağınızı öğrenin ve sahneyi FBX olarak kaydedin.
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java ile 3B silindir ve diğer temel 3B modelleri nasıl oluşturulur
url: /tr/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Primitive 3D Modelleri Oluşturma

## Giriş

Eğer Java kodundan doğrudan **3D silindir** nesneleri (veya başka temel şekiller) oluşturmanız gerektiğinde, Aspose.3D bu görevi zahmetsiz hale getirir. Bu öğreticide, ortamı kurmaktan sahneyi FBX dosyası olarak kaydetmeye kadar tüm iş akışını adım adım göstereceğiz—böylece 3D geometrisini programlı olarak hemen üretmeye başlayabilirsiniz.

## Hızlı Yanıtlar
- **Java'da 3D silindir oluşturmamı sağlayan kütüphane nedir?** Aspose.3D for Java.
- **Sahneyi hangi formata dışa aktarabilirim?** FBX (ASCII 7500) `FileFormat.FBX7500ASCII` kullanarak.
- **Geliştirme için lisansa ihtiyacım var mı?** Test için ücretsiz deneme çalışır; üretim için kalıcı lisans gereklidir.
- **Desteklenen temel primitive'lar nelerdir?** Box, Cylinder, Sphere, Cone ve daha fazlası.
- **Kod Java 8 ve sonrası ile uyumlu mu?** Evet, Aspose.3D JDK 8+ hedefler.

## 3D silindir primitive'ı nedir?

Silindir primitive'ı, yarıçap ve yükseklik ile tanımlanan temel bir geometrik şekildir. Birçok 3D iş akışında, borular, tekerlekler veya mimari sütunlar gibi daha karmaşık modellerin yapı taşı olarak hizmet eder. Aspose.3D, hazır bir `Cylinder` sınıfı sağlar, böylece köşeleri manuel olarak hesaplamanıza gerek kalmaz.

## Neden Aspose.3D for Java kullanmalısınız?

- **Tam özellikli 3D motor** – popüler formatların (FBX, OBJ, STL, vb.) içe/dışa aktarımını destekler.
- **Saf Java API** – yerel bağımlılık yok, çapraz platform projeler için mükemmel.
- **Sağlam sahne grafiği** – nesneleri hiyerarşik olarak düzenlemenizi sağlar.
- **Kolay lisanslama** – ücretsiz deneme ile başlayın, ardından kalıcı lisansa yükseltin.

## Önkoşullar

Koda başlamadan önce şunların olduğundan emin olun:

1. **Java Development Kit (JDK)** – Makinenizde JDK 8 veya daha yeni bir sürüm yüklü.  
2. **Aspose.3D for Java kütüphanesi** – [download page](https://releases.aspose.com/3d/java/) adresinden indirin ve kurun.  

## Paketleri İçe Aktarma

İlk olarak temel Aspose.3D ad alanını içe aktarın. Bu, `Scene`, `Box`, `Cylinder` ve dosya formatı sabitlerine erişmenizi sağlar.

```java
import com.aspose.threed.*;
```

Artık kütüphane referans alındığına göre, bir sahne oluşturalım ve bazı primitive geometriler ekleyelim.

## Bir sahnede 3D silindir ve diğer primitive'ları nasıl oluşturulur

### Adım 1: Bir Scene Nesnesi Başlatma

İlk olarak, tüm 3D düğümlerimizi tutacak bir `Scene` konteynerine ihtiyacımız var.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Adım 2: Bir 3D kutu modeli oluşturma

Kutu primitive'ı koordinat sistemini test etmek için faydalıdır. Burada, sahnenin kök düğümünün çocuğu olarak ekliyoruz.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Adım 3: Bir 3D silindir modeli oluşturma

Şimdi gerçekten **3D silindir** geometrisini oluşturuyoruz. `Cylinder` sınıfı mantıklı varsayılan boyutlarla gelir, ancak gerekirse yarıçap ve yüksekliği yapıcısı (constructor) aracılığıyla özelleştirebilirsiniz.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Adım 4: Çizimi FBX formatında kaydetme

Sahneyi birleştirdikten sonra, diğer araçların (ör. Unity, Blender) okuyabilmesi için dışa aktarın. Yaygın olarak desteklenen `FBX7500ASCII` formatını kullanıyoruz.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Yaygın Sorunlar ve Çözümleri

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Dosya bulunamadı** kaydederken | `myDir` var olmayan bir klasöre işaret ediyor | Dizinin var olduğundan emin olun veya `new File(myDir).mkdirs();` ile oluşturun. |
| **Boş sahne** dışa aktardıktan sonra | `save` çağrılmadan önce düğüm eklenmemiş | `createChildNode` çağrılarının yürütüldüğünü doğrulayın (`scene.getRootNode().getChildCount()` ile hata ayıklayın) |
| **Lisans istisnası** | Üretimde geçerli bir lisans olmadan çalıştırma | `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` kullanarak geçici veya kalıcı lisans uygulayın |

## Sık Sorulan Sorular

**S: Aspose.3D for Java'ı diğer programlama dilleriyle kullanabilir miyim?**  
C: Aspose.3D öncelikle Java'yı destekler, ancak .NET gibi diğer diller için de sürümler mevcuttur.

**S: Aspose.3D karmaşık 3D modelleme görevleri için uygun mu?**  
C: Kesinlikle! Aspose.3D kapsamlı özellik seti sunar ve hem basit hem de karmaşık 3D modelleme görevleri için uygundur.

**S: Ek yardım ve destek nereden bulabilirim?**  
C: Topluluk desteği ve tartışmalar için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**S: Aspose.3D'yi satın almadan önce deneyebilir miyim?**  
C: Evet, satın alma kararını vermeden önce bir [ücretsiz deneme](https://releases.aspose.com/) keşfedebilirsiniz.

**S: Aspose.3D için geçici lisans nasıl alabilirim?**  
C: Web sitesi üzerinden bir [geçici lisans](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

## Sonuç

Artık Aspose.3D for Java kullanarak **3D silindir**, kutu ve diğer primitive modelleri nasıl oluşturacağınızı ve **sahneyi FBX olarak kaydetmeyi** öğrendiniz. Diğer primitive'larla (Sphere, Cone, vb.) denemeler yapmaktan ve modellerinize gerçekçi bir görünüm kazandırmak için malzeme atamalarını keşfetmekten çekinmeyin.

---

**Son Güncelleme:** 2026-03-13  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11 (yazım zamanındaki en son)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}