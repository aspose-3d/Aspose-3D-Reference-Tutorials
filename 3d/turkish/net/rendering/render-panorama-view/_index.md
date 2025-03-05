---
title: Aspose.3D for .NET ile 3D Panoramaları Kolayca İşleyin
linktitle: 3D Sahnenin Panoramik Görünümünün Oluşturulması
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak büyüleyici 3D panorama görünümlerini nasıl oluşturacağınızı öğrenin. Sürükleyici sahne oluşturma için adım adım kılavuzumuzu izleyin.
type: docs
weight: 13
url: /tr/net/rendering/render-panorama-view/
---
## giriiş
Büyüleyici 3 boyutlu sahneler oluşturmak ve bunları panoramik görüntülere dönüştürmek, modern uygulamaların önemli bir unsuru haline geldi. Aspose.3D for .NET, 3D işleme yeteneklerini projelerine sorunsuz bir şekilde entegre etmek isteyen geliştiriciler için güçlü bir çözüm sunar. Bu eğitimde Aspose.3D for .NET kullanarak 3 boyutlu bir sahnenin panorama görünümünü oluşturma sürecini inceleyeceğiz.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:
-  Aspose.3D for .NET: Aspose.3D kütüphanesini indirip yükleyin. Kütüphaneyi ve belgeleri bulabilirsiniz[Burada](https://releases.aspose.com/3d/net/).
- .NET Geliştirme Ortamı: Makinenizde çalışan bir .NET geliştirme ortamının kurulu olduğundan emin olun.
- Örnek 3B Sahne: Panorama görünümünü oluşturmak için kullanacağımız "VirtualCity.glb" gibi örnek bir 3B sahne dosyasını indirin.
## Ad Alanlarını İçe Aktar
.NET projenize Aspose.3D ile çalışmak için gerekli ad alanlarını içe aktarın:
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
## 1. Adım: 3D Sahneyi Yükleyin
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
Aspose.3D'yi kullanarak 3D sahneyi yükleyin. "VirtualCity.glb"yi istediğiniz 3D sahne dosyasının yolu ile değiştirin.
## 2. Adım: Kamerayı ve Işıkları Ayarlayın
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
3D sahneyi uygun şekilde yakalamak için kamerayı ve ışıkları ayarlayın.
## 3. Adım: Oluşturucu ve İşleme Hedefleri Oluşturun
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
Bir oluşturucu oluşturun ve küp haritası ve son panoramik görüntü için oluşturma hedeflerini tanımlayın.
## Adım 4: Görünümü ve İşlemeyi Yapılandırma
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
Kamerayı kullanarak görünüm penceresini yapılandırın ve küp haritasını oluşturun.
## Adım 5: Panorama Görünümü için Son İşlemeyi Uygulayın
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
Panoramik görünümü oluşturmak için eşit dikdörtgen projeksiyon son işlemesini uygulayın.
## Adım 6: Oluşturulan Panoramayı Kaydet
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
İşlenen panorama görüntüsünü belirli bir çıktı dizinine kaydedin.
## Çözüm
Aspose.3D for .NET ile 3 boyutlu bir sahnenin panoramik görüntüsünü oluşturmak basit bir süreç haline geliyor. Sürükleyici 3D görselleştirmeleri sorunsuz bir şekilde birleştirerek uygulamalarınızı geliştirin.
## Sıkça Sorulan Sorular
### S: Özel 3D sahnemi panorama oluşturmak için kullanabilir miyim?
Evet, örnek sahne dosyası yolunu özel 3B sahnenizin yolu ile değiştirmeniz yeterlidir.
### S: Ek işleme sonrası efektler mevcut mu?
Aspose.3D for .NET, işlenmiş görüntülerinizi geliştirmek için çeşitli işlem sonrası efektler sağlar.
### S: İşleme performansını nasıl optimize edebilirim?
Uygulamanızın gereksinimlerine göre işleme parametrelerini ve hedef boyutları ayarlayın.
### S: Bu eğitimi bir web uygulamasına entegre edebilir miyim?
Evet, Aspose.3D for .NET'i .NET web projenize dahil ederek.
### S: Aspose.3D desteği için bir topluluk forumu var mı?
 Evet, ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği için.