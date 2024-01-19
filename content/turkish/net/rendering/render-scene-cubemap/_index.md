---
title: Sahneyi Altı Yüzlü Küp Haritasına Dönüştürme
linktitle: Sahneyi Altı Yüzlü Küp Haritasına Dönüştürme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile etkileyici küp haritaları oluşturun. 3B sahneleri büyüleyici altı yüzlü küp haritalarına dönüştürmek için adım adım kılavuzumuzu izleyin.
type: docs
weight: 14
url: /tr/net/rendering/render-scene-cubemap/
---
## giriiş
Aspose.3D for .NET kullanarak bir sahneyi altı yüzlü bir küp haritasına dönüştürmeyi anlatan bu adım adım kılavuza hoş geldiniz. Bu eğitimde, bir 3B sahneyi işleyerek çarpıcı bir küp haritası oluşturma sürecinde size yol göstereceğiz. Aspose.3D, 3D grafik manipülasyonunu basitleştiren güçlü bir .NET API'sidir ve bu kılavuzla, büyüleyici küp haritaları oluşturmak için onun yeteneklerinden yararlanacaksınız.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:
- C# ve .NET geliştirme konusunda çalışma bilgisi.
-  Aspose.3D for .NET kuruldu. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).
- İşleme için GLB formatında bir 3B sahne dosyası (örneğin, "VirtualCity.glb").
## Ad Alanlarını İçe Aktar
Aspose.3D için gerekli ad alanlarını C# kodunuza aktararak başlayın:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## 1. Adım: Sahneyi Yükleyin
Aşağıdaki kodu kullanarak 3B sahne dosyasını yükleyin:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2. Adım: Kamera ve Işıklar Oluşturun
Sahneyi aydınlatmak için bir kamera ve iki ışık oluşturun:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Adım 3: Oluşturucu ve İşleme Hedefi Oluşturun
Derinlik dokusuna sahip bir oluşturucu ve küp haritası oluşturma hedefi oluşturun:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## 4. Adım: Küp Haritası Yüzlerini Kaydetme
Küp haritasının her yüzünü belirtilen dosya adlarıyla diske kaydedin:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak 3 boyutlu bir sahneyi başarıyla küp haritasına dönüştürdünüz. Bu güçlü API ile daha fazla özelleştirme seçeneklerini keşfedin ve 3D grafik projelerinizi geliştirin.
## Sıkça Sorulan Sorular
### S: Aspose.3D for .NET'i diğer 3D dosya formatlarıyla kullanabilir miyim?
Evet, Aspose.3D çeşitli 3D dosya formatlarını destekleyerek projelerinizde esneklik sağlar.
### S: Aspose.3D için nasıl destek alabilirim?
 Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.
### S: Ücretsiz deneme mevcut mu?
 Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).
### S: Aspose.3D'yi kullanarak animasyonlu sahneleri işleyebilir miyim?
Kesinlikle! Aspose.3D, animasyonlu 3D sahnelerin oluşturulmasını destekler.
### S: Ayrıntılı belgeleri nerede bulabilirim?
 Bakın[Aspose.3D belgeleri](https://reference.aspose.com/3d/net/) derinlemesine bilgi için.