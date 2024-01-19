---
title: Aspose.3D ile Java'da 3D Küp Sahnesi Oluşturun
linktitle: Aspose.3D ile Java'da 3D Küp Sahnesi Oluşturun
second_title: Aspose.3D Java API'si
description: Aspose.3D for Java ile 3D küp sahne grafiklerinin harikalarını keşfedin. Çarpıcı sahneleri zahmetsizce yaratın.
type: docs
weight: 12
url: /tr/java/geometry/create-3d-cube-scene/
---
## giriiş

Aspose.3D kullanarak Java'daki 3D grafiklerin büyüleyici dünyasına hoş geldiniz! Bu eğitimde, Aspose.3D for Java'yı kullanarak etkileyici bir 3D küp sahnesi oluşturma sürecinde size rehberlik edeceğiz. Aspose.3D, 3D modeller ve sahnelerle çalışmak için kapsamlı işlevler sağlayan güçlü bir Java kütüphanesidir.

## Önkoşullar

3B küp sahnesinin oluşturulmasına geçmeden önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

1.  Java Geliştirme Kiti (JDK): Sisteminizde Java'nın kurulu olduğundan emin olun. En son sürümü şuradan indirebilirsiniz:[Oracle'ın web sitesi](https://www.oracle.com/java/).

2.  Aspose.3D for Java Library: Aspose.3D kütüphanesini indirin ve yükleyin. İndirme linkini bulabilirsiniz[Burada](https://releases.aspose.com/3d/java/).

## Paketleri İçe Aktar

Gerekli paketleri Java projenize aktararak başlayın:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

Şimdi 3 boyutlu küp sahnesi oluşturma sürecini birden fazla adıma ayıralım.

## 1. Adım: Sahneyi Başlatın

```java
// Sahne nesnesini başlat
Scene scene = new Scene();
```

## Adım 2: Düğümü ve Mesh'i Başlatın

```java
// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("box");

// Örgü örneğini ayarlamak için çokgen oluşturucu yöntemini kullanarak ortak sınıf oluşturma örgüsünü çağırın
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Düğümü Mesh geometrisine yönlendirin
cubeNode.setEntity(mesh);
```

## 3. Adım: Sahneye Düğüm Ekleyin

```java
// Bir sahneye Düğüm ekleme
scene.getRootNode().getChildNodes().add(cubeNode);
```

## 4. Adım: 3D Sahneyi Kaydedin

```java
// Belgeler dizininin yolu.
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

//3B sahneyi desteklenen dosya formatlarında kaydedin
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Adım 5: Başarı Mesajını Yazdırın

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## Çözüm

Tebrikler! Aspose.3D for Java'yı kullanarak başarılı bir şekilde 3D küp sahnesi oluşturdunuz. Bu eğitim, daha gelişmiş özellikleri keşfetmeniz ve 3D grafik dünyasında yaratıcılığınızı ortaya çıkarmanız için sağlam bir temel sağlar.

## SSS'ler

### S1: Aspose.3D'yi ticari projeler için kullanabilir miyim?

 A1: Evet, yapabilirsin. Kontrol edin[satın alma sayfası](https://purchase.aspose.com/buy) lisans ayrıntıları için.

### S2: Aspose.3D için nasıl destek alabilirim?

 A2: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği için.

### S3: Ücretsiz deneme sürümü mevcut mu?

 A3: Evet, ücretsiz deneme sürümünden yararlanabilirsiniz[Burada](https://releases.aspose.com/).

### S4: Aspose.3D belgelerini nerede bulabilirim?

 A4: Bkz.[Aspose.3D belgeleri](https://reference.aspose.com/3d/java/) detaylı bilgi için.

### S5: Aspose.3D için geçici lisans nasıl alınır?

 Cevap5: Geçici bir lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).