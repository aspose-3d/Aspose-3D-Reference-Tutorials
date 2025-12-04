---
date: 2025-12-04
description: Aspose.3D kullanarak Java’da **3D sahneleri nasıl canlandıracağınızı**
  öğrenin. Bu adım‑adım kılavuz, animasyon özelliklerini nasıl ekleyeceğinizi, anahtar
  kareler oluşturacağınızı ve sonucu dışa aktaracağınızı gösterir.
language: tr
linktitle: How to Animate 3D Scenes in Java – Add Animation Properties with Aspose.3D
  Tutorial
second_title: Aspose.3D Java API
title: Java'da 3D Sahneleri Nasıl Canlandırılır – Aspose.3D Öğreticisi ile Animasyon
  Özellikleri Ekleme
url: /java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da 3D Sahneleri Nasıl Canlandırılır – Aspose.3D ile Animasyon Özellikleri Ekleme

## Giriş

Java uygulamasında **3D nesneleri nasıl canlandırılır** konusunda net, uygulamalı bir rehber arıyorsanız doğru yerdesiniz. Bu öğreticide, Aspose.3D kütüphanesini kullanarak bir 3D sahneye animasyon özellikleri eklemek için gereken tüm adımları—sahne ve mesh oluşturulmasından anahtar karelerin tanımlanmasına ve nihayet animasyonlu dosyanın dışa aktarılmasına kadar—adım adım göstereceğiz. Sonunda, modern bir 3D görüntüleyici ya da oyun motorunda yükleyebileceğiniz çalışan bir FBX dosyanız olacak.

## Hızlı Cevaplar
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java  
- **FBX'ye dışa aktarabilir miyim?** Evet, öğreticide sahne FBX7500ASCII olarak kaydedilir.  
- **Geliştirme için lisansa ihtiyacım var mı?** Test için ücretsiz deneme çalışır; üretim için ticari lisans gereklidir.  
- **Hangi Java sürümü gerekiyor?** Java 8 veya üstü.  
- **Animasyon lineer mi yoksa spline mı?** Her ikisi de—anahtar kareler BEZIER veya LINEAR enterpolasyonu kullanabilir.

## Java'da “3D nasıl canlandırılır” nedir?

3D nesneleri canlandırmak, transform özelliklerini (konum, döndürme, ölçek) zaman içinde değiştirmek anlamına gelir. Aspose.3D, **bind point** oluşturmanıza, **keyframe sequence** eklemenize ve enterpolasyonu kontrol etmenize olanak tanıyan yüksek seviyeli bir API sağlar; böylece özel bir animasyon motoru yazmanıza gerek kalmaz.

## Neden animasyon için Aspose.3D kullanmalı?

- **Çapraz format desteği** – FBX, OBJ, 3MF ve daha fazlasına dışa aktarım.  
- **Yerel bağımlılık yok** – Saf Java, sunucu tarafı boru hatları için ideal.  
- **Zengin enterpolasyon seçenekleri** – BEZIER, LINEAR ve STEP eğrileri.  
- **Tam sahne grafiği** – Düğümler, ağlar, materyaller ve animasyon tek bir API üzerinden erişilebilir.

## Önkoşullar

- Temel Java programlama bilgisi.  
- Aspose.3D for Java yüklü (indir: [sürüm sayfası](https://releases.aspose.com/3d/java/)).  
- Örneği derlemek için bir Java IDE'si veya derleme aracı (Maven/Gradle) hazır.

## Paketleri İçe Aktarma

Java projenizde temel Aspose.3D sınıflarını ve basit bir mesh oluşturmak için kullanılan yardımcı `Common` sınıfını içe aktarın:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

Şimdi ad alanları hazır, sahneyi oluşturmaya başlayalım.

## Adım 1: Sahneyi Başlatma

```java
// Initialize scene object
Scene scene = new Scene();
```

`Scene`, tüm düğümleri, ağları, ışıkları ve animasyon verilerini tutan kapsayıcıdır.

## Adım 2: Polygon Builder ile Mesh Oluşturma

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

Yardımcı, daha sonra canlandıracağımız temel bir küp mesh'i oluşturur.

## Adım 3: Çeviri ile Küp Düğümü Oluşturma

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

Her düğüm kendi transformuna (çeviri, döndürme, ölçek) sahip olabilir. Burada **cube1** adlı bir alt düğüm ekliyoruz.

## Adım 4: Çeviri Özelliğini Bulma

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

`Translation` özelliği, küpü X, Y veya Z eksenleri boyunca hareket ettireceğimiz animasyon noktamızdır.

## Adım 5: Bağlama Noktası Oluşturma

```java
// Create a bind point based on the translation property
BindPoint bindPoint = new BindPoint(scene, translation);
```

Bir **bind point**, bir özelliği (ör. çeviri) bir animasyon eğrisine bağlar.

## Adım 6: X Ekseni için Animasyon Eğrisi Oluşturma

```java
// Create the animation curve on the X component of the scale
KeyframeSequence kfs = new KeyframeSequence();

// Add keyframes for X component
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X component
bindPoint.bindKeyframeSequence("X", kfs);
```

Eğri, zaman 0, 3 ve 5 saniyelerde üç anahtar kare tanımlar. İlk ikisi pürüzsüz hareket için **BEZIER**, sonuncusu ise **LINEAR** kullanır.

## Adım 7: Z Bileşeni için Tekrarlama

```java
// Repeat the process for the Z component
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

Z eksenini canlandırmak, küpe 3‑D uzayda daha dinamik bir yol verir.

## Adım 8: 3D Sahneyi Kaydetme

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

Sahne, Blender, Unity veya Autodesk Maya gibi araçlarda animasyonu ön izlemek için açabileceğiniz bir FBX dosyası olarak kaydedilir.

## Yaygın Sorunlar ve Çözümler

| Belirti | Muhtemel Neden | Çözüm |
|---------|----------------|-------|
| Hareket görünmüyor | Anahtar kareler yanlış bileşene eklendi (ör. “Y” yerine “X”) | `bindKeyframeSequence` içinde bileşen adını doğrulayın. |
| Animasyon atlıyor | BEZIER ve LINEAR karışımı hatalı | Daha akıcı hareket için enterpolasyonu tutarlı tutun veya teğetleri manuel ayarlayın. |
| Dosya kaydedilmedi | Geçersiz dizin yolu | `MyDir`'in mevcut yazılabilir bir klasöre işaret ettiğinden ve `.fbx` ile bittiğinden emin olun. |

## Sık Sorulan Sorular

**Q: Aspose.3D'yi ticari projelerde kullanabilir miyim?**  
A: Evet. Ticari bir lisans satın alın: [Aspose satın alma sayfası](https://purchase.aspose.com/buy).

**Q: Ücretsiz deneme mevcut mu?**  
A: Kesinlikle. Deneme sürümünü [Aspose sürüm sayfası](https://releases.aspose.com/) üzerinden indirin.

**Q: Aspose.3D için destek nereden bulabilirim?**  
A: Hem personelden hem kullanıcıdan yardım almak için [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) topluluğuna katılın.

**Q: Değerlendirme için geçici lisans nasıl alabilirim?**  
A: Test sırasında çalışma zamanı kısıtlamalarından kaçınmak için bir [geçici lisans](https://purchase.aspose.com/temporary-license/) isteyin.

**Q: Daha fazla öğretici mevcut mu?**  
A: Evet—ek örnekler ve ileri konular için tam [Aspose.3D dokümantasyonu](https://reference.aspose.com/3d/java/) keşfedin.

## Sonuç

Artık Aspose.3D kullanarak Java’da **3D nesneleri nasıl canlandırılır** biliyorsunuz: sahne oluşturma, çeviri özelliklerini bağlama, anahtar kare dizileri tanımlama ve animasyonlu FBX dosyasını dışa aktarma. Rotasyon, ölçekleme veya birden fazla düğümle deneyler yaparak oyunlar, simülasyonlar veya görselleştirmeler için daha zengin animasyonlar oluşturabilirsiniz.

---

**Son Güncelleme:** 2025-12-04  
**Test Edilen:** Aspose.3D for Java 24.12 (latest)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}