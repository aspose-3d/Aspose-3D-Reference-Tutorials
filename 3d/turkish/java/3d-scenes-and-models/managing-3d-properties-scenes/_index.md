---
date: 2025-12-01
description: Aspose.3D ile Java sahnelerinde doku rengini değiştirmeyi, malzeme özelliklerine
  erişmeyi, Vector3 değerlerini ayarlamayı ve adla özellikleri almayı öğrenin – eksiksiz
  bir Aspose 3D öğreticisi.
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: Aspose.3D kullanarak Java sahnelerinde doku rengini değiştirin ve 3B özellikleri
  yönetin
url: /tr/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java sahnelerinde Aspose.3D kullanarak doku rengini değiştirin ve 3D özelliklerini yönetin

## Giriş

Bu **Aspose 3D tutorial** içinde **doku rengini değiştirmeyi** ve Java sahneleri içinde 3D özellikleri ve özel verilerle çalışmayı keşfedeceksiniz. Bir oyun, ürün görselleştirici ya da bilimsel bir görüntüleyici oluşturuyor olun, çalışma zamanında malzeme niteliklerini değiştirebilmek tam sanatsal kontrol sağlar. Bir sahneyi yüklemekten *Diffuse* rengini bir `Vector3` değeriyle ayarlamaya kadar süreci adım adım inceleyelim.

## Hızlı Yanıtlar
- **Ne değiştirebilirim?** Bir doku rengini, opaklığı, parlaklığı ve bir materyale eklenmiş herhangi bir özel özelliği değiştirebilirsiniz.  
- **Hangi sınıf verileri tutar?** `Material` ve onun `PropertyCollection`.  
- **Yeni bir renk nasıl ayarlanır?** `props.set("Diffuse", new Vector3(r, g, b))` kullanın.  
- **Lisans gerekli mi?** Değerlendirme için geçici bir lisans yeterlidir; üretim için tam lisans gereklidir.  
- **Desteklenen formatlar?** FBX, OBJ, STL, GLTF ve daha fazlası.

## Önkoşullar

- Java Development Kit (JDK) 8 veya daha yeni bir sürüm yüklü.  
- Aspose.3D for Java kütüphanesi ([Aspose web sitesinden](https://releases.aspose.com/3d/java/) indirin).  
- Java sözdizimi ve nesne‑yönelimli kavramlara temel aşinalık.

## Paketleri İçe Aktarma

Herhangi bir mantık yazmadan önce, malzeme özelliklerine ve vektör manipülasyonuna erişmenizi sağlayan sınıfları içe aktarın.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### Neden bu sınıfları içe aktarıyoruz?

- `Scene` 3D dosyasını yükler ve temsil eder.  
- `Material` yüzey tanımını (dokular, renkler vb.) sağlar.  
- `PropertyCollection` ad ile **malzeme özelliklerine erişmenizi** sağlayan sözlük benzeri bir kapsayıcıdır.  
- `Vector3` renkler ve diğer üç bileşenli vektörler için kullanılan veri tipidir.

## Adım 1: Sahneyi Başlatma

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

Bir FBX dosyasını yükleyerek içinde zaten bir doku bulunan bir `Scene` nesnesi oluştururuz. Bu, **doku rengini değiştireceğimiz** tuvaldir.

## Adım 2: Malzeme Özelliklerine Erişme

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

Burada sahnedeki ilk mesh’in **malzeme özelliklerine** erişiyoruz. `Material` nesnesi, *Diffuse*, *Specular* ve özel kullanıcı verileri gibi yapılandırılabilir her niteliği saklayan bir `PropertyCollection` tutar.

## Adım 3: Tüm Özellikleri Listeleme

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

`props` üzerinde döngü kurmak, her özellik adını ve mevcut değerini yazdırır. Bu hızlı envanter, örneğin temel renk için `"Diffuse"` gibi daha sonra değiştirebileceğiniz anahtarları keşfetmenize yardımcı olur.

## Adım 4: Doku Rengini Değiştirmek İçin Vector3 Değeri Ayarlama

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Pro tip:** `Vector3` yapıcı, **kırmızı, yeşil ve mavi** bileşenlerini (0‑1 aralığında) temsil eden üç kayan nokta sayısı alır. `(1, 0, 1)` ayarlamak, dokunun temel rengini magenta yapar ve modelin **doku rengini değiştirmiş** olur.

## Adım 5: Özelliği İsimle Getirme

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

Bu, **özelliği isimle getirme** örneğidir. Dönen `Object`i `Vector3`e cast ederek rengi programatik olarak işleyebiliriz.

## Adım 6: Özellik Örneğine Erişme

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` tam `Property` nesnesini döndürür ve size özelliğin tipi, etiketi ve eklenmiş herhangi bir özel veri gibi meta verilere erişim sağlar.

## Adım 7: Özelliğin Alt‑Özelliklerini Gezinme

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

Bazı özellikler hiyerarşik yapıya sahiptir. `pdiffuse.getProperties()` üzerinden gezinmek, *Diffuse* girişine ait iç içe geçmiş nitelikleri (ör. doku koordinatları, animasyon anahtarları) gösterir.

## Yaygın Sorunlar ve Çözümler

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **`NullPointerException` on `material`** | Düğümde atanmış bir malzeme olmayabilir. | Özelliklere erişmeden önce `node.setMaterial(new Material())` çağırın. |
| **Color does not change** | Model, *Diffuse* rengi geçersiz kılan bir doku kullanıyor. | Dokuyu devre dışı bırakın veya doku görüntüsünü doğrudan değiştirin. |
| **`ClassCastException` when retrieving** | Vector3 olmayan bir özelliği cast etmeye çalışıyor. | Cast etmeden önce `pdiffuse.getValue().getClass()` ile özelliğin tipini doğrulayın. |

## Sıkça Sorulan Sorular

**Q: Aspose.3D kütüphanesini Java projemde nasıl kurabilirim?**  
A: JAR dosyasını [Aspose web sitesinden](https://releases.aspose.com/3d/java/) indirip projenizin sınıf yoluna veya Maven/Gradle bağımlılıklarına ekleyin.

**Q: Aspose.3D için ücretsiz deneme seçenekleri var mı?**  
A: Evet, tam işlevsel 30‑günlük bir deneme sürümünü [Aspose ücretsiz deneme sayfasından](https://releases.aspose.com/) temin edebilirsiniz.

**Q: Aspose.3D için Java’da detaylı dokümantasyonu nereden bulabilirim?**  
A: Resmi API referansı [Aspose.3D documentation](https://reference.aspose.com/3d/java/) adresinde mevcuttur.

**Q: Sorular sorabileceğim bir Aspose.3D destek forumu var mı?**  
A: Kesinlikle—[Aspose.3D support forum](https://forum.aspose.com/c/3d/18) adresini ziyaret ederek topluluk ve uzmanlarla iletişime geçebilirsiniz.

**Q: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
A: Aspose sitesindeki [temporary license page](https://purchase.aspose.com/temporary-license/) üzerinden talep edebilirsiniz.

**Q: Renk dışında başka malzeme niteliklerini değiştirebilir miyim?**  
A: Evet, `Specular`, `Opacity` ve özel kullanıcı verileri gibi özellikler aynı `props.set` deseniyle değiştirilebilir.

## Sonuç

Artık **doku rengini değiştirme**, **malzeme özelliklerine erişme**, **Vector3 değeri ayarlama** ve **özelliği isimle getirme** konularını Java sahnesinde Aspose.3D kullanarak öğrendiniz. Bu teknikler, herhangi bir 3D varlık üzerinde ince ayarlı kontrol sağlar, uygulamalarınızda dinamik görsel efektler ve çalışma zamanı özelleştirmeleri sunar.

---

**Son Güncelleme:** 2025-12-01  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}