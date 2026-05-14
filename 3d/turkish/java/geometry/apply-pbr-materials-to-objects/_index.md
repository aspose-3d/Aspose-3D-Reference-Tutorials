---
date: 2026-05-14
description: Java'da STL'yi dışa aktarmayı, bir 3D sahne oluşturarak, Aspose.3D ile
  gerçekçi PBR malzemeler uygulayarak ve modeli render için kaydederek öğrenin.
keywords:
- how to export stl
- Aspose 3D PBR materials
- Java 3D scene creation
linktitle: Java'da STL Nasıl Dışa Aktarılır – Aspose.3D ile 3D Sahne Oluşturma
schemas:
- author: Aspose
  dateModified: '2026-05-14'
  description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  headline: How to Export STL in Java – Create 3D Scene with Aspose.3D
  type: TechArticle
- description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  name: How to Export STL in Java – Create 3D Scene with Aspose.3D
  steps:
  - name: '**Java Development Environment** – JDK 8 or newer installed.'
    text: '**Java Development Environment** – JDK 8 or newer installed.'
  - name: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
  - name: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
    text: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
  - name: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
    text: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
  type: HowTo
- questions:
  - answer: It’s the process of building a `Scene` object that holds geometry, lights,
      and cameras in a Java application.
    question: What does “create 3d scene java” mean?
  - answer: Aspose.3D provides a ready‑made `PbrMaterial` class.
    question: Which library handles PBR materials?
  - answer: Yes – the `Scene.save` method supports STL (ASCII and binary).
    question: Can I export the result as STL?
  - answer: A permanent Aspose.3D license is required for commercial use; a temporary
      license works for testing.
    question: Do I need a license for production?
  - answer: Any Java 8+ runtime is supported.
    question: What Java version is required?
  type: FAQPage
second_title: Aspose.3D Java API
title: Java'da STL Nasıl Dışa Aktarılır – Aspose.3D ile 3D Sahne Oluşturma
url: /tr/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da STL Nasıl Dışa Aktarılır – Aspose.3D ile 3D Sahne Oluşturma

## Giriş

Bu uygulamalı öğreticide, bir Java uygulamasından tam bir 3D sahne oluşturarak, Fiziksel Tabanlı Rendering (PBR) malzemeleri uygulayarak ve sonucu Aspose.3D ile kaydederek **STL nasıl dışa aktarılır** öğreneceksiniz. 3‑D baskı, oyun motoru boru hatları veya ürün görselleştirme hedefliyor olun, aşağıdaki adımlar herhangi bir Java 8+ çalışma zamanında çalışan, tekrarlanabilir ve sürüm kontrolü yapılan bir iş akışı sunar.

## Hızlı Yanıtlar
- **“create 3d scene java” ne anlama geliyor?** Bu, bir Java uygulamasında geometri, ışıklar ve kameraları tutan bir `Scene` nesnesi oluşturma sürecidir.  
- **Hangi kütüphane PBR malzemelerini yönetir?** Aspose.3D, hazır bir `PbrMaterial` sınıfı sağlar.  
- **Sonucu STL olarak dışa aktarabilir miyim?** Evet – `Scene.save` yöntemi STL'yi (ASCII ve ikili) destekler.  
- **Üretim için lisansa ihtiyacım var mı?** Ticari kullanım için kalıcı bir Aspose.3D lisansı gereklidir; geçici bir lisans test için çalışır.  
- **Hangi Java sürümü gereklidir?** Herhangi bir Java 8+ çalışma zamanı desteklenir.

## Aspose.3D ile Java'da 3D sahne nasıl oluşturulur

`Scene`, bir 3D belgeyi temsil eden ana konteyner sınıfıdır. Bir sahneyi birkaç satır kodla yükleyebilir, yapılandırabilir ve kaydedebilirsiniz. İlk olarak bir `Scene` örneği oluşturursunuz, ardından geometri ve bir `PbrMaterial` ekler ve sonunda STL formatıyla `Scene.save` çağrısı yaparsınız. Bu uçtan uca akış, bir 3D editör açmadan varlık üretimini otomatikleştirmenizi sağlar.

## Java'da 3D sahne nedir?

*Sahne*, tüm nesneleri (düğümler), bunların geometrisini, malzemelerini, ışıklarını ve kameralarını tutan konteynerdir. Bunu, 3D modellerinizi yerleştirdiğiniz sanal bir sahne olarak düşünün. Aspose.3D’nin `Scene` sınıfı, bu sahneyi programlı bir şekilde oluşturmanız için temiz, nesne‑yönelimli bir yol sunar.

## Java'da 3D nesneleri render'lamak için PBR malzemeleri neden kullanılır?

PBR (Physically Based Rendering), metalik ve pürüzlülük parametrelerini kullanarak gerçek dünyadaki ışık etkileşimini taklit eder. Sonuç, herhangi bir aydınlatma koşulunda tutarlı görünen bir malzemedir; bu, gerçekçi ürün görselleştirme, AR/VR ve modern oyun motorları için esastır. Metalik, pürüzlülük, albedo ve normal haritaları kontrol ederek, el ile gölgelendiricileri ayarlamadan, parlatılmış metalden mat plastik'e kadar geniş bir yüzey bitişi yelpazesi elde edebilirsiniz.

## Önkoşullar

1. **Java Geliştirme Ortamı** – JDK 8 veya daha yeni bir sürüm yüklü.  
2. **Aspose.3D Kütüphanesi** – En son JAR'ı [download link](https://releases.aspose.com/3d/java/) adresinden indirin.  
3. **Dokümantasyon** – API'ye resmi [documentation](https://reference.aspose.com/3d/java/) üzerinden göz atın.  
4. **Geçici Lisans (İsteğe Bağlı)** – Kalıcı lisansınız yoksa, test için bir [temporary license](https://purchase.aspose.com/temporary-license/) alın.

## Ortak Kullanım Senaryoları

| Kullanım Durumu | Öğreticinin Yardımı |
|-----------------|----------------------|
| **3‑D baskı** | STL'ye dışa aktarmak, modeli doğrudan bir dilimleyiciye göndermenizi sağlar. |
| **Oyun varlık boru hattı** | PBR malzeme parametreleri modern oyun motorlarının beklentileriyle eşleşir. |
| **Ürün yapılandırıcı** | Metalik/pürüzlülük değerlerini ayarlayarak renk/bitiriş varyasyonlarını otomatikleştirin. |

## Paketleri İçe Aktarma

`Aspose.3D` ad alanı, derleyicinin öğreticide kullanılan sınıfları çözebilmesi için içe aktarılmalıdır.

```java
import com.aspose.threed.*;
```

## Adım 1: Bir Sahne Başlatma

`Scene`, tüm 3D içeriğin ana konteyneridir. Yeni bir örnek oluşturmak, geometri, ışık ve kamera ekleyebileceğiniz temiz bir tuval sağlar.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **İpucu:** `MyDir`'i yazılabilir bir klasöre işaret edecek şekilde tutun; aksi takdirde `save` çağrısı başarısız olur.

## Adım 2: Bir PBR Malzemesi Başlatma

`PbrMaterial`, metalik ve pürüzlülük gibi fiziksel tabanlı render özelliklerini tanımlar. Bir `PbrMaterial`, metalik, pürüzlülük ve diğer yüzey özelliklerini belirler. Yüksek bir metalik faktör (≈ 0.9) ve 0.9 pürüzlülük ayarlamak, gerçekçi bir fırçalanmış metal görünümü sağlar.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Neden bu değerler?** Yüksek bir metalik faktör, yüzeyi metal gibi davranmasını sağlar, yüksek bir pürüzlülük ise hafif bir dağılım ekleyerek mükemmel bir ayna bitişi önler.

## Adım 3: Bir 3D Nesne Oluştur ve Malzemeyi Uygula

Burada basit bir kutu geometrisi oluşturuyor, sahnenin kök düğümüne ekliyor ve az önce oluşturduğumuz `PbrMaterial`'ı atıyoruz.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Yaygın tuzak:** Düğümde malzemeyi ayarlamayı unutmak, nesneyi varsayılan (PBR olmayan) görünüme bırakır.

## Adım 4: 3D Sahneyi Kaydet (STL Dışa Aktarma)

`Scene.save`, sahneyi belirtilen formatta bir dosyaya yazar. Tüm sahneyi—PBR‑geliştirilmiş kutu dahil—STL dosyasına dışa aktarın. STL, 3‑D baskı ve hızlı görsel kontroller için yaygın olarak desteklenen bir formattır.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

`FileFormat.STLBINARY`, ASCII'den daha küçük olan ikili STL çıktısını belirtir. İnsan tarafından okunabilir bir dosya tercih ediyorsanız `FileFormat.STLASCII`'ı da seçebilirsiniz.

## Neden Önemli

Tutarlı malzeme parametreleri, oluşturulan her modelin farklı görüntüleyiciler ve aydınlatma ayarları arasında aynı görünmesini sağlar. Otomasyon, minimal çabayla büyük miktarda varyasyon üretmenizi sağlar; çapraz platform STL çıktısı ise Blender'dan 3‑D yazıcı dilimleyicilerine kadar çeşitli araçlarla uyumluluğu garanti eder. Bu faydalar birlikte geliştirme boru hatlarını hızlandırır ve manuel hataları azaltır.

## Sorun Giderme İpuçları

| Sorun | Muhtemel Neden | Çözüm |
|-------|----------------|-------|
| **Dosya kaydedilmedi** | `MyDir` var olmayan bir klasöre işaret ediyor ya da yazma izni yok | Dizinin mevcut olduğunu ve Java sürecinizin yazma erişimine sahip olduğunu doğrulayın |
| **Malzeme düz görünüyor** | Metallic/Roughness değerleri 0 olarak ayarlanmış | `setMetallicFactor` ve/veya `setRoughnessFactor` değerlerini artırın |
| **STL dosyası açılamıyor** | Görüntüleyici için yanlış dosya formatı bayrağı (ASCII vs Binary) | Hedef görüntüleyiciniz için uygun `FileFormat` enum'ını kullanın |

## Sıkça Sorulan Sorular

**Q:** Aspose.3D'yi ticari projelerde kullanabilir miyim?  
**A:** Evet. [purchase page](https://purchase.aspose.com/buy) üzerinden bir ticari lisans satın alın.

**Q:** Aspose.3D için destek nasıl alınır?  
**A:** Ücretsiz yardım için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) topluluğuna katılın veya geçerli bir lisansla bir destek bileti açın.

**Q:** Ücretsiz deneme sürümü mevcut mu?  
**A:** Kesinlikle. [free trial page](https://releases.aspose.com/) adresinden bir deneme sürümü indirin.

**Q:** Aspose.3D için ayrıntılı dokümantasyonu nerede bulabilirim?  
**A:** Tüm API referansları resmi [documentation](https://reference.aspose.com/3d/java/) adresinde mevcuttur.

**Q:** Test için geçici bir lisans nasıl alınır?  
**A:** [temporary license link](https://purchase.aspose.com/temporary-license/) üzerinden bir lisans talep edin.

---

**Son Güncelleme:** 2026-05-14  
**Test Edilen Versiyon:** Aspose.3D 24.12 (latest)  
**Yazar:** Aspose  

{{< blocks/products/products-backtop-button >}}

## İlgili Öğreticiler

- [Aspose 3D Java ile 3D Sahne Oluşturma](/3d/java/3d-scenes-and-models/)
- [Sahneyi FBX'e Dışa Aktarma ve Java'da 3D Sahne Bilgilerini Alma](/3d/java/3d-scenes-and-models/get-scene-information/)
- [OBJ'yi Dışa Aktarma - Java'da Hassas 3D Sahne Konumlandırma için Düzlem Yönelimini Değiştirme](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}