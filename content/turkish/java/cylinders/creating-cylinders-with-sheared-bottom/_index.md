---
title: Aspose.3D for Java'da Tabanı Kesilmiş Silindirler Oluşturma
linktitle: Aspose.3D for Java'da Tabanı Kesilmiş Silindirler Oluşturma
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java'yı kullanarak tabanı kesilmiş özelleştirilmiş silindirler oluşturmayı öğrenin. Bu adım adım kılavuzla 3D modelleme becerilerinizi geliştirin.
type: docs
weight: 12
url: /tr/java/cylinders/creating-cylinders-with-sheared-bottom/
---
## giriiş

Aspose.3D for Java kullanarak tabanı kesilmiş silindirler oluşturmaya yönelik bu adım adım kılavuza hoş geldiniz. Aspose.3D, 3D dosyalarla zahmetsizce çalışmanıza olanak tanıyan güçlü bir Java kütüphanesidir. Bu eğitimde, 3D modelleme becerilerinizi geliştirmek için Aspose.3D'yi kullanma konusunda uygulamalı bir deneyim sunarak, altları kesilmiş özelleştirilmiş silindirler oluşturma konusunu ele alacağız.

## Önkoşullar

Başlamadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:
- Sisteminizde Java Geliştirme Kiti (JDK) yüklü.
-  Aspose.3D for Java kütüphanesi indirildi ve projenize eklendi. İndirme linkini bulabilirsiniz[Burada](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktar

Başlamak için Aspose.3D ile çalışmak için gerekli paketleri Java uygulamanıza aktarın:
```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. Adım: Bir Sahne Oluşturun

Silindirlerinizi ekleyeceğiniz ve değiştireceğiniz bir 3B sahne oluşturarak başlayın:
```java
// ExStart:3
// Bir sahne yarat
Scene scene = new Scene();
// ExEnd:3
```

## Adım 2: Silindir 1'i Oluşturun

Şimdi tabanı kesilmiş ilk silindiri oluşturalım:
```java
// ExStart:4
// Silindir 1'i oluştur
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Silindir 1 için özelleştirilmiş kesme tabanı
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Xy düzleminde (z ekseni) 47,5 derecelik kayma
// 1. silindiri olay yerine ekleyin
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExBitiş:4
```

## Adım 3: Silindir 2'yi Oluşturun

Daha sonra sahneye tabanı kesilmemiş ikinci bir silindir ekleyelim:
```java
// ExStart:5
// Silindir 2'yi oluştur
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ShearBottom olmadan silindir 2'yi sahneye ekleyin
scene.getRootNode().createChildNode(cylinder2);
// ExBitiş:5
```

## Adım 4: Sahneyi Kaydedin

Özelleştirilmiş silindirlerin bulunduğu sahneyi belge dizininize kaydedin:
```java
// ExStart:6
// Sahneyi kaydet
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExBitiş:6
```

Tebrikler! Aspose.3D for Java'yı kullanarak tabanı kesilmiş silindirleri başarıyla oluşturdunuz.

## Çözüm

Bu eğitimde, 3D modelleme projelerinizi geliştirmek için Aspose.3D for Java'dan nasıl yararlanabileceğinizi araştırdık. Tabanı kesilmiş özelleştirilmiş silindirler oluşturmak tasarımlarınıza benzersiz bir dokunuş katar ve Aspose.3D süreci basitleştirir.

## SSS'ler

### S1: Aspose.3D for Java'yı diğer Java 3D kütüphaneleriyle birlikte kullanabilir miyim?

Cevap1: Aspose.3D for Java bağımsız çalışacak şekilde tasarlanmıştır. Onu diğer kitaplıklarla entegre edebilseniz de, çoğu 3D modelleme görevini tek başına gerçekleştirebilecek kadar güçlüdür.

### S2: Aspose.3D, 3D modellemeye yeni başlayanlar için uygun mudur?

Cevap2: Evet, Aspose.3D, kullanıcı dostu bir API sunarak 3D modellemede hem yeni başlayanlar hem de deneyimli geliştiriciler için uygun hale getiriyor.

### S3: Aspose.3D for Java için ek desteği nerede bulabilirim?

 A3: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.

### S4: Aspose.3D için nasıl geçici lisans alabilirim?

 Cevap4: Geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).

### S5: Aspose.3D for Java'yı satın alabilir miyim?

 Cevap5: Evet, Aspose.3D for Java'yı satın alabilirsiniz[Burada](https://purchase.aspose.com/buy).