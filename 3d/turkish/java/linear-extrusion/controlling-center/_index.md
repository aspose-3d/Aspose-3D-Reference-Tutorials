---
date: 2026-02-20
description: Aspose.3D ile lineer ekstrüzyonda merkezi kontrol etmeye yönelik bir
  Java 3D grafik öğreticisini öğrenin; yuvarlama yarıçapını nasıl ayarlayacağınızı
  ve Java'da OBJ dosyasını nasıl kaydedeceğinizi içeren.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D Grafik Öğreticisi – Doğrusal Ekstrüzyonda Merkez
url: /tr/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Grafik Öğreticisi – Doğrusal Ekstrüzyonda Merkez

## Giriş

Java'da 3D görselleştirmeler oluşturuyorsanız, ekstrüzyon tekniklerinde uzmanlaşmak çok önemlidir. Bu **java 3d graphics tutorial**, Aspose.3D for Java kullanarak doğrusal bir ekstrüzyonun merkezini kontrol etmenizi adım adım gösterir, böylece ekstra matematik yapmadan hassas ve simetrik modeller oluşturabilirsiniz. Bu rehberin sonunda `center` özelliğinin neden önemli olduğunu, **set rounding radius** nasıl ayarlanır ve **save OBJ file java**‑uyumlu çıktının nasıl kaydedilir öğreneceksiniz.

## Hızlı Yanıtlar
- **center özelliği ne işe yarar?** Ekstrüzyonun profilin orijini etrafında simetrik olup olmadığını belirler.  
- **Kod çalıştırmak için lisansa ihtiyacım var mı?** Test için geçici bir lisans yeterlidir; üretim için tam lisans gereklidir.  
- **Sonuç için hangi dosya formatı kullanılıyor?** Sahne Wavefront OBJ dosyası olarak kaydedilir.  
- **Dilimin sayısını değiştirebilir miyim?** Evet, `LinearExtrusion` nesnesinde `setSlices(int)` metodunu kullanın.  
- **Aspose.3D Java 8+ ile uyumlu mu?** Kesinlikle – tüm modern Java sürümlerini destekler.

## java 3d graphics tutorial nedir?

Bir **java 3d graphics tutorial**, Java kütüphanelerini kullanarak üç boyutlu nesneler oluşturma, manipüle etme ve render etme sürecini adım adım açıklar. Bu örnekte, 2‑D profilleri tam bir 3‑D mesh'e dönüştüren Aspose.3D’nin ekstrüzyon API’sine odaklanıyoruz.

## Aspose.3D for Java neden kullanılmalı?

- **High‑level API** – Düşük seviyeli mesh hesaplamaları yazmaya gerek yok.  
- **Cross‑format support** – OBJ, FBX, STL ve daha fazlasına dışa aktarım.  
- **Performance‑optimized** – Büyük sahneleri verimli bir şekilde işler.  
- **Rich documentation** – Aşağıdaki örnek gibi örnekler içerir.

## Ön Koşullar

Başlamadan önce, şunların kurulu olduğundan emin olun:

1. **Java Geliştirme Ortamı** – JDK 8 veya daha yeni bir sürüm yüklü.  
2. **Aspose.3D for Java** – Kütüphaneyi ve dokümantasyonu [buradan](https://reference.aspose.com/3d/java/) indirin.  
3. **Document Directory** – Makinenizde oluşturulacak bir klasör; buna **“Your Document Directory.”** diye atıfta bulunacağız.

## Paketleri İçe Aktarma

Java IDE'nizde, ihtiyacınız olan Aspose.3D sınıflarını içe aktarın. Bu, derleyicinin ekstrüzyon ve sahne oluşturma özelliklerine erişmesini sağlar.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım Adım Kılavuz

### Adım 1: Temel Profili Oluşturma

İlk olarak, ekstrüzyon yapılacak 2‑D şekli oluşturun. Burada bir dikdörtgen kullanıyoruz ve köşeleri yumuşatmak için **set rounding radius** değerini 0.3 olarak ayarlıyoruz.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Adım 2: 3D Sahne Oluşturma

`Scene` nesnesi, tüm 3‑D düğümler, ışıklar ve kameralar için bir kapsayıcı görevi görür.

```java
Scene scene = new Scene();
```

### Adım 3: Sol ve Sağ Düğümleri Ekleme

Merkezleme ile ve olmadan ekstrüzyonu karşılaştırabilmeniz için iki ayrı düğümü yan yana yerleştireceğiz.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Adım 4: Doğrusal Ekstrüzyon – Merkez Yok (Sol Düğüm)

Sol düğümde ekstrüzyonu oluşturun, merkezlemeyi devre dışı bırakın ve düşük poligon önizleme için mesh'i üç dilime sınırlayın.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Adım 5: Referans İçin Zemin Düzlemi Ekle (Sol Düğüm)

İnce bir kutu, görsel bir zemin görevi görerek ekstrüzyonun yönelimini görmenizi sağlar.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Adım 6: Doğrusal Ekstrüzyon – Merkezli (Sağ Düğüm)

Şimdi ekstrüzyonu tekrarlayın, bu sefer `center` özelliğini etkinleştirin. Geometri, profilin orijini etrafında simetrik olacaktır.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Adım 7: Referans İçin Zemin Düzlemi Ekle (Sağ Düğüm)

Sağ taraf için aynı zemin düzlemi, karşılaştırmayı netleştirir.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Adım 8: 3D Sahneyi Kaydet

Son olarak, tüm sahneyi bir Wavefront OBJ dosyasına dışa aktarın – çoğu 3‑D editörde kolayca kullanılabilen bir format.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Ekstrüzyon kaymış görünüyor** | `setCenter(false)` profilin köşesine sabitlenmiş kalmasına neden olur. | Simetrik sonuçlar için `setCenter(true)` kullanın. |
| **OBJ dosyası boş** | Çıktı dizini yolu hatalı veya yazma izinleri eksik. | `MyDir`'in mevcut bir klasöre işaret ettiğini ve uygulamanın yazma erişimine sahip olduğunu doğrulayın. |
| **Yuvarlatılmış köşeler keskin görünüyor** | Yuvarlatma yarıçapı, dikdörtgen boyutuna göre çok küçük. | Yarıçap değerini artırın (ör. `setRoundingRadius(0.5)`). |

## Sıkça Sorulan Sorular

### Q1: Aspose.3D for Java'ı ticari projelerde kullanabilir miyim?

A1: Evet, Aspose.3D for Java ticari kullanım için mevcuttur. Lisans detayları için [burayı](https://purchase.aspose.com/buy) ziyaret edin.

### Q2: Ücretsiz deneme mevcut mu?

A2: Evet, Aspose.3D for Java ücretsiz denemesini [buradan](https://releases.aspose.com/) inceleyebilirsiniz.

### Q3: Aspose.3D for Java için desteği nereden bulabilirim?

A3: Aspose.3D topluluk forumu, destek alabileceğiniz ve deneyimlerinizi paylaşabileceğiniz harika bir yerdir. Forumu [buradan](https://forum.aspose.com/c/3d/18) ziyaret edin.

### Q4: Test için geçici bir lisansa ihtiyacım var mı?

A4: Evet, test amaçlı geçici bir lisansa ihtiyacınız varsa, birini [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

### Q5: Dokümantasyonu nereden bulabilirim?

A5: Aspose.3D for Java dokümantasyonu [burada](https://reference.aspose.com/3d/java/) mevcuttur.

## Sonuç

Bu **java 3d graphics tutorial**'ı tamamlayarak, doğrusal bir ekstrüzyonun merkezini nasıl kontrol edeceğinizi, yuvarlatma yarıçapını nasıl ayarlayacağınızı ve Aspose.3D kullanarak **save OBJ file java** çıktısını nasıl kaydedeceğinizi öğrendiniz. Bu teknikler, mesh simetrisi üzerinde ince ayar kontrolü sağlar; bu da oyun varlıkları, CAD prototipleri ve bilimsel görselleştirmeler için hayati önemdedir. Farklı profiller, dilim sayıları ve dışa aktarma formatlarıyla denemeler yaparak 3‑D araç kutunuzu genişletebilirsiniz.

---

**Son Güncelleme:** 2026-02-20  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}