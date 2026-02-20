---
date: 2026-01-27
description: Java’da küre ağı nasıl oluşturulur ve Google Draco ile Aspose.3D kullanarak
  3D ağ dosyaları nasıl sıkıştırılır öğrenin. Verimli 3D geliştirme için adım adım
  rehber.
linktitle: How to Create Sphere Mesh in Java – Compress 3D Meshes with Google Draco
second_title: Aspose.3D Java API
title: Java'da Küre Mesh'i Oluşturma – Google Draco ile 3D Mesh'leri Sıkıştırma
url: /tr/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java’da Küre Mesh Nasıl Oluşturulur – Google Draco ile 3D Mesh’leri Sıkıştırma

## Giriş

Eğer Java’da **küre nasıl oluşturulur** mesh'i oluştururken dosya boyutunu küçük tutmak istiyorsanız, doğru yerdesiniz. Bu öğreticide **Aspose.3D** ile **Google Draco**'yu birlikte kullanarak **3D mesh'i sıkıştır**mayı adım adım göstereceğiz. Sonunda, Draco ile sıkıştırılmış bir `.drc` dosyası olarak kaydedilmiş, kullanıma hazır bir küre mesh'ine sahip olacaksınız; bu dosya, herhangi bir Java tabanlı 3D uygulamasında daha hızlı yüklenir ve çok daha az bant genişliği tüketir.

## Hızlı Yanıtlar
- **Bu öğreticinin kapsamı nedir?** Java’da bir küre mesh'i oluşturmak ve Aspose.3D aracılığıyla Google Draco ile sıkıştırmak.  
- **Ana kütüphane?** Java için Aspose.3D.  
- **Tipik uygulama süresi?** Temel bir küre için yaklaşık 10‑15 dakika.  
- **Ana önkoşul?** Java geliştirme ortamı ve classpath’inizde Aspose.3D JAR’ları.  
- **Sonuç?** Sıkıştırılmış küre mesh'ini içeren bir `.drc` dosyası.

## “how to create sphere” 3D geliştirme bağlamında ne anlama geliyor?

Küre mesh'i oluşturmak, mükemmel bir küreyi yaklaşık olarak temsil eden bir dizi köşe, kenar ve yüzey üretmek anlamına gelir. Aspose.3D'nin `Sphere` sınıfı bu işi halleder, size daha sonra işlenebilecek veya sıkıştırılabilecek temiz, üçgenleştirilmiş bir mesh sağlar.

## Aspose.3D ile Google Draco mesh sıkıştırması neden kullanılmalı?

- **Büyük boyut azaltma:** Draco, sıkıştırılmamış formatlarla karşılaştırıldığında mesh verilerini %90’a kadar küçültebilir.  
- **Hızlı çalışma zamanı çözümleme:** Unity ve three.js gibi modern motorlar Draco'yu yerel olarak çözer, bu da daha hızlı yükleme süreleri sağlar.  
- **Sorunsuz Java entegrasyonu:** Aspose.3D, yerel Draco kütüphanesini soyutlayarak, yerel ikili dosyalarla uğraşmadan Java ekosistemi içinde kalmanızı sağlar.

## Önkoşullar

- **Java Development Kit (JDK)** – 8 veya daha yeni bir sürüm kurulu ve yapılandırılmış.  
- **Aspose.3D for Java** – En son JAR'ları resmi sayfadan [burada](https://releases.aspose.com/3d/java/) indirin.  
- **Google Draco bilgisi** – Draco'nun bir geometri sıkıştırma kütüphanesi olduğunu anlamak; ağır işi Aspose.3D'nin sarmalayıcısı ile halledeceğiz.

## Paketleri İçe Aktarma

Java kaynak dosyanızda, mesh oluşturma ve Draco sıkıştırması için gereken sınıfları içe aktarın.

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

Seçtiğiniz IDE ile yeni bir Java projesi oluşturun ve Aspose.3D JAR'larını projenin classpath'ine ekleyin. Kaynak klasörünüzü, aşağıdaki kodun temiz bir pakette (ör. `com.example.draco`) yer alacak şekilde düzenleyin.

### Adım 2: Java’da Küre Mesh Nasıl Oluşturulur

Şimdi sıkıştırmak istediğimiz mesh olarak hizmet edecek basit bir küre modeli oluşturacağız.

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Pro ipucu:** `Sphere` sınıfı, varsayılan 1.0 yarıçapıyla otomatik olarak üçgenleştirilmiş bir mesh oluşturur. Senaryonuz gerektiriyorsa yarıçapı, tessellation'ı ve materyali özelleştirebilirsiniz.

### Adım 3: Mesh’i Google Draco ile Nasıl Sıkıştırılır

Küre hazır olduğunda, Aspose.3D'nin `DracoSaveOptions` sınıfı aracılığıyla Draco sıkıştırmasını çağırırız. Sıkıştırma seviyesini `OPTIMAL` olarak ayarlamak, kaliteyi korurken en iyi boyut azaltmasını sağlar.

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

### Adım 4: Sıkıştırılmış Mesh’i Kaydedin

Son olarak, sıkıştırılmış bayt dizisini bir `.drc` dosyasına yazın. Bu dosya istemcilere akış olarak gönderilebilir veya daha sonra kullanılmak üzere depolanabilir.

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Bu adımları, sadece geometri oluşturma çağrısını değiştirerek, küpler, özel modeller veya içe aktarılmış sahneler gibi diğer 3D nesneler için de tekrarlayabilirsiniz.

## Yaygın Sorunlar ve Çözümler

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JAR'ları classpath'te değil | Tüm Aspose.3D JAR dosyalarının dahil edildiğini ve sürümün dokümantasyonla eşleştiğini doğrulayın. |
| **Output file is empty** | `MyDir` var olmayan bir klasöre işaret ediyor | Dosyayı yazmadan önce klasörün var olduğundan emin olun veya programatik olarak oluşturun. |
| **Compressed mesh looks distorted** | Düşük bir sıkıştırma seviyesi kullanılıyor | `DracoCompressionLevel.OPTIMAL`'a geçin veya sıkıştırmadan önce mesh tessellation'ını ayarlayın. |

## Sıkça Sorulan Sorular

**S: Aspose.3D farklı 3D dosya formatlarıyla uyumlu mu?**  
C: Evet, Aspose.3D OBJ, FBX, STL ve GLTF dahil geniş bir format yelpazesini destekler, bu da onu birçok pipeline için çok yönlü kılar.

**S: Google Draco'yu diğer programlama dillerinde sıkıştırma için kullanabilir miyim?**  
C: Kesinlikle. Draco, C++, Python ve JavaScript için yerel kütüphaneler sunar. Bu öğretici Java'ya odaklanıyor, ancak kavramlar diğer dillere de uygulanabilir.

**S: Ek Aspose.3D dokümantasyonunu nerede bulabilirim?**  
C: Detaylı API referansları ve daha fazla örnek için [Aspose.3D Java dokümantasyonu](https://reference.aspose.com/3d/java/) adresini ziyaret edin.

**S: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
C: Geçici lisans seçeneklerini [burada](https://purchase.aspose.com/temporary-license/) keşfedin.

**S: Aspose.3D desteği için bir topluluk forumu var mı?**  
C: Evet, topluluk desteği ve tartışmalar için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

## Sonuç

Bu öğreticide Java’da **küre nasıl oluşturulur** mesh'i ve ardından Aspose.3D aracılığıyla Google Draco kullanarak **3D mesh'i sıkıştır**mayı gösterdik. Bu adımları izleyerek mesh dosya boyutlarını büyük ölçüde azaltabilir, yükleme sürelerini iyileştirebilir ve Java tabanlı 3D uygulamalarınızın yanıt verme süresini koruyabilirsiniz.

---

**Son Güncelleme:** 2026-01-27  
**Test Edildiği Versiyon:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Son Güncelleme:** 2026-01-27  
**Test Edildiği Versiyon:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose