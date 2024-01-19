---
title: Java ve Aspose.3D ile 3D Sahnelerde Düğüm Hiyerarşileri Oluşturun
linktitle: Java ve Aspose.3D ile 3D Sahnelerde Düğüm Hiyerarşileri Oluşturun
second_title: Aspose.3D Java API'si
description: Aspose.3D ile Java'da dinamik 3D sahneler oluşturmayı öğrenin. Düğüm hiyerarşilerini zahmetsizce oluşturun ve 3D grafik oyununuzu yükseltin.
type: docs
weight: 16
url: /tr/java/geometry/build-node-hierarchies/
---
## giriiş

3B grafiklerin ve Java programlamanın dinamik dünyasında, 3B sahnelerde düğüm hiyerarşileri oluşturmak ve yönetmek çok önemli bir beceridir. Aspose.3D for Java, karmaşık 3D sahneleri kolaylıkla oluşturmak için güçlü bir araç seti sunarak geliştiricilerin bunu sorunsuz bir şekilde başarmalarını sağlar. Bu eğitimde, Aspose.3D for Java'yı kullanarak düğüm hiyerarşileri oluşturma sürecinde size rehberlik edeceğiz ve yeni başlayanların bile takip edebilmesini sağlayacağız.

## Önkoşullar

Öğreticiye başlamadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

1. Java Geliştirme Ortamı: Makinenizde bir Java geliştirme ortamının kurulu olduğundan emin olun.
2.  Aspose.3D for Java Library: Aspose.3D for Java kütüphanesini aşağıdaki adresten indirip yükleyin:[indirme sayfası](https://releases.aspose.com/3d/java/).
3. Belge Dizini: 3B sahne dosyalarınızı depolamak için bir dizin oluşturun.

## Paketleri İçe Aktar

Aspose.3D for Java işlevlerinden yararlanmak için gerekli paketleri içe aktararak başlayın. Java kodunuza aşağıdaki satırları ekleyin:

```java
import com.aspose.threed.*;

```

## Adım 1: Sahne Nesnesini Başlatın

```java
// Sahne nesnesini başlat
Scene scene = new Scene();
```

## Adım 2: Alt Düğüm ve Mesh Oluşturun

```java
// Bir alt düğüm nesnesi alın
Node top = scene.getRootNode().createChildNode();

// İlk küp düğümünü oluşturun
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Ağ oluşturma yönteminizi kullanın
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// İkinci küp düğümünü oluşturun
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Adım 3: Döndürmeyi Üst Düğüme Uygulayın

```java
// Tüm alt düğümleri etkileyecek şekilde üst düğümü döndürün
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Adım 4: 3D Sahneyi Kaydet

```java
// 3D sahneyi desteklenen dosya formatında kaydedin (bu durumda FBX)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

Bu adım adım kılavuz, Aspose.3D for Java kullanarak 3D sahnelerde düğüm hiyerarşileri oluşturmak için sağlam bir temel sağlar. Farklı parametrelerle denemeler yapın ve kodu özel gereksinimlerinize göre uyarlayın.

## Çözüm

Düğüm hiyerarşilerinin oluşturulmasında ustalaşmak Aspose.3D for Java yolculuğunuzda önemli bir kilometre taşıdır. Bu eğitim sizi 3D sahnelerin karmaşıklıklarında sorunsuz bir şekilde gezinmenizi sağlayacak bilgiyle donattı. Artık yaratıcılığınızı serbest bırakın ve büyüleyici 3D ortamları güvenle oluşturun.

## SSS'ler

### S1: Aspose.3D for Java yeni başlayanlar için uygun mu?

A1: Kesinlikle! Aspose.3D for Java, kullanıcı dostu bir arayüz sunarak hem yeni başlayanlar hem de deneyimli geliştiriciler için erişilebilir olmasını sağlar.

### S2: Aspose.3D for Java'yı ticari projeler için kullanabilir miyim?

 A2: Evet, yapabilirsin. Ziyaret edin[satın alma sayfası](https://purchase.aspose.com/buy) lisans ayrıntıları için.

### S3: Aspose.3D for Java desteğini nasıl alabilirim?

 A3: Katılın[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluktan ve Aspose destek ekibinden yardım almak için.

### S4: Ücretsiz deneme sürümü mevcut mu?

 A4: Kesinlikle! Özellikleri ile keşfedin[ücretsiz deneme](https://releases.aspose.com/) bir taahhütte bulunmadan önce.

### S5: Belgeleri nerede bulabilirim?

 A5: Bkz.[dokümantasyon](https://reference.aspose.com/3d/java/) Aspose.3D for Java hakkında ayrıntılı bilgi için.