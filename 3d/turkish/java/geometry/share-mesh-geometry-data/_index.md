---
date: 2026-02-17
description: Aspose.3D kullanarak Java 3D'de malzeme rengini ayarlarken ve ağ geometrisi
  verilerini paylaşırken, ağı FBX'e nasıl dönüştüreceğinizi öğrenin.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Mesh'i FBX'e Dönüştür ve Java 3D'de Malzeme Rengini Ayarla
url: /tr/java/geometry/share-mesh-geometry-data/
weight: 15
---

 Create 3D Mesh Java Using Polygon Builder (create 3d mesh java)"

Translate "How to set material color for each node?" etc.

Translate "Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)"

Translate "Common Pitfalls & Tips" etc.

Translate FAQs.

Translate Additional FAQs.

Translate Conclusion.

Translate "Last Updated", "Tested With", "Author".

All other placeholders remain.

Let's craft translation.

Be careful with bold formatting: keep **.

Also keep parentheses.

Let's produce final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Mesh'i FBX'e Dönüştürme ve Java 3D'de Malzeme Rengini Ayarlama

## Giriş

Java tabanlı bir 3D uygulaması geliştiriyorsanız, aynı geometriyi birden fazla nesne arasında yeniden kullanmanız ve her örneğe benzersiz bir görünüm vermeniz sıkça gerekir. Bu öğreticide **mesh'i FBX'e nasıl dönüştüreceğinizi**, temel mesh geometrisini birkaç düğüm arasında nasıl paylaşacağınızı ve **her düğüm için farklı bir malzeme rengi nasıl ayarlayacağınızı** öğreneceksiniz. Sonunda, herhangi bir motor veya görüntüleyiciye aktarabileceğiniz, dışa aktarılmaya hazır bir FBX sahnesine sahip olacaksınız.

## Hızlı Yanıtlar
- **Ana hedef nedir?** Mesh'i FBX'e dönüştürmek, mesh geometrisini paylaşmak ve her düğüm için farklı bir malzeme rengi ayarlamak.  
- **Hangi kütüphane gereklidir?** Aspose.3D for Java.  
- **Sonucu nasıl dışa aktarırım?** `FileFormat.FBX7400ASCII` kullanarak sahneyi bir FBX dosyası olarak kaydedin.  
- **Lisans gerekli mi?** Üretim kullanımı için geçici ya da tam bir lisans gereklidir.  
- **Hangi Java sürümü çalışır?** Java 8+ ortamları.

## **convert mesh to FBX** nedir?

`convert mesh to fbx`, bellekte oluşturulan veya değiştirilen bir mesh nesnesini, Maya, Blender ve Unity gibi 3D araçları tarafından geniş çapta desteklenen FBX dosya formatına yazma işlemidir. Aspose.3D bu ağır işi üstlenir; siz sadece uygun `FileFormat` ile `scene.save(...)` çağırmanız yeterlidir.

## Neden mesh geometrisi paylaşılır?

Geometriyi paylaşmak, bellek tüketimini azaltır ve render süresini hızlandırır çünkü temel vertex tamponları yalnızca bir kez depolanır. Bu teknik, ormanlar, kalabalıklar veya modüler mimari gibi çok sayıda yinelenen nesnenin bulunduğu sahneler için mükemmeldir; her örnek sadece dönüşüm veya malzeme açısından farklılık gösterir.

## Önkoşullar

Öğreticiye başlamadan önce aşağıdaki önkoşulların sağlandığından emin olun:

- **Java Geliştirme Ortamı** – Java 8 veya daha yeni bir sürümle çalışan herhangi bir IDE ya da komut satırı kurulumu.  
- **Aspose.3D Kütüphanesi** – Resmi siteden en son JAR dosyasını indirin: [here](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktarma

Gerekli paketleri Java projenize dahil edin. Bu adım, Aspose.3D kütüphanesinin sunduğu işlevlere erişim için kritiktir.

```java
import com.aspose.threed.*;
```

## Adım 1: Sahne Nesnesini Başlatma (initialize scene java)

İşleme, bir sahne nesnesi başlatarak başlayalım. Bu nesne, 3D sihrimizin gerçekleşeceği tuval görevi görecek.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: Renk Vektörlerini Tanımlama

Bu adımda, 3D sahnemizin farklı öğelerine uygulanacak renk vektörlerinden oluşan bir dizi tanımlıyoruz.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Adım 3: Polygon Builder Kullanarak 3D Mesh Oluşturma (create 3d mesh java)

Common sınıfını kullanarak polygon builder yöntemiyle bir mesh oluşturun. Bu mesh, 3D öğelerimizin temelini oluşturacak.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Her düğüm için malzeme rengi nasıl ayarlanır?

Renk vektörleri üzerinden döngü kurun, küp düğümleri oluşturun ve malzeme, **set material color** ve konum gibi öznitelikleri ayarlayın. Bu, her mesh örneğinin görsel görünümünü kontrol etmenin çekirdeğidir.

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

Desteklenen dosya formatında, bu örnekte FBX7400ASCII, 3D sahneyi kaydetmek için dizin ve dosya adını belirtin. Bu adım aynı zamanda **convert mesh to FBX** işlemini de gösterir.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Yaygın Hatalar ve İpuçları

- **Yol Sorunları** – Dosya adını eklemeden önce dizin yolunun bir dosya ayırıcı (`/` veya `\\`) ile bittiğinden emin olun.  
- **Lisans Başlatma** – `scene.save` çağrısından önce Aspose.3D lisansını ayarlamazsanız, kütüphane deneme modunda çalışır ve bir filigran ekleyebilir.  
- **Malzeme Üzerine Yazma** – Aynı `LambertMaterial` örneğini birden fazla düğümde yeniden kullanmak, tüm düğümlerin aynı rengi paylaşmasına neden olur. Yukarıda gösterildiği gibi her yineleme için yeni bir malzeme oluşturun.  
- **Büyük Mesh'ler** – Milyonlarca verteks içeren mesh'ler için FBX dosya boyutunu kontrol altında tutmak amacıyla indeksli poligonlarla `MeshBuilder` kullanmayı düşünün.

## Sıkça Sorulan Sorular

**S: Sahneyi FBX dışındaki formatlara da dışa aktarabilir miyim?**  
C: Evet, Aspose.3D OBJ, STL, 3MF, GLTF ve daha fazlasını destekler. `save` çağrısındaki `FileFormat` enum değerini değiştirmeniz yeterlidir.

**S: Sahne oluşturulduktan sonra malzemeyi değiştirmem gerekirse ne yapmalıyım?**  
C: Düğümü alın, `LambertMaterial`'ini (ör. `setDiffuseColor`) değiştirin ve sahneyi yeniden kaydedin.

**S: Kütüphane büyük mesh'leri verimli bir şekilde işliyor mu?**  
C: Aspose.3D optimize edilmiş veri yapıları kullanır; ancak çok büyük mesh'ler için akış (streaming) veya sahneyi bölme yöntemlerini değerlendirin.

**S: Renk değişimini animasyon haline getirebilir miyim?**  
C: Evet, `AnimationController` API'si ile malzeme özelliklerini animasyonlayabilirsiniz.

## Ek Sıkça Sorulan Sorular

**S1: Aspose.3D'yi diğer Java framework'leriyle kullanabilir miyim?**  
C1: Evet, Aspose.3D çeşitli Java framework'leriyle sorunsuz çalışacak şekilde tasarlanmıştır.

**S2: Aspose.3D için lisans seçenekleri var mı?**  
C2: Evet, lisans seçeneklerini [buradan](https://purchase.aspose.com/buy) inceleyebilirsiniz.

**S3: Aspose.3D için destek nasıl alınır?**  
C3: Destek ve tartışmalar için Aspose.3D [forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S4: Ücretsiz deneme sürümü mevcut mu?**  
C4: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) alabilirsiniz.

**S5: Aspose.3D için geçici bir lisans nasıl elde ederim?**  
C5: Geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) temin edebilirsiniz.

## Sonuç

Tebrikler! **Mesh'i FBX'e dönüştürdünüz**, birden fazla düğüm arasında mesh geometrisi verisini paylaştınız ve Aspose.3D for Java kullanarak bireysel malzeme renklerini ayarladınız. Bu iş akışı, herhangi bir FBX‑uyumlu boru hattına aktarılabilecek hafif, yeniden kullanılabilir bir mesh mimarisi sağlar.

---

**Son Güncelleme:** 2026-02-17  
**Test Edilen Versiyon:** Aspose.3D 24.11 for Java  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}