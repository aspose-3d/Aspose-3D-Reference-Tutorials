---
date: 2026-10-24
description: Aspose.3D kullanarak Java'da OBJ dosyalarını dışa aktarma ve düzlem yönünü
  değiştirme yöntemini öğrenin. Bu adım adım kılavuz, eğimli bir düzlem oluşturmayı
  ve bir 3D model OBJ'yi dışa aktarmayı gösterir.
keywords:
- how to export obj
- create sloped plane
- export 3d model obj
- adjust plane orientation
lastmod: 2026-10-24
linktitle: Java'da OBJ dosyalarını dışa aktarma ve düzlem yönünü değiştirme
og_description: Aspose.3D ile Java'da OBJ dosyalarını dışa aktarma ve düzlem yönünü
  değiştirme yöntemini öğrenin. Bu kılavuzu izleyerek eğimli bir düzlem oluşturabilir
  ve bir 3D model OBJ'yi verimli bir şekilde dışa aktarabilirsiniz.
og_image_alt: 'Tutorial: export OBJ and adjust plane orientation in Java with Aspose.3D'
og_title: Java'da OBJ dosyalarını dışa aktarma ve düzlem yönünü değiştirme
schemas:
- author: Aspose
  dateModified: '2026-10-24'
  description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  headline: How to export OBJ and change plane orientation in Java
  type: TechArticle
- description: Learn how to export OBJ files and change plane orientation in Java
    using Aspose.3D. This step‑by‑step guide shows creating a sloped plane and exporting
    a 3D model OBJ.
  name: How to export OBJ and change plane orientation in Java
  steps:
  - name: set document directory path
    text: Define where the exported OBJ file will be saved. ` Replace `"Your Document
      Directory"` with the absolute path on your machine (e.g., `C:/3DOutputs/`).
  - name: initialize the scene – create 3D scene
    text: Create a fresh `Scene` object that will hold all geometry. `
  - name: initialize the plane – how to modify plane
    text: Instantiate a `Plane` object that we will later orient. `
  - name: set vector – how to set plane up
    text: Define a custom up‑vector for the plane. This is the core of **change plane
      orientation**. The vector `(1, 1, 3)` tilts the plane away from the default
      XY‑plane, giving you a sloped surface you can later **export OBJ**.
  - name: complete the plane orientation and export
    text: After this call, you’ll find `ChangePlaneOrientation.obj` in the directory
      you specified, ready for any **Aspose.3D export OBJ** workflow. Aspose.3D supports
      over 30 output formats—including OBJ, FBX, STL, and more—so you can switch formats
      with a single enum change.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D provides APIs for Java, .NET, and other platforms, each
      offering the same feature set.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Certainly! You can explore the features of Aspose.3D by accessing the
      free trial [here](https://releases.aspose.com/).
    question: Is a free trial available for Aspose.3D?
  - answer: For any queries or assistance, visit our [support forum](https://forum.aspose.com/c/3d/18).
    question: Where can I find support for Aspose.3D?
  - answer: To purchase Aspose.3D, visit our [buy page](https://purchase.aspose.com/buy).
    question: How can I purchase Aspose.3D?
  - answer: Yes, if you need a temporary license, you can obtain one [here](https://purchase.aspose.com/temporary-license/).
    question: Is there a temporary license option?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export obj
- Aspose.3D
- Java 3D
- plane orientation
- 3D modeling
title: Java'da OBJ dosyalarını dışa aktarma ve düzlem yönünü değiştirme
url: /tr/java/3d-scenes-and-models/change-plane-orientation/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# OBJ'yi dışa aktarma ve Java'da düzlem yönelimini değiştirme

## Giriş

Bu öğreticide **OBJ'yi nasıl dışa aktaracağınızı** ve Aspose.3D API'sını kullanarak Java'da düzlem yönelimini nasıl değiştireceğinizi öğreneceksiniz. Bir düzlemin up‑vektörünü ayarlamak, **3D sahne oluşturma** iş akışı içinde nesne yerleştirme üzerinde ayrıntılı kontrol sağlar—tam olarak oyunlar, simülasyonlar ve kesin konumlandırmanın önemli olduğu mimari görselleştirmeler için idealdir. Aspose.3D Java API, Aspose'un ana indirme sayfasından [burada](https://releases.aspose.com/) temin edilebilir.

## Hızlı Yanıtlar
- **“export OBJ” ne anlama geliyor?** 3‑D sahneyi Wavefront OBJ formatına dönüştürmek demektir, evrensel olarak desteklenen bir mesh dosya türüdür.  
- **Neden düzlem yönelimini ayarlamalıyım?** Düzlemin up‑vektörünü değiştirmek, geometrinin sahnedeki tam olarak ihtiyaç duyduğunuz yere hizalanmasını sağlar.  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme sürümü yeterlidir; üretim için ticari lisans gereklidir.  
- **Hangi Java sürümü destekleniyor?** Aspose.3D, Java 8 ve üzeri sürümlerle çalışır.  
- **Başka formatları dışa aktarabilir miyim?** Evet – API ayrıca FBX, STL ve daha fazlasını destekler.

## “Düzlem yönelimini değiştirme” nedir?
Düzlem yönelimini değiştirmek, bir düzlemin up‑vektörünü ayarlayarak düzlemin varsayılan XY‑düzleminden sapmasını sağlamak ve rampalar, çatıların veya özel referans düzlemlerinin gibi eğimli yüzeyler oluşturmanıza imkan tanımaktır. Bu işlem, **OBJ'yi dışa aktarmadan** önce geometrinin nasıl konumlandırıldığını doğrudan etkiler.

## Neden düzlem yönelimini değiştirmelisiniz?
Düzlem yönelimini değiştirmek, nesneleri özel eksenlerle hizalamanıza, eğimli yüzeyleri simüle etmenize ve dışa aktarılan OBJ mesh'inin tasarımınızın görsel amacını yansıtmasını sağlar. Özel bir up‑vektör kullanmak, yerleştirme doğruluğunu artırır ve geliştiriciler için dışa aktarma sonrası düzenleme süresini önemli ölçüde azaltır.

## Önkoşullar
Başlamadan önce şunların olduğundan emin olun:

- Java programlamaya temel bir anlayış.  
- Aspose.3D for Java yüklü – [buradan](https://releases.aspose.com/3d/java/) indirin.  
- Kodlama için hazır bir Java IDE veya derleme aracı (ör. IntelliJ IDEA, Maven veya Gradle).

## Paketleri içe aktar
Aşağıdaki içe aktarmalar, temel Aspose.3D sınıflarına erişim sağlar.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

import java.io.IOException;
```

- `Plane` sınıfı, 3D uzayda konumlandırılabilen ve yönlendirilebilen geometrik bir düzlemi temsil eder.  
- `Vector3` sınıfı, yönler ve konumlar için kullanılan üç boyutlu bir vektörü tanımlar.  
- `Scene` sınıfı, bir modeldeki tüm 3D nesneleri, ışıkları ve kameraları tutan bir kapsayıcıdır.  
- `FileFormat` enumu, bir sahneyi kaydederken kullanılacak çıktı dosya formatını belirtir.

## Adım adım kılavuz

### Adım 1: belge dizini yolunu ayarla  
Dışa aktarılan OBJ dosyasının kaydedileceği yeri tanımlayın.

````java
String MyDir = "Your Document Directory";
````

`"Your Document Directory"` ifadesini, makinenizdeki mutlak yol ile değiştirin (ör. `C:/3DOutputs/`).

### Adım 2: sahneyi başlat – 3D sahne oluştur  
Tüm geometrileri tutacak yeni bir `Scene` nesnesi oluşturun.

````java
Scene scene = new Scene();
````

### Adım 3: düzlemi başlat – düzlemi nasıl değiştireceksiniz  
Daha sonra yönlendireceğimiz bir `Plane` nesnesi örnekleyin.

````java
Plane plane = new Plane();
````

### Adım 4: vektörü ayarla – düzlemin up‑vektörünü nasıl ayarlarsınız  
Düzlem için özel bir up‑vektör tanımlayın. Bu, **düzlem yönelimini değiştirme** işleminin özüdür.  
`(1, 1, 3)` vektörü, düzlemi varsayılan XY‑düzleminden saptırarak daha sonra **OBJ'yi dışa aktarabileceğiniz** eğimli bir yüzey oluşturur.

### Adım 5: düzlem yönelimini tamamlayın ve dışa aktar  
```java
// ExStart:ChangePlaneOrientation
try {
    plane.setUp(new Vector3(1, 1, 3));
    
    scene.getRootNode().createChildNode(plane);
    
    scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
} catch (IOException e) {
    e.printStackTrace();
}
// ExEnd:ChangePlaneOrientation
```

Bu çağrıdan sonra, belirttiğiniz dizinde `ChangePlaneOrientation.obj` dosyasını bulacaksınız; bu, herhangi bir **Aspose.3D OBJ dışa aktarım** iş akışı için hazırdır. Aspose.3D, OBJ, FBX, STL ve daha fazlasını içeren 30'dan fazla çıktı formatını destekler—bu sayede tek bir enum değişikliğiyle formatları değiştirebilirsiniz.

## Yaygın sorunlar ve çözümler

| Sorun | Neden oluşur | Çözüm |
|-------|----------------|-----|
| **File not found** kaydetme hatası | `MyDir` mevcut değil veya yazma izni yok | Klasörü önceden oluşturun veya uygun izinlere sahip mutlak bir yol kullanın. |
| Düzlem görüntüleyicide düz görünüyor | Vektör varsayılan up‑vektörle aynı doğrultuda | Görünür bir eğim görmek için paralel olmayan bir vektör seçin (ör. `(1, 0, 1)`). |
| OBJ dosyası eksik dokularla yüklüyor | Dokular sahneye hiç eklenmemişti | Gerekirse dışa aktarmadan önce geometrik nesneye malzeme/dokuyu ekleyin. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'ı diğer programlama dilleriyle kullanabilir miyim?**  
C: Evet, Aspose.3D, Java, .NET ve diğer platformlar için API'ler sunar; hepsi aynı özellik setini sağlar.

**S: Aspose.3D için ücretsiz deneme mevcut mu?**  
C: Elbette! Aspose.3D'nin özelliklerini ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişerek keşfedebilirsiniz.

**S: Aspose.3D için desteği nereden bulabilirim?**  
C: Herhangi bir sorunuz veya yardıma ihtiyacınız olduğunda, [destek forumumuzu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Aspose.3D'yi nasıl satın alabilirim?**  
C: Aspose.3D'yi satın almak için [satın alma sayfamızı](https://purchase.aspose.com/buy) ziyaret edin.

**S: Geçici lisans seçeneği var mı?**  
C: Evet, geçici bir lisansa ihtiyacınız varsa, birini [buradan](https://purchase.aspose.com/temporary-license/) alabilirsiniz.

**S: Sahneyi OBJ dışındaki formatlara dışa aktarabilir miyim?**  
C: Kesinlikle. `Scene.save` yöntemi FBX, STL ve birkaç başka formatı destekler – sadece `FileFormat` enumunu değiştirmeniz yeterlidir.

## Sonuç
Özel bir up‑vektör ayarlayarak, düzlem yönelimini değiştirip eğimli geometri oluşturabilir ve ardından sonucu sadece birkaç kod satırıyla OBJ dosyası olarak dışa aktarabilirsiniz. Bu yaklaşım, 3D modellerinizin istenen eğimi korumasını sağlar ve oyun motorları, CAD araçları veya web görselleştiricileri gibi sonraki aşama boru hatları için hazır hale getirir.

---

**Son Güncelleme:** 2026-10-24  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11  
**Yazar:** Aspose

## İlgili Öğreticiler

- [Aspose.3D kullanarak Java'da Kuaterniyonlarla FBX Modeli Dışa Aktarma](/3d/java/geometry/transform-3d-nodes-with-quaternions/)
- [Aspose.3D ile Java'da PLY Dosyalarını Dışa Aktarmayı Öğrenin – nasıl ply dışa aktarılır](/3d/java/point-clouds/ply-export-point-clouds-java/)
- [Aspose.3D ile Java'da 3D Sahneleri Kaydet – 3D Dosyalarını Verimli Dönüştür](/3d/java/load-and-save/save-3d-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}