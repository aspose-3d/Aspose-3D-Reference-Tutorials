---
title: 3D Sahnelerde Görüntü Alanlarını Yakalama
linktitle: 3D Sahnelerde Görüntü Alanlarını Yakalama
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak büyüleyici 3D görünüm pencereleri yakalamayı öğrenin. Sahneleri esnek bir şekilde işlemek için adım adım kılavuz.
type: docs
weight: 11
url: /tr/net/3d-viewports/capture-viewport/
---
## giriiş

3D grafikler ve görselleştirme alanında, görüntü pencerelerini yakalamak, sahnelerinizin derinliğini ve ayrıntısını artıran önemli bir beceridir. Aspose.3D for .NET, 3D sahnelerin işlenmesi ve işlenmesi için güçlü bir çözüm sunar. Bu eğitim, Aspose.3D'yi kullanarak 3D sahnelerdeki görüntü pencerelerini yakalama sürecinde size rehberlik edecek ve kolaylıkla çarpıcı görselleştirmeler oluşturmanıza olanak tanıyacak.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

-  Aspose.3D for .NET Library: Aspose.3D kütüphanesinin kurulu olduğundan emin olun. Şuradan indirebilirsiniz[Burada](https://releases.aspose.com/3d/net/).

## Ad Alanlarını İçe Aktar

Başlamak için gerekli ad alanlarını .NET projenize aktarın:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## 1. Adım: Mevcut bir 3D Sahneyi Yükleyin

Mevcut bir 3B sahneyi projenize yükleyerek başlayın. Aşağıdaki kod parçacığı bunu göstermektedir:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## 2. Adım: Kamera Oluşturun

Ardından kameranın bir örneğini oluşturun ve konumunu ve hedefini ayarlayın:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## 3. Adım: Sahneye Aydınlatma Ekleyin

Bir ışık kaynağı ekleyerek sahnenizi geliştirin. Aşağıdaki kod parçacığı, nokta ışığının nasıl oluşturulacağını gösterir:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Adım 4: Oluşturucuyu ve İşleme Hedefini Yapılandırın

Oluşturucuyu kurun ve sahneyi yakalamak için bir oluşturma hedefi oluşturun:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (sonraki adımlarda devam)
    }
}
```

## Adım 5: Görünüm Pencerelerini Tanımlayın ve Oluşturun

Görünüm pencerelerini tanımlayın ve çıktı görüntüleri oluşturmak için sahneyi işleyin:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Adım 6: Görünümleri Değiştirin ve Yeniden Oluşturun

Aspose.3D'nin esnekliğini göstererek görünüm pencerelerini değiştirin ve sahneyi bir kez daha işleyin:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

İstenilen görsel efektleri elde etmek için farklı konfigürasyonlarla denemeler yapmaya devam edin.

## Çözüm

Bu eğitimde Aspose.3D for .NET'i kullanarak 3D sahnelerde görünüm yakalama sürecini araştırdık. Güçlü özelliklerinden yararlanarak, 3D grafik projelerinizi yeni boyutlara taşıyarak büyüleyici görsel deneyimler sağlayabilirsiniz.

## SSS'ler

### S1: Aspose.3D diğer 3D dosya formatlarıyla uyumlu mudur?

Cevap1: Evet, Aspose.3D çeşitli 3D dosya formatlarını destekleyerek çok çeşitli tasarım araçlarıyla uyumluluk sağlar.

### S2: Aspose.3D'yi oyun geliştirme için kullanabilir miyim?

Cevap2: Aspose.3D öncelikle grafik ve görselleştirme için tasarlanmış olsa da, işlevleri oyun geliştirmenin belirli yönlerini tamamlayabilir.

### S3: Ek örnekleri ve belgeleri nerede bulabilirim?

 A3: Kapsamlı olanı keşfedin[Aspose.3D belgeleri](https://reference.aspose.com/3d/net/) Daha fazla örnek ve detaylı bilgi için.

### S4: Ücretsiz deneme sürümü mevcut mu?

 Cevap4: Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).

### S5: Nasıl yardım isteyebilirim veya topluluğa nasıl katılabilirim?

 Cevap5: Aspose.3D topluluğuna katılın[destek Forumu](https://forum.aspose.com/c/3d/18) yardım ve işbirliği için.