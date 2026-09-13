---
date: 2026-09-13
description: Java ve Aspose.3D kullanarak FBX'i dokularla dışa aktarmayı öğrenin.
  Bu öğreticide, bir mesh'e malzeme atamayı, dokuları gömmeyi ve FBX'i dokularla verimli
  bir şekilde kaydetmeyi gösteriyoruz.
keywords:
- export fbx with textures
- save fbx with texture
- embed texture into fbx
- how to embed texture fbx
- how to assign material mesh
lastmod: 2026-09-13
linktitle: Java'da Aspose.3D ile 3D Nesnelere Malzeme Uygulama
og_description: Java ve Aspose.3D kullanarak FBX'i dokularla dışa aktarın. Bu kılavuz,
  malzeme atamayı, dokuları gömmeyi ve birkaç dakika içinde taşınabilir bir FBX dosyası
  kaydetmeyi adım adım anlatır.
og_image_alt: Tutorial showing how to export FBX with textures using Aspose.3D Java
  API
og_title: Java kullanarak Aspose.3D ile FBX'i dokularla dışa aktar
schemas:
- author: Aspose
  dateModified: '2026-09-13'
  description: Learn how to export FBX with textures using Java and Aspose.3D. This
    tutorial shows you how to assign material to a mesh, embed textures, and save
    FBX with textures efficiently.
  headline: How to export FBX with textures in Java using Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes, Aspose.3D lets you assign different materials to separate mesh parts
      or sub‑nodes via the `MeshPart` API.
    question: Can I apply multiple materials to a single 3D object?
  - answer: FBX, STL, OBJ, 3DS, and several others. See the official [documentation](https://reference.aspose.com/3d/java/)
      for the full list.
    question: What file formats does Aspose.3D support for saving scenes?
  - answer: Yes, you can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for evaluation.
    question: Is a temporary license available for Aspose.3D for Java?
  - answer: The [Aspose.3D forum](https://forum.aspose.com/c/3d/18) is the best place
      for community help.
    question: Where can I find support for Aspose.3D?
  - answer: Absolutely—use the [download link](https://releases.aspose.com/3d/java/)
      to get the latest JAR files.
    question: Can I download the Aspose.3D library from a specific link?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export fbx
- Aspose.3D
- Java 3D
- texture embedding
- 3D modeling
title: Java kullanarak Aspose.3D ile FBX'i dokularla nasıl dışa aktarılır
url: /tr/java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java kullanarak Aspose.3D ile FBX'i dokularla dışa aktarma

## Giriş

Bu **Java 3D grafik öğreticisinde** bir dokuyu doğrudan basit bir 3‑D küp içine gömerek **FBX'i dokularla dışa aktarmayı** öğreneceksiniz. Malzeme ve dokuların uygulanması, düz bir ağı gerçekçi bir nesneye dönüştürür; bu nesne oyunlarda, ürün görselleştirmelerinde veya hızlı prototiplemede kullanılabilir. Kılavuzun sonunda, herhangi bir görüntüleyicide doğru şekilde açılan tam dokulu bir FBX dosyanız olacak ve **mesh'e malzeme atama**, **3D nesnelere malzeme uygulama** ve **FBX'i dokularla kaydetme** konularını anlayacaksınız.

## Java kullanarak FBX'i dokularla dışa aktarma

Sahnenizi yükleyin, bir Phong malzemesi oluşturun, difüz bir doku ekleyin, doku baytlarını gömün (isteğe bağlı) ve `scene.save("cube.fbx", SaveFormat.FBX)` çağrısını yapın. Bu adım‑adım akış, görüntü verisini içinde taşıyan bir FBX 7.4 ASCII dosyası üretir ve dosya farklı makineler veya platformlar arasında taşındığında ortaya çıkan eksik doku hatalarını ortadan kaldırır.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Bir küp üzerine difüz doku ile Phong malzemesi uygulamak.  
- **Hangi kütüphane?** Java için Aspose.3D (ücretsiz deneme mevcut).  
- **Ne kadar sürer?** Çalışan bir örnek için yaklaşık 10‑15 dakika.  
- **Lisans gerekli mi?** Değerlendirme dışı derlemeler için geçici bir lisans gereklidir.  
- **Hangi dosya formatı üretilir?** FBX 7.4 ASCII (çoğu 3‑D aracına uyumlu).  

## Neden Aspose.3D ile FBX'e doku gömülür?

Aspose.3D **30+ giriş ve çıkış formatını** destekler – FBX, OBJ, STL ve 3DS dahil – ve modeli tamamen belleğe yüklemeden **500+ poligon** işleyebilir. Nesne‑yönelimli API'si, **malzeme mesh** özelliklerini tek bir akıcı çağrıyla atamanıza ve dokuları gömmenize olanak tanır; bu da manuel FBX düzenlemesine kıyasla **%100** eksik doku riskini azaltır.

## Önkoşullar

Başlamadan önce şunların yüklü olduğundan emin olun:

- Java Development Kit (JDK 8 ve üzeri) yüklü.  
- Projenizin classpath'ine en son Aspose.3D for Java JAR'ı eklenmiş.  
- Java sözdizimi ve nesne‑yönelimli programlama hakkında temel bir anlayış.  
- Diskte hazır bir doku dosyası (ör. `surface.dds` veya `embedded-texture.png`).  

## Paketleri içe aktar

Aşağıdaki importlar, sahne oluşturma ve malzeme işleme için gereken temel Aspose.3D sınıflarını getirir.  
```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Adım 1: Sahne nesnesini başlat

`Scene` sınıfı, düğümler, ışıklar, kameralar ve diğer kaynakları tutan bir 3‑D sahneyi temsil eder.  
```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: Küp düğüm nesnesini başlat

`Node`, geometri, dönüşüm ve alt düğümler içerebilen bir sahne‑grafik öğesidir.  
```java
// Initialize cube node object
Node cubeNode = new Node("cube");
```

## Adım 3: Poligon oluşturucu ile mesh oluştur

`Mesh`, bir 3‑D nesnenin şeklini tanımlayan vertex, index ve attribute verilerini depolar.  
```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = new Mesh();
```

## Adım 4: Düğümü mesh'e bağla

Oluşturulan `Mesh`i düğüme atayarak geometrinin sahne grafiğinin bir parçası olmasını sağlayın.  
```java
// Point node to the mesh
cubeNode.setEntity(mesh);
```

## Adım 5: Küpü sahneye ekle

`scene.addNode` ile küp düğümünü sahne hiyerarşisine ekleyin.  
```java
// Add cube to the scene
scene.getRootNode().addChildNode(cubeNode);
```

## Adım 6: PhongMaterial nesnesini başlat

`PhongMaterial`, Phong gölgelendirme modelini kullanan bir malzeme tanımlar; difüz, speküler ve diğer özellikleri ayarlamanıza izin verir.  
```java
// Initialize PhongMaterial object
PhongMaterial mat = new PhongMaterial();
```

## Adım 7: Doku nesnesini başlat

`Texture`, bir malzemenin yüzeyine uygulanabilen bir görüntüyü temsil eder.  
```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## Adım 8: Doku için yerel dosya yolunu ayarla

`setFileName`, dokunun dış dosya yolunu belirtir.  
```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## Adım 9: Gömülü doku için yerel dosya yolunu ayarla

`setEmbeddedFileName`, doku gömüldüğünde FBX içinde saklanacak yolu tanımlar.  
```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## Adım 10: Malzemenin dokusunu ayarla

`setTexture`, daha önce oluşturulan dokuyu malzemenin difüz kanalına bağlar.  
```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Adım 11: Ham içerik verisini FBX'e göm (isteğe bağlı)

`setEmbeddedContent`, ham görüntü baytlarını doğrudan FBX dosyasına gömmenizi sağlar.  
```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Adım 12: Speküler rengi ayarla

`setSpecularColor`, malzemenin speküler vurgularının rengini tanımlar.  
```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Adım 13: Parlaklığı ayarla

`setBrightness`, malzemenin genel parlaklığını ayarlar.  
```java
// Set brightness
mat.setShininess(100);
```

## Adım 14: Küp nesnesinin malzeme özelliğini ayarla

`node.setMaterial`, yapılandırılmış malzemeyi küp düğümüne atar.  
```java
// Set material property of the cube object
cubeNode.setMaterial(mat);
```

## Adım 15: 3D sahneyi kaydet

`scene.save`, gömülü dokular dahil tüm sahneyi bir FBX dosyasına yazar.  
```java
// Set the file name
MyDir = MyDir + "MaterialToCube.fbx";
// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Bunun önemi

Doku gömmek, FBX modeliyle birlikte ayrı görüntü dosyaları gönderme ihtiyacını ortadan kaldırır; bu, tasarımcılar, motorlar ve CDN'ler arasında hareket eden pipeline'larda sıkça görülen kırık varlık sorununu çözer. Ayrıca editörde gördüğünüz görselin son kullanıcılar tarafından da aynı şekilde görülmesini garanti eder.

## Yaygın kullanım senaryoları

- **Oyun varlık hatları** – Unity veya Unreal'a eksik doku endişesi olmadan tek bir FBX dosyası gönder.  
- **Ürün görselleştirme** – Tam dokulu modeli müşterilere, orijinal doku klasörü olmadan gönder.  
- **Hızlı prototipleme** – Konsept doğrulaması için hızlıca dokulu yer tutucular oluştur.  

## Yaygın sorunlar ve çözümler

| Sorun | Neden | Çözüm |
|-------|--------|-----|
| **Texture not visible** | Yanlış dosya yolu veya desteklenmeyen doku formatı. | `MyDir`'in doğru klasöre işaret ettiğini doğrulayın ve `.dds` veya `.png` gibi desteklenen bir format kullanın. |
| **FBX file fails to load** | Gömülü doku verisi eksik. | Dokuyu doğrudan FBX'e gömmek için isteğe bağlı bloğu (Adım 11) kullanın. |
| **Material appears black** | Speküler veya difüz değerler ayarlanmamış. | Kaydetmeden önce `setSpecularColor` ve `setTexture` çağrılarının yapıldığından emin olun. |

## Sıkça Sorulan Sorular

**S: Tek bir 3D nesnesine birden fazla malzeme uygulayabilir miyim?**  
C: Evet, Aspose.3D `MeshPart` API'si aracılığıyla farklı mesh bölümlerine veya alt‑düğümlere ayrı malzemeler atamanıza izin verir.

**S: Aspose.3D sahneleri kaydetmek için hangi dosya formatlarını destekliyor?**  
C: FBX, STL, OBJ, 3DS ve birkaç diğer format. Tam liste için resmi [documentation](https://reference.aspose.com/3d/java/) sayfasına bakın.

**S: Java için Aspose.3D geçici lisans sunuyor mu?**  
C: Evet, değerlendirme için bir [temporary license](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

**S: Aspose.3D için destek nereden bulunur?**  
C: Topluluk yardımı için en iyi yer [Aspose.3D forum](https://forum.aspose.com/c/3d/18) dur.

**S: Aspose.3D kütüphanesini belirli bir bağlantıdan indirebilir miyim?**  
C: Kesinlikle—en son JAR dosyalarını almak için [download link](https://releases.aspose.com/3d/java/) kullanın.

**S: Sahneyi FBX olarak dışa aktardıktan sonra eksik doku sorunu nasıl çözülür?**  
C: Dokunun ya gömülü olduğundan (Adım 11) emin olun ya da `setFileName` içinde kullanılan göreli yolun FBX dosyasıyla birlikte taşınacak bir konuma işaret ettiğini kontrol edin.

**S: Aspose.3D, malzeme mesh'ini bireysel yüzlere atamama izin veriyor mu?**  
C: Evet, birden fazla `Material` örneği oluşturup bunları `MeshPart` API'si ile belirli mesh parçalarına atayabilirsiniz.

## Sonuç

Artık Aspose.3D kullanarak Java uygulamasında **FBX'i dokularla dışa aktarmayı**, **malzeme mesh** özelliklerini **atanmayı** ve yaygın “eksik doku” sorunundan kaçınmayı biliyorsunuz. Farklı doku formatlarıyla deney yapın, speküler ayarlarını ince ayarlayın veya daha karmaşık modeller için birden fazla malzeme birleştirin. Hazır olduğunuzda, iş akışınızı genişletmek için OBJ veya STL gibi diğer dışa aktarma seçeneklerini keşfedin.

---

**Last Updated:** 2026-09-13  
**Tested With:** Aspose.3D for Java latest release  
**Author:** Aspose

## İlgili Eğitimler

- [Create an FBX File with Aspose.3D for Java – 3D Graphics Tutorial](/3d/java/load-and-save/create-empty-3d-document/)
- [Create Child Nodes and Export FBX in Java with Aspose.3D](/3d/java/geometry/build-node-hierarchies/)
- [Save 3D Scenes in Java with Aspose.3D – Convert 3D Files Efficiently](/3d/java/load-and-save/save-3d-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}