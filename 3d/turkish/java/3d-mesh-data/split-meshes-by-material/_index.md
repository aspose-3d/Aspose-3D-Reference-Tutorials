---
date: 2026-01-27
description: Aspose.3D ile Java’da malzemeye göre ağı verimli bir şekilde bölmeyi
  öğrenin. Bu kılavuz, malzemeye göre ağı bölerek çizim çağrılarını azaltmayı ve render
  performansını artırmayı gösterir.
linktitle: How to Split Mesh by Material in Java Using Aspose.3D
second_title: Aspose.3D Java API
title: Java'da Aspose.3D Kullanarak Malzemeye Göre Mesh'i Bölme
url: /tr/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java’da Aspose.3D Kullanarak Mesh’i Malzemeye Göre Bölme

## Giriş

Java’da 3D grafiklerle çalışıyorsanız, büyük mesh’lerin işlenmesinin özellikle tek bir mesh içinde birden fazla malzeme bulunduğunda performans darboğazına dönüşebileceğini çabucak fark edeceksiniz. **Mesh’i malzemeye göre bölmeyi** öğrenmek, her bir malzeme‑spesifik çokgen grubunu izole etmenizi sağlar; bu da daha hızlı render, daha kolay culling ve doku yönetiminde daha ayrıntılı kontrol anlamına gelir. Bu öğreticide, Aspose.3D kütüphanesini kullanarak **mesh’i malzemeye göre bölme** adımlarını, pratik açıklamaları, draw call sayısını azaltma ipuçlarını ve render performansını artırma tavsiyelerini adım adım göstereceğiz.

## Hızlı Yanıtlar
- **“Mesh’i malzemeye göre bölmek” ne anlama geliyor?** Tek bir mesh’i, aynı malzemeyi paylaşan çokgenleri içeren birden fazla alt‑mesh’e ayırır.
- **Neden Aspose.3D?** Düşük‑seviye dosya formatlarını soyutlayan, yüksek‑seviye, çapraz‑platform bir API sunar ve performansı korur.
- **Uygulama ne kadar sürer?** Yaklaşık 10–15 dakika kodlama ve test.
- **Lisans gerekli mi?** Ücretsiz deneme sürümü mevcuttur; üretim kullanımı için ticari lisans gerekir.
- **Hangi Java sürümü destekleniyor?** Java 8 ve üzeri.

## Mesh Bölme Nedir?

Mesh bölme, karmaşık bir 3D mesh’i daha küçük, yönetilebilir parçalara ayırma sürecidir. Bölme malzemeye dayalı olduğunda, ortaya çıkan her alt‑mesh yalnızca tek bir malzemeye referans veren çokgenleri içerir. Bu yaklaşım draw call sayısını azaltır, render performansını iyileştirir ve malzeme‑başına gölgelendirici uygulama gibi görevleri basitleştirir.

## Neden Mesh’i Malzemeye Göre Bölmeliyiz?

- **Performans:** Render motorları, malzeme başına draw call’ları toplu hâle getirebilir, GPU durum değişikliklerini azaltır.
- **Esneklik:** Her malzeme için farklı post‑işleme efektleri veya çarpışma mantığı uygulayabilirsiniz.
- **Bellek Yönetimi:** Daha küçük mesh’ler, özellikle mobil veya VR uygulamaları için, belleğe akışını ve çıkışını kolaylaştırır.
- **Azaltılmış Draw Call’lar:** Daha az durum değişikliği, GPU’nun çerçeveleri daha verimli işlemesini sağlar.
- **İyileştirilmiş Render Performansı:** Malzemelerin izole edilmesi, culling ve gölgelendirme sonuçlarını genellikle iyileştirir.

## Ön Koşullar

Kodlamaya başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Java programlama temelleri.
- Aspose.3D for Java kütüphanesi yüklü (indir: [Aspose web sitesi](https://releases.aspose.com/3d/java/)).
- Java geliştirme için yapılandırılmış bir IDE (IntelliJ IDEA, Eclipse veya VS Code gibi).

## Paketleri İçe Aktarma

İlk olarak, gerekli Aspose.3D sınıflarını ve ihtiyacınız olacak standart Java yardımcılarını içe aktarın:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Adım‑Adım KılavAşağıda, her adımın açıklamasını kod bloklarından önce vererek, tam olarak ne olduğunu anlamanızı sağlayacak kısa bir yürütme bulacaksınız.

### Adım 1: Bir Kutu Mesh’i Oluşturma

Basit bir geometrik primitive—bir kutu—ile başlıyoruz; böylece her yüzün (düzlemin) daha sonra kendi malzemesini almasını net bir şekilde görebiliriz.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Adım 2: Bir Material Element Oluşturma

`VertexElementMaterial`, her çokgen için malzeme indekslerini saklar. Mesh’e ekleyerek, her yüzün hangi malzemeyi kullandığını kontrol edebiliriz.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Adım 3: Farklı Malzeme İndekslerini Belirleme

Burada kutunun altı düzleminin her birine benzersiz bir malzeme indeksi atıyoruz. Dizi sırası, `Box` primitive’i tarafından oluşturulan çokgenlerin sırasıyla eşleşir.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Adım 4: Mesh’i Alt‑Mesh’lere Bölme

`PolygonModifier.splitMesh` metodunu `SplitMeshPolicy.CLONE_DATA` ile çağırmak, her farklı malzeme indeksi için yeni bir alt‑mesh oluşturur ve orijinal vertex verisini korur.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Adım 5: Malzeme İndekslerini Güncelle ve Tekrar Böl

Farklı bir bölme stratejisini göstermek için, ilk üç düzlemi malzeme 0, kalan üç düzlemi ise malzeme 1 altında gruplayıp, kullanılmayan vertex’leri ortadan kaldırmak amacıyla `COMPACT_DATA` politikasıyla bölüyoruz.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Adım 6: Başarıyı Doğrulama

Basit bir konsol mesajı, işlemin hatasız tamamlandığını size bildirir.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Draw Call’ları Azaltma ve Render Performansını Artırma

Her malzemeyi kendi mesh’i haline getirerek, grafik boru hattının her malzeme için tek bir draw call üretmesini sağlarsınız; bu da çokgen başına bir draw call yerine daha az draw call anlamına gelir. Bu azalma, özellikle düşük‑performanslı donanımlarda daha akıcı kare hızlarına dönüşür. Ayrıca, `COMPACT_DATA` politikası kullanılmayan vertex’leri kaldırarak bellek bant genişliğini daha da düşürür ve GPU’nun daha verimli render yapmasına yardımcı olur.

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|--------------|-------|
| **Alt‑mesh’ler yinelenen vertex içeriyor** | `CLONE_DATA` her alt‑mesh için tüm vertex verisini kopyalar. | Paylaşılan vertex’lerin tekilleştirilmesini istiyorsanız `COMPACT_DATA`’ya geçin. |
| **Yanlış malzeme ataması** | İndeks dizisi uzunluğu çokgen sayısıyla eşleşmiyor. | Çokgen sayısını (ör. bir kutunun 6 çokgeni vardır) doğrulayın ve eşleşen bir indeks dizisi sağlayın. |

## Sık Sorulan Sorular

**S: Aspose.3D diğer Java 3D kütüphaneleriyle uyumlu mu?**  
C: Evet, Aspose.3D, Java 3D veya jMonkeyEngine gibi kütüphanelerle birlikte çalışabilir; mesh’leri aralarında içe‑dışa aktarabilirsiniz.

**S: Bu teknik, yüzlerce malzemeye sahip karmaşık modellerde uygulanabilir mi?**  
C: Kesinlikle. Aynı API çağrıları, mesh karmaşıklığından bağımsız olarak çalışır; sadece indeks dizinizin malzeme düzenini doğru yansıtması gerekir.

**S: Tam Aspose.3D Java dokümantasyonunu nereden bulabilirim?**  
C: Ayrıntılı API referansları ve ek örnekler için resmi [Aspose.3D Java dokümantasyonu](https://reference.aspose.com/3d/java/) sayfasını ziyaret edin.

**S: Aspose.3D for Java için ücretsiz deneme sürümü var mı?**  
C: Evet, deneme sürümünü [Aspose Releases sayfasından](https://releases.aspose.com/) indirebilirsiniz.

**S: Sorun yaşarsam nasıl destek alabilirim?**  
C: Aspose topluluk forumu ([Aspose.3D forumu](https://forum.aspose.com/c/3d/18)) sorularınızı sorabileceğiniz ve Aspose ekibi ile diğer geliştiricilerden yardım alabileceğiniz harika bir yerdir.

---

**Son Güncelleme:** 2026-01-27  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}