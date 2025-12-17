---
date: 2025-12-17
description: Aspose.3D for Java'da lisansı nasıl ayarlayacağınızı ve ölçümlü lisanslama
  için genel ve özel anahtarların nasıl kullanılacağını öğrenin.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java'da Lisansı Nasıl Ayarlarsınız – Tam Rehber
url: /tr/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java'da Lisans Nasıl Ayarlanır

## Giriş

Hoş geldiniz! Bu adım‑adım öğreticide, bir Java uygulamasında Aspose.3D için **lisansın nasıl ayarlanacağını** ve ölçülen lisanslama için **public private anahtarların nasıl kullanılacağını** keşfedeceksiniz. Aspose.3D, 3D dosya formatlarıyla çalışmayı basitleştiren güçlü bir Java kütüphanesidir ve geçerli bir lisans, tam özellik setinin kilidini açar. Bu kılavzun sonunda, lisanslamayı herhangi bir Java projesine sorunsuz bir şekilde entegre edebileceksiniz.

## Hızlı Yanıtlar
- **Lisansı ayarlamanın temel yolu nedir?** `License` sınıfını kullanın ve `setLicense` metodunu dosya yolu veya akış ile çağırın.  
- **Lisansı bir akıştan yükleyebilir miyim?** Evet – bir `FileInputStream` mükemmel çalışır.  
- **Public/private anahtarlar ne işe yarar?** `Metered` sınıfı aracılığıyla ölçülen (metered) lisanslamayı etkinleştirir.  
- **Geliştirme için lisansa ihtiyacım var mı?** Test için geçici veya deneme lisansı yeterlidir; üretim için tam lisans gereklidir.  
- **Hangi Java sürümleri destekleniyor?** Aspose.3D Java 6 ve üzeri sürümlerle çalışır.

## Ön Koşullar

Başlamadan önce şunların olduğundan emin olun:

- Java programlamaya temel bir anlayış.  
- Projeye eklenmiş Aspose.3D kütüphanesi. Bunu [release page](https://releases.aspose.com/3d/java/) adresinden indirin.  
- Geçerli bir `.lic` dosyası veya public ve private ölçülen anahtarlarınız.

## Paketleri İçe Aktarma

Java kaynak dosyanıza gerekli importları ekleyin. Aspose.3D JAR dosyasının sınıf yolunda (classpath) olduğundan emin olun.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Dosya Kullanarak Lisans Nasıl Ayarlanır

### Adım 1: License Nesnesi Oluşturun

`License` sınıfını örnekleyin – bu nesne lisans bilgilerini tutacaktır.

```java
License license = new License();
```

### Adım 2: Dosyadan Lisans Ayarla

`.lic` dosyanızın göreli ya da mutlak yolunu sağlayın ve uygulayın.

```java
license.setLicense("Aspose._3D.lic");
```

> **İpucu:** Lisans dosyasını kaynak kontrol dizininizin dışına koyun, böylece yanlışlıkla ifşa edilmesini önlersiniz.

## Akış Kullanarak Lisans Nasıl Ayarlanır

### Adım 1: License Nesnesi Oluşturun

Yukarıdaki gibi, yeni bir `License` örneğiyle başlayın.

```java
License license = new License();
```

### Adım 2: Akıştan Lisans Ayarla

Lisans dosyasını bir `FileInputStream` içine okuyun ve akışı `setLicense` metoduna geçirin. `try‑with‑resources` bloğu, akışın otomatik olarak kapanmasını garanti eder.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Ölçülen Lisanslama için Public Private Anahtarlar Nasıl Kullanılır

### Adım 1: Metered Lisans Nesnesi Başlatın

Ölçülen (pay‑as‑you‑go) lisanslamayı yöneten `Metered` sınıfının bir örneğini oluşturun.

```java
Metered metered = new Metered();
```

### Adım 2: Public ve Private Anahtarları Ayarlayın

Aspose'tan aldığınız anahtarları sağlayın. Bu anahtarlar, kütüphanenin kullanımını lisans sunucusuna raporlamasını sağlar.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Uyarı:** Private anahtarınızı herkese açık dağıtılan bir JAR içinde asla sabit kodlamayın. Güvenli bir konumdan ya da ortam değişkeninden yüklemeyi düşünün.

## Yaygın Kullanım Senaryoları

- **Kurumsal 3D renderleme hatları** – lisans ayarlandıktan sonra yüksek performanslı API'lerin kilidi açılır.  
- **Otomatik test ortamları** – tam lisans satın almadan işlevselliği doğrulamak için geçici lisans kullanın (SSS'ye bakın).  
- **Ölçülen SaaS çözümleri** – müşterileri gerçek kullanımına göre faturalandırmak için public/private anahtarları entegre edin.

## Sonuç

Tebrikler! Artık Java'da bir dosya, bir akış kullanarak Aspose.3D için **lisansın nasıl ayarlanacağını** ve ölçülen lisanslama için **public private anahtarların nasıl kullanılacağını** biliyorsunuz. Bu adımlarla Aspose.3D'yi herhangi bir Java uygulamasına güvenle entegre edebilir ve 3D işleme yeteneklerinden tam olarak yararlanabilirsiniz.

## Sıkça Sorulan Sorular

**S1: Aspose.3D tüm Java sürümleriyle uyumlu mu?**  
C1: Evet, Aspose.3D Java 6 ve üzeri sürümlerle çalışır.

**S2: Ek belgeleri nerede bulabilirim?**  
C2: Belgeleri [buradan](https://reference.aspose.com/3d/java/) inceleyebilirsiniz.

**S3: Aspose.3D'yi satın almadan deneyebilir miyim?**  
C3: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

**S4: Aspose.3D için destek nasıl alınır?**  
C4: Topluluk ve resmi destek için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**S5: Test için geçici bir lisansa ihtiyacım var mı?**  
C5: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Son Güncelleme:** 2025-12-17  
**Test Edilen:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose