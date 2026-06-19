---
date: 2026-04-29
description: Aspose.3D kullanarak Java'da düzlem yönelimini nasıl değiştireceğinizi
  ve OBJ'yi nasıl dışa aktaracağınızı öğrenin. 3D model OBJ dosyalarını dışa aktarmak
  için adım adım rehber.
keywords:
- change plane orientation
- create sloped plane
- export obj java
- aspose 3d export obj
linktitle: Java'da Düzlem Yönelimini Değiştirme ve OBJ'yi Dışa Aktarma
second_title: Aspose.3D Java API
title: Java'da Düzlem Yönünü Değiştirme ve OBJ'yi Dışa Aktarma
url: /tr/java/3d-scenes-and-models/change-plane-orientation/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java'da Düzlem Yönelimini Değiştirme ve OBJ Dışa Aktarma

## Giriş

Bu öğreticide, Java kullanarak Aspose.3D Java API'si ile **how to change plane orientation** ve **export OBJ** dosyalarını keşfedeceksiniz. Bir düzlemin up‑vektörünü ayarlamak, **create 3D scene** iş akışı içinde nesne yerleşimi üzerinde ince ayar kontrolü sağlar—tam olarak konumlandırmanın önemli olduğu oyunlar, simülasyonlar ve mimari görselleştirmeler için mükemmeldir.

## Hızlı Yanıtlar
- **export OBJ** ne anlama geliyor? 3‑D sahneyi, evrensel olarak desteklenen bir mesh dosya türü olan Wavefront OBJ formatına dönüştürmek anlamına gelir.  
- **plane orientation** neden ayarlamalısınız? Düzlemin up‑vektörünü değiştirmek, geometrinin sahnedeki tam istediğiniz konuma hizalanmasını sağlar.  
- **Kodu çalıştırmak için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme sürümü çalışır; üretim için ticari lisans gereklidir.  
- **Hangi Java sürümü destekleniyor?** Aspose.3D, Java 8 ve üzeri sürümlerle çalışır.  
- **Başka formatlar dışa aktarabilir miyim?** Evet – API ayrıca FBX, STL ve daha fazlasını destekler.

## “change plane orientation” nedir?
Düzlem yönelimini değiştirmek, bir düzlemin **up‑vector** değerini yeniden tanımlayarak düzlemin varsayılan XY‑düzleminden sapmasını sağlama sürecidir. Bu, modeli dışa aktarmadan önce rampalar, çatıların veya özel referans düzlemlerin gibi **create sloped plane** geometrileri oluşturmanıza olanak tanır.

## Neden düzlem yönelimini değiştirmelisiniz?
Düzlemin yönelimini değiştirmek (**how to set plane up** kullanarak) şunları yapmanızı sağlar:

* Nesneleri varsayılan dünya eksenleri yerine özel eksenlerle hizalayın.  
* Rampalar, çatıların veya kamera referans düzlemlerinin gibi eğimli yüzeyleri simüle edin.  
* Dışa aktarılan OBJ mesh'lerinin tasarımınızın görsel amacına uygun olmasını sağlayarak **export 3d model obj** adımını güvenilir kılar.

## Önkoşullar

Başlamadan önce, aşağıdakilere sahip olduğunuzdan emin olun:

- Java programlamaya temel bir anlayış.  
- Aspose.3D for Java yüklü – [buradan](https://releases.aspose.com/3d/java/) indirin.  
- Kodlama için hazır bir Java IDE veya derleme aracı (ör. IntelliJ IDEA, Maven veya Gradle).

## Paketleri İçe Aktarma

İlk olarak, Aspose.3D işlevselliğine erişmenizi sağlayan sınıfları içe aktarın.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

## Adım‑Adım Kılavuz

### Adım 1: Belge Dizin Yolunu Ayarla  
Dışa aktarılan OBJ dosyasının nereye kaydedileceğini tanımlayın.

```java
String MyDir = "Your Document Directory";
```

`"Your Document Directory"` ifadesini makinenizdeki mutlak yol ile değiştirin (ör. `C:/3DOutputs/`).

### Adım 2: Sahneyi Başlat – create 3D scene  
Tüm geometrileri tutacak yeni bir sahne nesnesi oluşturun.

```java
Scene scene = new Scene();
```

### Adım 3: Düzlemi Başlat – how to modify plane  
Daha sonra yönlendireceğimiz bir `Plane` nesnesi örnekleyin.

```java
Plane plane = new Plane();
```

### Adım 4: Vektörü Ayarla – how to set plane up  
Düzlem için özel bir up‑vektör tanımlayın. Bu, **change plane orientation** işleminin özüdür.

```java
plane.setUp(new Vector3(1, 1, 3));
```

`(1, 1, 3)` vektörü, düzlemi varsayılan XY‑düzleminden saptırarak daha sonra **export obj java** yapabileceğiniz eğimli bir yüzey oluşturur.

### Adım 5: Düzlemi Oluştur – add plane to scene  
Düzlemi kök düğüme ekleyerek sahne hiyerarşisinin bir parçası olmasını sağlayın.

```java
scene.getRootNode().createChildNode(plane);
```

### Adım 6: Sahneyi Kaydet – export OBJ file  
Yönlendirilmiş düzlem dahil tüm sahneyi bir OBJ dosyasına dışa aktarın.

```java
scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
```

Bu çağrıdan sonra, belirttiğiniz dizinde `ChangePlaneOrientation.obj` dosyasını bulacaksınız; bu dosya herhangi bir **aspose 3d export obj** iş akışı için hazırdır.

## Yaygın Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |
|-------|----------------|-----|
| **File not found** hatası kaydederken | `MyDir` mevcut değil veya yazma izni yok | Klasörü önceden oluşturun veya uygun izinlere sahip mutlak bir yol kullanın. |
| Düzlem görüntüleyicide düz görünüyor | Vektör varsayılan up‑vektörle aynı doğrultuda | Görünür bir eğim görmek için paralel olmayan bir vektör seçin (ör. `(1, 0, 1)`). |
| OBJ dosyası eksik dokularla yükleniyor | Dokular sahneye hiç eklenmemiş | Gerekirse dışa aktarmadan önce geometrilere malzeme/doku ekleyin. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'ı diğer programlama dilleriyle kullanabilir miyim?**  
C: Evet, Aspose.3D, Java, .NET ve diğer platformları dil‑spesifik API'ler aracılığıyla destekler.

**S: Aspose.3D için ücretsiz deneme mevcut mu?**  
C: Elbette! Aspose.3D özelliklerini ücretsiz deneme sürümüne [buradan](https://releases.aspose.com/) erişerek keşfedebilirsiniz.

**S: Aspose.3D için desteği nereden bulabilirim?**  
C: Herhangi bir sorunuz veya yardıma ihtiyacınız olduğunda, [destek forumumuz](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Aspose.3D'yi nasıl satın alabilirim?**  
C: Aspose.3D'yi satın almak için [satın alma sayfamızı](https://purchase.aspose.com/buy) ziyaret edin.

**S: Geçici bir lisans seçeneği var mı?**  
C: Evet, geçici bir lisansa ihtiyacınız varsa, bunu [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

**S: Sahneyi OBJ dışındaki formatlara dışa aktarabilir miyim?**  
C: Kesinlikle. `Scene.save` metodu FBX, STL ve birkaç başka formatı destekler – sadece `FileFormat` enum'ını değiştirmeniz yeterlidir.

## Sonuç

Yukarıdaki adımları izleyerek Aspose.3D for Java'da **how to change plane orientation** ve **export OBJ** işlemlerini öğrendiniz. Farklı up‑vektörlerle deneyler yaparak özel eğimler, rampalar veya kamera referans düzlemleri oluşturun ve dışa aktarılan OBJ dosyalarını sonraki iş akışlarınıza entegre edin—ister bir oyun motoru, ister bir CAD aracı, ister web‑tabanlı 3‑D görüntüleyici olsun.

---

**Son Güncelleme:** 2026-04-29  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}