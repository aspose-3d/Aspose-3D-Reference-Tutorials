---
title: Aspose.3D'yi kullanarak Java'da Euler Açıları ile 3D Düğümleri dönüştürün
linktitle: Aspose.3D'yi kullanarak Java'da Euler Açıları ile 3D Düğümleri dönüştürün
second_title: Aspose.3D Java API'si
description: Aspose.3D ile Java'daki 3D dönüşüm dünyasını keşfedin. 3B düğümlerinize dinamik Euler açıları eklemek için adım adım kılavuzumuzu izleyin.
type: docs
weight: 19
url: /tr/java/geometry/transform-3d-nodes-with-euler-angles/
---
## giriiş

Aspose.3D kullanarak Java'da 3D düğümleri Euler açılarıyla dönüştürmeye yönelik bu adım adım eğitime hoş geldiniz. Bu kılavuzda, dinamik konumlandırma ve yönlendirme elde etmek için Euler açılarını kullanarak bir 3B düğüme dönüşümler ekleme sürecini derinlemesine inceleyeceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Java programlamanın temel bilgisi.
- Makinenizde Java Geliştirme Kiti (JDK) yüklü.
-  Aspose.3D kütüphanesinden edinebileceğiniz[Aspose.3D Java Belgeleri](https://reference.aspose.com/3d/java/).

## Paketleri İçe Aktar

 Gerekli paketleri Java projenize aktararak başlayın. Aspose.3D kütüphanesinin sınıf yolunuza doğru şekilde eklendiğinden emin olun. Henüz indirmediyseniz indirme bağlantısını bulabilirsiniz.[Burada](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## 1. Adım. Sahneyi ve Düğümü Başlatın

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Sahne nesnesini başlat
Scene scene = new Scene();

// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("cube");
```

## Adım 2. Mesh Oluşturun ve Geometriyi Ayarlayın

```java
// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Düğümü Mesh geometrisine yönlendirin
cubeNode.setEntity(mesh);
```

## Adım 3. Euler Açılarını ve Çeviriyi Ayarlayın

```java
// Euler açıları
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Çeviriyi ayarla
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Adım 4. Sahneye Düğüm Ekle

```java
// Sahneye küp ekle
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Adım 5. 3D Sahneyi Kaydet

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//3B sahneyi desteklenen dosya formatlarında kaydedin
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

"Belge Dizininiz"i makinenizdeki uygun yolla değiştirdiğinizden emin olun.

## Çözüm

Tebrikler! Aspose.3D ile Java'da Euler açılarını kullanarak 3 boyutlu düğümleri başarıyla dönüştürdünüz. Dinamik ve ilgi çekici 3D sahneler oluşturmak için farklı açıları ve çevirileri deneyin.

## SSS'ler

### S1: Aspose.3D for Java'yı ticari projelerde kullanabilir miyim?

 A1: Evet, yapabilirsin. Ziyaret edin[satın alma sayfası](https://purchase.aspose.com/buy) lisans ayrıntıları için.

### S2: Aspose.3D desteğini nerede bulabilirim?

 A2:[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) yardım aramanın ve toplulukla bağlantı kurmanın yeridir.

### S3: Ücretsiz deneme sürümü mevcut mu?

 A3: Evet, keşfedebilirsiniz[ücretsiz deneme](https://releases.aspose.com/) Aspose.3D'nin yeteneklerini deneyimlemek için.

### S4: Geçici lisansı nasıl alabilirim?

 Cevap4: Geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Belgeleri nerede bulabilirim?

 A5:[dokümantasyon](https://reference.aspose.com/3d/java/) Aspose.3D for Java kullanımına ilişkin kapsamlı rehberlik sağlar.