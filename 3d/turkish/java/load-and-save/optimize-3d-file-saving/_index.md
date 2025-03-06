---
title: Aspose.3D SaveOptions ile Java'da 3D Dosya Kaydetmeyi Optimize Edin
linktitle: Aspose.3D SaveOptions ile Java'da 3D Dosya Kaydetmeyi Optimize Edin
second_title: Aspose.3D Java API'si
description: Aspose.3D SaveOptions ile Java'da 3D dosya kaydetmeyi nasıl optimize edeceğinizi öğrenin. Performansı artırın ve çıktıları zahmetsizce özelleştirin.
weight: 16
url: /tr/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D SaveOptions ile Java'da 3D Dosya Kaydetmeyi Optimize Edin

## giriiş

Aspose.3D, geliştiricilerin 3D modellerle sorunsuz bir şekilde çalışmasını sağlayan, zengin özelliklere sahip bir Java kütüphanesidir. 3D dosyaları kaydetme söz konusu olduğunda SaveOptions sınıfı, çıktının gereksinimlerinize göre ince ayarını yapmak için çok sayıda ayar sunar. Bu eğitimde çeşitli kaydetme seçeneklerini ve süreci optimize etmek için bunlardan nasıl yararlanılabileceğini keşfedeceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for Java: Aspose.3D kütüphanesinin Java projenize entegre olduğundan emin olun. İndirebilirsin[Burada](https://releases.aspose.com/3d/java/).

- Java Geliştirme Ortamı: Makinenizde işlevsel bir Java geliştirme ortamı kurun.

- Belge Dizini: 3D dosyalarınızı kaydetmek istediğiniz bir dizin oluşturun ve daha sonra kullanmak üzere yolunu not edin.

## Paketleri İçe Aktar

 Aspose.3D ile çalışmak için gerekli paketleri Java projenize aktarın. Bu şunları içerir:`Scene` class ve çeşitli SaveOptions sınıfları. Aşağıda temel bir örnek verilmiştir:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Şimdi, farklı SaveOptions'ın kullanımını göstermek için her örneği birden çok adıma ayıralım.

## Adım 1: GLTF SaveOption'da Güzel Yazdırma

`prettyPrintInGltfSaveOption` yöntemi, insanların okuyabilmesi için girintili JSON içeriğine sahip bir GLTF dosyası oluşturmanıza olanak tanır.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // 3D sahneyi başlat
    Scene scene = new Scene(new Sphere());
    
    // GLTFSaveOptions'ı başlat
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Daha iyi okunabilirlik için güzel baskıyı etkinleştirin
    opt.setPrettyPrint(true);
    
    // 3D Sahneyi Kaydet
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Adım 2: HTML5 Kaydetme Seçeneği

`html5SaveOption` yöntemi, özelleştirme seçenekleri de dahil olmak üzere bir 3B sahnenin HTML5 dosyası olarak nasıl kaydedileceğini gösterir.

```java
public static void html5SaveOption() throws IOException {
    // Bir sahneyi başlat
    Scene scene = new Scene();
    
    // Silindirli bir alt düğüm oluşturma
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Alt düğümün özelliklerini ayarlama
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Sahneye ışık ekleyin
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // HTML5SaveOptions'ı başlat
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Seçenekleri özelleştirin (ör. ızgarayı ve kullanıcı arayüzünü kapatın)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Sahneyi HTML5 dosyası olarak kaydedin
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Aşağıdakiler gibi diğer SaveOptions yöntemleri için benzer dökümlerle devam edin:`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , Ve`drcSaveOptions`.

## Çözüm

Bu kapsamlı eğitimi takip ederek Aspose.3D SaveOptions'ı kullanarak Java'da 3D dosya kaydetmeyi nasıl optimize edeceğinizi öğrendiniz. İster GLTF dosyalarını güzel bir şekilde yazdırmak ister HTML5 çıktılarını özelleştirmek istiyor olun, Aspose.3D sizi 3D grafik iş akışınızı geliştirecek araçlarla donatır.

## SSS'ler

### S1: Varlıkları bir glTF dosyasına nasıl gömebilirim?

 Cevap1: Varlıkları gömmek için şunu kullanın:`setEmbedAssets(true)` yöntemdeki`GltfSaveOptions` sınıf.

###  S2: Amacınız nedir?`setPositionBits` method in `DracoSaveOptions`?

 A2:`setPositionBits` yöntemi, Draco sıkıştırma algoritmasındaki konum için niceleme bitlerini ayarlar.

### S3: Normal verileri bir U3D dosyasına aktarabilir miyim?

 A3: Evet, normal verileri ayarlayarak dışa aktarabilirsiniz.`setExportNormals(true)` içinde`U3dSaveOptions` sınıf.

### S4: OBJ dışa aktarımında malzeme dosyalarını kaydetmeyi nasıl atabilirim?

A4: Kullanın`setFileSystem(new DummyFileSystem())` yöntemdeki`ObjSaveOptions` Malzeme dosyalarını atmak için sınıf.

### S5: Bağımlılıkları bir OBJ dosyasındaki yerel dizine kaydetmenin bir yolu var mı?

 A5: Evet, kullanın`setFileSystem(new LocalFileSystem(MyDir))` yöntemdeki`ObjSaveOptions` bağımlılıkları yerel olarak kaydetmek için sınıf.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
