---
title: Aspose.3D for Java'da Doğrusal Ekstrüzyon Gerçekleştirme
linktitle: Aspose.3D for Java'da Doğrusal Ekstrüzyon Gerçekleştirme
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java ile 3D modelleme dünyasını keşfedin. Doğrusal ekstrüzyonu zahmetsizce gerçekleştirmeyi öğrenin.
weight: 10
url: /tr/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java'da Doğrusal Ekstrüzyon Gerçekleştirme

## giriiş

Aspose.3D for Java'da doğrusal ekstrüzyon gerçekleştirmeye yönelik bu kapsamlı eğitime hoş geldiniz! Java kullanarak 3D modelleme becerilerinizi geliştirmek istiyorsanız doğru yerdesiniz. Bu eğitimde, 3D modelleme için güçlü bir Java kütüphanesi olan Aspose.3D'yi kullanarak doğrusal ekstrüzyon gerçekleştirme sürecinde size rehberlik edeceğiz.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

1. Java Geliştirme Ortamı: Makinenizde bir Java geliştirme ortamının kurulu olduğundan emin olun.

2.  Aspose.3D Kütüphanesi: Aspose.3D kütüphanesini indirin ve yükleyin. Kütüphaneyi bulabilirsiniz[Burada](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktar

Geliştirme ortamınızı kurup Aspose.3D kütüphanesini kurduktan sonra gerekli paketleri içe aktarmanın zamanı geldi. Java kodunuza aşağıdakileri ekleyin:

```java
import com.aspose.threed.*;
```

Net bir anlayış sağlamak için her adımı ayrı ayrı ele alalım.

## 1. Adım: Belge Dizinini Ayarlayın

Belge dizininizin yolunu tanımlayın:

```java
String MyDir = "Your Document Directory";
```

Bu, oluşturulan 3D modelin belirtilen dizine kaydedilmesini sağlar.

## Adım 2: Temel Şekli Başlatın

Ekstrüzyon için temel profil olarak bir dikdörtgen şekli oluşturun:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Şekli özelleştirmek için yuvarlama yarıçapını gerektiği gibi ayarlayın.

## Adım 3: Doğrusal Ekstrüzyonu Gerçekleştirin

Taban profilinde doğrusal ekstrüzyon gerçekleştirin:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Burada şekli 10 birim ekstrüde ediyoruz, dilim sayısını ayarlıyoruz, ortalamayı etkinleştiriyoruz ve büküm ve büküm ofseti uyguluyoruz.

## 4. Adım: 3D Sahne Oluşturun

Bir 3B sahne oluşturun ve ekstrüzyonu alt düğüm olarak ekleyin:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Adım 5: 3D Sahneyi Kaydet

Oluşturulan 3B sahneyi Wavefront OBJ dosyası olarak kaydedin:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Artık Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonu başarıyla gerçekleştirdiniz!

## Çözüm

Tebrikler! Doğrusal ekstrüzyon gerçekleştirmek için Aspose.3D for Java'dan nasıl yararlanacağınızı öğrendiniz. Bu güçlü kütüphane, 3D modelleme projeleriniz için bir olasılıklar dünyasının kapılarını açar.

## SSS'ler

### S1: Aspose.3D tüm Java sürümleriyle uyumlu mu?

Cevap1: Aspose.3D, Java 1.6 ve sonraki sürümlerle çalışacak şekilde tasarlanmıştır.

### S2: Aspose.3D'yi ticari projeler için kullanabilir miyim?

C2: Evet, Aspose.3D hem kişisel hem de ticari projeler için kullanılabilir. Lisans ayrıntılarını kontrol edin[Burada](https://purchase.aspose.com/buy).

### S3: Aspose.3D için nasıl destek alabilirim?

 A3: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği için veya bir satın almayı düşünün[geçici lisans](https://purchase.aspose.com/temporary-license/) prim desteği için.

### S4: Aspose.3D'de başka 3D modelleme özellikleri var mı?

 Cevap4: Kesinlikle! Kapsamlı belgeleri keşfedin[Burada](https://reference.aspose.com/3d/java/) Kapsamlı bir özellik ve örnek listesi için.

### S5: Aspose.3D'nin ücretsiz deneme sürümü mevcut mu?

 C5: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
