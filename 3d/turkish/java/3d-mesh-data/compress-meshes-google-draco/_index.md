---
date: 2026-04-29
description: Java'da bir küre ağı oluşturarak ve Google Draco ile sıkıştırarak 3D
  model boyutunu nasıl azaltacağınızı öğrenin – Aspose.3D; Aspose 3D dışa aktarımı
  için vazgeçilmez.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Java'da Küre Mesh'i Nasıl Oluşturulur – Google Draco ile 3D Mesh'leri Sıkıştırma
second_title: Aspose.3D Java API
title: '3D Model Boyutunu Azalt: Java''da Draco ile Küre Mesh''i Oluştur'
url: /tr/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Model Boyutunu Azaltın: Java’da Draco ile Küre Mesh Oluşturma

## Giriş

Yüksek kaliteli geometri sunarken **3D model boyutunu azaltmanın** hızlı bir yolunu arıyorsanız doğru yerdesiniz. Bu öğreticide **Aspose.3D for Java** ile bir küre mesh’i oluşturup ardından **Google Draco** kullanarak bu mesh’i sıkıştıracağız. Sonunda, orijinaline göre dramatik şekilde daha küçük bir `.drc` dosyanız olacak; bu da web‑tabanlı görüntüleyiciler, mobil oyunlar veya bant genişliği sınırlı herhangi bir Java uygulaması için mükemmeldir.

## Hızlı Yanıtlar
- **Bu öğreticide ne ele alınıyor?** Java’da bir küre mesh’i oluşturmak ve Aspose.3D aracılığıyla Google Draco ile sıkıştırmak.  
- **Ana kütüphane?** Aspose.3D for Java (mesh oluşturma ve Draco dışa aktarma için kullanılır).  
- **Tipik uygulama süresi?** Temel bir küre için yaklaşık 10‑15 dakika.  
- **Temel ön koşul?** Aspose.3D JAR'larının sınıf yolunda bulunduğu bir Java geliştirme ortamı.  
- **Sonuç?** Sıkıştırılmamış bir mesh ile karşılaştırıldığında **3D model boyutunu** %90’a kadar azaltan bir `.drc` dosyası.

## “3D model boyutunu azaltma” 3D geliştirme bağlamında ne anlama gelir?

3D model boyutunu azaltmak, görsel kaliteyi belirgin şekilde düşürmeden aktarılması veya depolanması gereken geometri verisinin miktarını küçültmek demektir. Draco, vertex konumları, normal ve diğer öznitelikleri son derece sıkı bir ikili formatta kodlayarak bunu başarır. Aspose.3D ile birleştirildiğinde, tüm iş akışı Java içinde kalır; yerel ikili dosyalarla uğraşmanız gerekmez.

## Aspose.3D ile Google Draco mesh sıkıştırması neden kullanılmalı?

- **Büyük boyut azaltma:** Draco, OBJ veya STL gibi formatlarla karşılaştırıldığında mesh verilerini %90’a kadar azaltabilir.  
- **Hızlı çalışma zamanı çözümleme:** Unity, Unreal ve three.js gibi motorlar Draco'yu yerel olarak çözer, bu da daha hızlı yükleme süreleri sağlar.  
- **Sorunsuz Java entegrasyonu:** Aspose.3D, yerel Draco kütüphanesini soyutlayarak Java ekosisteminde kalmanızı sağlar.  
- **Tek durak Aspose 3D dışa aktarımı:** Geometri oluşturmak için kullandığınız aynı API, dışa aktarmayı da yönetir, böylece işlem hattı basitleşir.

## Önkoşullar

- **Java Development Kit (JDK)** – sürüm 8 veya daha yeni.  
- **Aspose.3D for Java** – resmi sayfadan en son JAR'ları indirin [buradan](https://releases.aspose.com/3d/java/).  
- **Google Draco hakkında temel bilgi** – Aspose.3D'nin sarmalayıcısını kullanacaksınız, bu yüzden yerel Draco kurulumu gerekli değildir.

## Paketleri İçe Aktarın

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Adım‑Adım Kılavuz

### Adım 1: Projeyi Kurun

Yeni bir Java projesi oluşturun (herhangi bir IDE çalışır) ve tüm Aspose.3D JAR'larını sınıf yoluna ekleyin. Kaynak dosyalarınızı `com.example.draco` gibi bir paket içinde tutarak netlik sağlayın.

### Adım 2: Java’da Küre Mesh Nasıl Oluşturulur

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Pro tip:** `Sphere` sınıfı, varsayılan yarıçapı 1.0 olan üçgenlenmiş bir mesh üretir. Sıkıştırmadan önce farklı bir detay seviyesine ihtiyacınız varsa özel yarıçap, tessellation veya materyal parametreleri geçirebilirsiniz.

### Adım 3: Mesh’i Google Draco ile Nasıl Sıkıştırılır

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Sıkıştırma seviyesini `OPTIMAL` olarak ayarlamak, görsel doğruluğu korurken en büyük boyut azaltmasını sağlar ve doğrudan **3D model boyutunu azaltmanıza** yardımcı olur.

### Adım 4: Sıkıştırılmış Mesh’i Kaydedin

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Ortaya çıkan `SphereMeshtoDRC_Out.drc` istemcilere akış olarak gönderilebilir, bir CDN'de depolanabilir veya Draco‑uyumlu herhangi bir motor tarafından doğrudan yüklenebilir.

## Yaygın Kullanım Senaryoları

| Senaryo | Model Boyutunu Neden Azaltmalı? | Bu Öğretici Nasıl Yardımcı Olur |
|----------|-------------------------------|---------------------------------|
| Web tabanlı ürün yapılandırıcıları | Yavaş bağlantılarda daha hızlı sayfa yüklemeleri | Draco sıkıştırmalı `.drc` dosyaları saniyeler içinde yüklenir |
| Mobil AR/VR uygulamaları | Cihazlarda daha düşük bellek ayak izi | Daha küçük mesh'ler uygulamanın yanıt vermesini sağlar |
| Bulut tabanlı render sahneleri | Bant genişliği maliyetlerini azaltır | Aspose.3D'den Draco'ya tek tıkla dışa aktarım |

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden | Çözüm |
|-------|-------|-------|
| **`NoClassDefFoundError` Draco sınıfları için** | Aspose.3D JAR'ları sınıf yolunda bulunmuyor | *Tüm* Aspose.3D JAR dosyalarının dahil edildiğini ve sürümün belgelerle eşleştiğini doğrulayın. |
| **Çıktı dosyası boş** | `MyDir` mevcut olmayan bir klasöre işaret ediyor | Dosyayı yazmadan önce dizini programatik olarak oluşturun (`Files.createDirectories(Paths.get(MyDir))`). |
| **Sıkıştırılmış mesh bozulmuş görünüyor** | Düşük sıkıştırma seviyesi veya yetersiz tessellation kullanılması | `DracoCompressionLevel.OPTIMAL`'a geçin ve kürenin tessellation'ını artırın (ör. `new Sphere(1.0, 64, 64)`). |

## Sıkça Sorulan Sorular

**S: Aspose.3D farklı 3D dosya formatlarıyla uyumlu mu?**  
C: Evet, Aspose.3D OBJ, FBX, STL, GLTF ve daha birçok formatı destekler; bu da **Aspose 3D dışa aktarımı** işlem hatları için çok yönlü bir seçim olmasını sağlar.

**S: Google Draco'yu başka programlama dillerinde de sıkıştırma için kullanabilir miyim?**  
C: Kesinlikle. Draco, C++, Python ve JavaScript için yerel kütüphaneler sunar. Bu öğretici Java'ya odaklanıyor, ancak kavramlar diğer dillerde de geçerlidir.

**S: Ek Aspose.3D belgelerini nerede bulabilirim?**  
C: Tam API referansları ve daha fazla örnek için [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) sayfasını ziyaret edin.

**S: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
C: Geçici lisans seçeneklerini [buradan](https://purchase.aspose.com/temporary-license/) inceleyin.

**S: Aspose.3D desteği için bir topluluk forumu var mı?**  
C: Evet, [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresindeki tartışmalara katılabilirsiniz.

## Sonuç

Bu rehberde, Java’da bir küre mesh’i oluşturup ardından Aspose.3D üzerinden Google Draco ile sıkıştırarak **3D model boyutunu nasıl azaltabileceğinizi** gösterdik. Bu kısa adımları izleyerek mesh dosyalarınızı dramatik şekilde küçültebilir, yükleme sürelerini iyileştirebilir ve Java‑tabanlı 3D uygulamalarınızı daha duyarlı ve bant genişliği dostu hâle getirebilirsiniz.

---

**Son Güncelleme:** 2026-04-29  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}