---
date: 2026-02-22
description: Aspose.3D for Java kullanarak lineer ekstrüzyonda yön ayarlamayı ve 3D
  model obj dosyasını dışa aktarmayı öğrenin. Adım adım rehberimizi izleyin.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Yön Nasıl Ayarlanır
url: /tr/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Doğrusal Ekstrüzyonda Yön Ayarlama

## Giriş

Bu kapsamlı öğreticide **doğrusal ekstrüzyonda yön nasıl ayarlanır** keşfedeceksiniz. CAD benzeri bir araç geliştiriyor ya da bir oyun motoru için geometri üretiyor olun, ekstrüzyon yönünü kontrol etmek, ihtiyacınız olan şekli tam olarak oluşturmanızı sağlar. Bir profili başlatmaktan sonucu bir OBJ dosyası olarak kaydetmeye kadar her adımı adım adım inceleyeceğiz, böylece **3d model obj** dosyalarını doğrudan Java’dan **export** edebileceksiniz.

## Hızlı Yanıtlar
- **Doğrusal ekstrüzyon için birincil sınıf nedir?** `LinearExtrusion`
- **Hangi metod ekstrüzyon yönünü tanımlar?** `setDirection(Vector3 direction)`
- **Sonucu OBJ olarak dışa aktarabilir miyim?** Evet, `scene.save(..., FileFormat.WAVEFRONTOBJ)` kullanarak
- **Geliştirme için lisansa ihtiyacım var mı?** Ücretsiz deneme mevcuttur; üretim için lisans gereklidir.
- **Hangi Java IDE’si en iyi çalışır?** IntelliJ IDEA veya Eclipse tamamen desteklenir.

## Doğrusal Ekstrüzyon Nedir?

Doğrusal ekstrüzyon, bir 2‑D profili (örneğin bir dikdörtgen veya daire) alır ve düz bir hat boyunca uzatarak bir 3‑D katı oluşturur. Varsayılan olarak ekstrüzyon pozitif Z‑ekseni izler, ancak Aspose.3D `setDirection` özelliğiyle bu yolu değiştirebilmenizi sağlar.

## Doğrusal Ekstrüzyonda Neden Yön Ayarlanmalı?

Özel bir yön ayarlamak aşağıdaki durumlarda faydalıdır:
- Sahnedeki mevcut nesnelerle geometrinin hizalanması.
- Ek dönüşüm adımları olmadan eğimli veya açılı parçalar oluşturulması.
- Belirli bir koordinat sistemine (ör. 3‑D baskı veya oyun motorları için) uyması gereken modellerin dışa aktarılması.

## Önkoşullar

İlerlemeye başlamadan önce şunların kurulu olduğundan emin olun:

- Java hakkında temel bilgi.
- Aspose.3D kütüphanesi yüklü. İndirmek için [buraya](https://releases.aspose.com/3d/java/) tıklayın.
- Eclipse veya IntelliJ IDEA gibi bir IDE.

## Paketleri İçe Aktar

İlk olarak, temel 3‑D sınıflarını ve yardımcı tipleri sağlayan ad alanlarını içe aktarın.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Temel Profili Başlat

Ekstrüde edilecek şekli oluşturun. Bu örnekte kenarları yumuşatmak için küçük bir yuvarlama yarıçapına sahip bir `RectangleShape` kullanıyoruz.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Adım 2: Bir Sahne Oluştur

`Scene` nesnesi, tüm 3‑D düğümler, ışıklar, kameralar ve materyaller için bir kapsayıcı görevi görür.

```java
Scene scene = new Scene();
```

## Adım 3: Düğümler Oluştur

Sahne köküne iki çocuk düğüm ekleyin—biri sol‑el ekstrüzyonu, diğeri sağ‑el ekstrüzyonu için. Sağ düğüm, iki nesnenin çakışmaması için çevrilir.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 4: Sol Düğümde Doğrusal Ekstrüzyon Gerçekleştir

Profili sol düğümde varsayılan Z‑eksen yönüyle ekstrude edin. Ayrıca tam 360° bir bükülme ekliyor ve daha pürüzsüz bir ağ için dilim sayısını artırıyoruz.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Adım 5: Sağ Düğümde Yön ile Doğrusal Ekstrüzyon Gerçekleştir

Burada **yön ayarlıyoruz**. `setDirection` metoduna özel bir `Vector3` geçirerek ekstrüzyonun (0.3, 0.2, 1) vektörünü takip etmesini sağlıyoruz; bu da eğimli bir şekil üretir.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Adım 6: 3D Sahneyi Kaydet

Son olarak, sahneyi Wavefront OBJ formatına dışa aktarın. Bu adım, **save obj file java** projelerini nasıl yapacağınızı gösterir ve sonucu herhangi bir 3‑D görüntüleyicide kolayca görüntülemenizi sağlar.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| OBJ dosyası boş görünüyor | Profil bir düğüme eklenmedi | `createChildNode` metodunun geçerli bir düğüm üzerinde çağrıldığından emin olun |
| Yön değişmemiş gibi görünüyor | `setDirection` ekstrüzyon zaten oluşturulmuşken çağrıldı | `LinearExtrusion` başlatıcısı içinde gösterildiği gibi yönü ayarlayın |
| Düşük çözünürlüklü ağ | `setSlices` değeri çok düşük | Dilim sayısını artırın (ör. 100 veya daha fazla) |

## Sonuç

Artık **doğrusal ekstrüzyonda yön nasıl ayarlanır**, bükülme ve dilim ayarlarının nasıl yapılır ve Aspose.3D for Java kullanarak **3d model obj** dosyalarının nasıl **export** edileceğini biliyorsunuz. Bu teknikler, geometri oluşturma üzerinde ince ayar yapmanızı sağlar ve 3‑D varlıkları daha büyük iş akışlarına entegre etmeyi kolaylaştırır.

## SSS

### S1: Aspose.3D’yi başka programlama dilleriyle kullanabilir miyim?

C1: Aspose.3D, .NET ve Java dahil olmak üzere çeşitli programlama dillerini destekler.

### S2: Aspose.3D için ücretsiz bir deneme mevcut mu?

C2: Evet, Aspose.3D özelliklerini ücretsiz deneme sürümüyle keşfedebilirsiniz: [burada](https://releases.aspose.com/).

### S3: Aspose.3D for Java için ayrıntılı belgeleri nereden bulabilirim?

C3: Kapsamlı dokümantasyon [burada](https://reference.aspose.com/3d/java/) mevcuttur.

### S4: Aspose.3D için destek nasıl alınır?

C4: Yardım ve sorularınız için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

### S5: Aspose.3D için geçici lisanslar mevcut mu?

C5: Evet, geçici bir lisans alabilirsiniz: [burada](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Son Güncelleme:** 2026-02-22  
**Test Edilen Versiyon:** Aspose.3D for Java (en son sürüm)  
**Yazar:** Aspose