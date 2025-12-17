---
date: 2025-12-13
description: Aspose 3D Java'yı kullanarak 3D düğümleri nasıl dönüştüreceğinizi öğrenin.
  Bu kılavuz, Euler açılarını nasıl kullanacağınızı, 3D dönüşüm eklemeyi ve Java'da
  yer değiştirmeyi nasıl ayarlayacağınızı gösterir.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Euler Açılarla 3D Düğümleri Dönüştür
url: /tr/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da Aspose.3D Kullanarak Euler Açılarla 3D Düğümleri Dönüştürme

## Giriş

Bu öğreticide **aspose 3d java**'yu kullanarak Euler açıları uygulayarak 3D düğümleri nasıl dönüştüreceğinizi keşfedeceksiniz. Kılavuzun sonunda döndürme 3d ekleyebilecek, java çevirisini ayarlayabilecek ve gerçek zamanlı verilere tepki veren dinamik sahneler oluşturabileceksiniz.

## Hızlı Yanıtlar
- **Java'da 3D dönüşümleri hangi kütüphane yönetir?** Aspose 3D for Java.  
- **Euler açılarıyla dönüşü ayarlayan yöntem hangisidir?** Düğümün dönüşümünde `setEulerAngles()`.  
- **Bir düğümü uzayda nasıl hareket ettiririm?** `Vector3` ile `setTranslation()` kullanın.  
- **Üretim için lisansa ihtiyacım var mı?** Evet, ticari bir Aspose 3D lisansı gereklidir.  
- **FBX olarak dışa aktarabilir miyim?** Kesinlikle – `scene.save(..., FileFormat.FBX7500ASCII)` doğrudan çalışır.

## Önkoşullar

Öğreticiye başlamadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

- Java programlama temelleri.  
- Makinenizde Java Development Kit (JDK) kurulu.  
- Aspose.3D kütüphanesi, bunu [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) adresinden edinebilirsiniz.

## Paketleri İçe Aktarma

Gerekli paketleri Java projenize içe aktararak başlayın. Aspose.3D kütüphanesinin sınıf yolunuza doğru şekilde eklendiğinden emin olun. Henüz indirmediyseniz, indirme bağlantısını [burada](https://releases.aspose.com/3d/java/) bulabilirsiniz.

```java
import com.aspose.threed.*;
```

## aspose 3d java – Euler Açılarla Çalışma

### Adım 1. Sahneyi ve Düğümü Başlatma

İlk olarak, dönüştürmek istediğiniz geometrinin tutulacağı bir sahne ve bir düğüm oluşturun.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Adım 2. Mesh Oluşturma ve Geometri Ayarlama

Sonra, basit bir mesh (bu örnekte bir küp) oluşturun ve düğüme ekleyin.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Bir Düğüm'e 3D Döndürme Ekleme

### Adım 3. Euler Açılar ve Çevirme Ayarlama

Şimdi Euler açılarıyla dönüşümü uyguluyor ve düğümü görünür bir konuma taşıyoruz.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Java Çevirme Ayarlama – Düğümü Konumlandırma

Yukarıdaki çevirme adımı, **set translation java**'yu pratikte gösterir: düğüm Z‑ekseni boyunca 20 birim kaydırılarak render sonrası görülebilir hâle getirilir.

## Adım 4. Düğümü Sahneye Ekleme

Dönüştürülmüş düğümü sahnenin kök düğümüne ekleyin.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Adım 5. 3D Sahneyi Kaydetme

Son olarak, sahneyi bir FBX dosyasına (veya desteklenen başka bir formata) dışa aktarın.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Makinenizdeki uygun yolu kullanarak `"Your Document Directory"` ifadesini değiştirmeniz gerektiğini unutmayın.

## Sonuç

Tebrikler! **aspose 3d java** ile Java’da Euler açıları kullanarak 3D düğümleri başarıyla dönüştürdünüz. Farklı açı ve çevirme değerleriyle denemeler yaparak dinamik ve etkileyici 3D sahneler oluşturabilirsiniz.

## Sık Sorulan Sorular

**S: Euler açıları ile quaternion dönüşümü arasındaki fark nedir?**  
**C:** Euler açıları sezgisel (pitch, yaw, roll) olsa da gimbal kilidi sorununa yol açabilir; quaternionlar bu sorunu ortadan kaldırır ve pürüzsüz interpolasyonlar için daha iyidir.

**S: Aynı düğümde birden fazla dönüşüm zincirleyebilir miyim?**  
**C:** Evet. `setEulerAngles`, `setTranslation` ve `setScale` metodlarını istediğiniz sırayla çağırabilirsiniz; kütüphane bunları tek bir dönüşüm matrisinde birleştirir.

**S: OBJ veya STL gibi diğer formatlara dışa aktarmak mümkün mü?**  
**C:** Kesinlikle. `scene.save` çağrısında `FileFormat.FBX7500ASCII` yerine `FileFormat.OBJ` veya `FileFormat.STL` kullanabilirsiniz.

**S: Aynı dönüşümü birden fazla düğüme aynı anda nasıl uygularım?**  
**C:** Bir üst düğüm oluşturun, dönüşümü bu üst düğüme uygulayın ve alt düğümleri ona ekleyin. Tüm alt düğümler dönüşümü miras alır.

**S: Kaydetme sonrası herhangi bir temizlik yöntemi çağırmam gerekiyor mu?**  
**C:** Java çöp toplayıcısı çoğu kaynağı otomatik yönetir, ancak büyük sahnelerle uzun süre çalışan uygulamalarda `scene.dispose()` metodunu açıkça çağırabilirsiniz.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}