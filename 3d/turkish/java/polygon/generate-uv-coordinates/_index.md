---
date: 2025-12-27
description: Aspose.3D kullanarak Java'dan OBJ dışa aktarırken UV koordinatlarını
  nasıl oluşturacağınızı ve UV'yi mesh'e nasıl ekleyeceğinizi öğrenin. Bu adım adım
  kılavuzu izleyin.
linktitle: How to Generate UV Coordinates for Texture Mapping in Java 3D Models
second_title: Aspose.3D Java API
title: Java 3D Modellerinde Doku Haritalama için UV Koordinatlarını Nasıl Oluşturulur
url: /tr/java/polygon/generate-uv-coordinates/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modellerinde Doku Haritalama için UV Koordinatlarını Nasıl Oluşturulur

## Introduction

Bu öğreticide **uv** koordinatlarını bir Java 3D mesh için nasıl oluşturacağınızı keşfedecek ve UV verisi eklemenin yüksek‑kaliteli doku haritalama için neden gerekli olduğunu öğreneceksiniz. Aspose.3D ile her adımı göstereceğiz, böylece **mesh'e uv ekleyebilir**, Java'dan OBJ dışa aktarabilir ve **obj olarak sahneyi kaydedebilir** herhangi bir 3D pipeline'da kullanmak için.

## Quick Answers
- **UV** ne anlama gelir? 2‑D doku koordinat sistemi (U‑yatay, V‑dikey) anlamına gelir.  
- **UV'leri manuel olarak neden oluşturmalısınız?** Bazı mesh'lerde UV verisi yoktur; bunları oluşturmak, dokuları doğru şekilde uygulamanızı sağlar.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java.  
- **Sonucu OBJ olarak dışa aktarabilir miyim?** Evet – öğreticinin sonunda sahne bir OBJ dosyası olarak kaydedilir.  
- **Lisans gerekli mi?** Ücretsiz deneme mevcuttur; üretim için ticari lisans gereklidir.

## What is UV Mapping?

UV haritalama, bir 3‑D modelin her köşesine 2‑D doku görüntüsü üzerinde bir konuma işaret eden bir (U, V) koordinat çifti atar. Doğru UV'ler, dokuların modeliniz etrafında gerilme veya dikiş olmadan sarılmasını sağlar.

## Why Use Aspose.3D for UV Generation?

Aspose.3D, UV oluşturmanın düşük seviyeli matematiğini soyutlayan yüksek seviyeli bir API sağlar. Tek bir çağrıyla **mesh'e uv ekleyebilir**, ardından **java'dan obj dışa aktarabilir** sorunsuz bir şekilde.

## Prerequisites

- Java programlama temelleri.  
- Aspose.3D for Java kütüphanesi kurulu. [buradan](https://releases.aspose.com/3d/java/) indirebilirsiniz.  
- IntelliJ IDEA veya Eclipse gibi bir Java Entegre Geliştirme Ortamı (IDE).

## Import Packages

Java projenizde, Aspose.3D'den gerekli sınıfları içe aktarın. Bu import'lar sahne oluşturma, mesh manipülasyonu ve UV oluşturma erişimini sağlar.

```java
import com.aspose.threed.Box;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.PolygonModifier;
import com.aspose.threed.Scene;
import com.aspose.threed.VertexElement;
import com.aspose.threed.VertexElementType;
```

Şimdi örneği adım adım inceleyelim.

## Step‑by‑Step Guide

### Step 1: Set Document Directory Path

Oluşturulan OBJ dosyasının kaydedileceği yeri tanımlayın.

```java
String MyDir = "Your Document Directory";
```

`"Your Document Directory"` ifadesini makinenizdeki mutlak ya da göreli bir yol ile değiştirin.

### Step 2: Create a Scene

Bir **scene**, tüm 3‑D nesneleri tutan kapsayıcıdır.

```java
Scene scene = new Scene();
```

### Step 3: Create a Mesh

Basit bir kutu ile başlayacağız, ardından mevcut UV verilerini kaldırarak UV'ye ihtiyaç duyan bir mesh simüle edeceğiz.

```java
Mesh mesh = (new Box()).toMesh();
mesh.getVertexElements().remove(mesh.getElement(VertexElementType.UV));
```

### Step 4: Manually Generate UV Coordinates

Aspose.3D, mesh geometrisine dayanarak UV'leri otomatik olarak oluşturabilir.

```java
VertexElement uv = PolygonModifier.generateUV(mesh);
```

### Step 5: Associate UV Data with the Mesh

Şimdi **mesh'e uv ekleyerek** oluşturulan UV elemanını ekliyoruz.

```java
mesh.addElement(uv);
```

### Step 6: Create a Node and Add Mesh to the Scene

Bir **node**, sahne grafiğinde dönüştürülebilir bir nesneyi temsil eder.

```java
Node node = scene.getRootNode().createChildNode(mesh);
```

### Step 7: Save the Scene as OBJ

Son olarak, sahneyi Wavefront OBJ formatında kaydederek **java'dan obj dışa aktaracağız**.

```java
scene.save(MyDir + "test.obj", FileFormat.WAVEFRONTOBJ);
```

Yukarıdaki kodu çalıştırdığınızda, kutu geometrinizi **UV koordinatlarıyla** içeren bir `test.obj` dosyası oluşturulur ve doku haritalama için hazır olur.

## Common Issues and Solutions

- **Dışa aktarma sonrası UV eksikliği** – Kaydetmeden önce `mesh.addElement(uv)` çağrısını yaptığınızdan emin olun.  
- **Dosya bulunamadı hatası** – `MyDir`'in mevcut ve yazılabilir bir klasöre işaret ettiğini doğrulayın.  
- **Yanlış doku hizalaması** – Oluşturulan UV'ler basit bir düzlemsel projeksiyon kullanır; karmaşık modeller için özel UV açma (unwrapping) düşünün.

## Frequently Asked Questions

**S: Aspose.3D for Java'yi diğer programlama dilleriyle kullanabilir miyim?**  
C: Aspose.3D öncelikle bir Java kütüphanesidir, ancak Aspose .NET ve diğer platformlar için eşdeğerler sunar. Dil‑spesifik sürümler için ürün sayfasına bakın.

**S: Aspose.3D için deneme sürümü mevcut mu?**  
C: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) kullanarak Aspose.3D özelliklerini keşfedebilirsiniz.

**S: Aspose.3D için destek nasıl alabilirim?**  
C: Topluluk desteği ve diğer kullanıcılarla etkileşim için Aspose.3D forumunu [buradan](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Aspose.3D için kapsamlı belgeleri nerede bulabilirim?**  
C: Belgeler [burada](https://reference.aspose.com/3d/java/) mevcuttur.

**S: Aspose.3D için geçici bir lisans satın alabilir miyim?**  
C: Evet, geçici lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Conclusion

Artık **uv** koordinatlarını nasıl oluşturacağınızı, **mesh'e uv ekleyebileceğinizi** ve Aspose.3D kullanarak **java'dan obj dışa aktarabileceğinizi** biliyorsunuz. Bu iş akışı, herhangi bir 3‑D modeli programlı olarak doku haritalama yeteneği sağlar ve varlıklarınızın görsel kalitesi üzerinde tam kontrol sunar.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-27  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose