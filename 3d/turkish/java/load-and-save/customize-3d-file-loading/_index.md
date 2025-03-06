---
title: Aspose.3D LoadOptions ile Java'da 3D Dosya Yüklemeyi Özelleştirin
linktitle: Aspose.3D LoadOptions ile Java'da 3D Dosya Yüklemeyi Özelleştirin
second_title: Aspose.3D Java API'si
description: Aspose.3D özelleştirilebilir LoadOptions ile Java'da 3D dosya yüklemenizi geliştirin. 3DS, OBJ, STL, U3D, glTF, PLY, X ve isteğe bağlı FBX için adım adım özelleştirmeyi öğrenin.
weight: 12
url: /tr/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D LoadOptions ile Java'da 3D Dosya Yüklemeyi Özelleştirin

## giriiş

Sürekli gelişen 3D tasarım ve geliştirme ortamında, 3D dosya formatlarının verimli şekilde kullanılması çok önemlidir. Aspose.3D for Java, çeşitli 3D dosya formatlarının yüklenmesini özelleştirmek için güçlü bir çözüm sunar. Bu eğitim, Aspose.3D'nin LoadOptions'ını kullanarak Java'da 3D dosya yüklemeyi özelleştirme sürecinde size rehberlik edecektir.

## Önkoşullar

Özelleştirme sürecine dalmadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Java programlamanın temel anlayışı.
- Java Geliştirme Kiti (JDK) kuruldu.
-  Aspose.3D for Java kütüphanesi indirildi. Onu elde edebilirsin[Burada](https://releases.aspose.com/3d/java/).
- 3DS, OBJ, STL, U3D, glTF, PLY, X ve FBX gibi 3D dosya formatlarına aşinalık.

## Paketleri İçe Aktar

Java projenizde gerekli Aspose.3D paketlerini içe aktardığınızdan emin olun:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 3D Dosya Yüklemeyi Özelleştirin

### 1. Adım: 3DS Dosya Yüklemeyi Özelleştirin

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Adım 2: OBJ Dosya Yüklemesini Özelleştirin

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Adım 3: STL Dosya Yüklemeyi Özelleştirin

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Adım 4: U3D Dosya Yüklemeyi Özelleştirin

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Adım 5: glTF Dosya Yüklemeyi Özelleştirin

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Adım 6: PLY Dosya Yüklemesini Özelleştirin

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Adım 7: X Dosya Yüklemeyi Özelleştirin

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Adım 8: FBX Dosya Yüklemeyi Özelleştirin (İsteğe Bağlı)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Çözüm

Aspose.3D'nin LoadOptions'ı ile Java'da 3D dosya yüklemeyi özelleştirmek, geliştiricilerin içe aktarma sürecini belirli gereksinimlere göre uyarlamasına olanak tanır. Aspose.3D, animasyon dönüşümlerini ayarlama, koordinat sistemlerini değiştirme veya dış bağımlılıkları yönetme gibi konularda kusursuz entegrasyon için gereken esnekliği sağlar.

## SSS

### S1: Aspose.3D for Java belgelerini nerede bulabilirim?

 A1: Belgeler mevcut[Burada](https://reference.aspose.com/3d/java/).

### S2: Aspose.3D for Java'yı nasıl indirebilirim?

 A2: İndirebilirsin[Burada](https://releases.aspose.com/3d/java/).

### S3: Ücretsiz deneme sürümü mevcut mu?

 C3: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S4: Aspose.3D for Java desteğini nereden alabilirim?

 Cevap4: Destek forumunu ziyaret edin[Burada](https://forum.aspose.com/c/3d/18).

### S5: Test için geçici bir lisansa ihtiyacım var mı?

 A5: Evet, geçici bir lisans alın[Burada](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
