---
date: 2026-05-04
description: Java'da Aspose.3D ile malzemeye göre ağı verimli bir şekilde bölmeyi
  öğrenin. Bu rehber, malzemeye göre ağı bölerek çizim çağrılarını azaltmayı ve render
  performansını artırmayı gösterir.
keywords:
- how to split mesh
- reduce draw calls
- improve rendering performance
- split mesh by material
linktitle: Java'da Aspose.3D Kullanarak Mesh'i Malzemeye Göre Bölme
second_title: Aspose.3D Java API
title: Java'da Aspose.3D Kullanarak Malzemeye Göre Mesh'i Bölme
url: /tr/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da Aspose.3D Kullanarak Mesh'i Malzemeye Göre Bölme

## Giriş

Java'da 3D grafiklerle çalışıyorsanız, büyük mesh'lerin işlenmesinin özellikle tek bir mesh birden fazla malzeme içerdiğinde performans darboğazı olabileceğini çabucak fark edeceksiniz. **Malzemeye göre mesh'i bölmeyi öğrenmek**, her bir malzeme‑özel çokgen grubunu izole etmenizi sağlar, daha hızlı render, daha kolay culling ve doku yönetimi üzerinde daha ayrıntılı kontrol sunar. Bu öğreticide, Aspose.3D kütüphanesini kullanarak **malzemeye göre mesh'i bölme** adımlarını, pratik açıklamalar, draw call'ları azaltma ipuçları ve render performansını artırma tavsiyeleriyle birlikte adım adım göstereceğiz.

## Hızlı Cevaplar
- **“Malzemeye göre mesh'i bölme” ne anlama geliyor?** Tek bir mesh'i birden fazla alt‑mesh'e ayırır, her biri aynı malzemeyi paylaşan çokgenleri içerir.  
- **Neden Aspose.3D kullanılmalı?** Düşük seviyeli dosya formatlarını soyutlayan, yüksek seviyeli, çapraz platform API'si sunar ve performansı korur.  
- **Uygulama ne kadar sürer?** Yaklaşık 10–15 dakikalık kodlama ve test.  
- **Lisans gerekiyor mu?** Ücretsiz deneme sürümü mevcuttur; üretim kullanımı için ticari lisans gereklidir.  
- **Hangi Java sürümü destekleniyor?** Java 8 ve üzeri.

## Malzemeye Göre Mesh'i Bölme – Genel Bakış
Malzemeye göre bir mesh'i bölmek temelde iki adımlı bir süreçtir: önce her çokgene bir malzeme indeksi etiketlersiniz, ardından Aspose.3D'ye mesh'i bu indekslere göre ayırmasını söylersiniz. Sonuç, daha küçük mesh'lerin bir koleksiyonu olur; her biri tek bir draw call ile render edilebilir—hem masaüstü hem de mobil GPU'larda **draw call'ları azaltmak** ve **render performansını iyileştirmek** için harikadır.

## Mesh Bölme Nedir?
Mesh bölme, karmaşık bir 3D mesh'i daha küçük, yönetilebilir parçalara ayırma sürecidir. Bölme malzemeye dayalı olduğunda, ortaya çıkan her alt‑mesh yalnızca tek bir malzemeye referans veren çokgenleri içerir. Bu yaklaşım draw call'ları azaltır, render performansını artırır ve malzeme bazlı gölgelendiricilerin uygulanması gibi görevleri basitleştirir.

## Neden Mesh'i Malzemeye Göre Bölmeliyiz?
- **Performans:** Render motorları malzeme başına draw call'ları toplu hâle getirebilir, GPU durum değişikliklerini azaltır.  
- **Esneklik:** Her malzeme için farklı post‑işlem efektleri veya çarpışma mantığı uygulayabilirsiniz.  
- **Bellek Yönetimi:** Daha küçük mesh'ler belleğe aktarımı ve bellekten çıkarılması daha kolaydır; bu, mobil veya VR uygulamaları için kritiktir.  
- **Azaltılmış Draw Call'lar:** Daha az durum değişikliği, GPU'nun çerçeveleri daha verimli işlemesini sağlar.  
- **İyileştirilmiş Render Performansı:** Malzemeleri izole etmek genellikle daha iyi culling ve gölgelendirme sonuçları verir.

## Yaygın Kullanım Senaryoları

| Senaryo | Bölmenin Faydası |
|----------|----------------------|
| **Gerçek‑zamanlı strateji oyunları** | Her arazi tipi kendi malzemesine sahip olabilir, bu da motorun tüm çim parçalarını tek bir çağrıda çizmesini sağlar. |
| **Mimari görselleştirme** | Duvarlar, cam ve metal ayrı ayrı işlenerek farklı gölgelendirici efektleri uygulanabilir. |
| **Mobil AR uygulamaları** | Draw call'ları azaltmak, sınırlı donanımda 60 fps'yi korumaya yardımcı olur. |
| **VR deneyimleri** | Daha düşük GPU iş yükü gecikmeyi azaltır, kullanıcı konforunu artırır. |

## Önkoşullar

Koda geçmeden önce aşağıdakilere sahip olduğunuzdan emin olun:

- Java programlama temelleri.  
- Aspose.3D for Java kütüphanesi kurulu (indirme için [Aspose web sitesini](https://releases.aspose.com/3d/java/) ziyaret edin).  
- Java geliştirme için yapılandırılmış IntelliJ IDEA, Eclipse veya VS Code gibi bir IDE.

## Paketleri İçe Aktarma

İlk olarak, gerekli Aspose.3D sınıflarını ve ihtiyacınız olabilecek standart Java yardımcı sınıflarını içe aktarın:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Adım‑Adım Kılavuz

Aşağıda her adımın kısa bir açıklaması, kod bloklarından önceki açıklamalarla birlikte verilmiştir, böylece ne olduğunu tam olarak bilirsiniz.

### Adım 1: Bir Kutu Mesh'i Oluşturma

Basit bir geometrik primitive—bir kutu—ile başlıyoruz, böylece daha sonra her yüzün (düzlemin) kendi malzemesini nasıl alacağını net bir şekilde görebiliriz.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Adım 2: Bir Malzeme Elemanı Oluşturma

`VertexElementMaterial`, her çokgen için malzeme indekslerini depolar. Mesh'e ekleyerek, her yüzün hangi malzemeyi kullandığını kontrol edebiliriz.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Adım 3: Farklı Malzeme İndekslerini Belirleme

Burada kutunun altı düzlemi için benzersiz bir malzeme indeksi atıyoruz. Dizi sırası, `Box` primitive'ı tarafından oluşturulan çokgenlerin sırasıyla eşleşir.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Adım 4: Mesh'i Alt‑Mesh'lere Bölme

`PolygonModifier.splitMesh` metodunu `SplitMeshPolicy.CLONE_DATA` ile çağırmak, orijinal vertex verilerini korurken her farklı malzeme indeksi için yeni bir alt‑mesh oluşturur.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Adım 5: Malzeme İndekslerini Güncelle ve Tekrar Böl

Farklı bir bölme stratejisini göstermek için, ilk üç düzlemi malzeme 0 altında, kalan üç düzlemi malzeme 1 altında gruplayıp, kullanılmayan vertex'leri ortadan kaldırmak için `COMPACT_DATA` ile bölüyoruz.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Adım 6: Başarıyı Doğrulama

Basit bir konsol mesajı, işlemin hatasız tamamlandığını bildirir.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Draw Call'ları Azaltma ve Render Performansını İyileştirme

Her malzemeyi kendi mesh'i haline getirerek, grafik boru hattının her çokgen yerine malzeme başına tek bir draw call vermesini sağlarsınız. Bu draw call azaltımı, özellikle düşük‑seviye donanımlarda daha akıcı kare hızlarına dönüşür. Ayrıca, `COMPACT_DATA` politikası kullanılmayan vertex'leri kaldırarak bellek bant genişliğini daha da düşürür ve GPU'nun daha verimli render etmesine yardımcı olur.

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **Alt‑mesh'ler duplicate vertex içerir** | `CLONE_DATA` kullanmak, her alt‑mesh için tüm vertex verilerini kopyalar. | Paylaşılan vertex'lerin tekilleştirilmesini istediğinizde `COMPACT_DATA`'ya geçin. |
| **Yanlış malzeme ataması** | İndeks dizisi uzunluğu çokgen sayısıyla eşleşmiyor. | Çokgen sayısını doğrulayın (örneğin, bir kutunun 6 çokgeni vardır) ve eşleşen bir indeks dizisi sağlayın. |

## Sıkça Sorulan Sorular

**Q: Aspose.3D diğer Java 3D kütüphaneleriyle uyumlu mu?**  
A: Evet, Aspose.3D Java 3D veya jMonkeyEngine gibi kütüphanelerle birlikte çalışabilir, böylece mesh'leri aralarında içe/dışa aktarabilirsiniz.

**Q: Bu teknik yüzlerce malzemeye sahip karmaşık modellerde uygulanabilir mi?**  
A: Kesinlikle. Aynı API çağrıları mesh karmaşıklığından bağımsız çalışır; sadece indeks dizinizin malzeme düzenini doğru yansıttığından emin olun.

**Q: Tam Aspose.3D Java belgelerini nerede bulabilirim?**  
A: Ayrıntılı API referansları ve ek örnekler için resmi [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) sayfasını ziyaret edin.

**Q: Aspose.3D for Java için ücretsiz deneme sürümü mevcut mu?**  
A: Evet, [Aspose Releases page](https://releases.aspose.com/) üzerinden bir deneme sürümü indirebilirsiniz.

**Q: Sorun yaşarsam nasıl destek alabilirim?**  
A: Aspose topluluk forumu ([Aspose.3D forum](https://forum.aspose.com/c/3d/18)) sorular sormak ve Aspose ekibi ile diğer geliştiricilerden yardım almak için mükemmel bir yerdir.

## Sonuç

Artık Java'da Aspose.3D kullanarak **malzemeye göre mesh'i bölme** için eksiksiz, üretime hazır bir yönteme sahipsiniz. Bu tekniği uyguladığınızda daha az draw call, daha iyi bellek kullanımı ve çeşitli cihazlarda daha akıcı render elde edeceksiniz. Farklı `SplitMeshPolicy` seçenekleriyle denemeler yapmaktan veya ortaya çıkan alt‑mesh'leri kendi render boru hattınıza entegre etmekten çekinmeyin.

---

**Son Güncelleme:** 2026-05-04  
**Test Edilen Sürüm:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}