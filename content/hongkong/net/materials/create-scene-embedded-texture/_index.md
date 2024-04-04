---
title: 建立帶有嵌入紋理的場景
linktitle: 建立帶有嵌入紋理的場景
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 創建具有嵌入紋理的迷人 3D 場景。按照我們的逐步指南獲得令人驚嘆的結果。
type: docs
weight: 10
url: /zh-hant/net/materials/create-scene-embedded-texture/
---
## 介紹
歡迎來到 Aspose.3D for .NET 令人興奮的 3D 圖形世界！在這個綜合教程中，我們將引導您完成使用 Aspose.3D 創建令人驚嘆的帶有嵌入紋理的 3D 場景的過程，Aspose.3D 是一個面向 .NET 開發人員的強大且多功能的庫。
## 先決條件
在深入學習本教程之前，請確保您具備以下先決條件：
- 對 C# 和 .NET 程式設計有基本了解。
- Visual Studio 安裝在您的電腦上。
- Aspose.3D for .NET 函式庫，您可以下載[這裡](https://releases.aspose.com/3d/net/).
- 熟悉 3D 圖形和場景創建的概念。
## 導入命名空間
首先將必要的命名空間匯入到您的專案中。這些命名空間將為您提供 3D 圖形操作所需的工具和功能。
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
## 第 1 步：建立場景
首先使用 Aspose.3D for .NET 建立一個新的 3D 場景。這將作為您的 3D 傑作的畫布。
```csharp
//創建帶有嵌入紋理的 FBX 文件
Scene scene = new Scene();
```
## 第 2 步：建立嵌入紋理
現在，讓我們透過嵌入紋理為場景添加一些視覺效果。我們將創建一個具有自訂內容的紋理並為其指定一個檔案名稱。
```csharp
//建立嵌入紋理
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //如果使用嵌入紋理，則需要檔案名稱。
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## 第 3 步：創建材質
接下來，為 3D 物件建立材質，結合先前建立的紋理和自訂屬性。
```csharp
//建立具有自訂屬性的材質
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## 第 4 步：建立 3D 對象
現在，讓我們透過添加 3D 物件來讓您的場景變得栩栩如生。在此範例中，我們將使用圓環並應用您剛剛建立的材質。
```csharp
//使用先前建立的材質建立一個圓環
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## 第 5 步：儲存場景
最後，將您的傑作保存到文件中。在此範例中，我們將其儲存為 FBX 格式。
```csharp
//將場景儲存到檔案中
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
恭喜！您已使用 Aspose.3D for .NET 成功建立了具有嵌入紋理的 3D 場景。
## 建立紋理內容原始碼
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
## 結論
在本教程中，我們探索了使用 Aspose.3D for .NET 創建具有嵌入紋理的視覺效果令人驚嘆的 3D 場景的基礎知識。有了這些知識，您就可以釋放您的創造力並建立迷人的 3D 應用程式。

## 經常問的問題

### Q：我可以將 Aspose.3D for .NET 與其他程式語言一起使用嗎？
答：Aspose.3D 主要是為 .NET 設計的，但也有適用於其他語言的類似函式庫。
### Q：如何將動畫應用到我的 3D 場景？
A：Aspose.3D提供動畫功能；請參閱文件以取得詳細說明。
### Q：Aspose.3D for .NET 有試用版嗎？
答：是的，您可以下載試用版[這裡](https://releases.aspose.com/).
### Q：我可以在哪裡找到更多支援和資源？
答：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)以獲得社區支持和討論。
### Q：我可以將 Aspose.3D 用於商業項目嗎？
答：是的，您可以購買許可證[這裡](https://purchase.aspose.com/buy).