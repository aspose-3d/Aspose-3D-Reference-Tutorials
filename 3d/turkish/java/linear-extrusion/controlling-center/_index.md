---
title: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Kontrol Merkezi
linktitle: Aspose.3D for Java ile Doğrusal Ekstrüzyonda Kontrol Merkezi
second_title: Aspose.3D Java API'si
description: Aspose.3D ile Java'daki 3D grafik dünyasını keşfedin. Doğrusal ekstrüzyonda merkezi zahmetsizce kontrol edin.
weight: 11
url: /tr/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java ile Doğrusal Ekstrüzyonda Kontrol Merkezi

## giriiş

3D grafik ve Java programlama dünyasında, doğrusal ekstrüzyonda merkezin kontrol edilmesi, projelerinizde istenilen efektlerin elde edilmesinde çok önemli bir rol oynar. Aspose.3D for Java, bu tür görevleri sorunsuz bir şekilde gerçekleştirmek için güçlü bir araç seti sağlar. Bu eğitimde, Aspose.3D for Java'yı kullanarak doğrusal ekstrüzyonda merkezi kontrol etme sürecine dalacağız ve sorunsuz ve kapsamlı bir anlayış sağlamak için her adımı parçalara ayıracağız.

## Önkoşullar

Bu eğitim yolculuğuna çıkmadan önce aşağıdaki ön koşulların yerine getirildiğinden emin olun:

1. Java Geliştirme Ortamı: Makinenizde bir Java geliştirme ortamının kurulu olduğundan emin olun.

2.  Aspose.3D for Java: Aspose.3D kütüphanesini indirin ve yükleyin. Kütüphaneyi ve belgelerini bulabilirsiniz.[Burada](https://reference.aspose.com/3d/java/).

3. Belge Dizini: Java belgelerinizi saklamak için bir dizin oluşturun. Buna "Belge Dizininiz" adını verelim.

## Paketleri İçe Aktar

Aspose.3D için gerekli paketleri Java geliştirme ortamınıza aktarın. Bu, kodunuzun kitaplık tarafından sağlanan işlevlere erişmesini sağlar.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Adım 1: Temel Profili Ayarlayın

Ekstrüzyona tabi tutulacak taban profilini başlatın. Bu örnekte yuvarlama yarıçapı 0,3 olan bir dikdörtgen şekli kullanacağız.

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2. Adım: 3B Sahne Oluşturun

Bir sahne oluşturarak 3D dünyanızın temelini oluşturun.

```java
Scene scene = new Scene();
```

## 3. Adım: Sol ve Sağ Düğümler Oluşturun

Sahnenizde sol ve sağ düğümler oluşturun. Bu düğümler, 3B nesneleriniz için tuval görevi görür.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Adım 4: Merkez Özelliğiyle Doğrusal Ekstrüzyon

Sol düğümde ortalamadan doğrusal ekstrüzyon gerçekleştirin ve dilim sayısını 3'e ayarlayın.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Adım 5: Referans için Zemin Düzlemini Ayarlayın

Sol düğüme bir zemin düzlemi ekleyerek görsel temsili geliştirin.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Adım 6: Merkez Özelliğiyle Doğrusal Ekstrüzyon (Sağ Düğüm)

Sağ düğümde doğrusal ekstrüzyon gerçekleştirin, bu sefer ekstrüzyonu ortalayın ve dilim sayısını tekrar 3'e ayarlayın.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Adım 7: Referans için Zemin Düzlemini Ayarlayın (Sağ Düğüm)

Sol düğüme benzer şekilde, referans için sağ düğüme bir zemin düzlemi ekleyin.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Adım 8: 3D Sahneyi Kaydedin

3D sahnenizi Wavefront OBJ formatında kaydedin.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Çözüm

Aspose.3D for Java ile doğrusal ekstrüzyonda merkezin kontrol edilmesi, 3D grafik geliştirmede heyecan verici olasılıkların önünü açıyor. Bu adım adım kılavuzu izleyerek, Java projelerinizde istediğiniz görsel efektleri elde etmenizi sağlayacak şekilde center özelliğini nasıl değiştireceğinizi öğrendiniz.

## SSS'ler

### S1: Aspose.3D for Java'yı ticari projelerde kullanabilir miyim?

 Cevap1: Evet, Aspose.3D for Java ticari kullanıma açıktır. Lisans ayrıntıları için şu adresi ziyaret edin:[Burada](https://purchase.aspose.com/buy).

### S2: Ücretsiz deneme sürümü var mı?

 Cevap2: Evet, Aspose.3D for Java'nın ücretsiz deneme sürümünü keşfedebilirsiniz[Burada](https://releases.aspose.com/).

### S3: Aspose.3D for Java desteğini nerede bulabilirim?

 Cevap3: Aspose.3D topluluk forumu, destek almak ve deneyimlerinizi paylaşmak için harika bir yerdir. Forumu ziyaret edin[Burada](https://forum.aspose.com/c/3d/18).

### S4: Test için geçici bir lisansa ihtiyacım var mı?

Cevap4: Evet, test amacıyla geçici bir lisansa ihtiyacınız varsa bir tane alabilirsiniz.[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Belgeleri nerede bulabilirim?

 Cevap5: Aspose.3D for Java'nın belgeleri mevcut[Burada](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
