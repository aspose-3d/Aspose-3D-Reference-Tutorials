---
date: 2026-05-24
description: Aspose.3D for Java kullanarak şekli nasıl ekstrüde edeceğinizi öğrenin.
  Bu java 3d modelleme öğreticisi, doğrusal ekstrüzyon, merkez kontrolü, yön, dilimler,
  bükülme ve daha fazlasını kapsar!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Java'da Doğrusal Ekstrüzyon ile 3D Modeller Oluşturma
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Şekil Nasıl Ekstrüde Edilir - Java'da Doğrusal Ekstrüzyon ile 3D Modeller Oluşturma
url: /tr/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Şekli Ekstrüde Etme – Java'da Lineer Ekstrüzyon ile 3B Modeller Oluşturma

Java uygulamasında **şekli nasıl ekstrüde ederim** diye merak ettiyseniz, doğru yerdesiniz. Bu öğreticide Aspose.3D for Java'nın lineer ekstrüzyon özelliklerini adım adım inceleyecek, basit 2‑D profilleri tam teşekküllü 3‑D modellere nasıl dönüştüreceğinizi göstereceğiz. CAD tarzı bir görüntüleyici, bir oyun varlık hattı oluşturuyor ya da sadece geometrilerle deneme yapıyor olun, lineer ekstrüzyonu ustalaşmak, sadece birkaç satır kodla karmaşık şekiller yaratma konusunda size güven verecek.

## Hızlı Yanıtlar
- **Lineer ekstrüzyon nedir?** 2‑D bir taslağı bir yönde uzatarak 3‑D bir katı haline getirmek.  
- **Hangi kütüphane yardımcı olur?** Aspose.3D for Java, ekstrüzyon görevleri için akıcı bir API sağlar.  
- **Bir lisansa ihtiyacım var mı?** Öğrenme için ücretsiz deneme çalışır; üretim için ticari bir lisans gereklidir.  
- **Hangi Java sürümü gereklidir?** Java 8 veya üzeri.  
- **Bükülmeler veya ofsetler uygulayabilir miyim?** Evet – API, bükülme açısı ve bükülme ofsetini kutudan çıkar çıkmaz destekler.  

## Java'da “şekli nasıl ekstrüde ederim” nedir?
`Extrusion` işlemi, Aspose.3D'nin düz bir konturu hacimsel bir ağ haline dönüştüren temel özelliğidir. Basitçe söylemek gerekirse, bir 2‑D profil (örneğin bir dikdörtgen veya özel bir çokgen) sağlarsınız, motorun ne kadar çekileceğini belirlersiniz ve kütüphane sizin için 3‑D geometrisini oluşturur.

## Neden Aspose.3D for Java kullanmalı?
Aspose.3D, **50+ giriş ve çıkış formatını** – OBJ, STL, FBX ve GLTF dahil – destekler ve tüm sahneyi belleğe yüklemeden **her ekstrüzyon başına 10 000 vertex** kadar ağ üretebilir. Çapraz platform motoru Windows, Linux ve macOS üzerinde çalışır ve masaüstü iş istasyonu ya da başsız CI sunucusu fark etmeksizin tutarlı sonuçlar verir.

## Ön Koşullar
- Geliştirme makinenizde Java 8 veya daha yeni bir sürüm yüklü.  
- Bağımlılık yönetimi için Maven veya Gradle.  
- Aspose.3D for Java lisans dosyası (deneme için isteğe bağlı).  

## Lineer ekstrüzyon nasıl çalışır?
Lineer ekstrüzyon, bir 2‑D profili düz bir hat boyunca süpürerek 3‑D bir katı oluşturur. Motor önce profili üçgenleştirir, ardından ekstrüzyon ekseni boyunca her dilimde kopyalar ve sonunda dilimleri birleştirerek su geçirmez bir ağ oluşturur. Bu süreç, normalleri ve UV koordinatlarını otomatik olarak hesaplar, böylece ek geometrik işleme gerek kalmadan sonucu render edebilirsiniz.

## Lineer ekstrüzyon için ana parametreler nelerdir?
Lineer ekstrüzyon, çeşitli parametrelerle özelleştirilebilir. **center** (merkez), ekstrüzyondan önce profilin dönme noktasını tanımlar. **direction** (yön) vektörü, ekstrüzyon eksenini belirler ve varsayılan olarak pozitif Z‑ekseni olur. **Slices** (dilimler), oluşturulan ara kesit sayısını kontrol eder ve bükülmüş veya konik şekillerin pürüzsüzlüğünü etkiler. **Twist angle** (bükülme açısı), profili başlangıçtan sona doğru kademeli olarak döndürür, **twist offset** (bükülme ofseti) ise eksen boyunca lineer bir kayma ekleyerek spiral formları mümkün kılar.

- **Center** – Ekstrüzyondan önce profilin konumlandırıldığı dönme noktası.  
- **Direction** – Ekstrüzyon eksenini tanımlayan bir vektör; varsayılan pozitif Z‑ekseni.  
- **Slices** – Ara kesit sayısı; daha fazla dilim, bükülmüş veya konik ekstrüzyonlarda daha pürüzsüz geçişler sağlar.  
- **Twist Angle** – Profilin başlangıçtan sona kadar uygulanan toplam dönüşü, derece cinsinden.  
- **Twist Offset** – Profilin ekstrüzyon ekseni boyunca bükülürken hareket ettiren lineer bir ofset, spiral şekilleri mümkün kılar.

## Aspose.3D for Java'da Lineer Ekstrüzyon Yapma

Profilinizi yükleyin, parametreleri yapılandırın ve API'nin ağı oluşturmasına izin verin. Aşağıdaki adımlar tipik iş akışını özetler.

### Adım 1: 2‑D profili tanımlama
Ekstrüde etmek istediğiniz şekli temsil eden bir `Polygon` veya `Polyline` oluşturun.  
*`Polygon` bir kapalı şekli, köşelerle tanımlanır, `Polyline` ise açık bir çizgi segmentleri serisidir.*  
Başlamak için hazırsınız? [Şimdi Lineer Ekstrüzyonu Gerçekleştir](./performing-linear-extrusion/)  
Detaylı bir öğretici için, bakınız [Aspose.3D for Java'da Lineer Ekstrüzyon Yapma](./performing-linear-extrusion/).

### Adım 2: Ekstrüzyon seçeneklerini yapılandırma
Bir `Extrusion` nesnesinde merkez, yön, dilimler, bükülme ve bükülme ofsetini ayarlayın.  
*`Extrusion` sınıfı, 2‑D profilden 3‑D ağ oluşturmak için gereken tüm parametreleri kapsar.*  
Merkez kontrolüyle uygulamalı deneyim: [Lineer Ekstrüzyonda Merkez Kontrolü](./controlling-center/)  
Merkez kontrolü hakkında daha fazla bilgi: [Aspose.3D for Java ile Lineer Ekstrüzyonda Merkez Kontrolü](./controlling-center/)

### Adım 3: Ekstrüzyonu sahneye ekleme
Bir `Scene` nesnesi oluşturun, ekstrüzyon ağını ekleyin ve istediğiniz formata dışa aktarın.  
*`Scene`, tüm 3‑D nesneleri tutan ve çeşitli dosya formatlarına dışa aktarmayı yöneten kapsayıcıdır.*  
Yönü ayarlamaya hazır mısınız? [Şimdi Keşfet](./setting-direction/)  
Yön hakkında daha fazla bilgi: [Aspose.3D for Java ile Lineer Ekstrüzyonda Yön Ayarlama](./setting-direction/)

### Adım 4: Dışa aktar veya renderla
`Scene.save()` metodunu kullanarak modeli OBJ, STL veya desteklenen herhangi bir formata yazın.  
*`Scene.save()` tüm sahneyi belirtilen dosya formatına yazar, gerekli olabilecek tüm sonrası işlemleri uygular.*  
Dilimleri belirtmeye başlayın: [Daha Fazla Öğren](./specifying-slices/)  
Ayrıntılı kılavuz: [Aspose.3D for Java ile Lineer Ekstrüzyonda Dilim Belirleme](./specifying-slices/)

## Ekstrüzyona nasıl bükülme uygulanır?
`twistAngle` özelliğini ekstrüzyon seçeneklerinde ayarlayarak bir bükülme uygulayın. Motor her dilimi orantılı olarak döndürür ve helisel bir etki yaratır. Açıyı ayarlayarak hafif bir burulmadan tam 360° spirallere kadar her şeyi üretebilirsiniz; bu, dekoratif elemanlar veya fonksiyonel yaylar için faydalıdır.  
Bükülmeyi uygulamaya hazır mısınız? [Şimdi Bükülme Uygula](./applying-twist/)  
Tam örnek: [Aspose.3D for Java ile Lineer Ekstrüzyonda Bükülme Uygulama](./applying-twist/)

## Spiral şekiller için bükülme ofseti nasıl kullanılır?
Bükülme ofseti, her dilimi döndürürken ekstrüzyon ekseni boyunca hareket ettirir ve bir spiral merdiven ya da vida geometrisi oluşturur. Bükülme açısını pozitif bir ofsetle birleştirerek pürüzsüz bir helisel rampa elde edilir, negatif ofset ise aşağı doğru spiraller yaratabilir. Bu teknik, diş, yay veya sanatsal şerit modellemede idealdir.  
Becerilerinizi geliştirin: [Bükülme Ofsetini Öğren](./using-twist-offset/)  
Kapsamlı kılavuz: [Aspose.3D for Java ile Lineer Ekstrüzyonda Bükülme Ofseti Kullanma](./using-twist-offset/)

## Lineer Ekstrüzyon için Yaygın Kullanım Senaryoları
- **Mechanical parts** – Basit taslaklardan çabucak cıvata, mil ve braketi oluşturun.  
- **Architectural elements** – Kat planlarını duvarlar veya sütunlar haline getirerek BIM prototipleri oluşturun.  
- **Game assets** – Çit, boru veya dekoratif raylar gibi düşük poligonlu nesneleri doğrudan 2‑D sanattan oluşturun.  
- **Educational tools** – Parametrik eğrileri ekstrüde ederek matematiksel yüzeyleri görselleştirin.

## Yaygın Sorunları Giderme
- **Missing faces** – Profilin kapalı bir döngü olduğundan emin olun; açık konturlar boşluklar oluşturur.  
- **Excessive memory usage** – `slices` sayısını azaltın veya `scene.setMemoryOptimization(true)` özelliğini etkinleştirin.  
- **Incorrect twist direction** – Pozitif açılar, ekstrüzyon yönüne bakıldığında saat yönünde döner; tersine çevirmek için negatif değerler kullanın.  

## Sıkça Sorulan Sorular

**Q: Aspose.3D for Java'yı ticari bir projede kullanabilir miyim?**  
A: Evet, üretim kullanımı için geçerli bir Aspose lisansı gereklidir, ancak değerlendirme için ücretsiz bir deneme mevcuttur.

**Q: Hangi Java sürümleri destekleniyor?**  
A: Kütüphane Java 8 ve üzeri çalışma zamanlarıyla çalışır, Java 11, 17 ve 21 dahil.

**Q: Büyük ekstrüzyonlar için belleği yönetmem gerekiyor mu?**  
A: Aspose.3D ağ oluşturmayı verimli bir şekilde yönetir, ancak büyük sahnelerle işiniz bittiğinde yerel kaynakları serbest bırakmak için `scene.dispose()` çağırabilirsiniz.

**Q: Tek bir modelde birden fazla ekstrüzyon işlemini birleştirebilir miyim?**  
A: Kesinlikle – birden fazla ekstrüzyon nesnesi oluşturabilir, bağımsız konumlandırabilir ve aynı sahneye ekleyebilirsiniz.

**Q: Bükülme ve bükülme ofsetini birlikte uygulamak için örnek kod var mı?**  
A: Evet, “Applying Twist” ve “Using Twist Offset” öğreticileri, aynı ekstrüzyon nesnesinde her iki özelliği nasıl ayarlayacağınızı gösterir.

**Son Güncelleme:** 2026-05-24  
**Test Edilen:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< blocks/products/products-backtop-button >}}

## İlgili Öğreticiler

- [Java 3D Grafik Öğreticisi – Lineer Ekstrüzyonda Merkez](/3d/java/linear-extrusion/controlling-center/)
- [Aspose.3D for Java ile Lineer Ekstrüzyonda Yön Ayarlama](/3d/java/linear-extrusion/setting-direction/)
- [Dilmlerle 3D Ekstrüzyon Oluşturma – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}