---
date: 2025-12-21
description: Aspose.3D SaveOptions kullanarak Java’da 3D dosya kaydetmeyi öğrenin
  – performansı optimize edin, güzel‑yazdırmayı etkinleştirin, HTML5 çıktısını özelleştirin
  ve daha fazlası.
linktitle: Save 3D File Java – Optimize 3D Saving with Aspose.3D SaveOptions
second_title: Aspose.3D Java API
title: 3D Dosyasını Java ile Kaydet – Aspose.3D SaveOptions ile 3D Kaydetmeyi Optimize
  Edin
url: /tr/java/load-and-save/optimize-3d-file-saving/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Dosyayı Java ile Kaydet – Aspose.3D SaveOptions ile 3D Kaydetmeyi Optimize Edin

## Giriş

**save 3d file java** projelerini hızlı ve verimli bir şekilde kaydetmeniz gerekiyorsa, Aspose.3D for Java size çıktıyı ince ayar yapmanızı sağlayan güçlü bir seçenek seti sunar. Bu öğreticide en faydalı `SaveOptions` ayarlarını inceleyecek, performansı nasıl artıracağınızı gösterecek ve GLTF dosyalarını güzel biçimde yazdırma ya da kendine özgü HTML5 görüntüleyiciler oluşturma gibi gerçek dünya senaryolarını örnekleyeceğiz.

## Hızlı Yanıtlar
- **Kaydetme için temel sınıf nedir?** `Scene.save()` ve belirli bir `*SaveOptions` alt sınıfı birlikte kullanılır.  
- **Hangi seçenek GLTF dosyalarını insan tarafından okunabilir hâle getirir?** `GltfSaveOptions.setPrettyPrint(true)`.  
- **GLTF dışa aktarımında varlıkları gömmek mümkün mü?** Evet – `GltfSaveOptions.setEmbedAssets(true)` kullanın.  
- **HTML5 dışa aktarımında UI’yı nasıl kapatırım?** `Html5SaveOptions.setShowUI(false)` ayarlayın.  
- **Üretim ortamı için lisansa ihtiyacım var mı?** Değerlendirme dışı kullanım için ticari bir lisans gereklidir.

## Önkoşullar

Öğreticiye başlamadan önce aşağıdaki önkoşulların sağlandığından emin olun:

- Aspose.3D for Java: Aspose.3D kütüphanesinin Java projenize entegre edildiğinden emin olun. Kütüphaneyi [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.

- Java Geliştirme Ortamı: Makinenizde çalışan bir Java geliştirme ortamı kurulu olsun.

- Belge Dizini: 3D dosyalarınızı kaydetmek istediğiniz bir dizin oluşturun ve yolunu daha sonra kullanmak üzere not edin.

## Paketleri İçe Aktarma

Java projenizde Aspose.3D ile çalışmak için gerekli paketleri içe aktarın. Bu, `Scene` sınıfı ve çeşitli `SaveOptions` sınıflarını içerir. Aşağıda temel bir örnek yer almaktadır:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Aspose.3D SaveOptions Kullanarak Java’da 3D Dosya Nasıl Kaydedilir

Aşağıda en yaygın `SaveOptions` yapılandırmalarını adım adım inceleyeceğiz. Her kod parçacığının ardından ayarın **neden** önemli olduğunu açıklayan kısa bir not bulunur.

### Adım 1: GLTF SaveOption’da Pretty Print

`prettyPrintInGltfSaveOption` yöntemi, insan tarafından okunabilir JSON içeriğiyle girintili bir GLTF dosyası oluşturmanızı sağlar.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initialize 3D scene
    Scene scene = new Scene(new Sphere());
    
    // Initialize GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Enable pretty print for better readability
    opt.setPrettyPrint(true);
    
    // Save 3D Scene
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

### Adım 2: HTML5 SaveOption

`html5SaveOption` yöntemi, bir 3D sahneyi HTML5 dosyası olarak kaydetmeyi ve özelleştirme seçeneklerini göstermektedir.

```java
public static void html5SaveOption() throws IOException {
    // Initialize a scene
    Scene scene = new Scene();
    
    // Create a child node with a cylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    // Set properties for the child node
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Add a light to the scene
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialize HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Customize options (e.g., turn off grid and user interface)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Save the scene as an HTML5 file
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

Diğer `SaveOptions` yöntemleri için benzer açıklamaları sürdürün: `colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` ve `drcSaveOptions`. Her biri aynı desen izler: bir sahne oluşturun, uygun `*SaveOptions` nesnesini yapılandırın ve `scene.save()` çağrısını yapın.

## Yaygın Tuzaklar ve İpuçları

- **Varlıkları gömmek** – Tek bir kendine özgü dosya gerektiğinde `GltfSaveOptions` üzerinde `setEmbedAssets(true)` çağırmayı unutmayın.  
- **Performans** – Büyük sahneler için kaydetmeden önce ağ (mesh) karmaşıklığını azaltmayı veya Draco sıkıştırmasını (`DracoSaveOptions`) kullanmayı düşünün.  
- **Dosya sistemi yönetimi** – OBJ dosyaları dışa aktarılırken `setFileSystem(new DummyFileSystem())` ile materyal dosyası oluşturulmasını engelleyerek istenmeyen yan dosyaları önleyebilirsiniz.  
- **UI öğeleri** – HTML5 dışa aktarımları varsayılan bir UI içerir; temiz bir görüntüleyici elde etmek için `setShowUI(false)` ile devre dışı bırakın.

## Sonuç

Bu kapsamlı öğreticiyi izleyerek Aspose.3D `SaveOptions` kullanarak **save 3d file java** işlemini verimli bir şekilde nasıl gerçekleştireceğinizi öğrendiniz. İster güzel biçimde yazdırılmış GLTF dosyaları, ister hafif HTML5 görüntüleyiciler, ister yüksek sıkıştırmalı Draco çıktıları ihtiyacınız olsun, bu seçenekler 3D grafik iş akışınız üzerinde tam kontrol sağlar.

## SSS

### S1: Bir glTF dosyasına varlıkları nasıl gömebilirim?

C1: `GltfSaveOptions` sınıfındaki `setEmbedAssets(true)` metodunu kullanın.

### S2: `DracoSaveOptions` içindeki `setPositionBits` metodunun amacı nedir?

C2: `setPositionBits` metodu, Draco sıkıştırma algoritmasında konum için kullanılan kantitatif bit sayısını ayarlar.

### S3: Bir U3D dosyasına normal verileri dışa aktarabilir miyim?

C3: Evet, `U3dSaveOptions` sınıfında `setExportNormals(true)` ayarlayarak normal verileri dışa aktarabilirsiniz.

### S4: OBJ dışa aktarımında materyal dosyalarını kaydetmeyi nasıl iptal ederim?

C4: `ObjSaveOptions` sınıfında `setFileSystem(new DummyFileSystem())` metodunu kullanarak materyal dosyalarının oluşturulmasını engelleyebilirsiniz.

### S5: OBJ dosyasında bağımlılıkları yerel bir dizine kaydetmenin bir yolu var mı?

C5: Evet, `ObjSaveOptions` sınıfında `setFileSystem(new LocalFileSystem(MyDir))` metodunu kullanarak bağımlılıkları yerel olarak kaydedebilirsiniz.

## Sıkça Sorulan Sorular

**S: Bu SaveOptions’ları başsız (headless) bir sunucu ortamında kullanabilir miyim?**  
C: Kesinlikle. Tüm `SaveOptions` UI gerektirmeden çalışır, bu da arka uç iş akışları için idealdir.

**S: Aspose.3D, yeni glTF 2.0 spesifikasyonuna kaydetmeyi destekliyor mu?**  
C: Evet. `GltfSaveOptions(FileFormat.GLTF2)` kullanarak glTF 2.0 formatını hedefleyebilirsiniz.

**S: OBJ’ye dışa aktarırken detay seviyesini nasıl kontrol ederim?**  
C: Kaydetmeden önce ağ sadeleştirmesi yapın veya `ObjSaveOptions` içinde vertex hassasiyetini ayarlayın.

**S: Dosyayı diske yazmadan önizleme yapmanın bir yolu var mı?**  
C: Dosyayı bir `ByteArrayOutputStream`’a kaydedebilir ve ardından baytları bir görüntüleyiciye ya da istemciye akıtabilirsiniz.

**S: Üretim kullanımı için hangi lisans gereklidir?**  
C: Değerlendirme dışı tüm dağıtımlar için ticari bir Aspose.3D lisansı gereklidir.

---

**Son Güncelleme:** 2025-12-21  
**Test Edilen Versiyon:** Aspose.3D for Java 24.12 (yazım anındaki en yeni sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}