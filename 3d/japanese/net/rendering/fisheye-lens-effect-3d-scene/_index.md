---
title: Aspose.3D for .NET を使用した魚眼レンズ効果の適用
linktitle: 3D シーンに魚眼レンズ効果を適用する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D シーンを強化しましょう!魅惑的な魚眼レンズ効果を段階的に適用する方法を学びましょう。ダウンロード中！
weight: 12
url: /ja/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET を使用した魚眼レンズ効果の適用

## 導入
3D シーンの視覚的な魅力を強化したいと考えていますか? Aspose.3D for .NET を使用して、魚眼レンズ エフェクトの魅力的な世界に飛び込んでください。このチュートリアルでは、3D シーンに魚眼レンズ エフェクトを適用して、ユニークで魅力的な視点を与える方法を段階的に説明します。
## 前提条件
始める前に、次の前提条件が満たされていることを確認してください。
-  Aspose.3D for .NET: .NET 用の Aspose.3D ライブラリがインストールされていることを確認します。そうでない場合は、ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).
- サンプル 3D シーン: サンプル 3D シーン ファイル (VirtualCity.glb) を使用して作業します。独自のシーンを使用するか、からサンプルをダウンロードできます。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/net/).
## 名前空間のインポート
.NET プロジェクトに、Aspose.3D 機能にアクセスするために必要な名前空間を含めます。コードの先頭に次の名前空間を追加します。
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
## ステップ 1: 3D シーンをロードする
次のコードを使用して、3D シーン ファイルをプロジェクトにロードします。
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## ステップ 2: カメラとライトをセットアップする
カメラとライトを作成して、シーンの視覚的な側面を強化します。必要に応じて、NearPlane、FarPlane、RotationMode などのパラメータを調整します。
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
## ステップ 3: レンダラーとレンダー ターゲットを作成する
レンダラーを設定し、キューブ マップと 2D テクスチャのレンダー ターゲットを作成します。
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## ステップ 4: 魚眼レンズ効果を適用する
レンダリングされたキューブ マップに対して魚眼レンズ エフェクトの後処理を実行します。
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## 結論
おめでとう！ Aspose.3D for .NET を使用して、魚眼レンズ エフェクトを 3D シーンに適用することに成功しました。創造性を発揮するために、さまざまなシーンやパラメータを試してください。
## よくある質問
### 魚眼効果を任意の 3D シーンに適用できますか?
はい、魚眼効果はどの 3D シーンにも適用できます。最適な結果を得るには、シーンが適切にロードされ、照明されていることを確認してください。
### 視野角 (fov) を 360 度に調整する意味は何ですか?
360 度の視野により完全な球状投影が保証され、見事な魚眼効果が得られます。
### 3D シーンの照明をカスタマイズするにはどうすればよいですか?
位置、タイプ、色などのライトのプロパティを調整して、目的の照明効果を実現できます。
### 処理できる 3D シーンのサイズに制限はありますか?
3D シーンのサイズは主にシステム リソースによって制限されます。ハードウェアがシーンのサイズを処理できることを確認してください。
### 魚眼効果の結果に PNG の代わりに別の出力形式を使用できますか?
はい、コードを変更して、要件に基づいて出力をさまざまな画像形式で保存できます。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
