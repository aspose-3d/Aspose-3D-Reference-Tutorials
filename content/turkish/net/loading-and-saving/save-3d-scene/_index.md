---
title: Yükleme ve Kaydetme - 3D Sahneyi Kaydetme
linktitle: Yükleme ve Kaydetme - 3D Sahneyi Kaydetme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'in gücünü keşfedin. Kesintisiz 3D sahne manipülasyonu için çok yönlü bir kitaplık. Zahmetsizce yükleyin, kaydedin ve sıkıştırın.
type: docs
weight: 20
url: /tr/net/loading-and-saving/save-3d-scene/
---
## giriiş

Aspose.3D for .NET kullanarak 3 boyutlu sahne manipülasyonu dünyasına heyecan verici bir yolculuğa hoş geldiniz! İster deneyimli bir geliştirici ister meraklı bir meraklı olun, bu eğitim size 3D sahneleri zahmetsizce yükleme, kaydetme ve sıkıştırma sürecinde rehberlik edecektir.

## Önkoşullar

3B sahne manipülasyonunun büyüleyici dünyasına dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

-  Aspose.3D for .NET: Aspose.3D kütüphanesini şuradan indirip yükleyin:[İndirme: {link](https://releases.aspose.com/3d/net/).
-  Dokümantasyon: Kapsamlı bilgiler aracılığıyla kütüphanenin işlevlerine aşina olun.[dokümantasyon](https://reference.aspose.com/3d/net/).
- Çıktı Dizininiz: Eğitim sırasında oluşturulan çıktı dosyalarını depolamak için bir dizin ayarlayın.

## Ad Alanlarını İçe Aktar

Gerekli ad alanlarını .NET ortamımıza aktararak araştırmamıza başlayalım:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Yükleme ve Kaydetme - 3D Sahneyi Kaydetme

### 1. Adım: 3D Belge Yükleyin

```csharp
Scene scene = new Scene();
scene.Open(RunExamples.GetDataFilePath("document.fbx"));
```

 Bu adımda yeni bir tane oluşturuyoruz.`Scene` kullanarak mevcut bir 3D belgeyi yükleyin ve yükleyin.`Open` yöntem.

### 2. Adım: Sahneyi Akışa Kaydetme

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

Yüklenen 3B sahneyi kullanarak bir bellek akışına kaydedin.`Save` İstenilen dosya formatını (bu durumda FBX7500ASCII) belirterek yöntemi kullanın.

### 3. Adım: Akış Konumunu Geri Sarın

```csharp
dstStream.Position = 0;
```

Sorunsuz bir işlem sağlamak üzere bir sonraki okuyucuya hazırlamak için akış konumunu sıfırlayın.

### Adım 4: Sahneyi Yerel Yola Kaydetme

```csharp
scene.Save("Your Output Directory" + "output_out.fbx", FileFormat.FBX7500ASCII);
```

Anlamlı bir çıktı dizini ve dosya adı sağlayarak 3B sahneyi yerel bir yola kaydedin.

## Sıkıştırma

Şimdi 3B sahneler için sıkıştırma seçeneklerini inceleyelim.

### 1. Adım: 3D Belge Yükleyin

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
```

 Önceki örneğe benzer şekilde, 3 boyutlu bir belgeyi`Scene` nesne.

### 2. Adım: Sıkıştırmayı Devre Dışı Bırakın ve Kaydedin

```csharp
scene.Save("Your Output Directory" + "UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

3B sahneyi kaydederken sıkıştırmayı devre dışı bırakarak net bir çıktı yolu ve dosya adı sağlayın.

## Çözüm

Bu eğitimde Aspose.3D for .NET kullanarak 3D sahneleri yükleme, kaydetme ve sıkıştırmanın temel yönlerini inceledik. Bu bilgiyle donanmış olarak, kendi 3D yolculuğunuza çıkmaya ve Aspose.3D dünyasındaki yaratıcı olanakları ortaya çıkarmaya hazırsınız.

## SSS'ler

### S1: Aspose.3D çeşitli 3D dosya formatlarıyla uyumlu mudur?

Cevap1: Evet, Aspose.3D çok çeşitli 3D dosya formatlarını destekleyerek projelerinizde esneklik sağlar.

### S2: Aspose.3D'yi diğer .NET kütüphaneleriyle entegre edebilir miyim?

A2: Kesinlikle! Aspose.3D, diğer .NET kitaplıklarıyla sorunsuz bir şekilde bütünleşerek uygulamalarınızın yeteneklerini artırır.

### S3: Aspose.3D için nasıl geçici lisans alabilirim?

 A3: Ziyaret edin[geçici lisans](https://purchase.aspose.com/temporary-license/) Geçici bir lisans almak için Aspose web sitesindeki sayfaya gidin.

### S4: Nereden yardım alabilirim veya toplulukla bağlantı kurabilirim?

 Cevap4: Canlı Aspose.3D topluluğuna katılın[forum](https://forum.aspose.com/c/3d/18) destek aramak, deneyimleri paylaşmak ve diğer meraklılarla işbirliği yapmak.

### S5: Aspose.3D'nin ücretsiz deneme sürümü mevcut mu?

 C5: Evet, Aspose.3D'nin özelliklerini, cihazınızı alarak keşfedin.[ücretsiz deneme](https://releases.aspose.com/) Bugün!