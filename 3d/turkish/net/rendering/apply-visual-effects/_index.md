---
title: 3B Görünüm Pencerelerinde Görsel Efekt Uygulama
linktitle: 3B Görünüm Pencerelerinde Görsel Efekt Uygulama
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D görselleştirme dünyasını keşfedin. Adım adım eğitimleri kullanarak sahnelerinize büyüleyici görsel efektler uygulamayı öğrenin. Projelerinizi pikselleştirme, gri tonlama, kenar algılama ve bulanıklaştırma efektleriyle geliştirin.
weight: 10
url: /tr/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3B Görünüm Pencerelerinde Görsel Efekt Uygulama

## giriiş

3D sahnelerin görsel çekiciliğini artırmak, sürükleyici deneyimler yaratmanın çok önemli bir yönüdür. Aspose.3D for .NET, 3D görünüm pencerelerine görsel efektler uygulamak için güçlü bir araç seti sağlar. Bu eğitimde pikselleştirme, gri tonlama, kenar algılama ve bulanıklık dahil olmak üzere 3 boyutlu bir sahneye çeşitli efektler uygulama sürecini ele alacağız.

## Önkoşullar

Eğiticiye dalmadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- C# ve .NET geliştirme konusunda çalışma bilgisi.
-  Aspose.3D for .NET kütüphanesi kuruldu. Şuradan indirebilirsiniz[Burada](https://releases.aspose.com/3d/net/).
- Deneme amaçlı bir 3 boyutlu sahne dosyası (örneğin, "scene.obj").

## Ad Alanlarını İçe Aktar

Başlamak için Aspose.3D ve diğer bağımlılıklar için gerekli ad alanlarını içe aktarın. Kodunuza aşağıdaki satırları ekleyin:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 3D sahnenizi kullanarak yükleyin.`Scene` sınıf.

## 2. Adım: Kamera Oluşturun

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Bir kamera örneği oluşturun ve konumunu ve hedefini ayarlayın.

## 3. Adım: Sahneye Işık Ekleyin

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Görsel efektleri geliştirmek için aydınlatmayı kullanın.

## Adım 4: Oluşturucu Oluşturun ve Oluşturma Hedefi

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Oluşturucu ayarlarını yapılandırma
    renderer.EnableShadows = false;

    // Oluşturma hedefi oluşturma
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Görünüm penceresini yapılandır
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Sahneyi dokuya dönüştürün
        renderer.Render(rt);

        // İşlenen dokuyu bir dosyaya kaydedin
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // İşlem sonrası efektlerle devam edin...
    }
}
```

Sahneyi yakalamak için bir oluşturucu ve oluşturma hedefi oluşturun.

## Adım 5: İşlem Sonrası Efektleri Uygulayın

### Adım 5.1 Pikselleştirme Etkisi

```csharp
// Pikselleştirme efekti oluştur
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Pikselleştirme efekti uygulayın ve sonucu kaydedin.

### Adım 5.2 Gri Tonlama Efekti

```csharp
// Gri tonlama efekti oluştur
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Gri tonlama efekti uygulayın ve sonucu kaydedin.

### Adım 5.3 Efektleri Birleştir

```csharp
// Gri tonlama ve pikselleştirme efektlerini birleştirin
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Benzersiz sonuçlar için birden fazla efekti birleştirin.

### Adım 5.4 Kenar Algılama Etkisi

```csharp
// Kenar algılama efekti oluştur
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Kenar algılama efektini uygulayın ve sonucu kaydedin.

### Adım 5.5 Bulanıklaştırma Efekti

```csharp
// Bulanıklaştırma efekti oluştur
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Bulanıklaştırma efekti uygulayın ve sonucu kaydedin.

## Çözüm

3B görünüm pencerelerinde görsel efektlerle denemeler yapmak, sahnelerinize derinlik ve yaratıcılık katar. Aspose.3D for .NET, projelerinizi geliştirecek bir dizi işlem sonrası efekt sunarak bu süreci basitleştirir.

## SSS'ler

### S1: Aynı anda birden fazla efekt uygulayabilir miyim?

Cevap1: Evet, benzersiz ve karmaşık sonuçlar için farklı işleme sonrası efektleri birleştirebilirsiniz.

### S2: Görsel efektlerin yoğunluğunu nasıl ayarlayabilirim?

Cevap2: Her efektin yoğunluğunu kontrol etmek için ayarlayabileceğiniz parametreler olabilir. Belirli ayrıntılar için belgelere bakın.

### S3: Aspose.3D oyun geliştirmeye uygun mu?

Cevap3: Aspose.3D öncelikle 3D modelleme ve renderleme için tasarlanmış olsa da oyun geliştirmenin belirli yönlerinde kullanılabilir.

### S4: Ek işleme sonrası efektler mevcut mu?

Cevap4: Aspose.3D çeşitli yerleşik işlem sonrası efektler sağlar ve kitaplığı kullanarak özel efektler oluşturabilirsiniz.

### S5: Aspose.3D'yi ticari projeler için kullanabilir miyim?

 Cevap5: Evet, Aspose.3D'yi ticari amaçlarla kullanabilirsiniz. Bakın[satın alma sayfası](https://purchase.aspose.com/buy) lisans ayrıntıları için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
