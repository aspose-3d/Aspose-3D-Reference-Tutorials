---
title: 3D'yi PDF'ye kaydetme
linktitle: 3D'yi PDF'ye kaydetme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i keşfedin. Kusursuz 3D modelleme ve işleme için başvurulacak kitaplığınız. 3D modelleri zahmetsizce PDF'ye kaydedin.
type: docs
weight: 19
url: /tr/net/loading-and-saving/pdf/save-3d-in-pdf/
---
## giriiş

Aspose.3D for .NET kullanımına ilişkin kapsamlı kılavuzumuza hoş geldiniz! Bu eğitimde, bir 3B modeli PDF formatında kaydetme görevine odaklanarak, 3B modelleri yükleme ve kaydetme sürecinde size yol göstereceğiz. Aspose.3D for .NET, 3D dosyalarla çalışmak için etkili araçlar sağlayan güçlü bir kütüphanedir ve bu da onu bu alandaki geliştiriciler ve meraklılar için önemli bir kaynak haline getirir.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET: Kitaplığın kurulu olduğundan emin olun. Değilse, adresinden indirebilirsiniz.[Aspose.3D for .NET belgeleri](https://reference.aspose.com/3d/net/).

- Geliştirme Ortamı: Tercih ettiğiniz .NET geliştirme ortamını kurun.

- 3D Kavramların Temel Anlaşılması: Bu kılavuz 3D modellemeye ilişkin temel bilgileri varsaydığından, temel 3D kavramlarına aşina olun.

## Ad Alanlarını İçe Aktar

.NET projenizde Aspose.3D tarafından sağlanan işlevlere erişmek için gerekli ad alanlarını içe aktardığınızdan emin olun:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## 1. Adım: Yeni Bir Sahne Yaratın

Aspose.3D kütüphanesini kullanarak yeni bir 3D sahneyi başlatarak başlayın. Bu, 3D modelinizin temelini oluşturur.

```csharp
Scene scene = new Scene();
```

## Adım 2: Silindir Alt Düğümü Ekleme

Kaydetme sürecini göstermek için basit bir 3 boyutlu model (silindir) oluşturalım. Sahneye alt düğüm olarak bir silindir ekleyin.

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## Adım 3: Oluşturma Modunu ve Aydınlatma Düzenini Ayarlayın

3B sahneniz için işleme modunu ve aydınlatma düzenini tanımlayın. Bu adım, modelinizin görsel görünümünü özelleştirmenize olanak tanır.

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## 4. Adım: PDF Formatında Kaydetme

Son olarak çıktı dizinini ve dosya adını belirterek kaydetme işlemini gerçekleştirin. Bu durumda 3D modeli PDF formatında kaydediyoruz.

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

"Çıktı Dizininiz"i istediğiniz yolla değiştirdiğinizden emin olun.

## Çözüm

 Tebrikler! Basit bir 3D model oluşturmak ve bunu PDF formatında kaydetmek için Aspose.3D for .NET'i nasıl kullanacağınızı başarıyla öğrendiniz. Bu, bu güçlü kütüphaneyle başarabileceklerinizin sadece başlangıcı. Daha fazla özellik ve olasılığı keşfedin[Aspose.3D belgeleri](https://reference.aspose.com/3d/net/).

## SSS'ler

### S1: Aspose.3D for .NET tüm 3D dosya formatlarıyla uyumlu mudur?

C1: Evet, Aspose.3D for .NET çok çeşitli 3D dosya formatlarını destekleyerek çeşitli endüstri standartlarıyla uyumluluk sağlar.

### S2: Kaydetme işlemi sırasında 3D modelimin görsel yönlerini özelleştirebilir miyim?

A2: Kesinlikle! Öğreticide gösterildiği gibi, istenen görsel sonuca ulaşmak için oluşturma modlarını, aydınlatma düzenlerini ve daha fazlasını ayarlayabilirsiniz.

### S3: Aspose.3D for .NET desteğini nerede bulabilirim?

 A3: Ziyaret edin[Aspose.3D Forumu](https://forum.aspose.com/c/3d/18) Aspose.3D for .NET ile ilgili topluluk desteği ve tartışmalar için.

### S4: Aspose.3D for .NET'in ücretsiz deneme sürümü mevcut mu?

 A4: Evet, erişebilirsiniz[ücretsiz deneme](https://releases.aspose.com/) satın almadan önce Aspose.3D for .NET'in özelliklerini keşfetmek için.

### S5: Aspose.3D for .NET için nasıl geçici lisans alabilirim?

 Cevap5: Geçici lisans almak için şu adresi ziyaret edin:[bu bağlantı](https://purchase.aspose.com/temporary-license/) ve verilen talimatları izleyin.