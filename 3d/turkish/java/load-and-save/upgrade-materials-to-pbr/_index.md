---
date: 2025-12-22
description: Aspose.3D kullanarak Java'da sahneyi glTF formatına nasıl dışa aktaracağınızı
  ve 3D materyalleri daha gerçekçi bir görünüm için PBR'ye yükseltmeyi öğrenin.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Java'da Aspose.3D ile Sahneyi glTF'ye Dışa Aktar
url: /tr/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java ile Aspose.3D’de Sahneyi glTF’ye Dışa Aktarma – Malzemeleri PBR’ye Yükseltme

## Introduction

Bu öğreticide, **export scene to glTF** işlemini Java’da Aspose.3D kullanarak nasıl yapacağınızı ve 3D malzemelerinizi Fiziksel‑Temelli Rendering (PBR) formatına nasıl yükselteceğinizi öğreneceksiniz. PBR’ye yükseltmek modellerinize çok daha gerçekçi bir görünüm kazandırır ve yaygın olarak desteklenen glTF 2.0 formatına dışa aktarmak, bu yüksek kaliteli varlıkları motorlar, tarayıcılar ve AR/VR platformları arasında paylaşmanızı sağlar. Gereksinimleri inceleyecek, gerekli paketleri içe aktaracak ve her örneği adım adım açıklayacağız, böylece bu tekniği kendi projelerinizde uygulayabilirsiniz.

## Quick Answers
- **“export scene to glTF” ne anlama geliyor?** Aspose.3D sahnesini glTF 2.0 dosya formatına dönüştürür, geometriyi, malzemeleri ve hiyerarşiyi korur.  
- **Malzemeleri önce neden PBR’ye yükseltmeliyim?** PBR malzemeleri, glTF’nin metalik‑pürüzlülük iş akışıyla doğrudan eşleşir ve ekstra dönüşüm adımları olmadan gerçekçi aydınlatma sağlar.  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme sürümü yeterlidir; üretim için ticari lisans gereklidir.  
- **Hangi Java IDE’leri destekleniyor?** Java derleyebilen herhangi bir IDE (Eclipse, IntelliJ IDEA, VS Code vb.).  
- **Büyük sahneleri dışa aktarabilir miyim?** Evet, Aspose.3D verileri verimli bir şekilde akıtır; sadece çok büyük modeller için yeterli yığın belleği ayırdığınızdan emin olun.

## What is “export scene to glTF”?

Bir sahneyi glTF’ye dışa aktarmak, tüm 3D sahneyi—mesh’ler, düğümler, kameralar, ışıklar ve malzemeler dahil—GL Transmission Format (glTF) içine serileştirmek anlamına gelir. glTF, gerçek‑zaman render için optimize edilmiş açık bir standarttır ve web, mobil ve oyun motorları için idealdir.

## Why upgrade materials to PBR before exporting?

PBR (Physically‑Based Rendering) malzemeleri, albedo, metalik ve pürüzlülük gibi parametrelerle ışığın yüzeyle etkileşimini tanımlar. glTF 2.0 yerel olarak PBR’yi destekler, bu yüzden Phong veya özel malzemeleri PBR’ye dönüştürmek, model herhangi bir glTF‑uyumlu görüntüleyicide yüklendiğinde renklerin, yansımaların ve gölgelendirmenin doğru görünmesini sağlar.

## Prerequisites

Başlamadan önce şunlara sahip olduğunuzdan emin olun:

1. **Aspose.3D for Java** – [release page](https://releases.aspose.com/3d/java/) adresinden indirin.  
2. **Java Development Environment** – JDK 8 veya üzeri ve tercih ettiğiniz bir IDE.  
3. **Document Directory** – 3D dosyalarını okuyup yazacağınız makinenizde bir klasör.

## Import Packages

Projeye temel Aspose.3D ad alanını ekleyin:

```java
import com.aspose.threed.*;
```

Bu tek import, `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` ve malzeme dönüşüm API’sine erişim sağlar.

## Step 1: Initialize a New 3D Scene

Geometri ve malzemelerinizi tutacak yeni bir sahne oluşturun:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Pro tip:** Geliştirme sırasında `MyDir` yolunu mutlak bir yol olarak tutun; böylece dosya‑bulunamadı hatalarının önüne geçersiniz.

## Step 2: Create a Box with a PhongMaterial

Klasik bir Phong malzemesi kullanan basit bir kutu oluşturacağız. Bu kutu dışa aktarım sırasında PBR malzemesine dönüştürülecek:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Why Phong?** PhongMaterial kurulumu kolaydır ve dönüşüm mantığının nasıl çalıştığını gösterir.

## Step 3: Save in GLTF 2.0 Format (Export Scene to glTF)

Her `PhongMaterial`ı otomatik olarak `PbrMaterial`a dönüştürecek GLTF kaydetme seçeneklerini yapılandırın. Bu, **export scene to glTF** işleminin çekirdeğidir:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

Bu kod çalıştığında sahne `Non_PBRtoPBRMaterial_Out.gltf` dosyasına yazılır. Özel `MaterialConverter`, Phong malzemesini bir PBR malzemesine dönüştürür, böylece ortaya çıkan glTF dosyası herhangi bir glTF görüntüleyicide gerçekçi gölgelendirme ile gösterilir.

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **FileNotFoundException** when saving | `MyDir` yolunun mevcut bir klasöre işaret ettiğini ve uygulamanın yazma iznine sahip olduğunu doğrulayın. |
| **ClassCastException** in the converter | Dönüştürücüye gönderilen malzemenin gerçekten bir `PhongMaterial` olduğundan emin olun. Farklı malzeme tipleri karıştırıyorsanız `instanceof` kontrolü ekleyin. |
| **Missing textures** after export | glTF, dokuları ayrı ayrı bekler; gerekirse dönüştürücüye doku işleme ekleyin. |

## Frequently Asked Questions

**Q: Aspose.3D, Eclipse dışındaki Java geliştirme ortamlarıyla uyumlu mu?**  
A: Evet, Aspose.3D herhangi bir Java IDE’siyle çalışır; IntelliJ IDEA, NetBeans ve VS Code dahil.

**Q: Aspose.3D’yi ticari projelerde kullanabilir miyim?**  
A: Evet, Aspose.3D’yi hem kişisel hem de ticari projelerde kullanabilirsiniz. Lisans detayları için [purchase page](https://purchase.aspose.com/buy) adresini ziyaret edin.

**Q: Ücretsiz deneme sürümü mevcut mu?**  
A: Evet, ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) ulaşabilirsiniz.

**Q: Aspose.3D için destek nereden alınır?**  
A: Topluluk desteği için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) adresini inceleyin.

**Q: Aspose.3D için geçici bir lisans nasıl alınır?**  
A: Geçici lisans bilgileri için [bu linke](https://purchase.aspose.com/temporary-license/) bakın.

## Conclusion

Yukarıdaki adımları izleyerek, Aspose.3D kullanarak Java’da **export scene to glTF** işlemini ve Phong malzemelerinin otomatik olarak PBR’ye yükseltilmesini öğrendiniz. Bu iş akışı, modern render pipeline’ları, web görüntüleyicileri ve AR/VR deneyimleri için hazır, yüksek‑kaliteli, fiziksel‑temelli varlıklar oluşturmanızı sağlar. Daha karmaşık geometriler, dokular ve aydınlatmalarla deney yaparak PBR ve glTF’nin gücünden tam anlamıyla yararlanın.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-22  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

---