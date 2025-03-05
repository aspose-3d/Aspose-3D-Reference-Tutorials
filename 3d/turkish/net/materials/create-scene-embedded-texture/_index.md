---
title: Gömülü Dokuyla Sahne Oluşturma
linktitle: Gömülü Dokuyla Sahne Oluşturma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i kullanarak gömülü dokularla büyüleyici 3D sahneler oluşturun. Çarpıcı sonuçlar için adım adım kılavuzumuzu izleyin.
type: docs
weight: 10
url: /tr/net/materials/create-scene-embedded-texture/
---
## giriiş
Aspose.3D for .NET ile 3D grafiklerin heyecan verici dünyasına hoş geldiniz! Bu kapsamlı eğitimde, .NET geliştiricileri için güçlü ve çok yönlü bir kütüphane olan Aspose.3D'yi kullanarak, gömülü dokularla büyüleyici 3D sahneler oluşturma sürecinde size rehberlik edeceğiz.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:
- C# ve .NET programlamanın temel anlayışı.
- Makinenizde Visual Studio yüklü.
- İndirebileceğiniz Aspose.3D for .NET kütüphanesi[Burada](https://releases.aspose.com/3d/net/).
- 3D grafik ve sahne oluşturma kavramlarına aşinalık.
## Ad Alanlarını İçe Aktar
Gerekli ad alanlarını projenize aktararak başlayın. Bu ad alanları size 3B grafik manipülasyonu için gerekli araçları ve işlevleri sağlayacaktır.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Adım 1: Sahne Oluşturma
Aspose.3D for .NET'i kullanarak yeni bir 3D sahne oluşturarak başlayın. Bu, 3D şaheseriniz için tuval görevi görecek.
```csharp
// Gömülü dokulara sahip bir FBX dosyası oluşturun
Scene scene = new Scene();
```
## Adım 2: Gömülü Doku Oluşturma
Şimdi bir doku yerleştirerek sahnenize görsel bir hava katalım. Özel içeriğe sahip bir doku oluşturacağız ve ona bir dosya adı atayacağız.
```csharp
// Gömülü bir doku oluşturma
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //Gömülü doku kullanılıyorsa dosya adı gereklidir.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Adım 3: Materyal Oluşturma
Daha sonra, 3B nesneleriniz için önceden oluşturulmuş doku ve özel özellikleri birleştirerek bir malzeme oluşturun.
```csharp
// Özel özelliğe sahip bir malzeme oluşturun
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Adım 4: 3B Nesne Oluşturma
Şimdi 3 boyutlu bir nesne ekleyerek sahnenize hayat verelim. Bu örnekte bir torus kullanacağız ve yeni oluşturduğunuz malzemeyi uygulayacağız.
```csharp
// Daha önce oluşturulan malzemenin uygulandığı bir simit oluşturun
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Adım 5: Sahneyi Kaydetme
Son olarak şaheserinizi bir dosyaya kaydedin. Bu örnekte onu FBX formatında kaydedeceğiz.
```csharp
// Sahneyi bir dosyaya kaydedin
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Tebrikler! Aspose.3D for .NET'i kullanarak gömülü dokulara sahip bir 3D sahneyi başarıyla oluşturdunuz.
## CreateTextureContent Kaynak Kodu
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Çözüm
Bu eğitimde Aspose.3D for .NET'i kullanarak gömülü dokularla görsel olarak büyüleyici 3D sahneler oluşturmanın temellerini araştırdık. Bu bilgiyle donanmış olarak yaratıcılığınızı serbest bırakabilir ve büyüleyici 3D uygulamalar oluşturabilirsiniz.

## Sıkça Sorulan Sorular

### S: Aspose.3D for .NET'i diğer programlama dilleriyle birlikte kullanabilir miyim?
C: Aspose.3D öncelikle .NET için tasarlanmıştır ancak diğer diller için de benzer kütüphaneler mevcuttur.
### S: Animasyonları 3B sahnelerime nasıl uygulayabilirim?
C: Aspose.3D animasyon yetenekleri sağlar; ayrıntılı talimatlar için belgelere bakın.
### S: Aspose.3D for .NET'in deneme sürümü mevcut mu?
 C: Evet, deneme sürümünü indirebilirsiniz[Burada](https://releases.aspose.com/).
### S: Ek destek ve kaynakları nerede bulabilirim?
 C: Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.
### S: Aspose.3D'yi ticari projeler için kullanabilir miyim?
 C: Evet, lisans satın alabilirsiniz[Burada](https://purchase.aspose.com/buy).