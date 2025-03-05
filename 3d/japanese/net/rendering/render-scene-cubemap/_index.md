---
title: シーンを 6 つの面を持つキューブマップにレンダリングする
linktitle: シーンを 6 つの面を持つキューブマップにレンダリングする
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、素晴らしいキューブマップを作成します。 3D シーンを魅力的な 6 面のキューブマップにレンダリングするためのステップバイステップ ガイドに従ってください。
type: docs
weight: 14
url: /ja/net/rendering/render-scene-cubemap/
---
## 導入
Aspose.3D for .NET を使用してシーンを 6 つの面を持つキューブマップにレンダリングするためのこのステップバイステップ ガイドへようこそ。このチュートリアルでは、3D シーンをレンダリングして見事なキューブマップを作成するプロセスを説明します。 Aspose.3D は、3D グラフィックスの操作を簡素化する強力な .NET API です。このガイドでは、その機能を活用して魅力的なキューブマップを作成します。
## 前提条件
チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。
- C# および .NET 開発の実践的な知識。
-  Aspose.3D for .NET がインストールされています。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).
- レンダリング用の GLB 形式の 3D シーン ファイル (「VirtualCity.glb」など)。
## 名前空間のインポート
まず、Aspose.3D に必要な名前空間を C# コードにインポートします。
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
## ステップ 1: シーンをロードする
次のコードを使用して 3D シーン ファイルをロードします。
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## ステップ 2: カメラとライトを作成する
シーンを照らすカメラと 2 つのライトを作成します。
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
## ステップ 3: レンダラーとレンダー ターゲットを作成する
レンダラーと深度テクスチャを使用したキューブ マップ レンダー ターゲットを作成します。
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## ステップ 4: キューブマップの面を保存する
キューブマップの各面を指定したファイル名でディスクに保存します。
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
## 結論
おめでとう！ Aspose.3D for .NET を使用して 3D シーンをキューブマップにレンダリングすることに成功しました。この強力な API を使用して、さらにカスタマイズ オプションを検討し、3D グラフィックス プロジェクトを強化します。
## よくある質問
### Q: Aspose.3D for .NET を他の 3D ファイル形式で使用できますか?
はい、Aspose.3D はさまざまな 3D ファイル形式をサポートしており、プロジェクトに柔軟性をもたらします。
### Q: Aspose.3D のサポートを受けるにはどうすればよいですか?
訪問[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。
### Q: 無料トライアルはありますか?
はい、無料トライアルにアクセスできます[ここ](https://releases.aspose.com/).
### Q: Aspose.3D を使用してアニメーション付きのシーンをレンダリングできますか?
絶対に！ Aspose.3D は、アニメーション 3D シーンのレンダリングをサポートしています。
### Q: 詳細なドキュメントはどこで入手できますか?
を参照してください。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/net/)詳細な情報については。