---
date: 2026-02-25
description: Aspose.3D LoadOptions kullanarak Java’da koordinat sistemini nasıl tersine
  çevireceğinizi ve 3D içe aktarmayı nasıl özelleştireceğinizi öğrenin. 3DS, OBJ,
  STL, U3D, glTF, PLY, X ve isteğe bağlı FBX için adım adım rehber.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Koordinat Sistemini Çevir – Aspose.3D ile Java’da 3D Dosya Yüklemeyi Özelleştirin
url: /tr/java/load-and-save/customize-3d-file-loading/
weight: 12
---

/tutorial-page-section >}}

# Flip Coordinate System – Customize 3D File Loading in Java with Aspose.3D

Translate title: "Flip Coordinate System – Customize 3D File Loading in Java with Aspose.3D" => "Koordinat Sistemini Ters Çevir – Aspose.3D ile Java’da 3D Dosya Yüklemeyi Özelleştirin". Keep the dash maybe.

We'll translate.

Then the paragraph.

Proceed step by step.

Make sure to keep markdown formatting.

Let's craft final output.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Koordinat Sistemini Ters Çevir – Aspose.3D ile Java’da 3D Dosya Yüklemeyi Özelleştirin

3D tasarım ve geliştirme alanı sürekli evrim geçirirken, modelleri içe aktarırken **koordinat sistemini ters çevirmek** yaygın bir gereksinimdir. Sağ‑el (right‑handed) bir sistemden sol‑el (left‑handed) bir sisteme varlıkları dönüştürmek ya da modelleri motorunuzun eksen kurallarıyla hizalamak istediğinizde Aspose.3D for Java size ince ayarlı kontrol sunar. Bu öğreticide, Aspose.3D’nin `LoadOptions` sınıfını kullanarak **3D içe aktarmayı özelleştirme** sürecini, 3DS, OBJ, STL, U3D, glTF, PLY, X ve isteğe bağlı FBX gibi en popüler formatları kapsayacak şekilde adım adım anlatıyoruz.

## Hızlı Yanıtlar
- **“Koordinat sistemini ters çevir” ne işe yarar?** X/Y/Z eksenlerini hedef koordinat konvansiyonuna uygun şekilde değiştirir.  
- **Hangi formatlar ters çevirmeyi destekler?** Tüm büyük formatlar (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) bir `setFlipCoordinateSystem` seçeneği sunar.  
- **Ek kütüphanelere ihtiyacım var mı?** Yalnızca Aspose.3D for Java JAR dosyası yeterlidir; harici dönüştürücüler gerekmez.  
- **Malzemeleri aynı anda yükleyebilir miyim?** Evet—OBJ dosyaları için `setEnableMaterials(true)` kullanın.  
- **Üretim ortamında lisans gerekli mi?** Deneme dışı dağıtımlar için geçerli bir Aspose.3D lisansı zorunludur.

## “Koordinat sistemini ters çevir” nedir?
Koordinat sistemini ters çevirmek, içe aktarılan modelin kullandığı eksen yönelimini değiştirir. Kaynak dosya, render motorunuzdan farklı bir el (right‑handed vs. left‑handed) kullanıyorsa, bu seçenek modellerin yansıtılmış veya ters görüntülenmesini önler.

## 3D içe aktarmayı neden özelleştirmelisiniz?
İçe aktarmayı özelleştirmek şunları sağlar:
- Animasyon dönüşlerini koruma (`setApplyAnimationTransform`).  
- Renk işleme düzeltmesi (`setGammaCorrectedColor`).  
- `getLookupPaths()` ile harici kaynak yollarını çözümleme.  
- Yalnızca ihtiyaç duyulan verileri yükleyerek bellek kullanımını optimize etme.

## Ön Koşullar

- Java programlamaya temel bir anlayış.  
- Yüklü Java Development Kit (JDK).  
- Aspose.3D for Java kütüphanesi indirilmiş. Kütüphaneyi [buradan](https://releases.aspose.com/3d/java/) edinebilirsiniz.  
- 3DS, OBJ, STL, U3D, glTF, PLY, X ve FBX gibi 3D dosya formatlarına aşinalık.

## Paketleri İçe Aktarma

Java projenizde gerekli Aspose.3D paketlerini şu şekilde içe aktarın:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## LoadOptions ile 3D içe aktarmayı nasıl özelleştirirsiniz

Aşağıda, desteklenen her format için **koordinat sistemini ters çevir** seçeneğini etkinleştiren adım adım kod parçacıkları yer almaktadır. Parçacıkları projenize doğrudan kopyalayabilirsiniz; sadece `"Your Document Directory"` ifadesini varlıklarınızın gerçek yolu ile değiştirin.

### Adım 1: 3DS Dosya Yüklemeyi Özelleştirme

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

### Adım 2: OBJ Dosya Yüklemeyi Özelleştirme

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Adım 3: STL Dosya Yüklemeyi Özelleştirme

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Adım 4: U3D Dosya Yüklemeyi Özelleştirme

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Adım 5: glTF Dosya Yüklemeyi Özelleştirme

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Adım 6: PLY Dosya Yüklemeyi Özelleştirme

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Adım 7: X Dosya Yüklemeyi Özelleştirme

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Adım 8: FBX Dosya Yüklemeyi Özelleştirme (İsteğe Bağlı)

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

## Yaygın Sorunlar ve Çözümler
- **Model yükleme sonrası ters görünüyor** – Doğru format için `setFlipCoordinateSystem(true)` ayarının yapıldığını kontrol edin.  
- **Malzemeler eksik** – OBJ dosyalarında `setEnableMaterials(true)` kullandığınızdan ve materyal dosyalarının (.mtl) lookup path’lerinden birinde bulunduğundan emin olun.  
- **Doku koordinatları ters** – glTF için eksenleri ters çevirmenin yanı sıra `setFlipTexCoordV(true)` eklemeniz gerekebilir.  
- **Dosya bulunamadı hataları** – Dış kaynakları (dokular, yardımcı dosyalar) içeren klasörü `loadOpts.getLookupPaths()` listesine ekleyin.

## Sonuç

Aspose.3D’nin `LoadOptions` özelliğini kullanarak **koordinat sistemini ters çevirebilir** ve **3D içe aktarmayı özelleştirebilirsiniz**; bu sayede neredeyse tüm büyük formatlarda ek işlem scriptlerine ihtiyaç kalmaz ve varlıklarınız ilk denemede doğru şekilde render edilir.

## Sık Sorulan Sorular

### S1: Aspose.3D for Java belgelerine nereden ulaşabilirim?
Cevap: Belgeler [burada](https://reference.aspose.com/3d/java/) mevcuttur.

### S2: Aspose.3D for Java’yı nasıl indirebilirim?
Cevap: İndirme bağlantısı [burada](https://releases.aspose.com/3d/java/) bulunur.

### S3: Ücretsiz deneme sürümü var mı?
Cevap: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişebilirsiniz.

### S4: Aspose.3D for Java için destek nasıl alınır?
Cevap: Destek forumu [burada](https://forum.aspose.com/c/3d/18) bulunur.

### S5: Test amaçlı geçici bir lisansa ihtiyacım var mı?
Cevap: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Son Güncelleme:** 2026-02-25  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11 (en yeni)  
**Yazar:** Aspose