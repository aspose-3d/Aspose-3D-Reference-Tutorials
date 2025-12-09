---
date: 2025-12-08
description: Java'da 3D sahne oluşturmayı, Aspose.3D kullanarak gerçekçi PBR malzemeler
  uygulamayı ve 3D nesneleri Java'da renderlemek için STL formatında 3D modeli kaydetmeyi
  öğrenin.
language: tr
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'Java ile 3D Sahne Oluştur: Aspose.3D ile PBR Malzemeleri Uygula'
url: /java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da 3D Sahne Oluşturma – Aspose.3D ile PBR Malzemeler Uygulama

## Giriş

Bu uygulamalı öğreticide **Java'da 3D sahne nasıl oluşturulur** öğrenecek ve Aspose.3D kütüphanesini kullanarak Fiziksel Tabanlı Render (PBR) malzemeleriyle zenginleştireceksiniz. Kılavuzun sonunda gerçekçi yüzeyler renderlayabilecek ve **3D modeli STL olarak kaydedebileceksiniz**; böylece herhangi bir 3D iş akışında kullanılabilir.

## Hızlı Yanıtlar
- **“create 3d scene java” ne anlama geliyor?** Bu, bir Java uygulamasında geometri, ışıklar ve kameraları tutan bir Scene nesnesi oluşturma sürecidir.  
- **Hangi kütüphane PBR malzemelerini yönetir?** Aspose.3D, hazır bir `PbrMaterial` sınıfı sağlar.  
- **Sonucu STL olarak dışa aktarabilir miyim?** Evet – `Scene.save` yöntemi STL'yi (ASCII ve ikili) destekler.  
- **Üretim için lisansa ihtiyacım var mı?** Ticari kullanım için kalıcı bir Aspose.3D lisansı gereklidir; geçici bir lisans test için çalışır.  
- **Hangi Java sürümü gerekiyor?** Herhangi bir Java 8+ çalışma zamanı desteklenir.

## Java'da 3D sahne nedir?

*Sahne*, tüm nesneleri (düğümleri), onların geometrilerini, malzemelerini, ışıklarını ve kameralarını tutan bir kapsayıcıdır. Bunu, 3D modellerinizi yerleştirdiğiniz sanal bir sahne olarak düşünün. Aspose.3D’nin `Scene` sınıfı, bu sahneyi programlı olarak oluşturmanız için temiz, nesne‑yönelimli bir yol sunar.

## Java'da 3D nesneleri renderlamak için PBR malzemeleri neden kullanılır?

PBR (Physically Based Rendering), metalik ve pürüzlülük faktörleri gibi parametreleri kullanarak gerçek dünyadaki ışık etkileşimini taklit eder. Sonuç, farklı aydınlatma koşullarında daha ikna edici bir görünüm sağlar; bu da özellikle ürün görselleştirme, oyunlar veya AR/VR deneyimleri için değerlidir.

## Önkoşullar

1. **Java Geliştirme Ortamı** – JDK 8 veya daha yeni bir sürüm yüklü.  
2. **Aspose.3D Kütüphanesi** – En son JAR dosyasını [download link](https://releases.aspose.com/3d/java/) adresinden indirin.  
3. **Dokümantasyon** – API'ye resmi [documentation](https://reference.aspose.com/3d/java/) üzerinden aşina olun.  
4. **Geçici Lisans (İsteğe Bağlı)** – Kalıcı bir lisansınız yoksa, test için bir [temporary license](https://purchase.aspose.com/temporary-license/) alın.

## Paketleri İçe Aktarma

Java kaynak dosyanıza Aspose.3D ad alanını ekleyin:

```java
import com.aspose.threed.*;
```

## Adım 1: Sahneyi Başlatma

Geometri ve malzemeleriniz için bir tuval görevi görecek sahneyi oluşturun.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Pro ipucu:** `MyDir`'i yazılabilir bir klasöre işaret edecek şekilde tutun; aksi takdirde `save` çağrısı başarısız olur.

## Adım 2: PBR Malzemesini Başlatma

Yakın metalik bir görünüm sağlayan metalik ve pürüzlülük değerleriyle bir PBR malzemesi yapılandırın.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Bu değerler neden?** Yüksek bir metalik faktör (≈ 0.9) yüzeyi metal gibi davranmasını sağlar, yüksek bir pürüzlülük (≈ 0.9) ise hafif bir dağılım ekleyerek mükemmel bir ayna bitişi önler.

## Adım 3: 3D Nesne Oluşturma ve Malzemeyi Uygulama

Burada basit bir kutu geometrisi oluşturuyor, sahnenin kök düğümüne ekliyor ve az önce oluşturduğumuz PBR malzemesini atıyoruz.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Yaygın tuzak:** Malzemeyi düğüme ayarlamayı unutmak, nesneyi varsayılan (PBR olmayan) görünümde bırakır.

## Adım 4: 3D Sahneyi Kaydetme (STL Dışa Aktarma)

PBR‑geliştirilmiş kutuyu da içeren tüm sahneyi bir STL dosyasına dışa aktarın. STL, 3‑D baskı ve hızlı görsel kontroller için yaygın olarak desteklenen bir formattır.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

Daha küçük bir dosya boyutu gerekiyorsa `FileFormat.STLBINARY` seçeneğini de kullanabilirsiniz.

## Yaygın Sorunlar ve Çözümleri

| Sorun | Muhtemel Neden | Çözüm |
|-------|----------------|-------|
| **Dosya kaydedilmedi** | `MyDir` var olmayan bir klasöre işaret ediyor veya yazma izni yok | Dizinin mevcut olduğunu ve Java işleminizin yazma erişimine sahip olduğunu doğrulayın |
| **Malzeme düz görünüyor** | Metallic/Roughness değerleri 0 olarak ayarlanmış | `setMetallicFactor` ve/veya `setRoughnessFactor` değerlerini artırın |
| **STL dosyası açılamıyor** | Görüntüleyici için yanlış dosya formatı bayrağı (ASCII vs Binary) | Hedef görüntüleyiciniz için uygun `FileFormat` enum değerini kullanın |

## Sıkça Sorulan Sorular

**S: Aspose.3D'yi ticari projelerde kullanabilir miyim?**  
C: Evet. [purchase page](https://purchase.aspose.com/buy) üzerinden ticari bir lisans satın alın.

**S: Aspose.3D için nasıl destek alabilirim?**  
C: Ücretsiz yardım için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) topluluğuna katılın veya geçerli bir lisansla destek talebi açın.

**S: Ücretsiz deneme sürümü mevcut mu?**  
C: Kesinlikle. [free trial page](https://releases.aspose.com/) adresinden deneme sürümünü indirin.

**S: Aspose.3D için ayrıntılı dokümantasyonu nerede bulabilirim?**  
C: Tüm API referansları resmi [documentation](https://reference.aspose.com/3d/java/) adresinde mevcuttur.

**S: Test için geçici bir lisans nasıl alabilirim?**  
C: [temporary license link](https://purchase.aspose.com/temporary-license/) üzerinden bir lisans talep edin.

## Sonuç

Artık **Java'da bir 3D sahne oluşturmuş**, gerçekçi bir PBR malzemesi uygulamış ve sonucu Aspose.3D kullanarak bir STL dosyası olarak dışa aktarmış bulunuyorsunuz. Bu iş akışı, daha zengin görselleştirmeler oluşturmak, varlıkları 3‑D baskı için hazırlamak veya modelleri oyun motorlarına beslemek için sağlam bir temel sağlar.

---

**Last Updated:** 2025-12-08  
**Tested With:** Aspose.3D 24.12 (latest)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}