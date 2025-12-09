---
date: 2025-12-01
description: Aspose.3D for Java ile 3D sahneleri sıkıştırarak 3D dosya boyutunu nasıl
  azaltacağınızı öğrenin. Optimum depolama ve paylaşım için adım adım rehberimizi
  izleyin.
linktitle: Reduce 3D File Size – Compress Scenes with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D Dosya Boyutunu Azaltın – Aspose.3D for Java ile Sahneleri Sıkıştırın
url: /tr/java/3d-scenes-and-models/compress-3d-scenes/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Dosya Boyutunu Azaltın – Aspose.3D for Java ile Sahneleri Sıkıştırın

## Giriş

Web üzerinden, e‑posta ile ya da bir bulut deposunda 3D varlıkları sunuyorsanız, büyük dosya boyutları hızla bir darboğaz haline gelebilir. Bu öğreticide **3D dosya boyutunu nasıl azaltacağınızı** Aspose.3D for Java kullanarak 3D sahneleri sıkıştırarak öğreneceksiniz. Bir sahne oluşturma, nesneler ekleme, dönüşümleri ayarlama ve sonunda görsel kaliteyi korurken dosyayı büyük ölçüde küçülten sıkıştırma seçenekleriyle sahneyi kaydetme adımlarını birlikte inceleyeceğiz.

## Hızlı Yanıtlar
- **“3d dosya boyutunu azaltmak” ne demektir?** Bir 3‑D dosyasına sıkıştırma teknikleri uygulayarak, geometrik ya da doku doğruluğunu kaybetmeden disk üzerindeki boyutunun küçültülmesi anlamına gelir.  
- **Aspose.3D’de hangi format sıkıştırmayı destekler?** `AmfSaveOptions` ile kullanılan AMF (Additive Manufacturing File) formatı.  
- **Sıkıştırma için lisansa ihtiyacım var mı?** Geliştirme için deneme sürümü çalışır; üretim ortamı için ticari lisans gereklidir.  
- **Sıkıştırma kayıpsız mı?** Evet, Aspose.3D’nin yerleşik sıkıştırması geometri ve dokular için kayıpsızdır.  
- **Ne kadar boyut azaltması bekleyebilirim?** Sahne karmaşıklığı ve doku sayısına bağlı olarak genellikle %30‑%60 arasındadır.

## Aspose.3D’de Sahne Sıkıştırması Nedir?
Sahne sıkıştırması, bir 3‑D sahnesini daha kompakt bir temsile kodlama sürecidir. Aspose.3D, AMF formatının yerleşik gzip‑stil sıkıştırmasını kullanarak büyük modelleri daha verimli bir şekilde gönderilmesini sağlar.

## Neden 3D Dosya Boyutunu Azaltmalısınız?
- **Daha hızlı indirmeler** – Sınırlı bant genişliğine sahip kullanıcılar daha akıcı bir deneyim yaşar.  
- **Düşük depolama maliyetleri** – Bulut depolama ücretleri GB başına hesaplanır.  
- **Gelişmiş performans** – Daha küçük dosyalar tarayıcılarda ve oyun motorlarında daha çabuk yüklenir.  
- **Daha kolay paylaşım** – E‑posta ekleri ve iş birliği platformları genellikle boyut sınırlamalarına sahiptir.

## Önkoşullar
Başlamadan önce aşağıdakilerin kurulu olduğundan emin olun:

- Java Development Kit (JDK) 8 veya daha yeni bir sürüm.  
- Resmi siteden indirilen Aspose.3D for Java kütüphanesi – indirme bağlantısını [burada](https://releases.aspose.com/3d/java/) bulabilirsiniz.  
- Örnek projeyi oluşturup çalıştırmak için bir Java IDE’si (IntelliJ IDEA, Eclipse veya VS Code).

## Paketleri İçe Aktarma
Gerekli Aspose.3D sınıflarını Java kaynak dosyanıza ekleyin:

```java
import com.aspose.threed.AmfSaveOptions;
import com.aspose.threed.Box;
import com.aspose.threed.Scene;
import com.aspose.threed.Transform;
import com.aspose.threed.Vector3;
```

## Adım‑Adım Kılavuz

### Adım 1: Java Projenizi Kurun
Tercih ettiğiniz IDE’de yeni bir Java projesi oluşturun ve Aspose.3D JAR dosyalarını projenizin sınıf yoluna ekleyin. Böylece derleyici içe aktarılan sınıfları bulabilir.

### Adım 2: Yeni Bir 3D Sahne Başlatın
Boş bir sahne nesnesi oluşturun. `Scene` sınıfı, tüm geometri, ışık, kamera ve hiyerarşi için konteyner görevi görür.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";

Scene scene = new Scene();
```

### Adım 3: Basit Bir Kutu Geometrisi Ekleyin
Gösterim amacıyla sahneye bir kutu primitive’i ekleyeceğiz. `Box` sınıfı, dönüştürebileceğimiz bir küp oluşturur.

```java
Box box = new Box();
Transform tr = scene.getRootNode().createChildNode(box).getTransform();
tr.setScale(new Vector3(12, 12, 12));
tr.setTranslation(new Vector3(10, 0, 0));
```

### Adım 4: Kutuyu Özelleştirin (Ölçek, Dönme, Konum)
Aynı kutuyu değiştirebilir ya da ek örnekler ekleyebilirsiniz. Aşağıda ölçeği değiştirip Euler açılarıyla nesneyi döndürüyoruz.

```java
tr = scene.getRootNode().createChildNode(box).getTransform();
tr.setScale(new Vector3(5, 5, 5));
tr.setEulerAngles(new Vector3(50, 10, 0));
```

### Adım 5: Sıkıştırma Etkinleştirilmiş Şekilde Sahneyi Kaydedin
**3d dosya boyutunu azaltmanın** anahtarı `AmfSaveOptions`’tadır. `setEnableCompression(true)` çağrısıyla AMF dosyası içinde gzip sıkıştırmasını etkinleştirin.

```java
AmfSaveOptions opt = new AmfSaveOptions();
opt.setEnableCompression(true);   // Turn on compression to shrink file size
scene.save(MyDir + "compressed_scene.amf", opt);
```

> **İpucu:** Hata ayıklama için orijinal sıkıştırılmamış sürümü tutmanız gerekiyorsa, `setEnableCompression(false)` ile ikinci bir kopya kaydedin.

Sahneye eklemek istediğiniz diğer nesneler için yukarıdaki adımları tekrarlayın. Her nesne aynı sıkıştırılmış konteyner içinde saklanır ve toplam dosya boyutu düşük kalır.

## Yaygın Sorunlar ve Çözümler
| Sorun | Neden | Çözüm |
|-------|-------|-----|
| **Kaydedilen dosya hâlâ büyük** | Sıkıştırma kapalı ya da desteklenmeyen bir format (ör. OBJ) kullanılıyor. | `opt.setEnableCompression(true)` ayarlandığından ve **AMF** olarak kaydedildiğinden emin olun. |
| **Yükleme sonrası dokular görünmüyor** | Dokular gömülmemiş; yol dışarıda. | `scene.getRootNode().getMaterial().setTexture(...).setEmbed(true)` kullanın. |
| **Büyük sahnelerde OutOfMemoryError** | Sahne tamamen belleğe yüklenip kaydediliyor. | `AmfSaveOptions.setEnableStreaming(true)` ile akış modunu etkinleştirin. |

## Sık Sorulan Sorular

**S: Aspose.3D for Java hem yeni başlayanlar hem de deneyimli geliştiriciler için uygun mu?**  
C: Evet, API net bir nesne‑yönelimli modelle tasarlanmıştır ve tüm beceri seviyeleri için çalışır.

**S: Aspose.3D for Java’yı ticari projelerde kullanabilir miyim?**  
C: Kesinlikle. [Aspose satın alma sayfası](https://purchase.aspose.com/buy) üzerinden ticari lisans satın alın.

**S: Ücretsiz deneme seçenekleri var mı?**  
C: Evet, tam işlevsel deneme sürümünü [buradan](https://releases.aspose.com/) indirebilirsiniz.

**S: Aspose.3D for Java için destek nereden alınır?**  
C: Topluluk forumu sorularınızı sormak için harika bir yerdir – [Aspose.3D forumu](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**S: Aspose.3D for Java için geçici bir lisans nasıl alınır?**  
C: Geçici‑lisans sayfasındaki adımları izleyin: [burada](https://purchase.aspose.com/temporary-license/).

**S: Sıkıştırma animasyon verilerini etkiler mi?**  
C: Hayır. Sıkıştırma yalnızca dosyanın ikili boyutunu azaltır; animasyon anahtar kareleri aynı kalır.

## Sonuç
Aspose.3D’nin `AmfSaveOptions`’unu sıkıştırma etkinleştirilmiş şekilde kullanarak, **3d dosya boyutunu** sahnenizin her ayrıntısını korurken dramatik biçimde azaltabilirsiniz. Bu, dağıtım, depolama ve gerçek‑zaman yüklemeyi çok daha verimli hâle getirir. Farklı nesne sayıları ve doku çözünürlükleriyle denemeler yaparak kendi kullanım senaryonuza en uygun dengeyi bulun.

---

**Son Güncelleme:** 2025-12-01  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12  
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}