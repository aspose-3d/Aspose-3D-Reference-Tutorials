---
title: 線形押出におけるねじれ
linktitle: 線形押出におけるねじれ
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、3D グラフィックスの魅力的な世界を探索してください。ツイストを使用した線形押し出しを段階的に学習します。
weight: 14
url: /ja/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線形押出におけるねじれ

## 導入

進化し続ける .NET 開発の世界において、3D グラフィックスのパワーを活用することはエキサイティングな取り組みです。 Aspose.3D for .NET は貴重なツールキットとして登場し、開発者が没入型で視覚的に美しいアプリケーションをシームレスに作成できるようにします。この包括的なガイドでは、興味深い機能の 1 つであるツイストによるリニア押し出しについて詳しく説明します。このチュートリアルでは、プロセスを段階的に説明し、Aspose.3D for .NET の可能性を解き放ちます。

## 前提条件

この 3D の旅に着手する前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: Aspose.3D ライブラリがインストールされていることを確認してください。そうでない場合は、ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

- .NET 開発の基本知識: このチュートリアルは、.NET 開発の基本を理解していることを前提としています。

## 名前空間をインポートします。

どの .NET プロジェクトでも、名前空間を適切に使用することが重要です。 Aspose.3D の機能を効果的に活用するために、必要な名前空間をインポートすることから始めます。以下にガイドとなるスニペットを示します。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

ここで、Aspose.3D for .NET を使用したツイストによる線形押し出しの興味深いプロセスをわかりやすい手順に分解してみましょう。

## ステップ 1: 基本プロファイルを初期化する

```csharp
//押し出すベースプロファイルを初期化します。
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

まず、押し出し用の基本プロファイルを設定します。この例では、指定された丸め半径を持つ長方形を使用します。

## ステップ 2: 3D シーンを作成する

```csharp
//シーンを作成する
Scene scene = new Scene();
```

すべての魔法が起こる 3D シーンを確立します。これは、3D 傑作のキャンバスとして機能します。

## ステップ 3: 左右のノードを作成する

```csharp
//左側のノードを作成する
var left = scene.RootNode.CreateChildNode();
//適切なノードを作成する
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

シーン内に左右のノードを生成します。左側のノードの移動を調整して、適切な位置に配置します。

## ステップ 4: 左側のノードでツイストを使用して線形押し出しを実行する

```csharp
//Twist プロパティは、プロファイルを押し出す際の回転の度合いを定義します。
//ツイストとスライスのプロパティを使用して、左側のノードで線形押し出しを実行します。
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

ここで魔法が起こります。左側のノードで線形押し出しを実行し、ツイスト プロパティを組み込んで回転の度合いを定義します。スライスの数を調整して、より詳細なディテールを表示します。

## ステップ 5: 右側のノードでツイストを使用して線形押し出しを実行する

```csharp
//ツイストとスライスのプロパティを使用して、右側のノードで線形押し出しを実行します。
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

右側のノードのプロセスをミラーリングし、さまざまなツイスト値を試して押し出しの変化を観察します。

## ステップ 6: 3D シーンを保存する

```csharp
// 3Dシーンを保存する
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

最後に、3D 傑作を目的の出力ディレクトリに保存します。好みに応じてファイル名を調整します。

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用して、ツイストによる線形押し出しの魅力的な領域を探索しました。この機能は創造的な可能性への扉を開き、開発者が動的な視覚要素をアプリケーションに簡単に注入できるようにします。

## よくある質問

### Q1: ツイストを伴う線形押し出しを他の形状に適用できますか?

A1: もちろんです！長方形以外にもさまざまな基本プロファイルを試して、無数のデザインの可能性を解き放つことができます。

### Q2: 「ツイスト」プロパティは線形押し出しにおいてどのような役割を果たしますか?

A2: 「ツイスト」プロパティは、押し出しプロセス中の回転の度合いを決定し、最終的な 3D 形状に影響します。

### Q3: 多数のスライスを使用する場合、パフォーマンスに関する考慮事項はありますか?

A3: スライスの数が増えると詳細が追加されますが、パフォーマンスに影響を与える可能性があります。アプリケーションの要件に基づいてバランスをとってください。

### Q4: Linear Extrusion を他の Aspose.3D 機能と組み合わせることはできますか?

A4：確かに！ Aspose.3D は豊富な機能セットを提供します。線形押し出しを他の機能と自由に組み合わせて、より複雑なデザインを実現します。

### Q5: Aspose.3D のサポートとディスカッションのためのコミュニティはありますか?

 A5: はい、Aspose.3D コミュニティに参加してください。[アスペス フォーラム](https://forum.aspose.com/c/3d/18)サポートと魅力的なディスカッションのために。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
