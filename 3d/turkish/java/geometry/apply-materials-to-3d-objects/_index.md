---
date: 2025-12-08
description: Aspose.3D kullanarak Java'da doku eklemeyi öğrenebileceğiniz bir Java
  3D grafik öğreticisi. Java'da 3D nesnelere hızlıca gerçekçi malzemeler uygulayın.
linktitle: Apply Materials to 3D Objects in Java with Aspose.3D
second_title: Aspose.3D Java API
title: java 3d grafik öğreticisi – Aspose.3D ile Java'da 3D nesnelere malzeme uygulama
url: /tr/java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D ile Java'da 3D Nesnelere Malzeme Uygulama

## Giriş

Bu **java 3d graphics tutorial**'da, Aspose.3D Java API'sını kullanarak basit bir 3‑D küp'e **java dokusu eklemeyi** göstereceğiz. Malzeme ve dokuların uygulanması, düz bir ağı gerçekçi bir nesneye dönüştüren temel adımdır; bu nesneyi oyunlarda, görselleştirmelerde veya ürün demolarında kullanabilirsiniz. Rehberin sonunda, herhangi bir 3‑D görüntüleyicide açabileceğiniz tamamen dokulanmış bir FBX dosyanız olacak.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Bir küpe difüz doku içeren Phong malzemesi uygulamak.  
- **Hangi kütüphane?** Aspose.3D for Java (ücretsiz deneme mevcut).  
- **Ne kadar sürer?** Çalışan bir örnek için yaklaşık 10‑15 dakika.  
- **Lisans gerekiyor mu?** Değerlendirme dışı derlemeler için geçici bir lisans gereklidir.  
- **Hangi dosya formatı üretilir?** FBX 7.4 ASCII (çoğu 3‑D aracına uyumlu).

## java 3d graphics tutorial nedir?

Bir **java 3d graphics tutorial**, Java tabanlı kütüphaneler kullanarak 3‑D içerik oluşturma, manipülasyon ve dışa aktarma sürecini adım adım gösterir. Bu örnekte, malzeme işleme—renk, doku ve gölgelendirme özelliklerini geometrik varlıklara atama—odak noktamızdır.

## Neden Aspose.3D ile texture java ekleyelim?

Aspose.3D, dosya formatlarının düşük seviyeli detaylarını soyutlayan temiz, nesne‑yönelimli bir API sunar. FBX, STL, OBJ vb. geniş bir format yelpazesini destekler ve dokuları doğrudan dosyaya gömmenize olanak tanır; bu, tek ve taşınabilir bir varlık istediğinizde mükemmeldir.

## Önkoşullar

- Java Development Kit (JDK 8 veya üzeri) yüklü.  
- En son Aspose.3D for Java JAR'ı projenizin sınıf yoluna eklenmiş.  
- Java sözdizimi ve nesne‑yönelimli programlamaya temel bir anlayış.

## Paketleri İçe Aktarma

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Adım 1: Scene Nesnesini Başlatma

```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: Cube Node Nesnesini Başlatma

```java
// Initialize cube node object
Node cubeNode = new Node("cube");
```

## Adım 3: Polygon Builder ile Mesh Oluşturma

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Adım 4: Node'u Mesh'e Bağlama

```java
// Point node to the mesh
cubeNode.setEntity(mesh);
```

## Adım 5: Küpü Scene'e Ekleme

```java
// Add cube to the scene
scene.getRootNode().addChildNode(cubeNode);
```

## Adım 6: PhongMaterial Nesnesini Başlatma

```java
// Initialize PhongMaterial object
PhongMaterial mat = new PhongMaterial();
```

## Adım 7: Texture Nesnesini Başlatma

```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## Adım 8: Texture için Yerel Dosya Yolunu Ayarlama

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## Adım 9: Gömülü Texture için Yerel Dosya Yolunu Ayarlama

```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## Adım 10: Malzemenin Texture'ını Ayarlama

```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Adım 11: Raw İçerik Verisini FBX'e Gömme (İsteğe Bağlı)

```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Adım 12: Specular Rengi Ayarlama

```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Adım 13: Parlaklığı Ayarlama

```java
// Set brightness
mat.setShininess(100);
```

## Adım 14: Küp Nesnesinin Malzeme Özelliğini Ayarlama

```java
// Set material property of the cube object
cubeNode.setMaterial(mat);
```

## Adım 15: 3D Scene'i Kaydetme

```java
// Set the file name
MyDir = MyDir + "MaterialToCube.fbx";
// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Yaygın Sorunlar ve Çözümleri

| Sorun | Sebep | Çözüm |
|-------|--------|-----|
| **Texture görünmüyor** | Yanlış dosya yolu veya desteklenmeyen doku formatı. | `MyDir`'in doğru klasöre işaret ettiğini doğrulayın ve `.dds` veya `.png` gibi desteklenen bir format kullanın. |
| **FBX dosyası yüklenemiyor** | Gömülü doku verisi eksik. | İsteğe bağlı bloğu (Adım 11) kullanarak doku baytlarını doğrudan FBX'e gömün. |
| **Malzeme siyah görünüyor** | Specular veya diffuse değerleri ayarlanmamış. | `setSpecularColor` ve `setTexture`'ın kaydetmeden önce çağrıldığından emin olun. |

## Sıkça Sorulan Sorular

**Soru: Tek bir 3D nesneye birden fazla malzeme uygulayabilir miyim?**  
Cevap: Evet, Aspose.3D farklı malzemeleri ayrı mesh parçalarına veya alt‑node'lara atamanıza izin verir.

**Soru: Aspose.3D sahneleri kaydederken hangi dosya formatlarını destekler?**  
Cevap: FBX, STL, OBJ, 3DS ve birkaç diğeri. Tam liste için resmi [documentation](https://reference.aspose.com/3d/java/) sayfasına bakın.

**Soru: Aspose.3D for Java için geçici bir lisans mevcut mu?**  
Cevap: Evet, değerlendirme için bir [temporary license](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

**Soru: Aspose.3D için desteği nereden bulabilirim?**  
Cevap: [Aspose.3D forum](https://forum.aspose.com/c/3d/18) topluluk yardımı için en iyi yerdir.

**Soru: Aspose.3D kütüphanesini belirli bir bağlantıdan indirebilir miyim?**  
Cevap: Kesinlikle—en son JAR dosyalarını almak için [download link](https://releases.aspose.com/3d/java/) kullanın.

---

**Son Güncelleme:** 2025-12-08  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}