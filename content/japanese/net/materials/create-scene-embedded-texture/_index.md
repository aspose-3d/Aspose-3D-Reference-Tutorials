---
title: テクスチャが埋め込まれたシーンの作成
linktitle: テクスチャが埋め込まれたシーンの作成
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、テクスチャが埋め込まれた魅力的な 3D シーンを作成します。素晴らしい結果を得るには、ステップバイステップのガイドに従ってください。
type: docs
weight: 10
url: /ja/net/materials/create-scene-embedded-texture/
---
## 導入
Aspose.3D for .NET を使用したエキサイティングな 3D グラフィックスの世界へようこそ!この包括的なチュートリアルでは、.NET 開発者向けの強力で多用途なライブラリである Aspose.3D を使用して、テクスチャが埋め込まれた見事な 3D シーンを作成するプロセスを説明します。
## 前提条件
チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。
- C# および .NET プログラミングの基本的な理解。
- Visual Studio がマシンにインストールされていること。
- Aspose.3D for .NET ライブラリ (ダウンロード可能)[ここ](https://releases.aspose.com/3d/net/).
- 3D グラフィックスとシーン作成の概念に精通していること。
## 名前空間のインポート
まず、必要な名前空間をプロジェクトにインポートします。これらの名前空間は、3D グラフィックスの操作に必要なツールと機能を提供します。
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
## ステップ 1: シーンの作成
まず、Aspose.3D for .NET を使用して新しい 3D シーンを作成します。これは、3D 傑作のキャンバスとして機能します。
```csharp
//テクスチャが埋め込まれた FBX ファイルを作成する
Scene scene = new Scene();
```
## ステップ 2: 埋め込みテクスチャの作成
次に、テクスチャを埋め込んでシーンに視覚的なセンスを加えてみましょう。カスタム コンテンツを含むテクスチャを作成し、ファイル名を割り当てます。
```csharp
//埋め込みテクスチャを作成する
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //埋め込みテクスチャを使用する場合はファイル名が必要です。
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## ステップ 3: マテリアルの作成
次に、以前に作成したテクスチャとカスタム プロパティを組み込んだ 3D オブジェクトのマテリアルを作成します。
```csharp
//カスタムプロパティを使用してマテリアルを作成する
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## ステップ 4: 3D オブジェクトの作成
次に、3D オブジェクトを追加してシーンに命を吹き込みましょう。この例では、トーラスを使用し、作成したマテリアルを適用します。
```csharp
//以前に作成したマテリアルを適用してトーラスを作成する
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## ステップ 5: シーンを保存する
最後に、傑作をファイルに保存します。この例では、FBX 形式で保存します。
```csharp
//シーンをファイルに保存する
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
おめでとう！ Aspose.3D for .NET を使用して、テクスチャが埋め込まれた 3D シーンを正常に作成できました。
## CreateTextureContent ソース コード
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
このチュートリアルでは、Aspose.3D for .NET を使用して、テクスチャが埋め込まれた視覚的に素晴らしい 3D シーンを作成する基本を学びました。この知識を活用すれば、創造性を発揮して魅力的な 3D アプリケーションを構築できます。

## よくある質問

### Q: Aspose.3D for .NET を他のプログラミング言語で使用できますか?
A: Aspose.3D は主に .NET 用に設計されていますが、他の言語でも使用できる同様のライブラリがあります。
### Q: 3D シーンにアニメーションを適用するにはどうすればよいですか?
A: Aspose.3D はアニメーション機能を提供します。詳細な手順については、ドキュメントを参照してください。
### Q: Aspose.3D for .NET の試用版はありますか?
 A: はい、試用版をダウンロードできます。[ここ](https://releases.aspose.com/).
### Q: 追加のサポートやリソースはどこで入手できますか?
 A: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。
### Q: Aspose.3D を商用プロジェクトに使用できますか?
 A: はい、ライセンスを購入できます。[ここ](https://purchase.aspose.com/buy).