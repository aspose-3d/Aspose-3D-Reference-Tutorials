---
title: Aspose.3D for .NET を使用して 3D パノラマを簡単にレンダリング
linktitle: 3D シーンのパノラマ ビューのレンダリング
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して見事な 3D パノラマ ビューを作成する方法を学びます。没入型シーンのレンダリングについては、ステップバイステップのガイドに従ってください。
weight: 13
url: /ja/net/rendering/render-panorama-view/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET を使用して 3D パノラマを簡単にレンダリング

## 導入
魅力的な 3D シーンを作成し、それをパノラマ ビューにレンダリングすることは、最新のアプリケーションの重要な側面となっています。 Aspose.3D for .NET は、3D レンダリング機能をプロジェクトにシームレスに統合したいと考えている開発者に堅牢なソリューションを提供します。このチュートリアルでは、Aspose.3D for .NET を使用して 3D シーンのパノラマ ビューをレンダリングするプロセスについて説明します。
## 前提条件
チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。
-  Aspose.3D for .NET: Aspose.3D ライブラリをダウンロードしてインストールします。ライブラリとドキュメントを見つけることができます[ここ](https://releases.aspose.com/3d/net/).
- .NET 開発環境: マシン上に動作する .NET 開発環境がセットアップされていることを確認してください。
- サンプル 3D シーン: サンプル 3D シーン ファイル (たとえば、「VirtualCity.glb」) をダウンロードします。これは、パノラマ ビューのレンダリングに使用します。
## 名前空間のインポート
.NET プロジェクトで、Aspose.3D を操作するために必要な名前空間をインポートします。
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
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
Aspose.3D を使用して 3D シーンを読み込みます。 「VirtualCity.glb」を目的の 3D シーン ファイルへのパスに置き換えます。
## ステップ 2: カメラとライトをセットアップする
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
3D シーンを適切にキャプチャするためにカメラとライトをセットアップします。
## ステップ 3: レンダラーとレンダー ターゲットを作成する
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
レンダラーを作成し、キューブ マップと最終的なパノラマ イメージのレンダー ターゲットを定義します。
## ステップ 4: ビューポートとレンダリングを構成する
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
カメラを使用してビューポートを構成し、キューブ マップをレンダリングします。
## ステップ 5: パノラマ ビューの後処理を適用する
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
正距円筒図法の後処理を適用してパノラマ ビューを生成します。
## ステップ 6: レンダリングされたパノラマを保存する
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
レンダリングされたパノラマ イメージを指定した出力ディレクトリに保存します。
## 結論
Aspose.3D for .NET を使用すると、3D シーンのパノラマ ビューのレンダリングが簡単なプロセスになります。没入型 3D ビジュアライゼーションをシームレスに組み込むことで、アプリケーションを強化します。
## よくある質問
### Q: パノラマのレンダリングにカスタム 3D シーンを使用できますか?
はい、サンプル シーン ファイルのパスをカスタム 3D シーンへのパスに置き換えるだけです。
### Q: 追加の後処理エフェクトは利用できますか?
Aspose.3D for .NET は、レンダリングされたイメージを強化するためのさまざまな後処理効果を提供します。
### Q: レンダリング パフォーマンスを最適化するにはどうすればよいですか?
アプリケーションの要件に基づいて、レンダリング パラメータとターゲットの寸法を調整します。
### Q: このチュートリアルを Web アプリケーションに統合できますか?
はい、Aspose.3D for .NET を .NET Web プロジェクトに組み込むことで可能です。
### Q: Aspose.3D サポートのためのコミュニティ フォーラムはありますか?
はい、訪問してください[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティサポートのために。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
