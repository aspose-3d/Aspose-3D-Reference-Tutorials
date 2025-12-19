---
date: 2025-12-19
description: Aspose.3D LoadOptions kullanarak Java’da 3D yüklemeyi nasıl özelleştireceğinizi
  öğrenin. 3DS, OBJ, STL, U3D, glTF, PLY, X ve isteğe bağlı FBX dosyalarını kapsayan
  adım adım rehber.
linktitle: Customize 3D Loading Java – How to customize 3d loading java with Aspose.3D
  LoadOptions
second_title: Aspose.3D Java API
title: 3D Yüklemeyi Özelleştirme Java – Aspose.3D LoadOptions ile 3D yüklemeyi nasıl
  özelleştirirsiniz
url: /tr/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Yükleme Java'yı Özelleştirme – Aspose.3D LoadOptions ile 3D yükleme Java'sını nasıl özelleştirirsiniz

## Giriş

Modern 3D uygulamalarda **customize 3d loading java** modellerin kaynak formatına bakılmaksızın tam olarak istenildiği gibi görünmesini sağlamak için hayati öneme sahiptir. Bir oyun motoru, AR/VR görüntüleyici veya CAD dönüşüm aracı geliştiriyor olun, 3DS, OBJ, STL, U3D, glTF, PLY, X ve hatta FBX dosyalarının nasıl içe aktarıldığını kontrol edebilmek saatler süren son‑işleme süresinden tasarruf sağlar. Bu öğretici, Aspose.3D’nin esnek `LoadOptions` sınıflarını kullanarak Java’da 3D dosya yüklemesini özelleştirmenin her adımını size gösterir.

## Hızlı Yanıtlar
- **“customize 3d loading java” ne anlama geliyor?** Aspose.3D’nin `LoadOptions` yapılandırılarak koordinat sistemi çevirme, malzeme işleme ve animasyon dönüşümleri gibi içe aktarım davranışlarını kontrol etmesi anlamına gelir.  
- **Hangi formatları özelleştirebilirim?** 3DS, OBJ, STL, U3D, glTF, PLY, X ve isteğe bağlı olarak FBX.  
- **Bunu denemek için lisansa ihtiyacım var mı?** Tam işlevsellik için geçici bir lisans gereklidir; ayrıca ücretsiz bir deneme sürümü de mevcuttur.  
- **Ek veri gerekiyor mu?** Dış kaynaklar (doku dosyaları veya malzeme kütüphaneleri) için arama yolları (lookup paths) sağlamanız gerekebilir.  
- **En son Aspose.3D for Java sürümünü nereden bulabilirim?** Aşağıdaki resmi indirme sayfasında.

## “customize 3d loading java” nedir?

Java’da 3D yüklemeyi özelleştirmek, Aspose.3D motorunun gelen dosyaları nasıl yorumladığını belirlemenizi sağlar. Çeşitli `*LoadOptions` sınıflarındaki özellikleri ayarlayarak şunları yapabilirsiniz:

* Renderleme hattınıza uyması için koordinat sistemini çevirme.  
* Performans‑kritik senaryolarda malzeme yüklemeyi etkinleştirme veya devre dışı bırakma.  
* Gamma düzeltmesi, animasyon dönüşümleri uygulama veya FBX dosyaları için yerleşik global ayarları koruma.  

## Aspose.3D LoadOptions neden kullanılmalı?

* **İnce ayarlı kontrol** – Her formatı bağımsız olarak ayarlayabilirsiniz.  
* **Çapraz‑format tutarlılığı** – Tüm desteklenen dosya türlerinde aynı koordinat sistemi kurallarını uygulayın.  
* **Performans optimizasyonu** – Gereksiz verileri (ör. malzemeler) atlayarak yükleme süresini kısaltın.  

## Önkoşullar

Başlamadan önce şunlara sahip olduğunuzdan emin olun:

- Java temellerine sağlam bir hakimiyet.  
- JDK 8 veya daha yeni bir sürüm yüklü.  
- Resmi siteden indirilen Aspose.3D for Java kütüphanesi — [buradan](https://releases.aspose.com/3d/java/) temin edebilirsiniz.  
- Çalışmayı planladığınız 3D dosya formatlarına (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) temel bir aşinalık.

## Paketleri İçe Aktarma

Java projenizde temel Aspose.3D sınıflarını ve standart I/O paketini içe aktarın:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 3D Dosya Yüklemeyi Özelleştirme

Aşağıda, her desteklenen format için ayrı bir yöntem bulacaksınız. Her kod parçacığı en yaygın özelleştirmeleri gösterir; özellikleri kendi iş akışınıza göre ayarlamaktan çekinmeyin.

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

*Bu neden önemli:* `ApplyAnimationTransform` etkinleştirildiğinde gömülü animasyon verileri hedef koordinat sistemine uyum sağlar; `GammaCorrectedColor` ise farklı render motorları arasında geçişte sıkça görülen renk yoğunluğu sorunlarını düzeltir.

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

*İpucu:* Dış `.mtl` malzeme dosyalarına referans veren OBJ dosyaları yüklüyorsanız, `EnableMaterials` değerini `true` tutun ve arama yolunun bu dosyaların bulunduğu klasöre işaret ettiğinden emin olun.

### Adım 3: STL Dosya Yüklemeyi Özelleştirme  

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

*Profesyonel ipucu:* STL dosyaları yalnızca geometri içerir, bu yüzden genellikle tek gerekli ayar koordinat sistemini çevirmektir.

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

*V doku koordinatları neden çevrilir?* Çoğu glTF dışa aktarıcı, geleneksel DirectX hatlarından farklı bir UV kökeni kullanır; `TexCoordV`’yi çevirmek dokuları doğru hizalar.

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

*Ne zaman kullanılmalı:* FBX dosyaları genellikle global ayarları (birimler, up‑axis) içerir. Bu ayarları korumak, içe aktarılan sahnenin orijinal yazarın niyetine uygun olmasını sağlar.

## Yaygın Sorunlar ve Çözümler

| Sorun | Muhtemel Neden | Çözüm |
|-------|----------------|-------|
| Dokular eksik görünüyor | Arama yolu ayarlanmamış veya büyük/küçük harf duyarlılığı hatalı | `loadOpts.getLookupPaths()` içine doğru dizini ekleyin ve dosya adlarını kontrol edin |
| Model ters görünüyor | Format için `FlipCoordinateSystem` etkinleştirilmemiş | İlgili `*LoadOptions` için `setFlipCoordinateSystem(true)` ayarlayın |
| Renkler soluk | 3DS için gamma düzeltmesi devre dışı | `Discreet3dsLoadOptions` üzerinde `setGammaCorrectedColor(true)` çağırın |
| FBX animasyonu hatalı | Global ayarlar üzerine yazılmış | `setKeepBuiltinGlobalSettings(true)` kullanın |

## Sık Sorulan Sorular

### S1: Aspose.3D for Java belgelerine nereden ulaşabilirim?  
C1: Belgeler [burada](https://reference.aspose.com/3d/java/) mevcuttur.

### S2: Aspose.3D for Java’yı nasıl indirebilirim?  
C2: İndirme bağlantısı [burada](https://releases.aspose.com/3d/java/) bulunur.

### S3: Ücretsiz bir deneme sürümü var mı?  
C3: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişebilirsiniz.

### S4: Aspose.3D for Java için destek nereden alınır?  
C4: Destek forumu [burada](https://forum.aspose.com/c/3d/18) bulunur.

### S5: Test için geçici bir lisansa ihtiyacım var mı?  
C5: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

### S6: Tek bir sahnede birden fazla format yükleyebilir miyim?  
C6: Kesinlikle. Her format için ayrı `LoadOptions` oluşturup `scene.open()` ile dosyaları açın; sahne geometrileri birleştirir.

### S7: Büyük dosyalar için yükleme performansını nasıl artırabilirim?  
C7: Gereksiz özellikleri devre dışı bırakın (ör. STL için malzeme yükleme) ve tekrar eden I/O’dan kaçınmak için `LookupPaths` kullanın.

### S8: Yükleme sonrası koordinat sistemini programatik olarak değiştirmek mümkün mü?  
C8: Evet, dosya açıldıktan sonra `scene.getRootNode().rotate()` veya `scene.getRootNode().scale()` çağırabilirsiniz.

---

**Son Güncelleme:** 2025-12-19  
**Test Edilen Sürüm:** Aspose.3D for Java 24.11 (yazım zamanındaki en yeni sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}