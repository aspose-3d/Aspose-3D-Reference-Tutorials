---
title: Aspose.3D for .NET ile Balıkgözü Lens Efekti Uygulama
linktitle: 3D Sahneye Balıkgözü Lens Efekti Uygulama
second_title: Aspose.3D .NET API'si
description: 3D sahnelerinizi Aspose.3D for .NET ile geliştirin! Büyüleyici bir balıkgözü lens efektini adım adım nasıl uygulayacağınızı öğrenin. Şimdi İndirin!
weight: 12
url: /tr/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile Balıkgözü Lens Efekti Uygulama

## giriiş
3D sahnelerinizin görsel çekiciliğini arttırmak mı istiyorsunuz? Aspose.3D for .NET ile balık gözü lens efektlerinin büyüleyici dünyasına dalın. Bu eğitim, balıkgözü lens efektini 3D sahnelerinize nasıl uygulayacağınız konusunda size adım adım rehberlik edecek ve onlara benzersiz ve büyüleyici bir perspektif kazandıracaktır.
## Önkoşullar
Başlamadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:
-  Aspose.3D for .NET: Aspose.3D for .NET kütüphanesinin kurulu olduğundan emin olun. Değilse indirebilirsiniz[Burada](https://releases.aspose.com/3d/net/).
-  Örnek 3B Sahne: Örnek bir 3B sahne dosyasıyla (VirtualCity.glb) çalışacağız. Kendi sahnenizi kullanabilir veya örneği şuradan indirebilirsiniz:[Aspose.3D belgeleri](https://reference.aspose.com/3d/net/).
## Ad Alanlarını İçe Aktar
.NET projenize Aspose.3D işlevlerine erişmek için gerekli ad alanlarını ekleyin. Kodunuzun başına aşağıdaki ad alanlarını ekleyin:
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
Aşağıdaki kodu kullanarak 3B sahne dosyasını projenize yükleyin:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2. Adım: Kamerayı ve Işıkları Ayarlayın
Sahnenizin görsel yönlerini geliştirmek için bir kamera ve ışıklar oluşturun. NearPlane, FarPlane ve RotationMode gibi parametreleri gerektiği gibi ayarlayın:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## 3. Adım: Oluşturucu ve İşleme Hedefleri Oluşturun
Oluşturucuyu kurun ve küp haritası ve 2B doku için oluşturma hedefleri oluşturun:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Adım 4: Balıkgözü Lens Efektini Uygulayın
İşlenen küp haritasında balıkgözü mercek efekti son işlemesini yürütün:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak 3D sahnenize başarıyla balıkgözü lens efekti uyguladınız. Yaratıcılığınızı ortaya çıkarmak için farklı sahneler ve parametrelerle denemeler yapın.
## Sıkça Sorulan Sorular
### Balık gözü efektini herhangi bir 3D sahneye uygulayabilir miyim?
Evet, balık gözü efektini herhangi bir 3D sahneye uygulayabilirsiniz. En iyi sonuçları elde etmek için sahnenin düzgün şekilde yüklendiğinden ve aydınlatıldığından emin olun.
### Görüş alanını (fov) 360 dereceye ayarlamanın önemi nedir?
360 derecelik görüş alanı, tam bir küresel projeksiyon sağlayarak çarpıcı bir balık gözü efekti yaratır.
### 3D sahnemdeki aydınlatmayı nasıl özelleştirebilirim?
İstenilen aydınlatma efektlerini elde etmek için ışıkların konum, tür ve renk gibi özelliklerini ayarlayabilirsiniz.
### İşlenebilecek 3 boyutlu sahnenin boyutunda bir sınır var mı?
3B sahnenin boyutu öncelikle sistem kaynaklarıyla sınırlıdır. Donanımınızın sahnenizin boyutunu karşılayabileceğinden emin olun.
### Balık gözü efekti sonucu için PNG yerine farklı bir çıktı formatı kullanabilir miyim?
Evet, çıktıyı ihtiyaçlarınıza göre farklı görüntü formatlarında kaydetmek için kodu değiştirebilirsiniz.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
