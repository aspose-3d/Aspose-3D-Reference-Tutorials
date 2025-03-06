---
title: Aspose.3D kullanarak Java'da 3D Düğümleri Kuaterniyonlarla Dönüştürün
linktitle: Aspose.3D kullanarak Java'da 3D Düğümleri Kuaterniyonlarla Dönüştürün
second_title: Aspose.3D Java API'si
description: Güçlü 3D dönüşümler için Java uygulamalarınızı Aspose.3D ile geliştirin. Bu adım adım kılavuzda kuaterniyonları kullanarak düğümleri dönüştürmeyi öğrenin.
weight: 20
url: /tr/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D kullanarak Java'da 3D Düğümleri Kuaterniyonlarla Dönüştürün

## giriiş

Aspose.3D kullanarak Java'da 3D düğümleri kuaterniyonlarla dönüştürmeye yönelik bu adım adım kılavuza hoş geldiniz. Java uygulamanızı güçlü 3B dönüşümlerle geliştirmek istiyorsanız bu eğitim tam size göre. Aspose.3D for Java, 3D grafiklerle çalışmak için güçlü özellikler sunar ve bu eğitimde, kuaterniyonlar kullanarak 3D düğümleri dönüştürmeye odaklanacağız.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

- Java programlamanın temel bilgisi.
- Aspose.3D for Java yüklü. İndirebilirsin[Burada](https://releases.aspose.com/3d/java/).
- 3D sahnelerinizi kaydetmek için ayarlanmış bir belge dizini.

## Paketleri İçe Aktar

Bu bölümde Aspose.3D kullanarak 3D dönüşümlere başlamak için gerekli paketleri içe aktaracağız.

```java
import com.aspose.threed.*;
```

## Adım 1: Sahne Nesnesini Başlatın

Başlamak için 3B öğeleriniz için kap görevi görecek bir sahne nesnesi oluşturun.

```java
Scene scene = new Scene();
```

## Adım 2: Düğüm Sınıfı Nesnesini Başlatın

Şimdi, bu durumda bir küpü temsil eden bir düğüm sınıfı nesnesi oluşturun.

```java
Node cubeNode = new Node("cube");
```

## Adım 3: Polygon Builder'ı kullanarak Mesh Oluşturun

Çokgen oluşturucu yöntemini kullanarak bir ağ oluşturmak için ortak sınıfı kullanın.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Adım 4: Mesh Geometrisini Ayarlayın

Oluşturulan ağı küp düğümüne atayın.

```java
cubeNode.setEntity(mesh);
```

## Adım 5: Kuaterniyon ile Döndürmeyi Ayarlayın

Kuaterniyonları kullanarak küp düğümüne döndürme uygulayın.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Adım 6: Çeviriyi Ayarlayın

Küp düğümünün çevirisini belirtin.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Adım 7: Sahneye Küp Ekleyin

Küp düğümünü sahneye dahil edin.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Adım 8: 3D Sahneyi Kaydet

3B sahneyi desteklenen bir dosya biçiminde (örneğin, FBX7500ASCII) kaydedin.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Çözüm

Tebrikler! Aspose.3D ile Java'da kuaterniyonlar kullanarak 3D düğümleri nasıl dönüştüreceğinizi başarıyla öğrendiniz. 3D uygulamalarınıza hayat vermek için farklı dönüşümleri deneyin.

## SSS'ler

### S1: Aspose.3D for Java'yı ücretsiz kullanabilir miyim?

Cevap1: Aspose.3D for Java ücretsiz deneme sürümü sunuyor. Bulabilirsin[Burada](https://releases.aspose.com/).

### S2: Aspose.3D for Java belgelerini nerede bulabilirim?

 A2: Belgeler mevcut[Burada](https://reference.aspose.com/3d/java/).

### S3: Aspose.3D for Java desteğini nasıl alabilirim?

 A3: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) destek için.

### S4: Geçici lisanslar mevcut mu?

 Cevap4: Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Aspose.3D for Java'yı nereden satın alabilirim?

 A5: Satın alabilirsiniz[Burada](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
