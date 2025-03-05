---
title: Özel Kaydetme Seçenekleri
linktitle: Özel Kaydetme Seçenekleri
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'in gücünü keşfedin. Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC ve RVM formatlarındaki adım adım kılavuzlarla 3D sahne kaydetmenizi nasıl özelleştireceğinizi öğrenin.
type: docs
weight: 21
url: /tr/net/loading-and-saving/custom-save-options/
---
## giriiş

.NET için Aspose.3D dünyasına hoş geldiniz! 3D geliştirme yeteneklerinizi geliştirmek istiyorsanız doğru yerdesiniz. Bu eğitimde, özellikle Özel Kaydetme Seçeneklerine odaklanarak Yükleme ve Kaydetme işlevlerini ayrıntılı olarak ele alacağız. Aspose.3D for .NET, geliştiricilerin 3D sahneleri verimli bir şekilde işlemesine ve kaydetmesine olanak tanıyan güçlü bir kitaplıktır.

## Önkoşullar

Aspose.3D'nin heyecan verici özelliklerini keşfetmeye başlamadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:

- C# ve .NET geliştirmenin temel anlayışı.
-  Aspose.3D for .NET kütüphanesi kuruldu. adresinden indirebilirsiniz.[yayın sayfası](https://releases.aspose.com/3d/net/).
- Visual Studio veya tercih edilen herhangi bir C# IDE ile kurulmuş bir geliştirme ortamı.

## Ad Alanlarını İçe Aktar

Başlamak için gerekli ad alanlarını içe aktaralım:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Artık aşamayı belirlediğimize göre, öğreticiyi birden fazla adıma ayıralım.

## Adım 1: Collada Kaydetme Seçeneği

Popüler bir 3D dosya formatı olan Collada ile başlayalım. Collada kaydetme seçeneklerini özelleştirmek için şu adımları izleyin:

### 1. Dizini Ayarlayın:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Collada Kaydetme Seçeneklerini Başlatın:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Seçenekleri Yapılandırın:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Adım 2: Gizli 3DS Kaydetme Seçeneği

Şimdi Discreet 3DS'i ve özelleştirme seçeneklerini inceleyelim:

### 1. Dizini Ayarlayın:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 3DS Kaydetme Seçeneklerini Başlatın:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Seçenekleri Yapılandırın:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Ek yapılandırma seçenekleri...
   ```

FBX, OBJ, STL, U3D, glTF ve DRC kaydetme seçenekleri için bu adım adım yaklaşımı sürdürün ve her birini gereksinimlerinize göre özelleştirin.

## 3. Adım: glTF Kaydetme Seçenekleri

Şimdi web ve mobil uygulamalarda yaygın olarak kullanılan bir format olan glTF'ye odaklanalım. glTF kaydetme seçeneklerinizi şu adımlarla özelleştirin:

### 1. Sahne Nesnesini Başlatın:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. glTF Kaydetme Seçeneklerini Ayarlayın:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. glTF Dosyasını Kaydet:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

DRC ve RVM gibi diğer kaydetme seçenekleri için de benzer yapıyı izleyin.

## Çözüm

Tebrikler! Aspose.3D for .NET'teki özel kaydetme seçeneklerini başarıyla incelediniz. Bu güçlü kitaplık, 3B sahne kaydetme sürecinizi uyarlamanız için sayısız seçenek sunar.

## SSS'ler

### S1: Aspose.3D for .NET'i diğer .NET çerçeveleriyle kullanabilir miyim?

C1: Evet, Aspose.3D çeşitli .NET çerçeveleriyle uyumludur ve geliştirme ortamınızda esneklik sağlar.

### S2: Aspose.3D için herhangi bir lisanslama seçeneği mevcut mu?

 Cevap2: Evet, lisanslama seçeneklerini keşfedebilirsiniz[Burada](https://purchase.aspose.com/buy).

### S3: Aspose.3D ile ilgili sorgular için desteği nerede bulabilirim?

 A3: Şu adresten destek arayabilirsiniz:[Aspose.3D forumu](https://forum.aspose.com/c/3d/18).

### S4: Ücretsiz deneme sürümü mevcut mu?

 Cevap4: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S5: Aspose.3D için nasıl geçici lisans alabilirim?

 Cevap5: Geçici bir lisans edinin[Burada](https://purchase.aspose.com/temporary-license/).