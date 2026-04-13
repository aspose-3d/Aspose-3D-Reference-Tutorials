---
date: 2026-02-22
description: Aspose.3D for Java kullanarak lineer ekstrüzyon bükülmesi ve bükülme
  ofseti ile 3D sahne oluşturmayı ve 3D sahneyi dışa aktarmayı öğrenin.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java kullanarak Doğrusal Ekstrüzyonda Twist Ofset ile 3D sahne
  nasıl oluşturulur
url: /tr/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Lineer Ekstrüzyonda Twist Offset Kullanımı

## Giriiş

3D grafiklerin dinamik dünyasında, **create 3d scene** sanatının ustalaşması, herhangi bir Java 3D bölümü projesi için oyunun kalıcı bir faktörüdür. Aspose.3D for Java ile biçimleri sadece lineer olarak ekstrüde etmekle kalmaz, aynı zamanda karmaşık, bükülmüş geometriler çıktısı için bir büküm ofseti kullanılabilir. Bu öğretilir, **3d sahne oluşturma** oluşturma, lineer ekstrüzyon büküm'i gösterilir ve sonunda **3d sahneyi dışa aktarma**'i yaygın bir OBJ dosyasına aktarmak için yapılması gereken tüm adımların boyutunu gösterir.

## Hızlı Yanıtlar
- **Twist Offset ne işe yarar?** Twist Offset, ekstrüzyon boyunca yolun başlangıcındaki ilerlemeyi kaydırarak rotasyonu ofsetlemenizi sağlar.
- **Doğrusal ekstrüzyonu hangi sınıf gerçekleştirir?** 'LinearExtrusion' – bu sınıfta büküm, dilimler ve büküm ofset düzeni yapılabilir.
- **Sonucu dışa aktarabilir miyim?** Evet, `scene.save(..., FileFormat.WAVEFRONTOBJ)` ölçeğiyle 3D sahneyi listeleyebilirsiniz.
- **Geliştirme için lisansa ihtiyacım var mı?** Test için geçici bir lisans yeterlidir; üretim ortamı için tam lisans gereklidir.
- **Hangi Java sürümü destekleniyor?** Yeni Aspose.3D kütüphanesi Java8+ çalışma saati ile uyumludur.

## Aspose.3D'de “3d sahne oluştur” nedir?
3D sahne oluşturmak, bir `Scene` nesnesi becerisi, geleceğe yönelik düğüm (nesne) seçme ve ardından sahneyi istediğiniz dosya formatını büyütmek gelir. Bu, Java'da herhangi bir 3D parçanın iş kapasitelerinin gerçekleştirilmesini sağlar.

## Neden büküm ofsetiyle doğrusal ekstrüzyon bükümü kullanmalısınız?
Ekstrüzyon sırasında bir büküm seçme, helisel sütunlar ya da dekoratif tutamaklar gibi spiral formların elde edilmesini sağlar. Twist offset, Twist’i özel bir şekilde başlatmanıza olanak tanır; Bu da mekanik parçalar, merkezi modeller veya mimari detaylar için daha hassas kontroller sunar.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- **Java Environment:** Sisteminizde bir Java geliştirme ortamı kurulu olduğunuzdan emin olun.
- **Aspose.3D for Java:** Aspose.3D kütüphanesini [indirme bağlantısı](https://releases.aspose.com/3d/java/) adresinden indirip kurun.
- **Dokümantasyon:** [Aspose.3D for Java dokümantasyonu](https://reference.aspose.com/3d/java/) sayfasına göz atarak temel kavramları öğrenin.

## Paketleri İçe Aktar

Aspose.3D for Java'yı kullanmaya başlamak için Java projenizde gerekli paketleri içe aktarın. Sorunsuz entegrasyon için gerekli kitaplıkları eklediğinizden emin olun.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 3B Sahne Oluşturma – Adım Adım Kılavuz

### Adım 1: Ortamı Kurun
Öncelikle Java geliştirme ortamınızı kurun ve Aspose.3D for Java'nın doğru şekilde yüklendiğinden emin olun. Bu adım, herhangi bir **Java 3B modelleme** çalışması için çok önemlidir.

### Adım 2: Temel Profili Başlatın
Ekstrüzyon için bir temel profil oluşturun; bu durumda, yuvarlama yarıçapı 0,3 olan bir `RectangleShape`. Profil, ekstrüzyon yolu boyunca süpürülecek kesiti tanımlar.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Adım 3: 3B Sahne Oluşturma
Ekstrüde edilmiş nesnelerinizi barındıracak bir 3B sahne oluşturun. Burada, her bir geometri parçasını temsil eden **alt düğüm** öğeleri oluşturacaksınız.

```java
// Create a scene
Scene scene = new Scene();
```

### Adım 4: Düğüm Oluşturma
Sahne içinde farklı varlıkları temsil etmek için düğümler oluşturun. Burada iki kardeş düğüm oluşturuyoruz—biri düz ekstrüzyon için, diğeri ise bükme ofseti kullanan bir düğüm.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Adım 5: Bükme ve Bükme Ofseti ile Doğrusal Ekstrüzyon Gerçekleştirme
Her iki düğüme de doğrusal ekstrüzyon uygulayın. Soldaki düğüm temel bir bükmeyi gösterirken, sağdaki düğüm bu özellik ile elde ettiğiniz ekstra kontrolü göstermek için bir bükme ofseti ekler.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Profesyonel ipucu:** `setSlices()` değerini artırarak, daha fazla bükülmeler yapmanız gerektiğinde ağınızı yükseltebilirsiniz.

### Adım 6: 3B Sahneyi Kaydedin (3B sahneyi dışa aktarın)
Son olarak, birleştirilmiş sahneyi herhangi bir standart 3B görüntüleyicide görüntüleyebilmeniz veya diğer işlem hatlarına aktarabilmeniz için bir OBJ dosyasına dışa aktarın.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Kod başarıyla çalıştığında, belirtilen dizinde `TwistOffsetInLinearExtrusion.obj` dosyasını bulacaksınız; bu dosyayı Blender, MeshLab veya herhangi bir CAD yazılımı ile açabilirsiniz.

## Yaygın Sorunlar ve Çözümler
| Sayı | Neden Olur | Düzelt |
|----------|-----|-----|
| **Sahne boş dosya olarak kaydedilir** | `MyDir` yolu hatalı veya yazma izni yok. | Dizin var mı ve yazılabilir mi kontrol edin, ya da mutlak bir yol kullanın. |
| **Büküm düz görünüyor** | `setSlices()` değeri çok düşük, ancak kaba bir ağ oluşturur. | Daha yüksek dilim sayıları (ör. 200) belirleyerek büküm'i pürüzsüzleştirin. |
| **Büküm ofsetinin etkisi yoktur** | Ofset vektörü ekstrüzyon boyunca aynı doğrultuda. | X veya Y üyelerinden birini sıfır olmayan bir değer yaparak ofset kaymasını görün. |

## Sıkça Sorulan Sorular

### S1: Aspose.3D for Java'yı ticari olmayan projelerde kullanabilir miyim?
A1: Evet, Aspose.3D for Java hem ticari hem de ticari olmayan projelerde kullanılabilir. Daha fazla bilgi için [lisanslama seçeneklerini](https://purchase.aspose.com/buy) kontrol edin.

### S2: Aspose.3D for Java için destek nerede bulabilirim?

A2: Yardım almak ve toplulukla bağlantı kurmak için [Aspose.3D for Java forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S3: Aspose.3D for Java için ücretsiz deneme sürümü mevcut mu?

A3: Evet, [sürümler sayfasından](https://releases.aspose.com/) ücretsiz deneme sürümünü inceleyebilirsiniz.

### S4: Aspose.3D for Java için geçici lisansı nasıl edinebilirim?

A4: Projeniz için geçici lisans almak için [bu bağlantıyı](https://purchase.aspose.com/temporary-license/) ziyaret edin.

### S5: Ek örnekler ve eğitimler mevcut mu?

C5: Evet, daha fazla örnek ve ayrıntılı eğitim için [belgelere](https://reference.aspose.com/3d/java/) bakın.

---

**Son Güncelleme:** 22.02.2026
**Test Edilen Sürüm:** Aspose.3D for Java 24.11 (en son sürüm)
**Yazar:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
