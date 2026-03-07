---
date: 2026-03-07
description: Aspose.3D kullanarak Java 3D modelleri için UV koordinatları oluşturmayı
  ve UV üretmeyi öğrenin ve basit adım adım bir rehberde OBJ dosyasını Java'ya dışa
  aktarın.
linktitle: Generate UV Coordinates for Texture Mapping in Java 3D Models
second_title: Aspose.3D Java API
title: Java 3D Modelleri için UV Koordinatları Nasıl Oluşturulur
url: /tr/java/polygon/generate-uv-coordinates/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modelleri için UV Koordinatları Nasıl Oluşturulur

## Giriş

Java 3D modelinde doku haritalama için **uv koordinatlarını nasıl oluşturacağınızı** öğrenmek istiyorsanız, doğru yerdesiniz. Bu öğreticide Aspose.3D ile UV verilerini manuel olarak üretme, bir mesh’e ekleme ve son olarak **OBJ dosyasını Java**‑uyumlu geometri olarak dışa aktarma adımlarını adım adım göstereceğiz. Sonunda UV haritalamanın neden önemli olduğunu, programlı olarak nasıl üretileceğini ve standart bir OBJ görüntüleyicide sonucu nasıl doğrulayacağınızı anlayacaksınız.

## Hızlı Yanıtlar
- **UV haritalama nedir?** 2‑D doku koordinatlarını (U & V) 3‑D köşelere atama sürecidir.  
- **Java’da UV üretmenize yardımcı olan kütüphane hangisidir?** Aspose.3D for Java.  
- **Bunu denemek için lisansa ihtiyacım var mı?** Ücretsiz bir deneme sürümü mevcuttur; üretim için lisans gereklidir.  
- **Sonucu OBJ olarak dışa aktarabilir miyim?** Evet – `scene.save(..., FileFormat.WAVEFRONTOBJ)` kullanın.  
- **Ana adımlar nelerdir?** Bir sahne oluşturun, bir mesh oluşturun, UV üretin, ekleyin ve kaydedin.

## UV Haritalama Nedir ve Neden Gereklidir?

UV haritalama, bir 2‑D resmi (doku) bir 3‑D nesnenin etrafına sarmanıza olanak tanır. Uygun UV koordinatları olmadan dokular uzar, hizalanmaz veya tamamen kaybolur. UV’leri manuel olarak üretmek, dokuların nasıl projeleneceği üzerinde tam kontrol sağlar; bu, oyunlar, simülasyonlar ve görsel‑zengin Java uygulamaları için hayati öneme sahiptir.

## Ön Koşullar

Başlamadan önce şunların kurulu olduğundan emin olun:

- Temel Java programlama bilgisi.  
- Aspose.3D for Java – [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.  
- Aspose.3D JAR dosyalarının sınıf yolunda bulunduğu bir Java IDE (IntelliJ IDEA, Eclipse, VS Code vb.).

## Paketleri İçe Aktarma

Java projenizde gerekli Aspose.3D sınıflarını içe aktarın. Bu importlar sahne yönetimi, mesh manipülasyonu ve köşe öğesi işleme yeteneklerini sağlar.

```java
import com.aspose.threed.Box;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.PolygonModifier;
import com.aspose.threed.Scene;
import com.aspose.threed.VertexElement;
import com.aspose.threed.VertexElementType;
```

## Adım‑Adım Kılavuz

### Adım 1: Belge Dizini Yolunu Ayarlama

Oluşturulacak OBJ dosyasının kaydedileceği yeri tanımlayın.

```java
String MyDir = "Your Document Directory";
```

> **İpucu:** Göreli yol sürprizlerinden kaçınmak için mutlak yol ya da `System.getProperty("user.dir")` kullanın.

### Adım 2: Bir Sahne Oluşturma

`Scene`, tüm 3‑D nesnelerinin üst‑seviye konteyneridir.

```java
Scene scene = new Scene();
```

### Adım 3: Bir Mesh Oluşturma

Basit bir kutu mesh’i oluşturacağız ve doku koordinatları içermeyen bir mesh simüle etmek için yerleşik UV verilerini kasıtlı olarak kaldıracağız.

```java
Mesh mesh = (new Box()).toMesh();
mesh.getVertexElements().remove(mesh.getElement(VertexElementType.UV));
```

### Adım 4: UV Koordinatlarını Manuel Olarak Nasıl Üretirsiniz

Aspose.3D, herhangi bir mesh için temel bir düzlemsel UV düzeni oluşturan `PolygonModifier.generateUV` metodunu sunar.

```java
VertexElement uv = PolygonModifier.generateUV(mesh);
```

### Adım 5: UV Verilerini Mesh’e Bağlama

Şimdi oluşturulan UV öğesini mesh’e ekleyerek köşe verisinin bir parçası haline getirin.

```java
mesh.addElement(uv);
```

### Adım 6: Bir Node Oluşturma ve Mesh’i Sahneye Ekleme

`Node`, sahne grafiğinde bir nesne örneğini temsil eder. Mesh’i bir node’a eklemek, onun renderlanabilir olmasını sağlar.

```java
Node node = scene.getRootNode().createChildNode(mesh);
```

### Adım 7: OBJ Dosyasını Java’da Nasıl Dışa Aktarırsınız

Son olarak, yeni oluşturulan UV koordinatları dahil tüm sahneyi bir OBJ dosyasına yazın; bu dosya neredeyse tüm 3‑D araçlarda açılabilir.

```java
scene.save(MyDir + "test.obj", FileFormat.WAVEFRONTOBJ);
```

> **Beklenen Sonuç:** `test.obj` dosyasını Blender gibi bir görüntüleyicide açtığınızda, kutu varsayılan UV düzeniyle gösterilir ve uyguladığınız herhangi bir doku doğru şekilde haritalanır.

## Yaygın Sorunlar ve Çözümler

| Sorun | Sebep | Düzeltme |
|-------|--------|-----|
| **UV’ler görüntüleyicide eksik görünüyor** | Mesh hâlâ eski bir UV öğesi içeriyor. | Yeni UV’leri üretmeden önce orijinal UV’yi (`mesh.getVertexElements().remove(...)`) kaldırdığınızdan emin olun. |
| **Dosya bulunamadı hatası** | `MyDir` mevcut olmayan bir klasöre işaret ediyor. | Klasörü önceden oluşturun veya `new File(MyDir).mkdirs();` kullanın. |
| **Lisans istisnası** | Üretimde geçerli bir lisans olmadan çalıştırılıyor. | Aspose belgelerinde açıklandığı gibi geçici ya da kalıcı bir lisans uygulayın. |

## Sık Sorulan Sorular

### S1: Aspose.3D for Java’yı başka programlama dilleriyle kullanabilir miyim?

C1: Aspose.3D temel olarak Java için tasarlanmıştır, ancak Aspose .NET, C++ ve diğer diller için bağlamalar da sunar. Dil‑spesifik API’ler için resmi dokümantasyona bakın.

### S2: Aspose.3D için bir deneme sürümü mevcut mu?

C2: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) keşfedebilirsiniz.

### S3: Aspose.3D için destek nasıl alabilirim?

C3: Topluluk desteği ve diğer kullanıcılarla etkileşim için Aspose.3D forumuna [buradan](https://forum.aspose.com/c/3d/18) ulaşabilirsiniz.

### S4: Aspose.3D için kapsamlı dokümantasyonu nerede bulabilirim?

C4: Dokümantasyon [burada](https://reference.aspose.com/3d/java/) mevcuttur.

### S5: Aspose.3D için geçici bir lisans satın alabilir miyim?

C5: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

---

**Son Güncelleme:** 2026-03-07  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11 (yazım anındaki en güncel)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}