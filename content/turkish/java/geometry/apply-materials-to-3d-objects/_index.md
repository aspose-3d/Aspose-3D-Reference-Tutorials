---
title: Aspose.3D ile Malzemeleri Java'daki 3D Nesnelere Uygulayın
linktitle: Aspose.3D ile Malzemeleri Java'daki 3D Nesnelere Uygulayın
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java ile 3D grafik dünyasını keşfedin. Malzemeleri 3B nesnelere sorunsuz bir şekilde nasıl uygulayacağınızı öğrenin. Gerçekçi görsellerle projelerinizi geliştirin.
type: docs
weight: 14
url: /tr/java/geometry/apply-materials-to-3d-objects/
---
## giriiş

3D grafiklerin dinamik dünyasında Aspose.3D for Java, projelerinize hayat verecek güçlü bir araç olarak öne çıkıyor. 3B nesnelere malzeme eklemek görsel çekiciliği artırarak onları daha gerçekçi hale getirir. Bu eğitimde, Aspose.3D for Java kullanarak malzemeleri 3 boyutlu bir küpe uygulama sürecinde size yol göstereceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Sisteminizde Java Geliştirme Kiti (JDK) yüklü.
- Aspose.3D for Java kütüphanesi indirildi ve projenize eklendi.
- Temel Java programlama kavramlarına aşinalık.

## Paketleri İçe Aktar

Başlamak için gerekli paketleri Java projenize aktarın. Kodunuzun başına aşağıdaki satırları ekleyin:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Adım 1: Sahne Nesnesini Başlatın

```java
// Sahne nesnesini başlat
Scene scene = new Scene();
```

## Adım 2: Küp Düğümü Nesnesini Başlatın

```java
// Küp düğümü nesnesini başlat
Node cubeNode = new Node("cube");
```

## Adım 3: Polygon Builder'ı kullanarak Mesh Oluşturun

```java
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Adım 4: Düğümü Ağa Yönlendirin

```java
// Düğümü ağa yönlendirin
cubeNode.setEntity(mesh);
```

## Adım 5: Sahneye Küp Ekleyin

```java
// Sahneye küp ekle
scene.getRootNode().addChildNode(cubeNode);
```

## Adım 6: PhongMaterial Nesnesini Başlatın

```java
// PhongMaterial nesnesini başlat
PhongMaterial mat = new PhongMaterial();
```

## Adım 7: Doku Nesnesini Başlatın

```java
// Doku nesnesini başlat
Texture diffuse = new Texture();
```

## Adım 8: Doku için Yerel Dosya Yolunu Ayarlayın

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
```

## Adım 9: Gömülü Doku için Yerel Dosya Yolunu Ayarlayın

```java
// Gömülü doku için yerel dosya yolunu ayarlayın
diffuse.setFileName(MyDir + "surface.dds");
```

## Adım 10: Malzemenin Dokusunu Ayarlayın

```java
// Malzemenin dokusunu ayarla
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Adım 11: Ham İçerik Verilerini FBX'e Gömme (İsteğe Bağlı)

```java
// Gömülü doku için dosya adını ayarlayın
diffuse.setFileName("embedded-texture.png");
// İkili içeriği ayarla
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Adım 12: Aynasal Rengi Ayarlayın

```java
// Aynasal rengi ayarla
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Adım 13: Parlaklığı Ayarlayın

```java
// Parlaklığı ayarla
mat.setShininess(100);
```

## Adım 14: Küp Nesnesinin Malzeme Özelliğini Ayarlayın

```java
// Küp nesnesinin malzeme özelliğini ayarlayın
cubeNode.setMaterial(mat);
```

## Adım 15: 3D Sahneyi Kaydet

```java
// Dosya adını ayarlayın
MyDir = MyDir + "MaterialToCube.fbx";
// 3B sahneyi desteklenen dosya formatlarında kaydedin
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak malzemeleri 3 boyutlu bir küpe başarıyla uyguladınız. Bu basit ama güçlü teknik, 3D projelerinizi yeni boyutlara taşıyarak gerçekçi ve görsel olarak büyüleyici bir deneyim sağlayabilir.

## SSS'ler

### S1: Tek bir 3B nesneye birden fazla malzeme uygulayabilir miyim?

Cevap1: Evet, Aspose.3D, gelişmiş kişiselleştirme için bir 3D nesnenin farklı bölümlerine birden fazla malzeme uygulamanıza olanak tanır.

### S2: Aspose.3D sahneleri kaydetmek için hangi dosya formatlarını destekliyor?

 Cevap2: Aspose.3D, FBX, STL ve 3DS dahil olmak üzere çeşitli dosya formatlarını destekler. Bakın[dokümantasyon](https://reference.aspose.com/3d/java/) tam liste için.

### S3: Aspose.3D for Java için geçici bir lisans mevcut mu?

 A3: Evet, alabilirsiniz[geçici lisans](https://purchase.aspose.com/temporary-license/) değerlendirme amaçlı.

### S4: Aspose.3D desteğini nerede bulabilirim?

 A4: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.

### S5: Aspose.3D kütüphanesini belirli bir bağlantıdan indirebilir miyim?

 A5: Evet, kullanın[İndirme: {link](https://releases.aspose.com/3d/java/) Aspose.3D for Java'nın en son sürümüne erişmek için.