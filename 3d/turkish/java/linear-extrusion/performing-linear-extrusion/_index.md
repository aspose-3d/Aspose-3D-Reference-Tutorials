---
date: 2025-12-18
description: Aspose.3D kullanarak Java'da şekil ekstrüzyonu yapmayı, 3D sahne oluşturmayı
  ve Wavefront OBJ dosyalarını zahmetsizce dışa aktarmayı öğrenin.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Java'da Aspose.3D Lineer Ekstrüzyon ile Şekil Nasıl Ekstrüde Edilir
url: /tr/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java'da Doğrusal Ekstrüzyon Yapma

## Giriş

Bu kapsamlı **how to extrude shape** öğreticisine hoş geldiniz! Java kullanarak 3D modelleme becerilerinizi geliştirmek istiyorsanız doğru yerdesiniz. Size bir 3D sahne oluşturmayı, doğrusal ekstrüzyon yapmayı ve sonucu Wavefront OBJ dosyası olarak dışa aktarmayı adım adım kod örnekleriyle göstereceğiz.

## Hızlı Yanıtlar
- **Doğrusal ekstrüzyon nedir?** 2D bir profili düz bir yol boyunca uzatarak 3D bir katı oluşturma işlemidir.  
- **Java'da bunu hangi kütüphane yönetir?** Aspose.3D for Java.  
- **OBJ'ye dışa aktarabilir miyim?** Evet, Wavefront OBJ dışa aktarma özelliği kullanılarak.  
- **Geliştirme için lisansa ihtiyacım var mı?** Test için ücretsiz deneme sürümü yeterlidir; üretim için lisans gereklidir.  
- **Hangi Java sürümü gereklidir?** Java 1.6 ve üzeri.

## “how to extrude shape” nedir?

Doğrusal ekstrüzyon, **3d modeling java** içinde düz bir profil—örneğin bir dikdörtgen—tanımlı bir mesafe boyunca çekilerek hacimsel bir nesneye dönüştüren temel bir tekniktir. Bu yöntem mekanik parçalar, mimari elemanlar ve dekoratif modeller oluşturmak için yaygın olarak kullanılır.

## Aspose.3D'yi doğrusal ekstrüzyon için neden kullanmalısınız?

- **Tam kontrol** geometrinin (dilimler, bükülme, ofset) üzerinde.  
- **Sorunsuz entegrasyon** Java projeleriyle—yerel bağımlılık yok.  
- **Yerleşik dışa aktarıcılar** popüler formatlar için, Wavefront OBJ dahil, böylece **generate 3d model** dosyalarını sonraki aşamalara kolayca aktarabilirsiniz.

## Önkoşullar

Bu öğreticiye başlamadan önce aşağıdaki önkoşulları karşıladığınızdan emin olun:

1. **Java Development Environment** – JDK (1.6 veya daha yeni) ve tercih ettiğiniz IDE.  
2. **Aspose.3D Library** – resmi siteden kütüphaneyi indirin ve kurun **[burada](https://releases.aspose.com/3d/java/)**.

## Paketleri İçe Aktarma

Geliştirme ortamınızı kurup Aspose.3D kütüphanesini yükledikten sonra gerekli paketi içe aktarın:

```java
import com.aspose.threed.*;
```

### Adım 1: Belge Dizinini Ayarla

Oluşturulan dosyaların kaydedileceği klasörü tanımlayın:

```java
String MyDir = "Your Document Directory";
```

> Bu, **generate 3d model** işleminin OBJ dosyasını bilinen bir konuma yazmasını sağlar.

### Adım 2: Temel Şekli Başlat

Ekstrüzyon profili olarak hizmet edecek bir dikdörtgen oluşturun:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Yuvarlatılmış köşeler elde etmek için yarıçapı ayarlayabilir veya mükemmel bir dikdörtgen için `0` olarak belirleyebilirsiniz.

### Adım 3: Doğrusal Ekstrüzyon Yap

Şimdi dikdörtgeni Z‑ekseni boyunca ekstrüde ediyor, dilimler ekliyor, ortalamayı etkinleştiriyor ve bir ofsetle bükülme uyguluyoruz:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` birim.  
- **Slices** – pürüzsüz geometri için `100`.  
- **Twist** – `360°` tam bir dönüş oluşturur.  
- **Twist offset** – bükülme orijini `(10, 0, 0)` konumuna taşır.

### Adım 4: 3D Sahne Oluştur

Bir sahne konteyneri oluşturun ve ekstrüzyonu alt düğüm olarak ekleyin. Bu adım **creates 3d scene** birden fazla nesneyi tutabilir:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Adım 5: 3D Sahneyi Kaydet

Sahneyi bir Wavefront OBJ dosyasına dışa aktarın. Bu, **wavefront obj export** ve **save 3d obj** yeteneklerini gösterir:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Kodu çalıştırdıktan sonra, belirttiğiniz dizinde `LinearExtrusion.obj` dosyasını bulacaksınız; bu dosya herhangi bir 3D görüntüleyicide açılabilir veya daha ileri işlenebilir.

## Yaygın Sorunlar ve Çözümleri

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| OBJ dosyası boş | Çıktı dizini yolu hatalı veya yazılabilir değil | `MyDir`'in mevcut bir klasöre işaret ettiğinden ve yazma izinlerine sahip olduğundan emin olun. |
| Bükülme uygulanmadı | `setCenter(true)` atlanmış | Ortalamayı etkinleştirin veya `setTwistOffset` değerlerini ayarlayın. |
| `LinearExtrusion` derleme hatası | Eski bir Aspose.3D sürümü kullanılıyor | En son Aspose.3D sürümüne güncelleyin. |

## Sıkça Sorulan Sorular

**S: Aspose.3D tüm Java sürümleriyle uyumlu mu?**  
**C:** Aspose.3D, Java 1.6 ve üzeri sürümlerle çalışır.

**S: Aspose.3D'yi ticari projelerde kullanabilir miyim?**  
**C:** Evet, geçerli bir lisansla ticari kullanım izni vardır. Lisansı **[burada](https://purchase.aspose.com/buy)** alabilirsiniz.

**S: Sorun yaşarsam nereden destek alabilirim?**  
**C:** Topluluk yardımı için **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** adresini ziyaret edin veya premium destek için **[geçici lisans](https://purchase.aspose.com/temporary-license/)** satın alın.

**S: Aspose.3D başka hangi 3D modelleme özelliklerini sunar?**  
**C:** Kütüphane ağ manipülasyonu, Boolean işlemleri, doku haritalama ve daha fazlasını içerir. Tam listeyi **[burada](https://reference.aspose.com/3d/java/)** görebilirsiniz.

**S: Ücretsiz bir deneme sürümü mevcut mu?**  
**C:** Evet, deneme sürümünü **[burada](https://releases.aspose.com/)** indirebilirsiniz.

## Sonuç

Artık Aspose.3D for Java kullanarak **how to extrude shape** işlemini nasıl yapacağınızı, bir 3D sahne oluşturup sonucu Wavefront OBJ dosyası olarak dışa aktarmayı öğrendiniz. Bu teknik, **3d modeling java** projelerinizde basit parçalarden karmaşık montajlara kadar geniş bir yelpazede kapı açar. Modelinizi daha da zenginleştirmek için Boolean işlemleri veya doku haritalama gibi ek özellikleri keşfedin.

---

**Last Updated:** 2025-12-18  
**Test Edildi:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## HEDEF ANAHTAR KELİMELER:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj