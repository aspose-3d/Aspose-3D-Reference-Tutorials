---
title: 3D シーンでのビューポートのキャプチャ
linktitle: 3D シーンでのビューポートのキャプチャ
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、見事な 3D ビューポートをキャプチャする方法を学びます。シーンを柔軟にレンダリングするためのステップバイステップのガイド。
weight: 11
url: /ja/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D シーンでのビューポートのキャプチャ

## 導入

3D グラフィックスとビジュアライゼーションの領域では、ビューポートのキャプチャはシーンの奥行きと詳細を向上させる重要なスキルです。 Aspose.3D for .NET は、3D シーンのレンダリングと操作のための堅牢なソリューションを提供します。このチュートリアルでは、Aspose.3D を使用して 3D シーンでビューポートをキャプチャするプロセスを説明し、見事なビジュアライゼーションを簡単に作成できるようにします。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリがインストールされていることを確認します。からダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

## 名前空間のインポート

まず、必要な名前空間を .NET プロジェクトにインポートします。

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

まず、既存の 3D シーンをプロジェクトにロードします。次のコード スニペットはこれを示しています。

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## ステップ 2: カメラを作成する

次に、カメラのインスタンスを作成し、その位置とターゲットを設定します。

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## ステップ 3: シーンに照明を追加する

光源を追加してシーンを強化します。以下のコード スニペットは、ポイント ライトの作成方法を示しています。

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## ステップ 4: レンダラーとレンダー ターゲットを構成する

レンダラーを設定し、シーンをキャプチャするためのレンダー ターゲットを作成します。

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (次のステップに続く)
    }
}
```

## ステップ 5: ビューポートを定義してレンダリングする

ビューポートを定義し、シーンをレンダリングして出力イメージを生成します。

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## ステップ 6: ビューポートを変更して再度レンダリングする

ビューポートを変更してシーンをもう一度レンダリングし、Aspose.3D の柔軟性を示します。

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

目的の視覚効果を実現するために、さまざまな構成を試し続けます。

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用して 3D シーンでビューポートをキャプチャするプロセスについて説明しました。その強力な機能を活用すると、3D グラフィックス プロジェクトを新たな高みに引き上げ、魅力的なビジュアル エクスペリエンスを提供できます。

## よくある質問

### Q1: Aspose.3D は他の 3D ファイル形式と互換性がありますか?

A1: はい、Aspose.3D はさまざまな 3D ファイル形式をサポートしており、幅広い設計ツールとの互換性を保証しています。

### Q2: ゲーム開発に Aspose.3D を使用できますか?

A2: Aspose.3D は主にグラフィックスと視覚化のために設計されていますが、その機能はゲーム開発の特定の側面を補完することができます。

### Q3: 追加の例やドキュメントはどこで入手できますか?

 A3: 包括的な内容を探索します。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/net/)より多くの例と詳細情報については、こちらをご覧ください。

### Q4: 無料トライアルはありますか?

 A4: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q5: 助けを求めたり、コミュニティに参加するにはどうすればよいですか?

 A5: Aspose.3D コミュニティに参加してください。[サポートフォーラム](https://forum.aspose.com/c/3d/18)支援と協力のために。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
