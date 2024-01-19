---
title: 3D ビューポートでの視覚効果の適用
linktitle: 3D ビューポートでの視覚効果の適用
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D ビジュアライゼーションの世界を探索してください。ステップバイステップのチュートリアルを使用して、魅力的な視覚効果をシーンに適用する方法を学びます。ピクセル化、グレースケール、エッジ検出、ぼかし効果を使用してプロジェクトをレベルアップします。
type: docs
weight: 10
url: /ja/net/3d-viewports/apply-visual-effects/
---
## 導入

3D シーンの視覚的な魅力を高めることは、没入型エクスペリエンスを作成する上で重要な側面です。 Aspose.3D for .NET は、3D ビューポートに視覚効果を適用するための強力なツール セットを提供します。このチュートリアルでは、ピクセレーション、グレースケール、エッジ検出、ブラーなどのさまざまな効果を 3D シーンに適用するプロセスを順を追って説明します。

## 前提条件

チュートリアルに入る前に、次のものが揃っていることを確認してください。

- C# および .NET 開発の実践的な知識。
- Aspose.3D for .NET ライブラリがインストールされています。からダウンロードできます[ここ](https://releases.aspose.com/3d/net/).
- 実験用の 3D シーン ファイル (「scene.obj」など)。

## 名前空間のインポート

まず、Aspose.3D およびその他の依存関係に必要な名前空間をインポートします。コードに次の行を追加します。

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

## ステップ 1: 既存の 3D シーンをロードする

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

を使用して 3D シーンをロードします。`Scene`クラス。

## ステップ 2: カメラを作成する

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

カメラ インスタンスを作成し、その位置とターゲットを設定します。

## ステップ 3: シーンに光を追加する

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

視覚効果を高めるために照明を導入します。

## ステップ 4: レンダラーとレンダー ターゲットを作成する

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    //レンダラ設定を構成する
    renderer.EnableShadows = false;

    //レンダーターゲットを作成する
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        //ビューポートの構成
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        //シーンをテクスチャにレンダリングする
        renderer.Render(rt);

        //レンダリングされたテクスチャをファイルに保存する
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        //後処理エフェクトを続行します...
    }
}
```

シーンをキャプチャするためのレンダラーとレンダー ターゲットを作成します。

## ステップ 5: 後処理エフェクトを適用する

### ステップ 5.1 ピクセル化効果

```csharp
//ピクセル化効果を作成する
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

ピクセル化効果を適用し、結果を保存します。

### ステップ 5.2 グレースケール効果

```csharp
//グレースケール効果を作成する
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

グレースケール効果を適用し、結果を保存します。

### ステップ 5.3 エフェクトを結合する

```csharp
//グレースケール効果とピクセル化効果を組み合わせる
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

複数のエフェクトを組み合わせてユニークな結果を生み出します。

### ステップ 5.4 エッジ検出効果

```csharp
//エッジ検出効果の作成
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

エッジ検出効果を適用し、結果を保存します。

### ステップ 5.5 ぼかし効果

```csharp
//ぼかし効果を作成する
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

ぼかし効果を適用し、結果を保存します。

## 結論

3D ビューポートで視覚効果を実験すると、シーンに深みと創造性が加わります。 Aspose.3D for .NET はこのプロセスを簡素化し、プロジェクトを向上させるさまざまな後処理効果を提供します。

## よくある質問

### Q1: 複数のエフェクトを同時に適用できますか?

A1: はい、さまざまな後処理エフェクトを組み合わせて、ユニークで複雑な結果を得ることができます。

### Q2: 視覚効果の強度を調整するにはどうすればよいですか?

A2: 各エフェクトには、その強度を制御するために調整できるパラメータがある場合があります。具体的な詳細については、ドキュメントを参照してください。

### Q3: Aspose.3D はゲーム開発に適していますか?

A3: Aspose.3D は主に 3D モデリングとレンダリング用に設計されていますが、ゲーム開発の特定の側面でも使用できます。

### Q4: 追加の後処理エフェクトは利用できますか?

A4: Aspose.3D にはさまざまな組み込みの後処理エフェクトが用意されており、ライブラリを使用してカスタム エフェクトを作成できます。

### Q5: Aspose.3D を商用プロジェクトに使用できますか?

 A5: はい、Aspose.3D は商用目的で使用できます。を参照してください。[購入ページ](https://purchase.aspose.com/buy)ライセンスの詳細については、