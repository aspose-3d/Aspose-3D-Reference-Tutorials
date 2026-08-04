---
date: 2026-03-31
description: Aspose.3D kullanarak Java’da bir sahneye küre ekleyip yarıçapını değiştirerek
  ve OBJ dosyasını dışa aktararak 3D’yi OBJ’ye nasıl dönüştüreceğinizi öğrenin.
linktitle: 'Convert 3D to OBJ: Add Sphere & Modify Radius in Java'
second_title: Aspose.3D Java API
title: '3D''yi OBJ''ye Dönüştür: Java''da Küre Ekle ve Yarıçapı Değiştir'
url: /tr/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D'yi OBJ'ye Dönüştür: Java'da Küre Ekle ve Yarıçapı Değiştir

## Giriş

Eğer **3D'yi OBJ'ye dönüştürmek** istiyorsanız ve bunu hızlı ve programlı bir şekilde yapmak istiyorsanız, bu kılavuz size bir sahneye nasıl küre ekleyeceğinizi, yarıçapını nasıl değiştireceğinizi ve ortaya çıkan OBJ dosyasını **Aspose.3D Java library** kullanarak nasıl yazacağınızı tam olarak gösterir. Kodun her satırını adım adım inceleyecek, her adımın neden önemli olduğunu açıklayacak ve yaygın hatalardan kaçınmanız için ipuçları vereceğiz— böylece bu iş akışını oyunlara, CAD araçlarına veya bilimsel görselleştirmelere güvenle entegre edebilirsiniz.

## Hızlı Yanıtlar
- **Bu öğreticinin ana hedefi nedir?** Bir küre oluşturarak, yarıçapını ayarlayarak ve modeli Java'da dışa aktararak 3D'yi OBJ'ye nasıl dönüştüreceğinizi göstermek.  
- **Hangi kütüphane 3D işlevselliğini sağlar?** Aspose.3D, tam özellikli bir **java 3d library tutorial**.  
- **Küre boyutunu nasıl değiştiririm?** `Sphere` örneği üzerinde `sphere.setRadius(double)` metodunu çağırın.  
- **OBJ dosyasını doğrudan Java'dan yazabilir miyim?** Evet—`scene.save("file.obj", FileFormat.WAVEFRONTOBJ)` kullanın.  
- **Üretim için lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme yeterlidir; ticari kullanım için kalıcı bir lisans gereklidir.

## Aspose.3D Kullanarak 3D'yi OBJ'ye Nasıl Dönüştürürsünüz

### Aspose.3D for Java Nedir?

Aspose.3D, geliştiricilerin dış bağımlılıklar olmadan 3D dosyaları oluşturmasına, düzenlemesine ve dönüştürmesine olanak tanıyan bir **java 3d library**'dir. OBJ, FBX, STL gibi popüler formatları destekler ve oyunlar, CAD araçları ve bilimsel görselleştirmeler için idealdir.

### Neden 3D'yi OBJ'ye Dönüştürmeliyiz?

- **Evrensel Uyumluluk** – OBJ, neredeyse tüm 3D görüntüleyiciler, oyun motorları ve modelleme yazılımları tarafından desteklenir.  
- **Hafif Dışa Aktarım** – OBJ, geometriyi düz metin formatında saklar, bu da inceleme ve hata ayıklamayı kolaylaştırır.  
- **İş Akışı Esnekliği** – Sunucu tarafı Java kodundan anında OBJ dosyaları üretebilir, varlık oluşturma için otomatikleştirilmiş hatlar sağlayabilirsiniz.

## Önkoşullar

- Temel Java programlama bilgisi.  
- Aspose.3D kütüphanesi yüklü – bunu [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresinden indirin.  
- Geliştirme makinenizde JDK 8 veya daha yeni bir sürüm yüklü.

## Paketleri İçe Aktar

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Adım‑Adım Kılavuz

### Adım 1: Bir Sahne Başlat

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

`Scene` oluşturmak, tüm geometri, ışıklar ve kameralar için bir kapsayıcı sağlar. Bu, daha sonra **sahneye küre ekle** yapacağımız yerdir.

### Adım 2: Bir Küre Başlat

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

`Sphere` nesnesi varsayılan olarak 1.0 yarıçapla başlar. Bunu dışa aktarmak istediğiniz şekil için boş bir tuval olarak düşünün.

### Adım 3: İstenen Yarıçapı Ayarla

```java
// set radius
sphere.setRadius(10);
```

Burada, tam yarıçapı ayarlayan **write obj file java**‑stilinde kod yazıyoruz. `10` değerini, tasarım gereksinimlerinize uygun herhangi bir `double` değerle değiştirin.

### Adım 4: Küreyi Sahneye Ekle

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Bu satır, kök düğümün altında bir alt düğüm oluşturarak **adds sphere to scene** (küreyi sahneye ekler). Geometrinin sahne grafiğinin bir parçası haline geldiği andır.

### Adım 5: Modeli OBJ Olarak Dışa Aktar

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

`scene.save` çağrısı, **exports obj file java**‑stilinde dışa aktarır, etkili bir şekilde **save scene as obj** (sahneyi obj olarak kaydet). Oluşturulan `sphere.obj` herhangi bir standart 3D görüntüleyicide açılabilir.

## Yaygın Sorunlar ve Çözümler

| Sorun | Çözüm |
|-------|----------|
| **Küre görüntüleyicide çok küçük görünüyor** | Yarıçap değerinin doğru ayarlandığını doğrulayın; bir ölçekleme dönüşümü uygulamadığınız sürece birimlerin keyfi olduğunu unutmayın. |
| **Dışa aktarılan OBJ'de malzeme yok** | Aspose.3D yalnızca geometri yazar; eğer dokuya ihtiyacınız varsa küreye bir malzeme ekleyin (`sphere.setMaterial(...)`). |
| **Çalışma zamanında lisans istisnası** | `Scene` oluşturulmadan önce geçici ya da kalıcı bir lisans dosyasının yüklendiğinden emin olun. |

## Sıkça Sorulan Sorular

### S: Aspose.3D for Java belgelerini nerede bulabilirim?

C: Kapsamlı rehberlik için [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) adresine başvurabilirsiniz.

### S: Aspose.3D for Java'ı nasıl indirebilirim?

C: Kütüphaneyi sürüm sayfasından indirin: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### S: Aspose.3D for Java için ücretsiz deneme mevcut mu?

C: Evet, özellikleri ücretsiz deneme ile keşfetmek için [Aspose.3D Free Trial](https://releases.aspose.com/) adresini ziyaret edin.

### S: Aspose.3D for Java için destek nereden alabilirim?

C: Yardım ve tartışmalar için [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) adresindeki Aspose topluluğuna katılın.

### S: Aspose.3D için geçici lisans nasıl alabilirim?

C: [Temporary License](https://purchase.aspose.com/temporary-license/) adresini ziyaret ederek geçici bir lisans edinin.

### S: Bu kodu STL gibi diğer 3D formatlarıyla kullanabilir miyim?

C: Kesinlikle – `scene.save` çağırırken `FileFormat` enumunu değiştirmeniz yeterlidir, örneğin `FileFormat.STL`.

## Sonuç

Artık bir küre ekleyerek, yarıçapını ayarlayarak ve sonucu Java'da Aspose.3D ile dışa aktararak **3D'yi OBJ'ye dönüştürmeyi** biliyorsunuz. Diğer temel şekillerle deneyler yapın, malzemeler uygulayın veya daha zengin modeller oluşturmak için birden fazla dönüşümü zincirleyin. **save scene as obj** veya **write obj file java** yapmanız gerektiğinde aynı desen geçerlidir.

---

**Last Updated:** 2026-03-31  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}