---
date: 2026-05-19
description: Java 3D'de Aspose.3D kullanarak malzeme rengini ayarlarken mesh'i FBX'e
  dönüştürmeyi ve mesh geometri verilerini paylaşmayı öğrenin.
keywords:
- convert mesh to fbx
- how to export fbx
- how to set material
- export mesh to fbx
- aspose 3d tutorial
linktitle: Mesh'i FBX'e Dönüştür ve Java 3D'de Malzeme Rengini Ayarla
schemas:
- author: Aspose
  dateModified: '2026-05-19'
  description: Learn how to convert mesh to FBX while setting material color and sharing
    mesh geometry data in Java 3D using Aspose.3D.
  headline: Convert Mesh to FBX and Set Material Color in Java 3D
  type: TechArticle
- questions:
  - answer: Yes, the shared mesh can be animated via skeletal rigs or morph targets
      while each node retains its own material.
    question: Can I reuse the same mesh for animated characters?
  - answer: Absolutely, Aspose.3D writes full UV data, so textures map correctly in
      downstream tools.
    question: Does the FBX export preserve UV coordinates?
  - answer: The library can stream meshes exceeding 2 GB without loading the entire
      file into memory, making it suitable for large scenes.
    question: What is the maximum file size Aspose.3D can handle?
  - answer: Pass a different `FileFormat` enum value, such as `FileFormat.FBX201400ASCII`,
      to `scene.save`.
    question: How do I change the FBX version?
  - answer: Yes, you can create a new `Scene`, add the desired nodes, and then save
      that scene to FBX.
    question: Is it possible to export only a subset of nodes?
  type: FAQPage
second_title: Aspose.3D Java API
title: Mesh'i FBX'e Dönüştür ve Java 3D'de Malzeme Rengini Ayarla
url: /tr/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Mesh'i FBX'e Dönüştürme ve Java 3D'de Malzeme Rengini Ayarlama

## Giriş

Java tabanlı bir 3D uygulaması geliştiriyorsanız, aynı geometriyi birden fazla nesne arasında yeniden kullanmanız ve her örneğe benzersiz bir görünüm vermeniz sıkça gerekir. Bu öğreticide **mesh'i FBX'e nasıl dönüştüreceğinizi**, temel mesh geometrisini birkaç düğüm arasında nasıl paylaşacağınızı ve **her düğüm için farklı bir malzeme rengi nasıl ayarlayacağınızı** öğreneceksiniz. Sonunda, herhangi bir motor veya görüntüleyiciye aktarabileceğiniz hazır bir FBX sahnesine sahip olacaksınız.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Mesh'i FBX'e dönüştürmek, mesh geometrisini paylaşmak ve her düğüm için ayrı bir malzeme rengi ayarlamak.  
- **Hangi kütüphane gereklidir?** Java için Aspose.3D.  
- **Sonucu nasıl dışa aktarırım?** `FileFormat.FBX7400ASCII` kullanarak sahneyi bir FBX dosyası olarak kaydedin.  
- **Lisans gerekli mi?** Üretim kullanımı için geçici veya tam bir lisans gereklidir.  
- **Hangi Java sürümü çalışır?** Java 8 ve üzeri herhangi bir ortam.

## **convert mesh to FBX** nedir?

Mesh'i FBX'e dönüştürmek, bellekte bulunan bir mesh nesnesini FBX dosya formatına yazmak anlamına gelir; bu, Maya, Blender, Unity ve birçok diğer 3D aracının desteklediği de‑facto bir standarttır. Aspose.3D bu işi halleder, bu yüzden sadece uygun `FileFormat` ile `scene.save(...)` çağırmanız yeterlidir.

## Neden mesh geometri verisini paylaşmalı?

Geometriyi paylaşmak, temel vertex tamponlarının yalnızca bir kez depolanması sayesinde bellek tüketimini azaltır ve render süresini hızlandırır. Bu teknik, birçok yinelenen nesnenin bulunduğu sahneler için mükemmeldir — ormanlar, kalabalıklar veya modüler mimari gibi — burada her örnek sadece dönüşüm veya malzeme açısından farklılık gösterir.

## Ön Koşullar

Öğreticiye başlamadan önce aşağıdaki ön koşulların sağlandığından emin olun:

- **Java Geliştirme Ortamı** – Java 8 veya daha yeni bir sürümle çalışan herhangi bir IDE veya komut satırı kurulumu.  
- **Aspose.3D Kütüphanesi** – resmi siteden en son JAR'ı indirin: [here](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktarma

`com.aspose.threed` ad alanı, sahneler, mesh'ler ve malzemeler oluşturmak için ihtiyaç duyacağınız tüm sınıfları içerir. Derleyicinin türleri çözebilmesi için bu paketleri Java dosyanızın en üstüne içe aktarın.

```java
import com.aspose.threed.*;
```

## Adım 1: Scene Nesnesini Başlatma (initialize scene java)

`Scene` sınıfı, Aspose.3D'nin tüm bir 3D dünyayı temsil eden üst‑seviye konteyneridir. Bir `Scene` başlatmak, mesh'lerin, ışıkların ve kameraların eklenebileceği temiz bir tuval sağlar.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: Renk Vektörlerini Tanımlama

`Vector3`, konumlar, yönler veya renkler için kullanılan üç bileşenli bir vektörü (X, Y, Z) temsil eder.  
RGB değerlerini tutan bir `Vector3` nesnesi dizisi oluşturun. Her vektör daha sonra ayrı bir düğüme atanacak ve her örneğe kendi malzeme tonunu verecek.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Adım 3: Polygon Builder Kullanarak 3D Mesh Oluşturma (create 3d mesh java)

`PolygonBuilder` sınıfı, köşe ve yüzleri manuel olarak tanımlayarak bir mesh oluşturmanıza olanak tanır. Bu mesh, tüm düğümler arasında yeniden kullanılacak ve geometri paylaşımının pratikte nasıl çalıştığını gösterecek.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Her düğüm için malzeme rengi nasıl ayarlanır?

`LambertMaterial`, bir mesh için difüz rengi tanımlayan basit bir malzeme türüdür.  
Renk vektörleri üzerinde döngü yapın, her giriş için bir küp düğümü oluşturun, mevcut renk ile yeni bir `LambertMaterial` atayın ve düğümü bir çeviri matrisi kullanarak konumlandırın. Bu desen, her düğümün aynı temel mesh'e referans vermeye devam ederken benzersiz bir renk göstermesini sağlar.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Adım 5: 3D Sahneyi Kaydetme (save scene fbx, convert mesh to fbx)

Desteklenen dosya formatında, bu durumda FBX7400ASCII, 3D sahneyi kaydetmek için dizin ve dosya adını belirtin. Bu adım aynı zamanda **mesh'i FBX'e dönüştürme** işlemini, paylaşılan geometri sahnesini diske kaydederek gösterir.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Yaygın Tuzaklar ve İpuçları

- **Yol Sorunları** – Dosya adını eklemeden önce dizin yolunun bir dosya ayırıcı (`/` veya `\\`) ile bittiğinden emin olun.  
- **Lisans Başlatma** – `scene.save` çağırmadan önce Aspose.3D lisansını ayarlamayı unutursanız, kütüphane deneme modunda çalışır ve bir filigran ekleyebilir.  
- **Malzeme Üzerine Yazma** – Aynı `LambertMaterial` örneğini birden fazla düğümde yeniden kullanmak, tüm düğümlerin aynı rengi paylaşmasına neden olur. Yukarıda gösterildiği gibi her yineleme için yeni bir malzeme oluşturun.  
- **Büyük Mesh'ler** – Milyonlarca verteks içeren mesh'ler için FBX dosya boyutunu yönetilebilir tutmak amacıyla indeksli çokgenlerle `MeshBuilder` kullanmayı düşünün.

## Ek Sık Sorulan Sorular

**Q1: Aspose.3D'yi diğer Java çerçeveleriyle kullanabilir miyim?**  
A1: Evet, Aspose.3D çeşitli Java çerçeveleriyle sorunsuz çalışacak şekilde tasarlanmıştır.

**Q2: Aspose.3D için herhangi bir lisans seçeneği var mı?**  
A2: Evet, lisans seçeneklerini [here](https://purchase.aspose.com/buy) adresinden inceleyebilirsiniz.

**Q3: Aspose.3D için nasıl destek alabilirim?**  
A3: Destek ve tartışmalar için Aspose.3D [forum](https://forum.aspose.com/c/3d/18) adresini ziyaret edin.

**Q4: Ücretsiz deneme mevcut mu?**  
A4: Evet, ücretsiz denemeyi [here](https://releases.aspose.com/) adresinden alabilirsiniz.

**Q5: Aspose.3D için geçici bir lisans nasıl elde ederim?**  
A5: Geçici lisansı [here](https://purchase.aspose.com/temporary-license/) adresinden alabilirsiniz.

## Sık Sorulan Sorular

**Q: Aynı mesh'i animasyonlu karakterler için yeniden kullanabilir miyim?**  
A: Evet, paylaşılan mesh iskelet rig'leri veya morf hedefleriyle animasyonlandırılabilir ve her düğüm kendi malzemesini korur.

**Q: FBX dışa aktarımı UV koordinatlarını korur mu?**  
A: Kesinlikle, Aspose.3D tam UV verisini yazar, böylece dokular sonraki araçlarda doğru şekilde haritalanır.

**Q: Aspose.3D'nin işleyebileceği maksimum dosya boyutu nedir?**  
A: Kütüphane, tüm dosyayı belleğe yüklemeden 2 GB'yi aşan mesh'leri akış olarak işleyebilir, bu da büyük sahneler için uygundur.

**Q: FBX sürümünü nasıl değiştiririm?**  
A: `scene.save`'e `FileFormat.FBX201400ASCII` gibi farklı bir `FileFormat` enum değeri geçirerek.

**Q: Sadece bir düğüm alt kümesini dışa aktarmak mümkün mü?**  
A: Evet, yeni bir `Scene` oluşturup istediğiniz düğümleri ekleyebilir ve ardından o sahneyi FBX olarak kaydedebilirsiniz.

## Sonuç

Tebrikler! Aspose.3D for Java kullanarak **mesh'i FBX'e dönüştürdünüz**, mesh geometri verisini birden fazla düğüm arasında paylaştınız ve bireysel malzeme renklerini ayarladınız. Bu iş akışı, herhangi bir FBX‑uyumlu pipeline'a aktarılabilecek hafif, yeniden kullanılabilir bir mesh mimarisi sağlar.

---

**Last Updated:** 2026-05-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< blocks/products/products-backtop-button >}}

## İlgili Öğreticiler

- [Java'da Aspose.3D Kullanarak Malzemeye Göre Mesh'i Bölme](/3d/java/3d-mesh-data/split-meshes-by-material/)
- [Java'da FBX Doku Gömme – Aspose.3D ile 3D Nesnelere Malzeme Uygulama](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Java'da Sahneyi FBX'e Dışa Aktarma ve 3D Sahne Bilgilerini Alma](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}