---
date: 2026-09-28
description: Aspose.3D kullanarak Java'da 3D sahneleri nasıl canlandıracağınızı öğrenin,
  animation properties ekleyin, keyframes oluşturun ve linear interpolation 3D teknikleriyle
  animasyonlu FBX dosyalarını dışa aktarın.
keywords:
- how to animate 3d
- linear interpolation 3d
- export animated fbx
- create keyframe animation
- add animation properties
lastmod: 2026-09-28
linktitle: Java ile Aspose.3D kullanarak 3D sahneleri nasıl canlandırılır
og_description: Aspose.3D kullanarak Java'da 3D sahneleri nasıl canlandıracağınızı
  öğrenin. Bu adım adım rehber, animation properties eklemeyi, keyframes oluşturmayı
  ve animasyonlu FBX dosyalarını dışa aktarmayı gösterir.
og_image_alt: Developer guide showing how to animate 3D scenes in Java with Aspose.3D
og_title: Java'da 3D sahneleri nasıl canlandırılır – Aspose.3D guide
schemas:
- author: Aspose
  dateModified: '2026-09-28'
  description: Learn how to animate 3D scenes in Java using Aspose.3D, add animation
    properties, create keyframes, and export animated FBX files with linear interpolation
    3d techniques.
  headline: How to animate 3D scenes in Java with Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes. Purchase a commercial license on the [Aspose purchase page](https://purchase.aspose.com/buy).
    question: Can I use Aspose.3D for commercial projects?
  - answer: Absolutely. Download a trial from the [Aspose releases page](https://releases.aspose.com/).
    question: Is a free trial available?
  - answer: Join the community at the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)
      for help from staff and other developers.
    question: Where can I get support?
  - answer: Request a [temporary license](https://purchase.aspose.com/temporary-license/)
      to remove runtime restrictions during testing.
    question: How do I obtain a temporary evaluation license?
  - answer: Yes—explore the full [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for advanced scenarios such as skeletal animation, morph targets, and custom
      shaders.
    question: Are there more tutorials?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- animate 3d java
- Aspose.3D
- linear interpolation
- FBX export
- Java animation tutorial
title: Java ile Aspose.3D kullanarak 3D sahneleri nasıl canlandırılır
url: /tr/java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java ile Aspose.3D'de 3D sahneleri nasıl canlandırılır

## Giriş

Bu eğitimde, Aspose.3D kullanarak bir Java uygulamasında **3D nesneleri nasıl canlandıracağınızı** öğreneceksiniz. Bir sahne oluşturma, basit bir mesh inşa etme, animasyon özelliklerini bağlama, lineer interpolasyon ile anahtar kareler tanımlama ve sonunda sonucu animasyonlu bir FBX dosyası olarak dışa aktarma adımlarına başlayacağız. Sonunda Unity, Blender veya herhangi bir modern 3D görüntüleyicide çalışan, kullanıma hazır bir FBX elde edeceksiniz.

## Hızlı cevaplar
- **Animasyonu sağlayan kütüphane nedir?** Aspose.3D for Java, saf Java tabanlı bir 3D motor.  
- **Sonucu FBX olarak dışa aktarabilir miyim?** Evet – örnek, tüm anahtar kareleri koruyan bir `FBX7500ASCII` dosyası kaydeder.  
- **Bunu denemek için ücretli lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme sürümü çalışır; üretim kullanımı için ticari lisans gereklidir.  
- **Hangi Java sürümü gereklidir?** Java 8 veya daha yenisi.  
- **Interpolasyon lineer mi yoksa spline mı?** İkisi de desteklenir; düz hat hareketi için `Interpolation.LINEAR`, yumuşak eğriler için `Interpolation.BEZIER` seçebilirsiniz.

## Lineer interpolasyon 3D nedir?

Lineer interpolasyon 3D, iki anahtar kare arasındaki ara dönüşüm değerlerini düz bir hat formülüyle hesaplamaktır. Aspose.3D'de bir anahtar kare eklerken `Interpolation.LINEAR` seçersiniz ve motor, kareler arasında otomatik olarak sabit hızlı bir hareket üretir.

## Neden bir sahneye animasyon özellikleri eklenir?

Animasyon özellikleri eklemek, statik geometrileri oyunlarda, simülasyonlarda veya ürün görselleştirmelerinde yeniden kullanılabilecek dinamik içeriğe dönüştürür. Aspose.3D ile birçok düğümü bağımsız olarak canlandırabilir, tamamen animasyonlu FBX dosyaları dışa aktarabilir ve tüm iş akışını yerel DLL'ler olmadan saf Java içinde tutabilirsiniz.

## Neden animasyon için Aspose.3D kullanılır?

Aspose.3D, **12+** dışa aktarma formatını (FBX, OBJ, 3MF, STL ve GLTF dahil) destekler; böylece herhangi bir iş akışını hedefleyebilirsiniz. Kütüphane yalnızca JVM üzerinde çalışır, yerel bağımlılıkları ortadan kaldırır. Ayrıca üç interpolasyon modu (BEZIER, LINEAR, STEP) ve düğümleri, mesh'leri, materyalleri ve animasyonları tek, tutarlı bir nesne modeli üzerinden yönetmenizi sağlayan tam bir sahne‑grafik API'si sunar.

## Önkoşullar

- Java programlama temelleri.  
- Aspose.3D for Java yüklü – bunu [sürüm sayfasından](https://releases.aspose.com/3d/java/) indirebilirsiniz.  
- Örnek projeyi derlemek için Maven veya Gradle kurulmuş.  

## Paketleri içe aktar

Java kaynak dosyanızda, temel Aspose.3D ad alanlarını ve basit bir küp mesh'i oluşturan yardımcı `Common` sınıfını içe aktarın. `Common` sınıfı, bir birim küp gibi temel geometri üretmek için statik yöntemler sağlar.

```java
import com.aspose.threed.*;
```

Ad alanları hazır olduğuna göre, sahneyi oluşturmaya başlayalım.

## Adım 1: sahneyi başlat

`Scene` sınıfı, tüm düğümleri, mesh'leri, ışıkları ve animasyon verilerini tutan Aspose.3D'nin üst‑seviye konteyneridir.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: çokgen oluşturucu ile mesh oluştur

`Mesh` sınıfı, bir 3‑D nesneyi tanımlayan köşe, yüz ve normal koleksiyonunu temsil eder. Bu adımda yardımcı, daha sonra canlandıracağımız temel bir küp mesh'i oluşturur.

```java
Mesh mesh = new Mesh();
```

## Adım 3: çeviri ile küp düğümü oluştur

`Node`, bir mesh ve onun dönüşüm özelliklerini (çeviri, döndürme, ölçek) tutabilen sahne grafiğindeki bir öğedir. Burada küp mesh'ini yeni bir düğüme ekliyor ve kök noktasına konumlandırıyoruz.

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Adım 4: çeviri özelliğini bul

**Bağlama noktası**, çeviri gibi belirli bir özelliği bir animasyon eğrisine bağlar. Çeviri bağlama noktasını bulduğunuzda, motorun zaman içinde düğümün konumunu değiştirmesini sağlarsınız.

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

## Adım 5: x ekseni için animasyon eğrisi oluştur

Bir animasyon eğrisi, tek bir bileşen (X, Y veya Z) için bir dizi anahtar kare saklar. Aşağıdaki eğri, 0 s, 3 s ve 5 s zamanlarında üç anahtar kare tanımlar. İlk ikisi yumuşak geçiş için BEZIER kullanırken, son anahtar kare lineer interpolasyonu göstermek için LINEAR kullanır.

```java
// Create an animation node for the scene
AnimationNode animNode = new AnimationNode("TranslationAnimation");

// Create a bind point for the translation property on the cube's transform
BindPoint bp = animNode.createBindPoint(cube1.getTransform(), "Translation");

// Create the animation curve on the X component of the translation
KeyframeSequence kfsX = new KeyframeSequence();

// Add keyframes for X component
kfsX.add(0, 10.0f, Interpolation.BEZIER);
kfsX.add(3, 20.0f, Interpolation.BEZIER);
kfsX.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X channel of the bind point
bp.bindKeyframeSequence("X", kfsX);
```

## Adım 6: z bileşeni için tekrarla

Z eksenini canlandırmak, küpün hareketine derinlik katarak daha dinamik bir 3‑D yol oluşturur. Aynı bağlama noktası ve eğri mantığı uygulanır, ancak küpü ileri ve geri hareket ettiren değerlerle.

```java
// Repeat the process for the Z component
KeyframeSequence kfsZ = new KeyframeSequence();
kfsZ.add(0, 10.0f, Interpolation.BEZIER);
kfsZ.add(3, -10.0f, Interpolation.BEZIER);
kfsZ.add(5, 0.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the Z channel of the same bind point
bp.bindKeyframeSequence("Z", kfsZ);
```

## Animasyonlu FBX nasıl dışa aktarılır

`scene.save(...)` metodunu `FileFormat.FBX7500ASCII` ile çağırmak, tüm animasyon eğrilerini, bağlama noktalarını ve anahtar kareleri tek bir FBX konteynerine yazar. `FileFormat`, `FBX7500ASCII` dahil desteklenen çıktı formatlarını tanımlayan bir enum'dur. Hedef dizinin mevcut olduğundan ve yazma izniniz olduğundan emin olun; aksi takdirde kaydetme işlemi bir istisna fırlatır.

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

Oluşturulan dosya, Blender, Unity, Autodesk Maya veya FBX formatını destekleyen herhangi bir görüntüleyicide açılabilir; böylece animasyonu anında önizleyebilirsiniz.

## Yaygın sorunlar ve çözümler

| Belirti | Muhtemel neden | Çözüm |
|---------|----------------|-------|
| Hareket görünmüyor | Anahtar kareler yanlış bileşene eklendi (ör. “Y” yerine “X”) | `bindKeyframeSequence` içinde bileşen adını doğrulayın. |
| Animasyon atlıyor | BEZIER ve LINEAR karıştırılması hatalı | Daha akıcı hareket için interpolasyonu tutarlı tutun veya teğetleri manuel ayarlayın. |
| Dosya kaydedilmedi | Geçersiz dizin yolu | `MyDir`'in mevcut, yazılabilir bir klasöre işaret ettiğinden ve `.fbx` ile bittiğinden emin olun. |

## Sıkça sorulan sorular

**S: Aspose.3D'yi ticari projelerde kullanabilir miyim?**  
C: Evet. Ticari bir lisansı [Aspose satın alma sayfasından](https://purchase.aspose.com/buy) satın alabilirsiniz.

**S: Ücretsiz deneme mevcut mu?**  
C: Kesinlikle. [Aspose sürüm sayfasından](https://releases.aspose.com/) bir deneme indirin.

**S: Destek nereden alınabilir?**  
C: Personel ve diğer geliştiricilerden yardım almak için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) topluluğuna katılın.

**S: Geçici bir değerlendirme lisansı nasıl alınır?**  
C: Test sırasında çalışma zamanı kısıtlamalarını kaldırmak için bir [geçici lisans](https://purchase.aspose.com/temporary-license/) talep edin.

**S: Daha fazla eğitim var mı?**  
C: Evet—iskelet animasyonu, morf hedefleri ve özel gölgelendiriciler gibi ileri senaryolar için tam [Aspose.3D belgelerini](https://reference.aspose.com/3d/java/) inceleyin.

## Sonuç

Artık Java ile Aspose.3D'de **3D nesneleri nasıl canlandırılacağını** biliyorsunuz: bir sahne oluşturun, çeviri özelliklerini bağlayın, lineer interpolasyonlu anahtar kare dizileri tanımlayın ve animasyonlu bir FBX dosyası dışa aktarın. Oyunlar, simülasyonlar veya ürün görselleştirmeleri için daha zengin animasyonlar oluşturmak üzere döndürme, ölçekleme veya birden fazla düğümle deneyler yapın.

**Son Güncelleme:** 2026-09-28  
**Test Edilen:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose

## İlgili Eğitimler

- [Aspose.3D for Java ile bir FBX Dosyası Oluştur – 3D Grafik Eğitimi](/3d/java/load-and-save/create-empty-3d-document/)
- [Aspose.3D ile Java'da 3D Sahneleri Kaydet – 3D Dosyalarını Verimli Dönüştür](/3d/java/load-and-save/save-3d-scenes/)
- [Aspose.3D kullanarak Java'da Kuaterniyonlarla Modeli FBX'e Dışa Aktar](/3d/java/geometry/transform-3d-nodes-with-quaternions/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}